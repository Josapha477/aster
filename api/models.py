from django.db import models
from django.contrib.auth.models import User


class ProfilUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    bio = models.CharField(max_length=50)
    imgP = models.ImageField(upload_to='profil', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.bio}'
    

class PostUserVente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postuservente')
    description = models.TextField()
    prix = models.IntegerField()
    whatsapp = models.CharField(max_length=50)
    imgV = models.ImageField(upload_to='imgV')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.description} - {self.prix} - {self.whatsapp}'
    


class PostUserMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postusermedia')
    description = models.TextField()
    imgM = models.ImageField(upload_to='imgM')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.description} - {self.created_at}"
