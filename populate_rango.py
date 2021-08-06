import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Sport

def populate():
    sports = {
        'athletics':{
            'name': 'athletics',
            'views': 10,
            'likes': 10,
            'information': 'about athletics'},
        'soccer':{
            'name': 'soccer',
            'views': 20,
            'likes': 20,
            'information': 'about soccer'},
        'gymnastics':{
            'name': 'gymnastics',
            'views': 30,
            'likes': 30,
            'information': 'about gymnastics'}
    }
    # 'builtin_function_or_method' object is not iterable
    for sport,sport_data in sports.items():
        s = add_sport(sport,information=sport_data['information'],views=sport_data['views'],likes=sport_data['likes'])
      

    for s in Sport.objects.all():
            print(s)

def add_sport(name,information,views=0, likes=0):
    s = Sport.objects.get_or_create(name=name)[0]
    s.views = views
    s.likes = likes
    s.informantion = information
    s.save()
    return s

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()


    
    