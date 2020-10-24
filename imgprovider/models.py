from django.db import models
from django.conf import settings
from django.utils import timezone

class ImgPost(models.Model): 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    rating = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    def publish(self):
            self.published_date = timezone.now()
            self.save()

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ForeignKey(ImgPost, on_delete=models.CASCADE)
    vote = models.BooleanField(null=True)

    class Meta:
        unique_together = ['user', 'image',]

    def set_vote(self, vote = None):
        if vote is not None:
            self.vote = vote

        self.save()

        if self.vote == True:
            self.image.rating += 1

        elif vote == False:
            self.image.rating -= 1

        self.image.save()