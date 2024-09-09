# FILE: /blog_project/djangoapp/utils/model_validators.py

# EXPORT⬇: /blog_project/djangoapp/site_setup/models.py
def validate_png(image): ##
    if not image.name.lower().endswith('.png'): ##
        print()
        print()
        print("It's not png.") ##
        print()
        print()
        

#1: Criei um validador. Se não for '.png', vai imprimir a mensagem.