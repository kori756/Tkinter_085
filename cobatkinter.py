import tkinter as tk
from tkinter import messagebox

def hitung_prediksi():
    label_hasil.config(text="teknologi informasi")
    
top = tk.Tk()
top.title("Aplikasi Prediksi Prodi Pilihan")
top.geometry("450x800")
top.configure(bg = "lightblue")

#judul
label_judul = tk.Label(top, text = "Aplikasi Prediksi Prodi Pilihan", font = ("helvetica", 16, "bold"), bg = "lightblue" ,fg = "black", justify = "center")
label_judul.pack(pady = 20, padx = 10)

