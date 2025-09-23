from core.models import Restaurant, Rating
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
def run():
    print(Rating.objects.filter(rating = 5))