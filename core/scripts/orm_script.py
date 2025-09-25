from core.models import Restaurant, Rating
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
def run():
    user = User.objects.first()
    restaurant = Restaurant.objects.first()
    rating = Rating(user=user, restaurant= restaurant, rating = 9)   
    
    rating.full_clean()
    rating.save()