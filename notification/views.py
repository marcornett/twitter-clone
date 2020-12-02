from django.shortcuts import render
from .models import Notifications

def notification_view(request):
    notifications = Notifications.objects.all()
    # TODO: if a get request
    # TODO: if request.method == "GET":
    # TODO: then delete notifications currently here
    # TODO: notifications.delete()
    context = {'notifications': notifications}
    return render(request, 'notification/notifications.html', context)
    
