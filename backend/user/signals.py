from django.db.models.signals import post_save, post_delete

from .models import User, Profile


def create_profile(sender, instance, created, **kwargs):
    if created:
        user=instance
        new_profile = Profile.objects.create(
            user=user,
            email=user.email,
            phone= user.phone,
            full_name=user.full_name,
        )
        

def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(create_profile, sender=User)


post_delete.connect(delete_user, sender=Profile)
