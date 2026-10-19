from django.test import TestCase


class HelloDjangoViewTests(TestCase):
    def test_homepage_displays_greeting(self):
        response = self.client.get("/")

        self.assertContains(response, "Hello, Django!")

    def test_hello_route_displays_greeting(self):
        response = self.client.get("/hello/")

        self.assertContains(response, "Hello, Django!")
