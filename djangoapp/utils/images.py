# FILE: /blog_project/djangoapp/utils/images.py

from pathlib import Path
from django.conf import settings #1:
from PIL import Image #2:

#EXPORT⬇: /blog_project/djangoapp/site_setup/models.py
def resize_image(image_django, new_width=800, optimize=True, quality=60): #3:
    # IMPORT⬇: /blog_project/project/settings.py
    image_path = Path(settings.MEDIA_ROOT / image_django.name).resolve() #4: #5:
    image_pillow = Image.open(image_path) #6:
    original_width, original_height = image_pillow.size #7:

    if original_width <= new_width: #8:
        image_pillow.close() #9:
        return image_pillow #10:
    
    new_height = round(new_width  * original_height / original_width) #11:
    new_image = image_pillow.resize((new_width, new_height), Image.LANCZOS) #12:
    new_image.save(image_path, optimize=optimize, quality=quality,) #13:

    return new_image ##


# ------------------------------------------------------------------
#1: 'settings' contém todas as configurações do projeto Django, como MEDIA_ROOT, que é usado para localizar onde os arquivos de mídia são armazenados no sistema de arquivos.
#2: 'Pillow' é usada para abrir, manipular e salvar arquivos de imagem. Neste contexto, é usada para redimensionar imagens.
#3: Esta função é usada para redimensionar imagens para uma nova largura (new_width), otimizá-las e ajustar sua qualidade. É útil para manter o tamanho do arquivo pequeno e a imagem com uma qualidade apropriada.
#4: Cria um caminho absoluto para a imagem usando o nome do arquivo e MEDIA_ROOT das configurações do Django. Esta linha calcula o caminho completo no sistema de arquivos onde a imagem está armazenada.
#5: O método resolve() é usado com objetos Path da biblioteca pathlib em Python. Ele converte um caminho (path) potencialmente relativo para um caminho absoluto, resolvendo todos os símbolos de link, links simbólicos e referências relativas como . (diretório atual) e .. (diretório pai).
#6: Abre a imagem localizada no caminho image_path usando a biblioteca Pillow. Carrega a imagem para manipulá-la (redimensionar, otimizar, etc.) usando a funcionalidade da biblioteca Pillow.
#7: Obtém a largura (original_width) e altura (original_height) da imagem original.
#8: Verifica se a largura original da imagem é menor ou igual à nova largura desejada. Se a imagem original já é menor ou igual à nova largura, a função retorna a imagem original sem redimensionamento.
#9: Fecha o arquivo de imagem para liberar os recursos associados. Quando a largura da imagem original é menor ou igual à new_width desejada, não é necessário redimensionar a imagem, e o arquivo de imagem é fechado imediatamente.
#10: Retorna o objeto Image original quando a imagem não precisa ser redimensionada.
#11: Calcula a nova altura da imagem mantendo a proporção original. A fórmula usada é uma regra de três simples. Garante que a imagem seja redimensionada proporcionalmente para evitar distorções.
#12: Cria uma nova imagem redimensionada usando o método resize() da biblioteca Pillow. O filtro Image.LANCZOS é utilizado para alta qualidade na redução do tamanho da imagem.
#13: Salva a nova imagem redimensionada no mesmo caminho da imagem original (image_path), usando os parâmetros optimize e quality para controlar a otimização e a qualidade de compressão da imagem. Substitui a imagem original pela versão redimensionada, o que é essencial quando queremos atualizar o arquivo de imagem no sistema de arquivos.