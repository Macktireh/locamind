from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):
    def test_index_view(self) -> None:
        """
        Ensure the view returns an HTTP 200 status code.
        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_index_template_used(self) -> None:
        """
        Ensure the view uses the correct template.
        """
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "index.html")
