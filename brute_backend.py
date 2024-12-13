import secrets
import time
import threading

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

    def generate_guess(self, structure=None) -> str:
        if structure:
            guess = []
            for char_set in structure:
                index = secrets.randbelow(len(char_set))  # Random index in char_set
                guess.append(char_set[index])
            return ''.join(guess)
        else:
            guess = []
            for _ in range(self.password_length):
                index = secrets.randbelow(len(self.char_set))  # Random index in char_set
                guess.append(self.char_set[index])
            return ''.join(guess)

class BruteForceBackend:
    def __init__(self):
        self._running = False
        self._attempt_count = 0
        self._password_found = None
        self._elapsed_time = 0
        self._thread = None

    def start_brute_force(self, password: str, time_limit: int):
        if self._running:
            raise RuntimeError("Brute force is already running.")

        self._running = True
        self._attempt_count = 0
        self._password_found = None
        self._elapsed_time = 0
        #self.guess = None


        def brute_force_task():
            char_set_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            char_set_digits = '1234567890'
            char_set_special = '!@#$%^&*()_+-=[]{}|;:,.<>?'

            structure = []
            for char in password:
                if char in char_set_letters:
                    structure.append(char_set_letters)
                elif char in char_set_digits:
                    structure.append(char_set_digits)
                elif char in char_set_special:
                    structure.append(char_set_special)
                else:
                    raise ValueError("Unsupported character in password!")

            password_manager = PasswordManager(password)
            brute_force = BruteForce('', password_manager.get_password_length())

            start_time = time.time()
            while self._running:
                current_time = time.time()
                self._elapsed_time = current_time - start_time

                if self._elapsed_time > time_limit:
                    self._running = False
                    break

                guess = brute_force.generate_guess(structure)
                self._attempt_count += 1

                if password_manager.validate(guess):
                    self._password_found = guess
                    self._running = False
                else:
                    self._password_found = guess

        self._thread = threading.Thread(target=brute_force_task)
        self._thread.start()

    def get_status(self):
        return {
            "running": self._running,
            "attempt_count": self._attempt_count,
            "password_found": self._password_found,
            "elapsed_time": f"{self._elapsed_time:.2f}"
        }

    def stop_brute_force(self):
        self._running = False
        if self._thread:
            self._thread.join()

# CLI Testing
if __name__ == "__main__":
    backend = BruteForceBackend()

    def test_brute_force():
        password = input("Enter a password to test: ")
        time_limit = int(input("Enter time limit in seconds: "))

        backend.start_brute_force(password, time_limit)

        while True:
            status = backend.get_status()
            print(f"Status: {status}")
            time.sleep(1)

            if not status["running"]:
                print("Brute force completed.")
                break

    test_brute_force()
