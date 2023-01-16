from django.shortcuts import render


def profile(request):
    """
    A view to show the user profile page
    """
    return render(request, 'profile/profile.html')
