# ORM_series

ORM_series is a project covering concepts about the Object Relational Mapping(ORM).

## Database Used

Made use of the sqlite3 database.

## Creating Models

I created three models which included the Restaurant, Rating, Sale model.

### Restaurant Model

```python
class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GR', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'Fast Food'
        OTHER = 'OT', 'Other'

    name = models.CharField(max_length = 100)
    website = models.URLField(default = '')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    restaurant_type = models.CharField(max_length = 2, choices = TypeChoices.choices)

    def __str__(self):
        return self.name
```

### Rating Model

```python
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Rating: {self.rating}"
```

### Sale Model

```python
class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
    income = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()
```

## Creating And Querying Data

- Querying database with Django to get data.
- Creating rows with Django ORM.
- Querying Foreign Keys with ORM.

#### Creating a new row in the database table

This python code below creates a new row in the table

```python
def run():
    restaurant = Restaurant() # first creates an instance of the Restaurant model
    restaurant.name = 'My Italian Restaurant' # This field is newly created on a fly
    restaurant.latitude = 50.2
    restaurant.longitude = 50.2
    restaurant.date_opened = timezone.now()
    restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN

    restaurant.save() # After initializing data to the fields the object is then saved to the database
```

#### OR

Using the,

- objects.create() method.

```python
def run():
    Restaurant.objects.create(name = 'Piza Shop',latitude = 50.2, longitude = 50.2, date_opened = timezone.now(), restaurant_type = Restaurant.TypeChoices.ITALIAN)
```

### Fetching all data in the database table

This code below returns a querySet containing all rows available in the database table.

```python
def run():
    restaurant = Restaurant.objects.all() # This returns a querySet that has all table rows.
    print(restaurant)
```

This below fetches the first row in the database table.

```python
def run():
    restaurant = Restaurant.objects.first()
```

#### OR

Using the indexing method.

```python
def run():
    restaurant = Restaurant.objects.all()[0]
```

### Working with Foreign Keys.

The code below creates a Rating instance or table row with User ID and Restaurant ID being a foreign key which depicts a one-to-many relationship.

```python
def run():
    restaurant = Restaurant.objects.first() # get a reference to a specific row or restaurant
    user = User.objects.first() # reference to a specific user
    Rating.objects.create(restaurant = restaurant, user = user, rating = 3) #creates the rating object
```

### Working filtering rows in the database table

- Equal-to
  This return the Rating rows whose rating is equal to 5.

```python
def run():
    print(Rating.objects.filter(rating = 5))
```

- Greater-than
  This returns Rating rows whose rating is greater-than 5.

```python
def run():
    print(Rating.objects.filter(rating__gt = 5))
```

- Greater-than-or-equal-to (rating >= 5)
  This returns one or more rows from the database Rating table whose rating >= 5

```python
def run():
    print(Rating.objects.filter(rating__gte = 5))
```

- Less-than (rating < 5)
  This returns one or more rows from the Rating table whose rating < 5

```python
def run():
    print(Rating.objects.filter(rating__lt = 5))
```

#### OR

```python
def run():
    print(Rating.objects.filter(rating__lte = 5)) # returns rows that are <= 5
```

### Updating Fields in the database table

This updates the name field of a particular row in the database table named Restaurant.

```python
def run():
    restaurant = Restaurant.objects.first() # returns the row reference
    restaurant.name = "Cafe Javas" # use the object to rename its name field
    restaurant.save() # saves the updated object to the database
```
