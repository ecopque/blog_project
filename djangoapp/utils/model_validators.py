# FILE: /blog_project/djangoapp/utils/model_validators.py

from django.core.exceptions import ValidationError ##

# EXPORT⬇: /blog_project/djangoapp/site_setup/models.py
def validate_png(image): ##
    if not image.name.lower().endswith('.png'): ##
        raise ValidationError('Image must be PNG.') ##
 

#1: Criei um validador. Se não for '.png', vai imprimir a mensagem.