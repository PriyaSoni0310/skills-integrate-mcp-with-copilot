"""Configuration sample showing secure session and CSRF settings.

Copy values to environment variables in production and document in README.
"""
import os

# SECRET_KEY must come from an environment variable in production
SECRET_KEY = os.environ.get("SECRET_KEY", "please-set-a-secret-key")

# Session cookie security
SESSION_COOKIE_SECURE = True  # send only over HTTPS
SESSION_COOKIE_HTTPONLY = True  # not accessible to JavaScript
SESSION_COOKIE_SAMESITE = "Lax"  # or 'Strict' for stricter CSRF protection

# CSRF: install and enable Flask-WTF CSRFProtect in the app factory
# from flask_wtf import CSRFProtect
# csrf = CSRFProtect()
