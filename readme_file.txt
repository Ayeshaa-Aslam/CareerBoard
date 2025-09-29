CareerBoard – Job Listing Web App

CareerBoard is a full-stack job listing application where recruiters can add, update, and delete jobs, and users can browse/search/filter available jobs.  

Features
- Recruiters can:
  - Add jobs (title, company, location, type, tags, description)
  - Update jobs
  - Delete jobs
- Users can:
  - Browse all jobs
  - Filter jobs by title, company, location, type
  - Search jobs with keywords
  - Sort jobs by posting date
- Responsive & modern UI with animated hero section

 Tech Stack

Frontend
-React.js (UI framework)
-Axios (API calls)
-React Toastify (notifications)
-React Icons (icons)
-CSS Modules (styling, animations)

Backend
- Flask(Python web framework)
- Flask-CORS (CORS handling)
- SQLAlchemy (ORM)
- Psycopg2 (PostgreSQL connector)
- Python-Dotenv (environment variables)

 Database
- PostgreSQL

Setup Instructions
Backend (Flask + PostgreSQL)

1. Navigate to Backend folder:
   cd Backend

2.Create virtual environment:
  python -m venv venv
  source venv/Scripts/activate

3. Install dependencies:
  pip install flask flask-cors sqlalchemy psycopg2-binary python-dotenv

4. Setup PostgreSQL:
   Create a database named job_listings_db
   Update app.py connection string if needed

configure the database connection 
        "DATABASE_URL",
        "postgresql://postgres:1234@localhost:5432/job_listings_db"

5. Initialize database:
   python init_db.py

6. Run backend:
   python app.py


Frontend (React)

1. Navigate to frontend:
   cd frontend

2. Install dependencies:
   npm install React, Axios, React Toastify, React Icons etc.

3. Start frontend
   npm Start

Scrapping using Selenium

Packages Install for Scrapping

1. Bckend requirements
pip install selenium beautifulsoup4 webdriver-manager
2. Install ChromeDriver automatically
pip install webdriver-manager

Links of website: 
"https://www.workingnomads.com/jobs",
"https://remoteok.com/remote-dev-jobs",
"https://weworkremotely.com/"





