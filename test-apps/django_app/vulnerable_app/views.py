from django.shortcuts import render

def vulnerable_view1(request):
    user_input = request.GET.get('name', 'Guest')
    return render(request, 'vulnerable.html', {'user_input': user_input})

def safe_view(request):
    user_input = request.GET.get('name', 'Guest')
    return render(request, 'safe.html', {'user_input': user_input})
