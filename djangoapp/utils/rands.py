# FILE: /blog_project/djangoapp/utils/rands.py

from random import SystemRandom
import string
from django.utils.text import slugify

def random_letters(k=5): #2:
    return ''.join(SystemRandom().choices(string.ascii_letters + string.digits, k=k)) #3:

def slugify_new(text, k=5): #4:
    return slugify(text + '-' + random_letters(k)) #5:

# print(slugify_new('Vá vô va fi Fi')) #1:



#1: Resposta: va-vo-va-fi-fi-wni73;
#2: Gera uma string de k caracteres aleatórios composta de letras e dígitos (alfanuméricos). O padrão é 5 caracteres (k=5);
#3: Usa SystemRandom().choices() para escolher k caracteres aleatórios do conjunto de letras (ascii_letters) e dígitos (digits), e ''.join(...) para unir esses caracteres em uma string.
#4: Gera um slug a partir de um texto (text) e adiciona uma string aleatória ao final, separada por um hífen.
#5: Chama a função random_letters(k) para gerar uma sequência de k caracteres aleatórios e a concatena ao text fornecido com um hífen no meio. Em seguida, utiliza a função slugify() do Django para criar um slug formatado.

# https://linktr.ee/edsoncopque