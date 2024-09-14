# from django.shortcuts import render
# from .models import MyModel
# import time

# def create_my_model(request):
#     print("Starting request handling...")
#     instance = MyModel.objects.create(name="Test Instance")
#     print("Instance created. Waiting for signal processing to finish...")
#     return render(request, 'success.html')

from django.shortcuts import render
from .models import MyModel
import threading
from django.db import transaction

def create_my_model(request):
    try:
        # Wrap in atomic transaction to ensure rollback on error
        with transaction.atomic():
            # Proving signals are synchronous and in the same thread
            print(f"Request handling in thread: {threading.get_ident()} (view)")

            # Save a new instance to trigger the post_save signal
            print("Saving instance...")
            MyModel.objects.create(name="Test Instance")
            print("Instance saved. Waiting for signal...")
    
    except Exception as e:
        print(f"Exception caught: {e}")

    return render(request, 'success.html')
