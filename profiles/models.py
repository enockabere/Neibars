from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

User = get_user_model()
# Create your models here.

class Profile(models.Model):
    hood = models.CharField(blank=True,max_length=300)
    location = models.CharField(blank=True,max_length=300)
    bio = models.TextField(blank=True)
    image = CloudinaryField('image', blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,related_name='profile_user',)
    def __str__(self):
        return str(self.user)
class Hood(models.Model):
    hoods = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,related_name='allhood')
class Business(models.Model):
    name = models.CharField(blank=True,max_length=300)
    image = CloudinaryField('image', blank=True)
    info = models.TextField(blank=True)
    hood = models.ForeignKey(Hood,on_delete=models.CASCADE,blank=True,related_name="business_hood")
    owner =models.ForeignKey(User,on_delete=models.CASCADE,blank=True,related_name='owner')
    def __str__(self):
        return str(self.name)
class Post(models.Model):
    image = CloudinaryField('image',blank=True)
    description = models.TextField(blank=True)
    liked = models.ManyToManyField(User,blank=True,related_name='liked')
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,related_name='author')
    def __str__(self):
        return self.description
    @property
    def num_likes(self):
        return self.likes.all().count()
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike','Unlike'),
)
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like',max_length=10)
    
    def __str__(self):
        return str(self.post)
    