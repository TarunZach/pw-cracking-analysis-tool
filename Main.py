"""
[*] Software Optimization Project Winter 2024
[*] Version: 0.0.1
[*] Team Members:
[*] Shayan Rahimian - Number 1
[*] Aida Shard - Number 2
[*] Anamay Brahme - Number 3
[*] Mahdi - Number 4
[*] Saeedeh - Number 5
[*] Tarun Zacharias - Number 6
[*] Reza - Number 7
"""

import random
import string
import re
import tkinter as tk
from tkinter import ttk, messagebox
import secrets
import time  # Simulating time for the progress bar
import hashlib


class PasswordAnalysisTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Cyber Security Password Analyzer")
        self.root.geometry("1200x800")

        # Color Scheme
        self.bg_color = "#0A0A1A"  # Deep dark blue-black
        self.fg_color = "#E0E0FF"  # Soft light blue-white
        self.accent_color = "#00FFFF"  # Bright cyan neon
        self.button_bg = "#000000"  # Pure black button background

        # Star animation parameters
        self.stars = []
        self.max_stars = 100

        # Create background canvas for star animation
        self.create_starry_background()

        # Create main application
        self.create_main_page()

    def create_starry_background(self):
        # Background canvas for star animation
        self.bg_canvas = tk.Canvas(self.root, bg=self.bg_color, highlightthickness=0)
        self.bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)

        # Create stars
        for _ in range(self.max_stars):
            x = random.randint(0, 1200)
            y = random.randint(0, 800)
            size = random.uniform(1, 3)
            star = self.bg_canvas.create_oval(
                x, y, x + size, y + size, fill="white", outline=""
            )
            self.stars.append(
                {
                    "obj": star,
                    "x": x,
                    "y": y,
                    "size": size,
                    "speed": random.uniform(0.1, 0.5),
                }
            )

        # Start star animation
        self.animate_stars()

    def animate_stars(self):
        for star in self.stars:
            # Move star
            star["y"] += star["speed"]

            # Reset star if it goes below screen
            if star["y"] > 800:
                star["y"] = 0
                star["x"] = random.randint(0, 1200)

            # Update star position
            self.bg_canvas.move(star["obj"], 0, star["speed"])

        # Continue animation
        self.root.after(50, self.animate_stars)

    def create_main_page(self):
        # Main frame
        self.main_frame = tk.Frame(self.root, bg=self.bg_color)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Add SVG image at the top of the main page
        self.password_icon = tk.Label(
            self.main_frame,
            text="🔒",  # Placeholder for SVG image
            font=("Arial", 64),
            bg=self.bg_color,
            fg=self.accent_color,
        )
        self.password_icon.pack(pady=(0, 20))

        # Title
        title_label = tk.Label(
            self.main_frame,
            text="Password Security Analyzer",
            font=("Arial", 24, "bold"),
            bg=self.bg_color,
            fg=self.accent_color,
        )
        title_label.pack(pady=(0, 20))

        # Display "SAMPLE" text under the title
        sample_label = tk.Label(
            self.main_frame,
            text="Software Opmization Project Winter 2024",
            font=("Arial", 18, "italic"),
            bg=self.bg_color,
            fg=self.accent_color,
        )
        sample_label.pack(pady=(0, 20))

        # Password Entry
        self.password_entry = tk.Entry(
            self.main_frame,
            show="*",
            font=("Courier", 18),
            width=30,
            bg="white",
            fg=self.bg_color,
            insertbackground=self.accent_color,
        )
        self.password_entry.pack(pady=20)

        # Real-time Analysis Label
        self.analysis_label = tk.Label(
            self.main_frame,
            text="Password Strength: N/A",
            font=("Arial", 16),
            bg=self.bg_color,
            fg=self.accent_color,
        )
        self.analysis_label.pack(pady=10)

        # Bind real-time analysis
        self.password_entry.bind("<KeyRelease>", self.analyze_password_strength)

        # Buttons
        buttons_config = [
            ("BRUTE FORCE", self.open_brute_force_window),
            ("DICTIONARY", self.open_dictionary_attack_window),
            ("RAINBOW TABLE", self.open_rainbow_table_window),
            ("ABOUT", self.show_about),
            ("EXIT", self.exit_application),
        ]

        for text, command in buttons_config:
            btn = tk.Button(
                self.main_frame,
                text=text,
                command=command,
                font=("Arial", 16, "bold"),
                width=25,
                bg=self.button_bg,
                fg="blue",  # Updated font color
                activebackground="#1A1A3A",
                activeforeground=self.fg_color,
            )
            btn.pack(pady=10)

    def analyze_password_strength(self, event=None):
        password = self.password_entry.get()
        strength = self.calculate_password_strength(password)

        # Update strength label with color coding
        if strength < 30:
            color = "red"
            level = "Very Weak"
        elif strength < 60:
            color = "orange"
            level = "Weak"
        elif strength < 80:
            color = "yellow"
            level = "Moderate"
        else:
            color = "green"
            level = "Strong"

        self.analysis_label.config(
            text=f"Password Strength: {level} ({strength}%)", fg=color
        )

    def calculate_password_strength(self, password):
        """
        Replaces the original password strength calculation with your custom score logic.
        Returns an integer from 0 to 100.
        """

        # Edge case: empty or very short password
        if not password or len(password.strip()) == 0:
            return 0

        score = 0

        # --- Check for common password file ---
        try:
            with open("./dst/common_1mil.txt", "r") as f:
                common = f.read().splitlines()
            if password in common:
                # Password is too common, immediate score 0
                return 0
        except FileNotFoundError:
            # If the file doesn't exist, just skip this step
            pass

        # --- Check length ---
        length = len(password)
        if length > 8:
            score += 1
        if length > 12:
            score += 1
        if length > 16:
            score += 1
        if length > 20:
            score += 1

        # --- Character diversity ---
        upper_case = any(c.isupper() for c in password)
        lower_case = any(c.islower() for c in password)
        special = any(c in string.punctuation for c in password)
        digits = any(c.isdigit() for c in password)
        char_types_count = sum([upper_case, lower_case, special, digits])

        if char_types_count > 1:
            score += 1
        if char_types_count > 2:
            score += 1
        if char_types_count > 3:
            score += 1

        # --- Check for common names in password ---
        try:
            with open("./dst/filtered_names.txt", "r") as N:
                names = N.read().splitlines()
            for name in names:
                if name.lower() in password.lower():
                    score -= 1
                    break
        except FileNotFoundError:
            pass

        # --- Check for repeated characters (3+ in a row) ---
        repeated_chars = re.search(r"(.)\1{2,}", password)
        if repeated_chars:
            score -= 1

        # --- Check for numeric sequences ---
        numeric_sequence = re.search(
            r"(012|123|234|345|456|567|678|789|890|987|876|765|654|543|432|321|210)",
            password,
        )
        if numeric_sequence:
            score -= 1

        # --- Check for common keyboard patterns ---
        try:
            with open("./dst/keyboard_patterns.txt", "r") as kp_file:
                keyboard_patterns = kp_file.read().splitlines()
            for pattern in keyboard_patterns:
                if pattern.lower() in password.lower():
                    score -= 1
                    break
        except FileNotFoundError:
            pass

        # Ensure final score is within 0–7
        if score < 0:
            score = 0
        elif score > 7:
            score = 7

        # Convert 0–7 score to a percentage (0–100)
        strength_percentage = int((score / 7) * 100)
        return strength_percentage

    def open_brute_force_window(self):
        self.create_attack_window("Brute Force Attack", self.perform_brute_force_action)

    def open_dictionary_attack_window(self):
        self.create_attack_window(
            "Dictionary Attack", self.perform_dictionary_attack_action
        )

    def open_rainbow_table_window(self):
        self.create_attack_window(
            "Rainbow Table Attack", self.perform_rainbow_table_action
        )

    def perform_brute_force_action(self, text_box):
        attack_name = "Brute Force Attack"
        delay = 0.05

        # Create the attack window first
        attack_window = tk.Toplevel()
        attack_window.title(attack_name)

        # # Create and pack the label
        # label = tk.Label(attack_window, text=f"{attack_name} in Progress...").pack(
        #     pady=10
        # )

        # Create and pack the progress bar
        progress = ttk.Progressbar(
            attack_window, orient="horizontal", length=300, mode="determinate"
        )
        progress.pack(pady=10)

        # Hardcoded password for brute force simulation
        print(str(text_box.get("1.0", tk.END)))
        password = str(
            text_box.get("1.0", tk.END).replace("\n", "")
        )  # Example password to crack
        time_limit = 180  # Time limit for the brute-force simulation (in seconds)

        # Character sets for brute force
        char_set_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        char_set_digits = "1234567890"
        char_set_special = "!@#$%^&*()_+-=[]{}|;:,.<>?"

        # Creating structure for password
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

        # Brute force simulation (simplified)
        attempt_count = 0
        password_found = None
        start_time = time.time()

        def generate_guess():
            guess = []
            for char_set in structure:
                index = secrets.randbelow(len(char_set))
                guess.append(char_set[index])
            return "".join(guess)

        while time.time() - start_time < time_limit:
            guess = generate_guess()
            print(generate_guess())
            attempt_count += 1

            if guess == password:
                password_found = guess
                break

            # Update the progress bar
            progress["value"] = attempt_count % 101
            attack_window.update_idletasks()
            time.sleep(delay)

        elapsed_time = time.time() - start_time

        if password_found:
            messagebox.showinfo(
                attack_name,
                f"{attack_name} Completed! Password Found: {password_found} in {elapsed_time:.2f} seconds",
            )
            progress.pack_forget()

        else:
            messagebox.showinfo(
                attack_name,
                f"{attack_name} Completed! Password not found within the {time_limit} seconds.",
            )
            progress.destroy()

        # Update the text box with status
        progress.pack_forget()
        attack_window.destroy()
        text_box.insert(tk.END, "\nSimulating Brute Force Attack...\n")
        text_box.insert(tk.END, "\nCompleted! Password Found: " + password_found + "\n")

        # text_box.insert(tk.END, "\n"+password_found+"\n")

    def perform_dictionary_attack_action(self, text_box):
        attack_name = "Dictionary Attack"
        delay = 0.05

        # Create the attack window
        attack_window = tk.Toplevel()
        attack_window.title(attack_name)

        # Create and pack the label
        tk.Label(attack_window, text=f"{attack_name} in Progress...").pack(pady=10)

        # Create and pack the progress bar
        progress = ttk.Progressbar(
            attack_window, orient="horizontal", length=300, mode="determinate"
        )
        progress.pack(pady=10)

        # Get the target password from the text box
        target_password = text_box.get("1.0", tk.END).strip()

        # Load the wordlist
        wordlist_file = "./dst/passwords.txt"
        try:
            with open(wordlist_file, "r") as wfile:
                wordlist = [line.strip() for line in wfile if line.strip()]
        except FileNotFoundError:
            messagebox.showerror(
                attack_name, f"Error: Wordlist file '{wordlist_file}' not found."
            )
            attack_window.destroy()
            return

        total_words = len(wordlist)
        progress["value"] = 0  # Initialize progress

        # Define hash comparison mode (set to True if target_password is hashed)
        hash_mode = False

        # Helper function to hash the word
        def hash_password(word):
            return hashlib.sha256(word.encode()).hexdigest()

        # Calculate and display estimated time
        estimated_time = total_words * delay
        est_minutes, est_seconds = divmod(estimated_time, 60)
        tk.Label(
            attack_window,
            text=f"Estimated Time: {int(est_minutes)} minutes, {int(est_seconds)} seconds",
        ).pack(pady=5)

        # Start the attack
        for attempt_count, candidate in enumerate(wordlist, 1):
            # Update the progress bar
            progress["value"] = (attempt_count / total_words) * 100
            attack_window.update_idletasks()

            # Perform comparison
            attempt = hash_password(candidate) if hash_mode else candidate
            if attempt == target_password:
                # Success: Update the UI and display success message
                text_box.insert(tk.END, f"\nSuccess! Password found: {candidate}\n")
                text_box.see(tk.END)
                messagebox.showinfo(
                    attack_name,
                    f"{attack_name} Completed!\nPassword Found: {candidate}",
                )
                attack_window.destroy()
                return

            # Log the attempt in the text box
            text_box.insert(tk.END, f"Trying password: {candidate}\n")
            text_box.see(tk.END)

            # Add delay to simulate realistic attack speed
            time.sleep(delay)

        # If password is not found
        text_box.insert(tk.END, "\nPassword not found in the wordlist.\n")
        text_box.see(tk.END)
        messagebox.showinfo(
            attack_name, f"{attack_name} Completed!\nPassword not found."
        )
        attack_window.destroy()

    def perform_rainbow_table_action(self, text_box):
        import hashlib
        import time

        attack_name = "Rainbow Table"
        delay = 0.02  # Reduced delay for faster progress bar updates

        attack_window = tk.Toplevel()
        attack_window.title(attack_name)

        # Create and pack the label
        tk.Label(attack_window, text=f"{attack_name} in Progress...").pack(pady=10)

        progress = ttk.Progressbar(
            attack_window, orient="horizontal", length=300, mode="determinate"
        )
        progress.pack(pady=10)

        rainbow_table_file = "./dst/rainbow_table_file.txt"
        hash_function = hashlib.md5

        try:
            # Step 1: Collect user input from the text box
            user_input = text_box.get("1.0", tk.END).strip()

            if not user_input:
                messagebox.showerror(attack_name, "No input provided in the text box.")
                attack_window.destroy()
                return

            # Step 2: Determine if input is already a hash
            is_hash = len(user_input) == 32 and all(
                c in "0123456789abcdef" for c in user_input.lower()
            )

            if not is_hash:
                # Input is a plaintext password, hash it and display the hash
                user_password_hash = hash_function(user_input.encode()).hexdigest()
                text_box.insert(tk.END, f"\nInput hashed: {user_password_hash}\n")
                messagebox.showinfo(
                    attack_name, f"Hash of the password: {user_password_hash}"
                )
                # Stop further execution since this was a plaintext input
                attack_window.destroy()
                return

            # If input is a hash, proceed with comparison
            user_password_hash = user_input

            # Step 3: Read the rainbow table file
            with open(rainbow_table_file, "r") as file:
                lines = file.readlines()

            # Parse the rainbow table into a dictionary
            rainbow_table = {}
            for line in lines:
                password, hash_value = line.strip().split(":")
                rainbow_table[hash_value] = password

            # Step 4: Compare the user's hash with the rainbow table
            total_hashes = len(rainbow_table)
            progress_step = 100 / total_hashes

            found_password = None
            for index, (hash_value, password) in enumerate(
                rainbow_table.items(), start=1
            ):
                progress["value"] = index * progress_step
                attack_window.update_idletasks()
                time.sleep(delay)

                if hash_value == user_password_hash:
                    found_password = password
                    break

            # Display results
            if found_password:
                messagebox.showinfo(
                    attack_name,
                    f"Password found: {found_password}\nHash: {user_password_hash}",
                )
            else:
                messagebox.showinfo(
                    attack_name, "Password not found in the rainbow table."
                )

        except Exception as e:
            messagebox.showerror(attack_name, f"An error occurred: {str(e)}")

        # Cleanup: Hide or destroy the label, progress bar, and attack window
        progress.pack_forget()
        attack_window.destroy()

        # Update the text box with the result
        text_box.insert(
            tk.END, f"\n{attack_name} operation completed. Check results above.\n"
        )

    def show_about(self):
        top = tk.Toplevel(self.root)
        top.title("About Us")
        top.geometry("800x600")
        top.configure(bg=self.bg_color)

        label = tk.Label(
            top,
            text="About Us",
            font=("Arial", 25, "bold"),
            bg=self.bg_color,
            fg=self.accent_color,
        )
        label.pack(pady=20)

        about_text = """
This application is developed to help users analyze password strength and learn about security techniques by
        ✔️ Shayan Rhimi
        ✔️ Aida Sharbatdar
        ✔️ Anamay Charudatta Brahme
        ✔️ Mahdi Roshanizarmehri
        ✔️ Saeedeh Alamkar
        ✔️ Tarun Zacharias Akkarakalam
        ✔️ Mohammadreza Rashidi
        """
        about_label = tk.Label(
            top,
            text=about_text,
            font=("Arial", 22),
            bg=self.bg_color,
            fg=self.fg_color,
            wraplength=450,
            justify="left",
        )
        about_label.pack(pady=20)

        close_button = tk.Button(
            top,
            text="Close",
            command=top.destroy,
            font=("Arial", 14, "bold"),
            bg=self.button_bg,
            fg="blue",
        )
        close_button.pack(pady=10)

    def create_attack_window(self, title, action_function):
        top = tk.Toplevel(self.root)
        top.title(title)
        top.geometry("400x300")
        top.configure(bg=self.bg_color)

        label = tk.Label(
            top,
            text=f"{title} Window",
            font=("Arial", 18, "bold"),
            bg=self.bg_color,
            fg=self.accent_color,
        )
        label.pack(pady=20)

        text_box = tk.Text(
            top,
            height=5,
            width=40,
            bg="black",
            fg=self.fg_color,
            font=("Courier", 12),
            wrap="word",
        )
        text_box.pack(pady=10)

        action_button = tk.Button(
            top,
            text="Start",
            command=lambda: action_function(text_box),
            font=("Arial", 14, "bold"),
            bg=self.button_bg,
            fg="blue",
            activebackground="#1A1A3A",
            activeforeground=self.fg_color,
        )
        action_button.pack(pady=10)

        close_button = tk.Button(
            top,
            text="Close",
            command=top.destroy,
            font=("Arial", 14, "bold"),
            bg=self.button_bg,
            fg="blue",
            activebackground="#1A1A3A",
            activeforeground=self.fg_color,
        )
        close_button.pack(pady=10)

    def exit_application(self):
        self.root.destroy()


# Create main application window
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordAnalysisTool(root)
    root.mainloop()
