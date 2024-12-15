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
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time  # Simulating time for the progress bar

class PasswordAnalysisTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Cyber Security Password Analyzer")
        self.root.geometry("1200x800")

        # Color Scheme
        self.bg_color = '#0A0A1A'  # Deep dark blue-black
        self.fg_color = '#E0E0FF'  # Soft light blue-white
        self.accent_color = '#00FFFF'  # Bright cyan neon
        self.button_bg = '#000000'  # Pure black button background

        # Star animation parameters
        self.stars = []
        self.max_stars = 100

        # Create background canvas for star animation
        self.create_starry_background()

        # Create main application
        self.create_main_page()

    def create_starry_background(self):
        # Background canvas for star animation
        self.bg_canvas = tk.Canvas(
            self.root,
            bg=self.bg_color,
            highlightthickness=0
        )
        self.bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)

        # Create stars
        for _ in range(self.max_stars):
            x = random.randint(0, 1200)
            y = random.randint(0, 800)
            size = random.uniform(1, 3)
            star = self.bg_canvas.create_oval(
                x, y, x + size, y + size,
                fill='white',
                outline=''
            )
            self.stars.append({
                'obj': star,
                'x': x,
                'y': y,
                'size': size,
                'speed': random.uniform(0.1, 0.5)
            })

        # Start star animation
        self.animate_stars()

    def animate_stars(self):
        for star in self.stars:
            # Move star
            star['y'] += star['speed']

            # Reset star if it goes below screen
            if star['y'] > 800:
                star['y'] = 0
                star['x'] = random.randint(0, 1200)

            # Update star position
            self.bg_canvas.move(
                star['obj'],
                0,
                star['speed']
            )

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
            font=('Arial', 64),
            bg=self.bg_color,
            fg=self.accent_color
        )
        self.password_icon.pack(pady=(0, 20))

        # Title
        title_label = tk.Label(
            self.main_frame,
            text="Password Security Analyzer",
            font=('Arial', 24, 'bold'),
            bg=self.bg_color,
            fg=self.accent_color
        )
        title_label.pack(pady=(0, 20))

        # Display "SAMPLE" text under the title
        sample_label = tk.Label(
            self.main_frame,
            text="Software Opmization Project Winter 2024",
            font=('Arial', 18, 'italic'),
            bg=self.bg_color,
            fg=self.accent_color
        )
        sample_label.pack(pady=(0, 20))

        # Password Entry
        self.password_entry = tk.Entry(
            self.main_frame,
            show='*',
            font=('Courier', 18),
            width=30,
            bg='white',
            fg=self.bg_color,
            insertbackground=self.accent_color
        )
        self.password_entry.pack(pady=20)

        # Real-time Analysis Label
        self.analysis_label = tk.Label(
            self.main_frame,
            text="Password Strength: N/A",
            font=('Arial', 16),
            bg=self.bg_color,
            fg=self.accent_color
        )
        self.analysis_label.pack(pady=10)

        # Bind real-time analysis
        self.password_entry.bind('<KeyRelease>', self.analyze_password_strength)

        # Buttons
        buttons_config = [
            ("BRUTE FORCE", self.open_brute_force_window),
            ("DICTIONARY", self.open_dictionary_attack_window),
            ("RAINBOW TABLE", self.open_rainbow_table_window),
            ("ABOUT", self.show_about),
            ("EXIT", self.exit_application)
        ]

        for text, command in buttons_config:
            btn = tk.Button(
                self.main_frame,
                text=text,
                command=command,
                font=('Arial', 16, 'bold'),
                width=25,
                bg=self.button_bg,
                fg='blue',  # Updated font color
                activebackground='#1A1A3A',
                activeforeground=self.fg_color
            )
            btn.pack(pady=10)

    def analyze_password_strength(self, event=None):
        password = self.password_entry.get()
        strength = self.calculate_password_strength(password)

        # Update strength label with color coding
        if strength < 30:
            color = 'red'
            level = 'Very Weak'
        elif strength < 60:
            color = 'orange'
            level = 'Weak'
        elif strength < 80:
            color = 'yellow'
            level = 'Moderate'
        else:
            color = 'green'
            level = 'Strong'

        self.analysis_label.config(
            text=f"Password Strength: {level} ({strength}%)",
            fg=color
        )

    def calculate_password_strength(self, password):
        # Comprehensive password strength calculation
        strength = 0

        # Length bonus
        length_bonus = min(len(password) * 4, 40)
        strength += length_bonus

        # Complexity bonuses
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(not c.isalnum() for c in password)

        if has_upper:
            strength += 10
        if has_lower:
            strength += 10
        if has_digit:
            strength += 10
        if has_special:
            strength += 20

        # Penalize common patterns
        common_patterns = ['123', 'abc', 'qwe', 'password']
        for pattern in common_patterns:
            if pattern in password.lower():
                strength -= 10

        # Ensure strength is between 0-100
        return max(0, min(100, strength))

    def open_brute_force_window(self):
        self.create_attack_window("Brute Force Attack", self.perform_brute_force_action)

    def open_dictionary_attack_window(self):
        self.create_attack_window("Dictionary Attack", self.perform_dictionary_attack_action)

    def open_rainbow_table_window(self):
        self.create_attack_window("Rainbow Table Attack", self.perform_rainbow_table_action)

    def perform_brute_force_action(self, text_box):
        attack_name = "Simulate Attack"
        delay = 0.05

        # Create the attack window first
        attack_window = tk.Toplevel()
        attack_window.title(attack_name)
        
        # Create and pack the label
        tk.Label(attack_window, text=f"{attack_name} in Progress...").pack(pady=10)
        
        # Create and pack the progress bar
        progress = ttk.Progressbar(attack_window, orient="horizontal", length=300, mode="determinate")
        progress.pack(pady=10)

        # Now update the progress bar
        for i in range(101):
            progress['value'] = i
            attack_window.update_idletasks()
            time.sleep(delay)
        
        # Show completion message
        messagebox.showinfo(attack_name, f"{attack_name} Completed!")
        
        # Update the text box
        text_box.insert(tk.END, "\nSimulating Brute Force Attack...\n")




    def perform_dictionary_attack_action(self, text_box):
        attack_name = "Dictionary Attack"
        delay = 0.05

        # Create the attack window first
        attack_window = tk.Toplevel()
        attack_window.title(attack_name)
        
        # Create and pack the label
        tk.Label(attack_window, text=f"{attack_name} in Progress...").pack(pady=10)
        
        # Create and pack the progress bar
        progress = ttk.Progressbar(attack_window, orient="horizontal", length=300, mode="determinate")
        progress.pack(pady=10)

        # Now update the progress bar
        for i in range(101):
            progress['value'] = i
            attack_window.update_idletasks()
            time.sleep(delay)
        
        # Show completion message
        messagebox.showinfo(attack_name, f"{attack_name} Completed!")
        
        # Update the text box
        text_box.insert(tk.END, "\nExecuting Dictionary Attack...\n")

    def perform_rainbow_table_action(self, text_box):
        attack_name = "Rainbow Table"
        delay = 0.05

        # Create the attack window first
        attack_window = tk.Toplevel()
        attack_window.title(attack_name)
        
        # Create and pack the label
        tk.Label(attack_window, text=f"{attack_name} in Progress...").pack(pady=10)
        
        # Create and pack the progress bar
        progress = ttk.Progressbar(attack_window, orient="horizontal", length=300, mode="determinate")
        progress.pack(pady=10)

        # Now update the progress bar
        for i in range(101):
            progress['value'] = i
            attack_window.update_idletasks()
            time.sleep(delay)
        
        # Show completion message
        messagebox.showinfo(attack_name, f"{attack_name} Completed!")
        
        # Update the text box
        text_box.insert(tk.END, "\nGenerating Rainbow Table...\n")

    def show_about(self):
        top = tk.Toplevel(self.root)
        top.title("About Us")
        top.geometry("800x600")
        top.configure(bg=self.bg_color)

        label = tk.Label(
            top,
            text="About Us",
            font=('Arial', 25, 'bold'),
            bg=self.bg_color,
            fg=self.accent_color
        )
        label.pack(pady=20)

        about_text = """
This application is developed to help users analyze password strength and learn about security techniques by
        ✔️ Shayan - Number 1
        ✔️ Aida - Number 2
        ✔️ Anamay - Number 3
        ✔️ Mahdi - Number 4
        ✔️ Saeedeh - Number 5
        ✔️ Tarun - Number 6
        ✔️ Reza - Number 7
        """
        about_label = tk.Label(
            top,
            text=about_text,
            font=('Arial', 22),
            bg=self.bg_color,
            fg=self.fg_color,
            wraplength=350,
            justify="left"
        )
        about_label.pack(pady=20)

        close_button = tk.Button(
            top,
            text="Close",
            command=top.destroy,
            font=('Arial', 14, 'bold'),
            bg=self.button_bg,
            fg='blue'
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
            font=('Arial', 18, 'bold'),
            bg=self.bg_color,
            fg=self.accent_color
        )
        label.pack(pady=20)

        text_box = tk.Text(
            top,
            height=5,
            width=40,
            bg='black',
            fg=self.fg_color,
            font=('Courier', 12),
            wrap='word'
        )
        text_box.pack(pady=10)

        action_button = tk.Button(
            top,
            text="Start",
            command=lambda: action_function(text_box),
            font=('Arial', 14, 'bold'),
            bg=self.button_bg,
            fg='blue',
            activebackground='#1A1A3A',
            activeforeground=self.fg_color
        )
        action_button.pack(pady=10)

        close_button = tk.Button(
            top,
            text="Close",
            command=top.destroy,
            font=('Arial', 14, 'bold'),
            bg=self.button_bg,
            fg='blue',
            activebackground='#1A1A3A',
            activeforeground=self.fg_color
        )
        close_button.pack(pady=10)

    def exit_application(self):
        self.root.destroy()

# Create main application window
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordAnalysisTool(root)
    root.mainloop()

