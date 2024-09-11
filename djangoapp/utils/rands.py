# FILE: /blog_project/djangoapp/utils/rands.py

from random import SystemRandom
import string
from django.utils.text import slugify

def random_letters(k=5): ##
    return ''.join(SystemRandom().choices(string.ascii_letters + string.digits, k=k)) ##

def slugify_new(text):
    return slugify(text + random_letters(4))

# print(slugify_new('Vá vô va fi Fi')) #1:



#1: Resposta: va-vo-va-fi-firh0o;

# https://linktr.ee/edsoncopque