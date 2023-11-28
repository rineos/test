import tkinter as tk
from tkinter import messagebox

def on_exit():
    if messagebox.askyesno("Вихід", "Ви впевнені, що хочете вийти?"):
        root.destroy()

def show_about():
    messagebox.showinfo("Про програму", "Це приклад Tkinter меню.")

def encrypt_text():
    text1 = input_entry.get()
    text = list(text1)
    key = int(key_entry.get())
    encrypted_list = []
    part = ""
    completed = ""
    second_key = key
    a = 0
    while a <= key + 1:
        for i in range(key - 1, len(text), second_key):
            part += text[i]
        encrypted_list.append(part)
        key = key - 1
        part = ""
        a += 1
    encrypted_text = ''.join(encrypted_list)
    result_label.config(text=f"Зашифрований текст: {encrypted_text}")

root = tk.Tk()
root.title("Моя програма")

# Створення меню
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Додаємо розділ "Файл" та пункти меню
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Вихід", command=on_exit)

# Додаємо розділ "Допомога" та пункти меню
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Допомога", menu=help_menu)
help_menu.add_command(label="Про програму", command=show_about)

# Додамо віджети для шифрування тексту
input_label = tk.Label(root, text="Введіть слово:")
input_label.pack()

input_entry = tk.Entry(root)
input_entry.pack()

key_label = tk.Label(root, text="Введіть ключ:")
key_label.pack()

key_entry = tk.Entry(root)
key_entry.pack()

encrypt_button = tk.Button(root, text="Зашифрувати", command=encrypt_text)
encrypt_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()