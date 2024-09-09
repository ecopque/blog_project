# FILE: /blog_project/djangoapp/utils/images.py

from pathlib import Path
from django.conf import settings ##
from PIL import Image ##

#EXPORT⬇: /blog_project/djangoapp/site_setup/models.py
def resize_image(image_django, new_width=800, optimize=True, quality=60): ##
    # IMPORT⬇: /blog_project/project/settings.py
    image_path = Path(settings.MEDIA_ROOT / image_django.name).resolve() ##
    image_pillow = Image.open(image_path) ##
    original_width, original_height = image_pillow.size ##

    if original_width <= new_width: ## A:
        image_pillow.close() ## A:
        return image_pillow ##
    
    new_height = round(new_width  * original_height / original_width) ##
    new_image = image_pillow.resize((new_width, new_height), Image.LANCZOS) ##

    new_image.save(image_path, optimize=optimize, quality=quality,) ##

    return new_image ##


# ------------------------------------------------------------------

#A: Se a imagem for menor que 'new_digth', então podemos cancelar o redimensionamento. Por isso, close().
