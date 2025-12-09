# SkillBridge

SkillBridge is a platform that connects individuals who want to teach a skill with those who want to learn. It is a full-stack web application built with Flask (Backend) and Vue.js (Frontend).

## Features

-   **User Authentication**: Secure Login/Registration using Token-based Auth (Flask-Security).
-   **Skill Management**: Create, Read, and List skills.
-   **Booking System**: Request sessions with instructors and view booking status.
-   **Dashboard**: Central hub for managing skills and bookings.
-   **RESTful API**: Well-structured API serving the frontend.
-   **Responsive UI**: Modern interface built with Vue.js 3 and Vanilla CSS.

## Tech Stack

-   **Backend**: Python, Flask, SQLAlchemy, Flask-Security, PostgreSQL (Ready)
-   **Frontend**: Vue.js 3, Vite, Pinia, Axios
-   **Database**: SQLite (Development) / PostgreSQL (Production)

## Installation Steps

### Backend

1.  Navigate to `backend/`
2.  Install dependencies: `pip install -r requirements.txt`
3.  Run the app: `python app.py`
    *   The database will be automatically initialized with a test user (`test@example.com` / `password`).
    *   API runs at `http://localhost:5000`

### Frontend

1.  Navigate to `frontend/`
2.  Install dependencies: `npm install`
3.  Run the dev server: `npm run dev`
4.  Open `http://localhost:5173`

## API Documentation

-   `GET /api/skills`: List all skills
-   `GET /api/skills/<id>`: Get skill details
-   `POST /api/skills`: Create a new skill (Auth required)
-   `GET /api/dashboard`: Get user's skills (Auth required)
-   `POST /api/bookings`: Book a session (Auth required)
-   `GET /api/my-bookings`: Get user's bookings (Auth required)

## Team/Author

Built as part of the App Development Project.

