from django.shortcuts import render


def profile(request):
    """
    A view to show the store homepage
    """
    return render(request, 'profile/profile.html')
