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
        print(json.dumps(payload, indent=2))
        return JsonResponse({"status": "ok"}, status=200)






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
