# FILE: /blog_project/djangoapp/utils/rands.py

from random import SystemRandom
import string

def random_letters(k=5): ##
    return SystemRandom().choices(string.ascii_letters + string.digits, k=k) ##

print(random_letters())





# https://linktr.ee/edsoncopque