from django.test import TestCase


class ExampleTestCase(TestCase):

    def test_true_equal_true(self):
        self.assertEquals(True, True)
