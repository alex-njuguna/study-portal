# StudyMate App

This project is a comprehensive study portal built using Django. It includes multiple apps for managing various aspects of a student's study routine, such as books, activity tracking, homework, notes, dictionary, conversions, and more.

# Live project deployment
[Explore how this app works](https://study-portal-five.vercel.app/)

# Project Structure
.
├── activity
├── book
├── books
├── conversion
├── dashboard
├── dictionary
├── homework
├── note
├── portal
├── static
├── staticfiles
├── wiki
└── youtube

# Detailed Structure

# activity: Manages user activities.

admin.py: Admin configurations for activity app.
apps.py: App configuration.
forms.py: Forms used in activity app.
models.py: Database models.
templates/activity: HTML templates.
urls.py: URL routing.
views.py: Views for the activity app.


# book: Manages book-related functionalities.

admin.py, apps.py, forms.py, models.py, urls.py, views.py: Similar to the structure in the activity app.
templates/book: HTML templates specific to book functionalities.


# conversion: Handles conversion functionalities.

admin.py, apps.py, models.py, urls.py, views.py: Similar structure.
templates/conversion: HTML templates for conversion app.


# dashboard: Main app for user interface and navigation.

admin.py, apps.py, forms.py, models.py, urls.py, views.py: Standard structure.
static/dashboard: Static files (CSS, JS, images).
templates/dashboard: HTML templates for dashboard views.


# dictionary: Manages dictionary functionalities.

Standard structure with templates in templates/dictionary.


# homework: Manages homework tracking and management.

Standard structure with templates in templates/homework.


# note: Manages note-taking functionalities.

Standard structure with templates in templates/note.


# wiki: Manages wiki functionalities.

Standard structure with templates in templates/wiki.


# youtube: Manages YouTube-related functionalities.

Standard structure with templates in templates/youtube.

# portal: Main Django project settings and configuration.

asgi.py, settings.py, urls.py, wsgi.py: Django configurations.
static: Directory for static files used across the project.

# Getting Started
Prerequisites
Python 3.x
Django
Pipenv (for managing virtual environment)

# Installation
Clone the repository:

`git clone https://github.com/yourusername/study-portal.git`
`cd study-portal`

Set up the virtual environment:

`pipenv install`
`pipenv shell`

Apply migrations:

`python manage.py migrate`

Run the development server:

`python manage.py runserver`

Environment Variables
Create a .env file in the root directory and add your environment-specific variables. For example:

`SECRET_KEY=your_secret_key`
`DEBUG=True`
`DATABASE_URL=your_database_url`

Static Files
Collect static files for production:

`python manage.py collectstatic`

Admin User
Create a superuser for accessing the Django admin interface:

`python manage.py createsuperuser`

Usage

Navigate to `http://127.0.0.1:8000` in your web browser to access the portal. Log in with the admin credentials to manage different aspects of the study portal.

Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to contact the project maintainers for any issues or feature requests. Happy studying!

