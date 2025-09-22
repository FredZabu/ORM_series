from core.models import Restaurant
from django.utils import timezone
from django.db import connection
def run():
    # Restaurant.objects.create(name = 'Piza Shop',latitude = 50.2, longitude = 50.2, date_opened = timezone.now(), restaurant_type = Restaurant.TypeChoices.ITALIAN)
    print(Restaurant.objects.count())
    print(connection.queries)