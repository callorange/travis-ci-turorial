from django.test import TestCase


class TravisTest(TestCase):
    def test_start(self):
        self.assertEqual(1, 2, 'Raise Error')
