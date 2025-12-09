# Deployment Guide

Follow these steps to deploy **SkillBridge** to production using **Neon** (Database), **Render** (Backend), and **Vercel** (Frontend).

## Prerequisites
-   GitHub Repository pushed and up-to-date.
-   Accounts on [Neon.tech](https://neon.tech), [Render.com](https://render.com), and [Vercel.com](https://vercel.com).
-   Vercel CLI installed (`npm i -g vercel`).

---

## Part 1: Database (Neon)

1.  Log in to the **Neon Console**.
2.  Click **"New Project"**.
3.  Name it `skillbridge-db`.
4.  Select the latest Postgres version.
5.  **Copy the Connection String**. It looks like:
    `postgres://user:password@ep-xyz.Region.neon.tech/neondb?sslmode=require`
    *   *Keep this safe! You will need it for the Backend.*

---

## Part 2: Backend (Render)

Since Render works best with GitHub integration, we will deploy by connecting your repository.

1.  Log in to **Render Dashboard**.
2.  Click **"New + "** -> **"Web Service"**.
3.  Select **"Build and deploy from a Git repository"**.
4.  Connect your `SkillBridge` repo.
5.  **Configure Service**:
    *   **Name**: `skillbridge-api`
    *   **Region**: Closest to you.
    *   **Branch**: `main`
    *   **Root Directory**: `backend` (Important!)
    *   **Runtime**: `Python 3`
    *   **Build Command**: `pip install -r requirements.txt`
    *   **Start Command**: `gunicorn app:app`
6.  **Environment Variables** (Advanced Section):
    Add the following:
    *   `DATABASE_URL`: *(Paste your Neon Connection String)*
    *   `SECRET_KEY`: *(Generate a random strong string)*
    *   `SECURITY_PASSWORD_SALT`: *(Generate another random string)*
    *   `FLASK_CONFIG`: `production`
7.  Click **"Create Web Service"**.
8.  **Wait for Deploy**. Once live, copy the **onrender.com URL** (e.g., `https://skillbridge-api.onrender.com`).

---

## Part 3: Frontend (Vercel CLI)

1.  Open your terminal in the project root (`d:\Project2`).
2.  Navigate to the frontend:
    ```powershell
    cd frontend
    ```
3.  Run the Vercel deploy command:
    ```powershell
    vercel
    ```
4.  **Follow the Interactive Prompts**:
    *   Set up and deploy? **Y**
    *   Which scope? **(Select your account)**
    *   Link to existing project? **N**
    *   Project Name? **skillbridge-frontend**
    *   In which directory is your code located? **./** (default)
    *   Want to modify these settings? **N** (Vite settings are auto-detected)
5.  **Environment Variables**:
    *   Go to the Vercel Dashboard for this new project.
    *   Settings -> Environment Variables.
    *   Add: `VITE_API_URL` = `https://skillbridge-api.onrender.com` (Your Render Backend URL).
    *   *Note: Remove any trailing slash from the URL.*
6.  **Redeploy**:
    Run `vercel --prod` in your terminal to create a production build with the new env vars.
    ```powershell
    vercel --prod
    ```

## Verification

1.  Visit your new Vercel URL.
2.  Try to **Register** a new user.
3.  If successful, the app is fully connected!
