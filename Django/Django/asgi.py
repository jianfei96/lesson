"""
ASGI config for Django project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
# 标准接口，与python服务器通信
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django.settings')

application = get_asgi_application()
