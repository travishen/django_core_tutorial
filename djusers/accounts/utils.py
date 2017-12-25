import random
import string

from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 20)


def code_generator(size=SHORTCODE_MIN,
                   chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

