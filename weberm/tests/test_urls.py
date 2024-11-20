from django.test import SimpleTestCase
from django.urls import resolve, reverse

from sunshineEmr.views import index

class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)