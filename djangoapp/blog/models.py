# FILE: /blog/project/djangoapp/blog/models.py

from django.db import models
from utils.rands import slugify_new
from django.contrib.auth.models import User

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    # URL⬇: http://127.0.0.1:8000/admin/blog/tag/add/
    name = models.CharField(max_length=15) #2:
    slug = models.SlugField(unique=True, default=None, null=True, blank=True, max_length=255,) #3:
    
    def save(self, *args, **kwargs):
        if not self.slug: #1: #4:
            self.slug = slugify_new(self.name, 4) #5:
        return super().save(*args, **kwargs) #6:
    
    # URL⬇: http://127.0.0.1:8000/admin/blog/tag/1/change/
    def __str__(self) -> str: #8: #9:
        return self.name

class Category(models.Model): #7:
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=15)
    slug = models.SlugField(unique=True, default=None, null=True, blank=True, max_length=255,)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 4)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class Page(models.Model):
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
    # EXPORT⬇: /blog/project/djangoapp/blog/admin.py
    # URL⬇: http://127.0.0.1:8000/admin/blog/page/
    title = models.CharField(max_length=65,) #10:
    slug = models.SlugField(unique=True, default="", null=False, blank=True, max_length=255,)
    is_published = models.BooleanField(default=False, help_text=('This field must be checked for the page to be displayed publicly. Glu Glu, Yeh Yeh.'),) #11:
    content = models.TextField() #12:
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 4)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title
    
class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    title = models.CharField(max_length=65,) #10:
    slug = models.SlugField(unique=True, default="", null=False, blank=True, max_length=255,)
    excerpt = models.CharField(max_length=150) #13:
    is_published = models.BooleanField(default=False, help_text=('This field must be checked for the post to be displayed publicly.'),)

    content = models.TextField() #22:
    #EXPORT⬇: /blog_project/data/web/media/posts/year/month/
    cover = models.ImageField(upload_to='post/%Y/%m/', blank=True, default='') #14:
    cover_in_post_content = models.BooleanField(default=True, help_text='Display the cover image also within the post content?') #15:
    created_at = models.DateTimeField(auto_now_add=True) #16:
    updated_at = models.DateTimeField(auto_now=True) #17:
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='post_created_by') #20:
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='post_updated_by') #21:
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None,) #18:
    tags = models.ManyToManyField(Tag, blank=True, default='') #19:

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 4)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    

    
# ------------------------------------------------------------------
#13: Este camarada será o resumo do nosso post. Este campo armazena um resumo ou uma breve descrição de um post.
#14: Este aqui será a capa do post. 'cover' é um campo do modelo Post definido como um ImageField, que é um campo específico para o upload de imagens. O parâmetro upload_to='post/%Y/%m/' indica o diretório dentro de MEDIA_ROOT onde as imagens enviadas serão armazenadas, organizadas por ano (%Y) e mês (%m). blank=True permite que este campo seja opcional e default='' define um valor padrão vazio.
#15: Se marcado, vai exibir a imagem de capa dentro do post. 'cover_in_post_content' é um campo booleano (BooleanField) que determina se a imagem de capa (cover) também será exibida dentro do conteúdo do post. default=True significa que, por padrão, a imagem será exibida no conteúdo do post, e help_text fornece uma dica para os usuários do painel de administração do Django.
#16: Este é o campo de data do post. Quando o post for salvo ele vai adicionar a data ao post. 'created_at' é um campo do modelo Post definido como um DateTimeField. O parâmetro auto_now_add=True faz com que a data e hora atuais sejam automaticamente definidas quando o objeto é criado. Este campo geralmente é usado para rastrear quando um post foi criado.
#17: Toda vez que salvar o post vai ser gerado uma nova data. 'updated_at' é um campo do modelo Post definido como um DateTimeField. O parâmetro auto_now=True faz com que a data e hora sejam automaticamente atualizadas sempre que o objeto for salvo. 
#18: Terei muitos posts que poderão estar na mesma categoria, mas quando apagar uma categoria o post não será deletado. 'category' é um campo ForeignKey que cria um relacionamento entre o modelo Post e o modelo Category. on_delete=models.SET_NULL indica que, se a categoria associada for excluída, o valor deste campo será definido como NULL. null=True e blank=True permitem que este campo seja opcional, e default=None define o valor padrão como None.
#19: 'tags' é um campo ManyToManyField que cria um relacionamento muitos-para-muitos entre o modelo Post e o modelo Tag. blank=True permite que este campo seja opcional, e default='' define o valor padrão como uma string vazia.
#20: user.post_created_by.all. created_by é um campo ForeignKey que cria um relacionamento entre o modelo Post e o modelo User do Django (importado de django.contrib.auth.models). Este campo rastreia o usuário que criou o post. on_delete=models.SET_NULL define o valor como NULL se o usuário for excluído. blank=True e null=True permitem que o campo seja opcional, e related_name='post_created_by' define o nome para referenciar esse campo no relacionamento reverso.
#21: user.post_updated_by.all. updated_by é semelhante ao campo created_by, mas rastreia o usuário que atualizou o post pela última vez. As opções on_delete=models.SET_NULL, blank=True, null=True, e related_name='post_updated_by' funcionam da mesma forma.
#22: Diferentemente de CharField, TextField não tem limite de comprimento, sendo apropriado para o corpo principal de um post, onde o conteúdo é mais extenso.
# ------------------------------------------------------------------
#7: Após criar o 'Category()' e 'CategoryAdmin()' você precisa realizar o makemigrations. Melhor rodar o comando 'docker compose up --build --force-recreate'.
#8: Se eu não inserir o 'def __str__()', na url (http://127.0.0.1:8000/admin/blog/category/1/change/) vai aparecer: 'Category object (1)' em vez de 'First Category'.
#9: O método __str__ é um método especial do Python que retorna uma string que representa o objeto. Neste caso, para a classe Tag, ele retorna o valor do atributo name da instância. Isso é útil quando você deseja uma representação legível do objeto. Por exemplo, no Django Admin, ao listar objetos Tag, o nome da tag será mostrado ao invés de "Tag object (1)", etc.
#10: Define o campo title da model Page como um CharField (campo de caracteres) com um comprimento máximo de 65 caracteres. Esse campo é necessário para armazenar o título da página.
#11: Define o campo is_published como um BooleanField (campo booleano) que indica se a página deve ser exibida publicamente ou não. O valor padrão é False, o que significa que a página não está publicada até que este campo seja marcado como True. O argumento help_text fornece uma mensagem de ajuda que será exibida no Django Admin.
#12: Define o campo content da model Page como um TextField, que é um campo de texto grande. Este campo é utilizado para armazenar o conteúdo da página. Essencial para armazenar o conteúdo da página, como artigos, textos de blog, conteúdo html, informações, etc.
# ------------------------------------------------------------------
#1: Se a pessoa não tiver enviado uma slug, vou gerar uma nova 'slug'.
#2: Esse campo é do tipo CharField, que armazena uma string com comprimento máximo de 15 caracteres. Este campo representará o nome da tag.
#3: Define um campo chamado slug no modelo Tag. Este campo é do tipo SlugField, que armazena strings "slugificadas" (normalmente usadas em URLs). O campo slug é configurado como único (unique=True), o que significa que cada slug deve ser único no banco de dados. Também permite valores None (com null=True) e valores em branco (com blank=True), com comprimento máximo de 255 caracteres.
#4: A condição if not self.slug verifica se o campo slug da instância do modelo Tag está vazio. Se estiver, ele entrará no bloco de código a seguir.
#5: A função slugify_new cria um "slug" a partir do name e adiciona 4 caracteres aleatórios ao final (detalhes dessa função estão explicados no módulo 'admin.py' do projeto).
#6:  Chama o método save() da classe pai (models.Model) para salvar a instância no banco de dados. O uso de super() garante que a implementação padrão do Django para salvar objetos seja executada.

# https://linktr.ee/edsoncopque