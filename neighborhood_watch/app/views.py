from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Alert

def index(request):
    return render(request, 'index.html')

def alert(request):
    alerts = Alert.objects.all()
    return render(request, 'alert.html', {'alerts': alerts})
@csrf_exempt
def add_alert(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            # If the user is authenticated, use their instance; otherwise, set to None
            user = request.user if request.user.is_authenticated else None
            alert = Alert(user=user, message=message)
            alert.save()
            return redirect('alert')
        else:
            return JsonResponse({'error': 'Message is required'}, status=400)
    return render(request, 'add_alert.html')


# @csrf_exempt
# def add_alert(request):
#     try:
#         data = json.loads(request.body)
#         message = data.get('message')
#         if message:
#             Alert.objects.create(user=request.user, message=message)
#             return JsonResponse({'status': 'success'})
#         return JsonResponse({'status': 'error', 'message': 'Message is required'}, status=400)
#     except json.JSONDecodeError:
#         return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)