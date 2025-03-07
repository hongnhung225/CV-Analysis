from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import jwt
from datetime import datetime, timedelta
# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('hr', 'HR'),
        ('cand', 'Candidate'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    @property
    def token(self):
        token = jwt.encode({'username': self.username,'email': self.email, 
                            'exp': datetime.utcnow()+ timedelta(hours=24)}, 
                            settings.SECRET_KEY, algorithm='HS256')
        return token