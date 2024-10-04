# FILE: /blog_project/djangoapp/utils/model_validators.py

from django.core.exceptions import ValidationError #1:

# EXPORT⬇: /blog_project/djangoapp/site_setup/models.py
def validate_png(image): #2:
    if not image.name.lower().endswith('.png'): #3: #4:
        raise ValidationError('Image must be PNG.')
 

# ------------------------------------------------------------------

#1: ValidationError é usada para gerar exceções de validação em Django. Quando uma validação falha (como no caso de uma imagem que não é PNG), uma exceção ValidationError é lançada para informar o usuário.
#2: Esta função é usada como um validador personalizado para verificar se a imagem fornecida é um arquivo PNG. Ela é aplicada como um validador de campo em um modelo Django.
#3: Verifica se o nome do arquivo de imagem não termina com a extensão .png. Se a condição for verdadeira, significa que o arquivo não é um PNG, e o código dentro do bloco if será executado. 
#4: O método lower() retorna uma cópia da string original convertida para minúsculas. O método endswith() verifica se a string termina com o sufixo especificado (um ou mais caracteres) (filename = "example.png" | print(filename.endswith(".png"))  # Output: True | print(filename.endswith(".jpg"))  # Output: False).