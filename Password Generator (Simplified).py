import tkinter as tk
import random
import string
from PIL import Image, ImageTk
import requests
from io import BytesIO


def generate_password():
    word = word_entry.get()
    include_numbers = include_numbers_var.get()
    include_characters = include_characters_var.get()
    shuffle_password = shuffle_var.get()

    password = "".join(random.choice([c.upper(), c.lower()]) for c in word)

    if include_numbers:
        password += "".join(random.choice(string.digits) for _ in range(5))

    if include_characters:
        password += "".join(random.choice(string.punctuation) for _ in range(5))

    if shuffle_password:
        password = "".join(random.sample(password, len(password)))

    result_textbox.config(state="normal")
    result_textbox.delete("1.0", "end")
    result_textbox.insert("1.0", password)
    result_textbox.config(state="disabled")


root = tk.Tk()
root.title("Password Generator")

img_url = "https://cdn-icons-png.flaticon.com/128/5617/5617976.png"
response = requests.get(img_url, timeout=10)
img_data = response.content
image = Image.open(BytesIO(img_data))
image = image.resize((57, 57))
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.pack(pady=10)

tk.Label(root, text="Enter a Word:").pack(pady=5)
word_entry = tk.Entry(root)
word_entry.pack(pady=5)

include_numbers_var = tk.IntVar()
tk.Checkbutton(root, text="Include Numbers", variable=include_numbers_var).pack()

include_characters_var = tk.IntVar()
tk.Checkbutton(
    root, text="Include Special Characters", variable=include_characters_var
).pack()

shuffle_var = tk.IntVar()
tk.Checkbutton(root, text="Shuffle Password", variable=shuffle_var).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

result_textbox = tk.Text(root, height=5, width=30, state="disabled")
result_textbox.pack(pady=5)

root.geometry("300x450")
root.resizable(False, False)
root.mainloop()
