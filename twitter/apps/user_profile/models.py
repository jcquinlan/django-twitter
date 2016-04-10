from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name = 'profile')
    relation = models.ManyToManyField(
        'self',
        through = 'Relation',
        symmetrical = False,
        related_name = 'related_to',
        default = None
    )

    def __unicode__(self):
        return self.user.get_full_name()

class Relation(models.Model):
    follower = models.ForeignKey(UserProfile, related_name = 'follows')
    is_followed = models.ForeignKey(UserProfile, related_name = 'followers')
    followed_time = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return '%s follows %s' % (self.follower.user.username, self.is_followed.user.username)

    class Meta:
        unique_together = ('follower', 'is_followed')


def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user = user)

# post_save.connect(create_profile, sender = User)
