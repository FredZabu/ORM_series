from core.models import Restaurant
from django.utils import timezone
def run():
    restaurant = Restaurant()
    restaurant.name = 'My Italian Restaurant'
    restaurant.latitude = 50.2
    restaurant.longitude = 50.2
    restaurant.date_opened = timezone.now()
    restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN
    
    restaurant.save()