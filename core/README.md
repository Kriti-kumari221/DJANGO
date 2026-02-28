📁 1. __init__.py

This file tells Python that this folder is a Python package.

It is NOT exactly a constructor.

It allows Python to treat the directory as a module.

Usually, it is empty.

👉 Purpose: Package initialization.

📁 2. asgi.py

ASGI = Asynchronous Server Gateway Interface

Used for handling asynchronous requests

Supports:

WebSockets

Real-time applications

Async views

👉 Used in modern deployment (like Django Channels).

📁 3. wsgi.py

WSGI = Web Server Gateway Interface

Used for handling synchronous requests

Traditional production servers like:

Gunicorn

uWSGI

Apache

👉 Used in most normal Django deployments.

📁 4. urls.py

Used to map URLs to views

It connects:

URL → View → Logic → Response

Example:

path('home/', views.home)

👉 It decides what happens when a user visits a specific URL.

📁 5. settings.py

This is the most important file.

It contains:

Installed apps

Database configuration

Static files

Templates

Middleware

Security settings

Debug mode

Example:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
]

👉 All project configuration happens here.

🧩 What is an App in Django?

When we build a big project, we divide functionality into small reusable modules called Apps.

Example:

Authentication app

Blog app

Payment app

Home app

📌 How to Create an App
python manage.py startapp appname

Example:

python manage.py startapp home
python manage.py startapp account

This creates:

account/
    models.py
    views.py
    tests.py
    admin.py
    apps.py
📁 Important Files Inside an App
1️⃣ models.py

Used to create database tables

Each model = one table

Defines structure of data

Example:

class User(models.Model):
    username = models.CharField(max_length=100)

👉 Database logic lives here.

2️⃣ views.py

Contains the logical part

Handles requests

Returns responses

👉 This is the brain of the application.

3️⃣ admin.py

Used to register models

So we can manage data from Django Admin panel

Example:

admin.site.register(User)
4️⃣ tests.py

Used for testing functionality

Helps verify if code works correctly

🔐 Authentication Example

If we want features like:

Login

Register

Password reset

Email verification

We create a separate app:

python manage.py startapp account

Inside this app we implement:

Login system

Registration system

Password reset

Email verification

👉 This makes code modular and reusable.

🔁 Why Django Apps Are Reusable?

Django apps are modular.

If you build a good authentication app once,
you can reuse it in another project.

Just copy the app and add it to INSTALLED_APPS.

That’s why Django architecture is powerful.

🚀 How to Run the Server

To start the development server:

python manage.py runserver

Default:

http://127.0.0.1:8000/
Run on Different Port
python manage.py runserver 0.0.0.0:5000

This means:

0.0.0.0 → accessible from other devices

5000 → custom port

🔥 Important Concept Flow in Django
User → URL → urls.py → views.py → models.py → Database

Response comes back in reverse direction.

🧠 Final Concept Summary
Component	Purpose
Project	Main configuration
App	Specific functionality
models.py	Database structure
views.py	Business logic
urls.py	URL routing
admin.py	Admin panel
settings.py	Project configuration
runserver	Boot the server
