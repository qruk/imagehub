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

    def get_vote(self, user, vote):
        _vote = Vote.objects.filter(image = self, user = user)

        if _vote.exists():
            _vote = Vote.objects.get(image = self, user = user)
            
            if (vote != _vote.vote):
                _vote.vote = vote
                _vote.save()
                self.set_vote(vote)

        else:
            Vote.objects.create(user = user, image = self, vote = vote)
            self.set_vote(vote)

    def set_vote(self, vote):
        if vote == True:
            self.rating += 1
        elif vote == False:
            self.rating -= 1
        self.save()

    def update_rating(self):
        # TODO: function of hard rating update by counting SELECT strings in Vote model
        pass

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ForeignKey(ImgPost, on_delete=models.CASCADE)
    vote = models.BooleanField(null=True)