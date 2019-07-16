from django.contrib.auth.models import User
from django.test import TestCase

from team_app import models
# Create your tests here.


class TeamTestCase(TestCase):
    fixtures = ['auth.json', 'team.json']

    def test_team_str(self):
        team = models.TeamModel.objects.get(id=1)
        self.assertEqual(team.__str__(), 'Павел Таньчев')

    def test_skill_str(self):
        skill = models.SkillModel.objects.get(id=1)
        self.assertEqual(skill.__str__(), 'Системный администратор Linux')

    def test_contact_str(self):
        contact = models.ContactModel.objects.get(id=1)
        self.assertEqual(contact.__str__(), '998909199375 998909199375 dcopm999@gmail.com')

    def test_service_str(self):
        service = models.ServiceModel.objects.get(id=1)
        self.assertEqual(service.__str__(), 'Разработка Web приложений')

    def test_service_item_str(self):
        item = models.ServiceItemModel.objects.get(id=1)
        self.assertEqual(item.__str__(), 'Django Web framework')

    def test_about_str(self):
        about = models.AboutModel.objects.get(id=1)
        self.assertEqual(about.__str__(), 'Наши услуги')

    def test_about_item_str(self):
        item = models.AboutItemModel.objects.get(id=1)
        self.assertEqual(item.__str__(), 'Автоматизация бизнес процессов.')

    def test_certs_str(self):
        cert = models.CertificatesModel.objects.get(id=1)
        self.assertEqual(cert.__str__(), 'Павел Таньчев')

    def test_feedback_str(self):
        feed = models.FeedbackModel.objects.get(id=1)
        self.assertEqual(feed.__str__(), 'test@test.test')
