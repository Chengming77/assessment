import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Athlete, Sport


def populate():
    sports = {
        'athletics':{
            'name': 'athletics',
            'pic_url':'images/AthleticsIcon.png',
            'web_url':'https://olympics.com/tokyo-2020/en/sports/athletics/',
            'views': 1,
            'likes': 10,
            'information': 'The athletics track at the Olympic Stadium is a 400m oval. For all track events the finish line is in the same place, at the end of the ‘home straight’. The track programme comprises sprints, middle-distance and long-distance events for men and women; hurdles and steeplechase races; and relays. Most events start with heats, with the fastest athletes or teams progressing to semi-finals and then the final.To become the fastest human being at a particular distance requires not only speed but also supreme fitness, strength and the ability to master challenging techniques, such as the start in sprints and clearing the barriers in hurdles and steeplechase events.'},
        'table-tennis':{
            'name': 'table-tennis',
            'pic_url':'images/TableTennisIcon.png',
            'web_url':'https://olympics.com/tokyo-2020/en/sports/table-tennis/',
            'views': 2,
            'likes': 20,
            'information': 'Table tennis has come a long way from its late 19th century origins as an after-dinner game played by upper-class English families. More than a century later, table tennis has a greater number of recreational players than any other sport and Olympic-level competition is a breathtaking spectacle.Legend has it that the first players used the lids of cigar boxes for rackets and a rounded-off cork from a champagne bottle as the ball. Today, the game is played with sophisticated rackets comprising a wooden blade coated with rubber on both sides, and a hollow plastic ball weighing just 2.7g.'},
        'Archery':{
            'name': 'Archery',
            'pic_url':'images/ArcheryIcon.png',
            'web_url':'https://olympics.com/tokyo-2020/en/sports/archery/',
            'views': 3,
            'likes': 30,
            'information': 'Archery dates back over 10,000 years, when bows and arrows were first used for hunting and warfare, before it developed as a competitive activity in medieval England. There are several variants, including target archery, where competitors shoot at stationary targets on a flat range; and field archery, which involves shooting at targets of varying and often unmarked distance, typically in woodland and rough terrain. Only target archery is an Olympic sport, practised in more than 140 countries around the world.'}
    }

    athletes = {
        'Su Bingtian':{
            'name': 'Su Bingtian',
            'views': 101,
            'likes': 101,
            'information': 'about Su Bingtian'},
        'Peaty Adam':{
            'name': 'Peaty Adam',
            'views': 22,
            'likes': 22,
            'information': 'Peaty Adam'},
        'Dressel Caeleb':{
            'name': 'Dressel Caeleb',
            'views': 33,
            'likes': 33,
            'information': 'Dressel Caeleb'}
    }

    for sport,sport_data in sports.items():
        s = add_sport(sport,pic_url=sport_data['pic_url'],web_url=sport_data['web_url'],info=sport_data['information'],views=sport_data['views'],likes=sport_data['likes'])
      

    for s in Sport.objects.all():
        print(s)
        print(s.pic_url)
        print(s.web_url)
        print(s.likes)
        print(s.views)
        print(s.info)


    for athlete,athlete_data in athletes.items():
        a = add_athlete(athlete,info=athlete_data['information'],views=athlete_data['views'],likes=athlete_data['likes'])

    for a in Athlete.objects.all():
       print(a)
       print(a.info)


def add_sport(name,pic_url,web_url,info,views=0, likes=0):
    s = Sport.objects.get_or_create(name=name)[0]
    s.views = views
    s.likes = likes
    s.info = info
    s.pic_url = pic_url
    s.web_url = web_url
    s.save()
    return s

def add_athlete(name,info,views=0, likes=0):
    a = Athlete.objects.get_or_create(name=name)[0]
    a.views = views
    a.likes = likes
    a.info = info
    a.save()
    return a

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()


    
    