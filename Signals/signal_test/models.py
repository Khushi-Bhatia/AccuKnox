from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading
from django.db import transaction

class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal receiver that listens for post_save signals
@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):
    # Proving signal is synchronous and in the same thread
    print(f"Signal received in thread: {threading.get_ident()} (signal handler)")
    
    # Proving signals are in the same database transaction by raising an error
    print("Signal received. Raising an exception to check transaction rollback...")
    raise Exception("Simulated signal handler error")
