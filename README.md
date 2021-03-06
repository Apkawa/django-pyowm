# Django PyOWM

A Django ORM interface for PyOWM domain entities


## Requirements

  - Django 1.8+
  - PyOWM >=2.5,<2.7

Python 2.7 is supported.


** Please notice that the API can be unstable as this project is still in beta testing **

## Install

Install the library with `pip`:

```shell
$ pip install django_pyowm
```

Then add `django_pyowm` to the `INSTALLED_APPS` list into your Django project's `settings.py` file:
 
```python
INSTALLED_APPS = [
    ...
    'django_pyowm'  # <---
]
```

Finally generate tables by applying migrations:

```shell
$ python manage.py makemigrations django_pyowm
$ python manage.py migrate
```


## Features
Models behave as all other Django models but they have a few useful 
functions:

  -  `<Model_class>.from_entity(entity)` - creates a PyOWM model instance
     from the corresponding PyOWM domain object instance
  -  `<Model_instance>.to_entity(entity)` - turns the model instance to
     the corresponding PyOWM domain object instance
  - `<Model_class>.save_all()` - persists the model instance along with all related objects

## Quick usage examples

```python
from pyowm import OWM
from django_pyowm import models


# Get data an Observation from the API 
owm = OWM(API_key='my_key')
obs = owm.weather_at_place('London,UK')

# Create a model instance from API response
m = models.Observation.from_entity(obs)

# Save related objects and then the model itself
m.location.save()
m.weather.save()
m.save()

# .. or save everything in one shot
m.save_all()

# From model instance to entity
original_obs = m.to_entity()
```

## Testing
All details about testing are [here](https://github.com/csparpa/django-pyowm/wiki/Testing)
