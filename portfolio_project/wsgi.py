"""
WSGI config for portfolio_project project.
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

# ponytail: run migrations + seed on Vercel cold start (idempotent)
if os.environ.get('VERCEL'):
    import django
    from django.core.management import call_command
    django.setup()
    try:
        call_command('migrate', '--noinput')
        call_command('seed_data')
    except Exception:
        pass  # db not ready yet, retry on next cold start

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
