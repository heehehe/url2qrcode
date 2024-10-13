from django.shortcuts import render
from django.http import JsonResponse
from modules.generate_qr_code import generate_qr_code


def home(request):
    return JsonResponse({'status': 'succeed'})


def get_qr_code(request):
    url = request.GET.get("url", "")
    response_type = request.GET.get("response_type", "json")
    qr_code = generate_qr_code(url)
    context = {'qr_code': qr_code}
    if response_type == "html":
        return render(request, 'qr_code.html', context)

    return JsonResponse(context)
