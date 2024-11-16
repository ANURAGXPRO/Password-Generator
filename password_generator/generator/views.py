# generator/views.py
from django.shortcuts import render
import random
import string

def index(request):
    password = None
    if request.method == 'POST':
        length = int(request.POST.get('length', 12))
        include_uppercase = 'uppercase' in request.POST
        include_lowercase = 'lowercase' in request.POST
        include_numbers = 'numbers' in request.POST
        include_symbols = 'symbols' in request.POST
        
        characters = ''
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_numbers:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation
        
        if characters:
            password = ''.join(random.choice(characters) for _ in range(length))
    
    return render(request, 'generator/index.html', {'password': password})
