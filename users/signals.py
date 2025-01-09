from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile



# Signal pour créer automatiquement un profil lors de la création d'un utilisateur
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print(f"Signal appelé : création d'un profil pour {instance.username}")
        Profile.objects.create(user=instance)

# Signal pour sauvegarder le profil lors de la sauvegarde de l'utilisateur
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    print(f"Signal appelé : sauvegarde du profil pour {instance.username}")
    instance.profile.save()