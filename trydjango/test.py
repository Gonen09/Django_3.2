import os
from django.test import TestCase
from django.contrib.auth.password_validation import validate_password


class TryDjangoConfigTest (TestCase):
    # https://docs.python.org/3/library/unittest.html

    def test_secret_key_strength(self):

        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
        # self.assertNotEqual (SECRET_KEY,'abc123')

        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f'Weak Secret Key {e.messages}'
            self.fail(msg)
