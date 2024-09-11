# FILE: /blog_project/djangoapp/utils/rands.py

from random import SystemRandom
import string

def random_letters(k=5): ##
    return SystemRandom().choices(string.aschii_letters + string.digits, k=5) ##






# https://linktr.ee/edsoncopque