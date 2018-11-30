from django.test import TestCase
from twentyPass.models import TwentyPass
# Create your tests here.
class TwentyPassTestCase(TestCase):
    def test_generate(self):
        t = TwentyPass(title='han', question='hello my\nname is\n han ho\n Woo!', answer='han')
        t.update_dates()
        print(t.update_date)
        print(t.title)
        print(t.question)
        print(t.answer)
