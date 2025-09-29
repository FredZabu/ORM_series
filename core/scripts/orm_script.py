from core.models import Restaurant, Rating
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
def run():
    user = User.objects.first()
    restaurant = Restaurant.objects.first()
    print(restaurant.name)
    
    restaurant.name = "New Restaurant Name"
    restaurant.save()