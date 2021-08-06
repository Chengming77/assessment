from rango.views import athlete
from django.test import TestCase
from rango.models import Sport,Athlete

# Create your tests here.
class SportMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        sport = Sport(name='test',views=1,likes=0)
        sport.save
        self.assertEqual((sport.views>=0),True)

    def test_str_representation(self):
        sport = Sport(name='test',views=1,likes=0)
        sport.save
        self.assertEqual(sport.__str__(), sport.name)

class AthleteMethodTests(TestCase):
    def test_str_representation(self):
        athlete = Athlete(name='Chen')
        athlete.save
        self.assertEqual(athlete.__str__(), athlete.name)
        
class SportViewTestCase(TestCase):
     def test_visit_a_nonexistent_category(self):
        url = 'rango:warships'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

