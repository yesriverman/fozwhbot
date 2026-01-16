from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def whatsapp_webhook(request):
    if request.method == "GET":
        # Verification challenge from Meta
        verify_token = "my_secure_verify_token"  # choose your own
        mode = request.GET.get('hub.mode')
        token = request.GET.get('hub.verify_token')
        challenge = request.GET.get('hub.challenge')

        if mode and token:
            if mode == 'subscribe' and token == verify_token:
                return JsonResponse(int(challenge), safe=False)
            else:
                return JsonResponse({"error": "Invalid token"}, status=403)
        return JsonResponse({"error": "No mode or token"}, status=400)

    elif request.method == "POST":
        data = json.loads(request.body)
        print("Webhook received:", json.dumps(data, indent=2))
        return JsonResponse({"status": "received"})
