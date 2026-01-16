# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json

# VERIFY_TOKEN = "my_secure_verify_token"

# @csrf_exempt
# def whatsapp_webhook(request):
#     # STEP 1: Webhook verification (GET)
#     if request.method == "GET":
#         mode = request.GET.get("hub.mode")
#         token = request.GET.get("hub.verify_token")
#         challenge = request.GET.get("hub.challenge")

#         if mode == "subscribe" and token == VERIFY_TOKEN:
#             return HttpResponse(challenge, status=200)

#         return HttpResponse("Verification failed", status=403)

#     # STEP 2: Incoming messages (POST)
#     if request.method == "POST":
#         payload = json.loads(request.body.decode("utf-8"))
#         print("Webhook received:", json.dumps(payload, indent=2))
#         return JsonResponse({"status": "ok"}, status=200)

import requests
from django.conf import settings

def send_whatsapp_message(to, text):
    url = f"https://graph.facebook.com/v19.0/{settings.WHATSAPP_PHONE_ID}/messages"

    headers = {
        "Authorization": f"Bearer {settings.WHATSAPP_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {
            "body": text
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    print("Send message response:", response.text)



from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

VERIFY_TOKEN = "my_secure_verify_token"

@csrf_exempt
def whatsapp_webhook(request):

    if request.method == "GET":
        print("GET params:", request.GET)

        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")

        print("mode:", mode)
        print("token:", token)
        print("challenge:", challenge)

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)

        return HttpResponse("Verification failed", status=403)

    if request.method == "POST":
        payload = json.loads(request.body.decode("utf-8"))

    try:
        message = payload["entry"][0]["changes"][0]["value"]["messages"][0]
        sender = message["from"]
        text = message["text"]["body"]

        reply_text = f"مرحبا {sender} 👋\nتوصلنا برسالتك: {text}"
        send_whatsapp_message(sender, reply_text)

    except KeyError:
        pass  # ignore non-message events

    return JsonResponse({"status": "ok"}, status=200)



    # if request.method == "POST":
    #     payload = json.loads(request.body.decode("utf-8"))
    #     print(json.dumps(payload, indent=2))
    #     return JsonResponse({"status": "ok"}, status=200)






# @csrf_exempt
# def whatsapp_webhook(request):
#     if request.method == "GET":
#         # Verification challenge from Meta
#         verify_token = "my_secure_verify_token"  # choose your own
#         mode = request.GET.get('hub.mode')
#         token = request.GET.get('hub.verify_token')
#         challenge = request.GET.get('hub.challenge')

#         if mode and token:
#             if mode == 'subscribe' and token == verify_token:
#                 return JsonResponse(int(challenge), safe=False)
#             else:
#                 return JsonResponse({"error": "Invalid token"}, status=403)
#         return JsonResponse({"error": "No mode or token"}, status=400)

#     elif request.method == "POST":
#         data = json.loads(request.body)
#         print("Webhook received:", json.dumps(data, indent=2))
#         return JsonResponse({"status": "received"})
