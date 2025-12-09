import os
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from config import config
from models import db
from flask_security import auth_required, current_user


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize Extensions
    db.init_app(app)
    CORS(app) # Enable CORS for frontend

    # Setup Flask-Security
    from flask_security import Security, SQLAlchemyUserDatastore, hash_password
    from models import User, Role
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    # Create Database Tables (for dev/testing)
    with app.app_context():
        db.create_all()
        
        # Create a test user if not exists
        if not user_datastore.find_user(email="test@example.com"):
            user_datastore.create_user(email="test@example.com", password=hash_password("password"), full_name="Test User")
            db.session.commit()

    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to SkillBridge API"})

    @app.route('/api/health')
    def health_check():
        return jsonify({"status": "healthy"})

    @app.route('/api/login', methods=['POST'])
    def api_login():
        from flask_security import verify_password, login_user
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        user = user_datastore.find_user(email=email)
        
        if not user:
             return jsonify({"response": {"errors": ["User not found"]}}), 404
             
        if verify_password(password, user.password):
            if not user.active:
                 return jsonify({"response": {"errors": ["Account disabled"]}}), 400
                 
            token = user.get_auth_token()
            
            return jsonify({
                "response": {
                    "user": {
                        "id": user.id,
                        "email": user.email,
                        "full_name": user.full_name,
                        "authentication_token": token
                    }
                }
            })
        
        return jsonify({"response": {"errors": ["Invalid password"]}}), 400

    # --- Skill API Endpoints ---

    @app.route('/api/skills', methods=['GET'])
    def get_skills():
        from models import Skill
        skills = Skill.query.all()
        return jsonify([skill.to_dict() for skill in skills])

    @app.route('/api/skills', methods=['POST'])
    @auth_required("token")
    def create_skill():
        from models import Skill
        data = request.get_json()
        if not data or 'name' not in data or 'description' not in data:
            return jsonify({'error': 'Missing name or description'}), 400
        
        skill = Skill(
            name=data['name'],
            description=data['description'],
            instructor_id=current_user.id
        )
        db.session.add(skill)
        db.session.commit()
        return jsonify(skill.to_dict()), 201

    @app.route('/api/skills/<int:skill_id>', methods=['GET'])
    def get_skill(skill_id):
        from models import Skill
        skill = Skill.query.get_or_404(skill_id)
        return jsonify(skill.to_dict())

    @app.route('/api/skills/<int:skill_id>', methods=['PUT'])
    @auth_required("token")
    def update_skill(skill_id):
        from models import Skill
        skill = Skill.query.get_or_404(skill_id)
        if skill.instructor_id != current_user.id:
            return jsonify({'error': 'Unauthorized'}), 403
            
        data = request.get_json()
        if 'name' in data:
            skill.name = data['name']
        if 'description' in data:
            skill.description = data['description']
            
        db.session.commit()
        return jsonify(skill.to_dict())

    @app.route('/api/skills/<int:skill_id>', methods=['DELETE'])
    @auth_required("token")
    def delete_skill(skill_id):
        from models import Skill
        skill = Skill.query.get_or_404(skill_id)
        if skill.instructor_id != current_user.id:
            return jsonify({'error': 'Unauthorized'}), 403
            
        db.session.delete(skill)
        db.session.commit()
        return jsonify({'message': 'Skill deleted'})

    # Dashboard Endpoint
    @app.route('/api/dashboard', methods=['GET'])
    @auth_required("token")
    def get_dashboard_data():
        from models import Skill
        # Get skills taught by current user
        my_skills = Skill.query.filter_by(instructor_id=current_user.id).all()
        return jsonify({
            'user': {
                'email': current_user.email,
                'full_name': current_user.full_name
            },
            'my_skills': [skill.to_dict() for skill in my_skills]
        })

    # --- Booking Endpoints ---

    @app.route('/api/bookings', methods=['POST'])
    @auth_required("token")
    def create_booking():
        from models import Booking, Skill
        data = request.get_json()
        skill_id = data.get('skill_id')
        
        skill = Skill.query.get_or_404(skill_id)
        
        if skill.instructor_id == current_user.id:
            return jsonify({'error': 'Cannot book your own skill'}), 400
            
        booking = Booking(
            skill_id=skill_id,
            student_id=current_user.id
        )
        db.session.add(booking)
        db.session.commit()
        return jsonify(booking.to_dict()), 201

    @app.route('/api/my-bookings', methods=['GET'])
    @auth_required("token")
    def get_my_bookings():
        from models import Booking, Skill
        # Bookings I made as a student
        student_bookings = Booking.query.filter_by(student_id=current_user.id).all()
        # Bookings received for my skills
        instructor_bookings = Booking.query.join(Skill).filter(Skill.instructor_id == current_user.id).all()
        
        return jsonify({
            'as_student': [b.to_dict() for b in student_bookings],
            'as_instructor': [b.to_dict() for b in instructor_bookings]
        })

    return app



    return app


# Create the application instance for Gunicorn
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run(port=5000)
