import random
import string

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    KirrURL_instance = instance.__class__
    
    is_code_exists = KirrURL_instance.objects.filter(shortcode=new_code).exists()

    if(is_code_exists):
        return create_shortcode(instance, size=size)
    return new_code