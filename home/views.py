from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

def home(request):
    social_links = [
        {"id": 1, "href": "https://github.com", "icon": "GitHub Icon"},
        {"id": 2, "href": "https://linkedin.com", "icon": "LinkedIn Icon"},
        {"id": 3, "href": "https://x.com/rohit_ashva900", "icon": "Twitter Icon"},
        {"id": 4, "href": "https://linkedin.com", "icon": "LinkedIn Icon"},
    ]
    skills = [
        {"id": 1, "text": "Python", "image": "🐍", "level": "Advanced"},
        {"id": 2, "text": "Django", "image": "🦄", "level": "Advanced"},
        {"id": 3, "text": "ReactJs", "image": "⚛️", "level": "Intermediate"},
    ]

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for contacting us.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, 'home.html', {'social_links': social_links, 'skills': skills, 'form': form})
