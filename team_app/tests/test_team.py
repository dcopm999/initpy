from django.contrib.auth.models import User
from django.test import TestCase

from team_app import models
# Create your tests here.


class TeamTestCase(TestCase):
    fixtures = ['auth.json', 'team.json']

    def setUp(self):
        self.USER = User.objects.get(id=1)
        self.MEMBER = models.TeamModel.objects.get(user_id=self.USER.id)

    def test_team_id(self):
        self.assertEqual(self.MEMBER.id, 1)

    def test_team_position(self):
        self.assertEqual(self.MEMBER.position, 'Django/Python разработчик')

    def test_team_photo(self):
        self.assertEqual(self.MEMBER.photo.url, '/media/team/photo_2E4JL6i.jpg')
