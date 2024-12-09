# brute_force_app/views.py

from django.shortcuts import render
from .forms import PasswordForm
from random import randint

class PasswordManager:
    def __init__(self, password: str):
        self._password = password

    def validate(self, guess: str) -> bool:
        return self._password == guess

    def get_password_length(self) -> int:
        return len(self._password)

class BruteForce:
    def __init__(self, char_set: str, password_length: int):
        self.char_set = char_set
        self.password_length = password_length

    def generate_guess(self) -> str:
        return ''.join(self.char_set[randint(0, len(self.char_set) - 1)] for _ in range(self.password_length))

def brute_force_view(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            user_pass = form.cleaned_data['password']
            password_manager = PasswordManager(user_pass)
            brute_force = BruteForce('abcdefghijklmnopqrstuvwxyz1234567890', password_manager.get_password_length())
            
            attempt_count = 0
            attempts = []
            while True:
                guess = brute_force.generate_guess()
                attempt_count += 1
                attempts.append(guess)
                if password_manager.validate(guess):
                    return render(request, 'brute_force_app/result.html', {
                        'password': guess,
                        'attempts': attempt_count,
                        'attempts_list': attempts
                    })
    else:
        form = PasswordForm()

    return render(request, 'brute_force_app/brute_force.html', {'form': form})