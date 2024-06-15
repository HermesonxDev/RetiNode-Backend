from django.db import models
from uuid import uuid4

def upload_image_discussion(instance, filename):
    return f"{instance.postID}-{filename}"

def upload_image_logs(instance, filename):
    return f"{instance.logID}-{filename}"

def upload_image_user(instance, filename):
    return f"{instance.userID}-{filename}"

class User(models.Model):
    userID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField("Nome", max_length=255, null=False, blank=False)
    username = models.CharField("Nome do perfil", max_length=255, null=False, blank=False)
    date_of_birth = models.DateField("Data de nascimento", null=False, blank=False)
    email = models.EmailField("Email", max_length=255, null=False, blank=False)
    password = models.CharField("Senha", max_length=255, null=False, blank=False)
    image = models.ImageField("Foto de usuário", upload_to=upload_image_user, null=True, blank=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self) -> str:
        return self.name
    
class Discussions(models.Model):
    postID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    linkPost = models.CharField("Link pessoal", max_length=255, null=False, blank=False)
    date = models.DateTimeField("Data da publicação", auto_now_add=True, null=False, blank=False)
    title = models.CharField("Título", max_length=255, null=False, blank=False)
    description = models.TextField("Descrição", null=False, blank=False)
    image = models.ImageField("Imagem do post", upload_to=upload_image_discussion, null=True, blank=True)
    likes = models.IntegerField("Likes na publicação", default=0)
    reads = models.IntegerField("Leituras na publicação", default=0)

    class Meta:
        verbose_name = 'Discussão'
        verbose_name_plural = 'Discussões'

    def __str__(self) -> str:
        return "{} - Por {} - Publicado em {}".format(self.title, self.user.name, self.date)
    
class Logs(models.Model):
    logID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField("Título", max_length=255, default="Mudanças", editable=False, null=False, blank=False)
    subTitle = models.CharField("Sub-título", max_length=255, null=False, blank=False)
    description = models.CharField("Descrição", max_length=255, null=False, blank=False, default="Novas Mudanças chegaram ao RetiNode!")
    date = models.DateTimeField("Data", auto_now_add=True, null=False, blank=False)
    image = models.ImageField("Imagem", upload_to=upload_image_logs, null=True, blank=True)

    class Meta:
        verbose_name = 'Mudança'
        verbose_name_plural = 'Mudanças'

    def __str__(self) -> str:
        return "{} - Publicado em {}".format(self.title, self.date)
    
class Comments(models.Model):
    commentID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField("Comentário", max_length=255, null=False, blank=False)
    date = models.DateTimeField("Data", auto_now_add=True, null=False, blank=False)
    commented_post = models.ForeignKey(Discussions, on_delete=models.CASCADE)
    likes = models.IntegerField("Likes no comentário", default=0)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
    
    def __str__(self) -> str:
        return "Comentário de {} - Publicado em {}".format(self.user.name, self.date)