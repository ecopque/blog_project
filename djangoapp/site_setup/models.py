# FILE: /blog_project/djangoapp/site_setup/models.py

from django.db import models
from utils.model_validators import validate_png
from utils.images import resize_image

# EXPORT⬇: /blog_project/djangoapp/site_setup/admin.py
# URL⬇: http://127.0.0.1:8000/admin/site_setup/menulink/
class MenuLink(models.Model): #12:
    class Meta: #2:
        # URL⬇: http://127.0.0.1:8000/admin/
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'
    # URL⬇: http://127.0.0.1:8000/admin/site_setup/menulink/add/
    # IMPORT⬇: values/var from /blog_project/djangoapp/site_setup/admin.py
    text = models.CharField(max_length=50)
    # EXPORT⬇: /blog_project/djangoapp/templates/blog/partials/_header.html
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False) #6:
    # URL3⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/add/
    site_setup = models.ForeignKey('SiteSetup', on_delete=models.CASCADE, blank=True, null=True, default=None,) #3: #4: #14:
    def __str__(self): #7:
        return self.text

# URL⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/
# EXPORT⬇: /blog_project/djangoapp/site_setup/admin.py
class SiteSetup(models.Model): #15:
    class Meta: #2:
        # URL⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/
        verbose_name = 'Setup'
        verbose_name_plural = 'Setup'
    
    # URL⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/add/
    title = models.CharField(max_length=65) #8:
    description = models.CharField(max_length=255) #9:
    show_header = models.BooleanField(default=True) #10:
    show_search = models.BooleanField(default=True) #10:
    show_menu = models.BooleanField(default=True) #10:
    show_description = models.BooleanField(default=True) #10:
    show_pagination = models.BooleanField(default=True) #10:
    show_footer = models.BooleanField(default=True) #10:

    # URL⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/add/
    # EXPORT⬇: /blog_project/data/web/media/assets/favicon/"year"/"month"
    # IMPORT⬇: /blog_project/djangoapp/utils/model_validators.py
    favicon = models.ImageField(upload_to='assets/favicon/%Y/%m/', blank=True, default='', validators=[validate_png],) #17: #1:

    def save(self, *args, **kwargs): #5: #11:
        current_favicon_name = str(self.favicon.name) #13:
        print('current_favicon_name', current_favicon_name) #16:
        super().save(*args, **kwargs) #17:
        favicon_changed = False #18:

        if self.favicon: #19: #20:
            favicon_changed = current_favicon_name != self.favicon.name #21: #22:
        print('favicon_changed', favicon_changed)

        # IMPORT⬇: /blog_project/djangoapp/utils/images.py
        if favicon_changed: #23:
            resize_image(self.favicon, 32) #24:

    def __str__(self):
        return self.title #25:


#25: Em meus testes, se eu apontar tipo '{{site_setup}}' em algum template, vou ter como resposta o 'title'. Isto é sensacional.

# ------------------------------------------------------------------
#1: Estamos usando como 'validators=' a nossa função criada em 'model_validators.py'. Usa o 'validador validate_png', importado do módulo /blog_project/djangoapp/utils/model_validators.py, para garantir que o arquivo de imagem seja um PNG.
#5: Sobrescreve o método 'save' do modelo 'SiteSetup'. Customiza o comportamento de salvamento para adicionar uma lógica de verificação e manipulação da imagem de favicon. Permite executar código adicional antes e depois de salvar a instância no banco de dados.
#11: Porque estamos sobrescrevendo o método 'save()', se ele já tem sua função? Porque podemos executar algo antes e depois de salvar.
#13: Armazena o nome do arquivo favicon atual em uma variável 'current_favicon_name'.
#16 No terminal, vai aparecer o nome do arquivo que subiu. Se o arquivo for excluído, o print será vazio, sem o nome do arquivo.
#17: Precisamos que o nosos 'save()' agora atue como o 'save()' default.
#18: Inicializa a variável 'favicon_changed' como False. Esta variável é usada para acompanhar se o favicon foi alterado após o salvamento.
#19: Verifica se o campo favicon tem um valor (ou seja, se um favicon foi enviado). Se um favicon for fornecido, o código dentro do bloco if será executado.
#20: Se favicon for alterado (ou diferente ou True), retorne o print com True ou False.
#21: Verifica se o nome do favicon mudou após o salvamento. Atualiza a variável favicon_changed para True se o nome atual do favicon for diferente do nome armazenado antes do salvamento.
#22: Perceba que 'current_favicon_name' vem antes do 'save()'. 
#23: Verifica se o favicon foi alterado. Se 'favicon_changed' for True, o código dentro do bloco if será executado, iniciando o processo de redimensionamento da imagem.
#24: Chama a função resize_image para redimensionar o favicon para uma largura de 32 pixels.
# ------------------------------------------------------------------
#2: Os atributos 'verbose_name' e 'verbose_name_plural' definem como o modelo deve ser exibido na interface de administração do Django, no singular e no plural, respectivamente.
#3: 'Sitesetup' can have multiple 'MenuLinks'. Otherwise it cannot.
#4: Is you delete the link from 'site_setup', it will delete all links.
#6: Caixa de seleção do Django.
#7: String representation.
#8: Website title.
#9: Description field.
#10: Visible fields and if selected marked on Django Admin.
#12: Define a classe 'MenuLink', que herda de 'models.Model', tornando-a um modelo Django. Este modelo representa um link de menu na aplicação.
#14: Permite que vários 'MenuLinks' sejam associados a um único 'SiteSetup'. 'on_delete=models.CASCADE' garante que quando um 'SiteSetup' for excluído, todos os 'MenuLinks' relacionados também sejam excluídos.
#15: Define a classe 'SiteSetup', que herda de 'models.Model', tornando-a um modelo Django. Este modelo representa a configuração do site na aplicação.
#17: Permite o upload de um favicon, definindo onde as imagens serão armazenadas (upload_to) e permitindo que o campo seja opcional (blank=True) com um valor padrão de uma string vazia (default='').

# https://linktr.ee/edsoncopque