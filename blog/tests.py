from django.test import TestCase
from django.urls import reverse


class BlogTestCase(TestCase):
    def test_index_get(self):
        response = self.client.get(reverse('blog.index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            'blog': 'get'
        })

    def test_index_post(self):
        response = self.client.post(reverse('blog.index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            'blog': 'post'
        })
