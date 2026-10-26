from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase

from .models import TodoModel
from .views import home


class HomeSearchTests(TestCase):
    def test_alphabetic_search_does_not_use_numeric_id_lookup(self):
        user = User.objects.create_user(username='tester', password='password')
        todo = TodoModel.objects.create(
            title='AP task',
            desc='Description',
            user=user,
        )

        request = RequestFactory().get('/home?q=AP')
        request.user = user

        with patch('base.views.profile_image'), patch('base.views.render') as render:
            home(request)

        context = render.call_args.args[2]
        self.assertEqual(list(context['data']), [todo])
