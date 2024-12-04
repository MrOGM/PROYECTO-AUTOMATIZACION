from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
from .serial_communication import send_command
import time
from icecream import ic


def Home(request):
    return render(request, "home.html")


def control_led(request):
    """
    Renders the webpage and handles LED control.
    """
    if request.method == "POST":
        action = request.POST.get("action")
        if action in ["R", "G", "B"]:
            send_command(action)

            # return JsonResponse({"status": f"LED turned {action}"})
    return render(request, "home.html")
