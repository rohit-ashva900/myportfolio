from django.shortcuts import render

def home(request):
    social_links = [
        {"id": 1, "href": "https://github.com", "icon": "GitHub Icon"},
        {"id": 2, "href": "https://linkedin.com", "icon": "LinkedIn Icon"},
        {"id": 3, "href": "https://x.com/rohit_ashva900", "icon": "LinkedIn Icon"},
        {"id": 4, "href": "https://linkedin.com", "icon": "LinkedIn Icon"},
        
        # Add more social links as needed
    ]
    skills = [
        {"id": 1, "text": "Python", "image": "🐍", "level": "Advanced"},
        {"id": 2, "text": "Django", "image": "🦄", "level": "Advanced"},
        {"id": 3, "text": "ReactJs", "image": "⚛️", "level": "Intermediate"},
        # Add more skills as needed
    ]
    
    return render(request, 'home.html', {'social_links': social_links,'skills': skills})


   

