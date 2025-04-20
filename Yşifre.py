import random
import string
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("GÜÇLÜ ŞİFRE ÜRETİCİ")
root.geometry("600x800")

tk.Label(root, text="Güçlü Şifre Üreticiye hoş geldiniz.", font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Şifre uzunluğunu giriniz:").pack(pady=5)
şifre_uzunluk_entry = tk.Entry(root)
şifre_uzunluk_entry.pack(pady=5)

tk.Label(root, text="Sadece sayılardan mı (s), yoksa karışık mı (k):").pack(pady=5)
tür_entry = tk.Entry(root)
tür_entry.pack(pady=5)

şifre = ""  # Şifreyi global bir değişkende tutuyoruz

def üret():
    global şifre
    şifre_uzunluk = şifre_uzunluk_entry.get()
    tür = tür_entry.get()

    if not şifre_uzunluk.isdigit():
        messagebox.showerror("Hata", "Geçerli bir sayı girin.")
    else:
        uzunluk = int(şifre_uzunluk)

        if tür.lower() == "s":
            karakterler = string.digits
        elif tür.lower() == "k":
            karakterler = string.ascii_letters + string.digits + string.punctuation
        else:
            messagebox.showerror("Hata", "Geçersiz tür seçimi yaptınız.")
            return

        şifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
        messagebox.showinfo("Oluşturulan Şifre", f"ŞİFRENİZ: {şifre}")

def kopyala():
    if şifre:
        root.clipboard_clear()
        root.clipboard_append(şifre)
        root.update()  # Panoyu güncellemek için
        messagebox.showinfo("Bilgi", "Şifre panoya kopyalandı!")
    else:
        messagebox.showerror("Hata", "Önce bir şifre üretin.")

şifre_button = tk.Button(root, text="Şifre Üret", command=üret)
şifre_button.pack(pady=20)

kopyala_button = tk.Button(root, text="Şifreyi Kopyala", command=kopyala)
kopyala_button.pack(pady=20)

root.mainloop()