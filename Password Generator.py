import tkinter as tk
import random
import string
from PIL import Image, ImageTk
import requests
from io import BytesIO


class PasswordGeneratorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        img_url = "https://cdn-icons-png.flaticon.com/128/5617/5617976.png"
        response = requests.get(img_url, timeout=10)
        img_data = response.content
        image = Image.open(BytesIO(img_data))
        image = image.resize((57, 57))
        self.photo = ImageTk.PhotoImage(image)

        self.image_label = tk.Label(self.root, image=self.photo)
        self.image_label.pack(pady=10)

        tk.Label(self.root, text="Enter a Word:").pack(padx=10, pady=5)
        self.word_entry = tk.Entry(self.root)
        self.word_entry.pack(padx=10, pady=5)

        self.include_numbers_var = tk.IntVar()
        tk.Checkbutton(self.root,
                       text="Include Numbers",
                       variable=self.include_numbers_var).pack(padx=10, pady=1)

        self.num_numbers_frame = tk.Frame(self.root)
        self.num_numbers_frame.pack(padx=10, pady=5)
        self.num_numbers_entry = tk.Entry(self.num_numbers_frame, width=5)
        self.num_numbers_entry.pack(side="left")
        self.num_numbers_var = tk.IntVar()
        self.num_numbers_scale = tk.Scale(self.num_numbers_frame,
                                          from_=0,
                                          to=100,
                                          orient="horizontal",
                                          variable=self.num_numbers_var,
                                          length=150)
        self.num_numbers_scale.pack(side="left")
        self.num_numbers_entry.config(textvariable=self.num_numbers_var)

        self.include_characters_var = tk.IntVar()
        tk.Checkbutton(self.root,
                       text="Include Special Characters",
                       variable=self.include_characters_var).pack(padx=10,
                                                                  pady=1)

        self.num_characters_frame = tk.Frame(self.root)
        self.num_characters_frame.pack(padx=10, pady=5)
        self.num_characters_entry = tk.Entry(self.num_characters_frame,
                                             width=5)
        self.num_characters_entry.pack(side="left")
        self.num_characters_var = tk.IntVar()
        self.num_characters_scale = tk.Scale(self.num_characters_frame,
                                             from_=0,
                                             to=100,
                                             orient="horizontal",
                                             variable=self.num_characters_var,
                                             length=150)
        self.num_characters_scale.pack(side="left")
        self.num_characters_entry.config(textvariable=self.num_characters_var)

        self.shuffle_var = tk.IntVar()
        tk.Checkbutton(self.root,
                       text="Shuffle Password",
                       variable=self.shuffle_var).pack(padx=10, pady=1)

        tk.Button(self.root,
                  text="Generate Password",
                  command=self.update_password).pack(pady=10)

        self.result_textbox = tk.Text(self.root,
                                      height=5,
                                      width=30,
                                      state="disabled")
        self.result_textbox.pack(padx=10, pady=5)

        self.center_window()

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def update_password(self):
        word = self.word_entry.get()

        if not word:
            word = self.generate_random_word()

        include_numbers = self.include_numbers_var.get() == 1
        num_numbers = int(self.num_numbers_entry.get() if self.
                          num_numbers_entry.get() else 0)
        include_characters = self.include_characters_var.get() == 1
        num_characters = int(self.num_characters_entry.get() if self.
                             num_characters_entry.get() else 0)
        shuffle_password = self.shuffle_var.get() == 1

        password = self.generate_password(word, include_numbers, num_numbers,
                                          include_characters, num_characters,
                                          shuffle_password)
        self.result_textbox.config(state="normal")
        self.result_textbox.delete("1.0", "end")
        self.result_textbox.insert("1.0", password)
        self.result_textbox.config(state="disabled")

    def generate_password(self, word, include_numbers, num_numbers,
                          include_characters, num_characters,
                          shuffle_password):
        password = ""

        alternating_case_word = self.generate_alternating_case_word(word)
        password += alternating_case_word

        if include_numbers:
            password += ''.join(
                random.choice(string.digits) for _ in range(num_numbers))

        if include_characters:
            password += ''.join(
                random.choice(string.punctuation)
                for _ in range(num_characters))

        if shuffle_password:
            password_list = list(password)
            random.shuffle(password_list)
            password = ''.join(password_list)

        return password

    def generate_alternating_case_word(self, word):
        alternating_case_word = ''.join([
            c.upper() if random.choice([True, False]) else c.lower()
            for c in word
        ])
        return alternating_case_word

    def generate_random_word(self):
        length = random.randint(6, 12)
        return ''.join(
            random.choice(string.ascii_letters) for _ in range(length))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Password Generator")
    app = PasswordGeneratorApp(root)
    root.geometry("370x550")
    root.resizable(False, False)
    root.mainloop()
