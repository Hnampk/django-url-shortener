import random
import string
from django.conf import settings

SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 6) # if did not configured => set to 16

def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=SHORTCODE_MIN):
    new_code = code_generator(size=size)
    KirrURL_instance = instance.__class__
    
    is_code_exists = KirrURL_instance.objects.filter(shortcode=new_code).exists()

    if(is_code_exists):
        return create_shortcode(instance, size=size)
    return new_code