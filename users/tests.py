from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import ProfileUser


def create_user(name):
	UserModel = get_user_model()
	if not UserModel.objects.filter(username=name).exists():
		user = UserModel.objects.create_user(name, password='chinelinho')
		user.is_superuser = True
		user.is_staff = True
		user.save()
		return user



class ProfileUserTestCase(TestCase):

	def setUp(self):
		admin = create_user('jhony')

	def test_user(self):
		usuario = ProfileUser.objects.get(username='jhony')
		self.assertEqual(usuario.username, 'jhony')	