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

#pengisisan
frame_input = tk.Frame(top, bg = "#b0e0e6")
frame_input.pack(pady=5)

entries = []

#loop untuk mata pelajaran
for i in range(1, 11):
    lbl_matkul = tk.Label(
        frame_input, 
        text=f"Nilai Mata Pelajaran {i}:", 
        font=("Arial", 10), 
        bg="#b0e0e6", 
        anchor="w"
    )
    lbl_matkul.grid(row=i-1, column=0, sticky="w", padx=10, pady=4)
    
    entry_nilai = tk.Entry(frame_input, width=15, bd=2)
    entry_nilai.grid(row=i-1, column=1, padx=10, pady=4)
    entries.append(entry_nilai)

#button
btn_prediksi = tk.Button(
    top, 
    text="Hasil Prediksi", 
    font=("Arial", 11, "bold"), 
    bg="#4CAF50", 
    fg="white", 
    padx = 10,
    pady = 3,
    command=hitung_prediksi
)
btn_prediksi.pack(pady=15)

#label luaran hasil prediksi
label_hasil = tk.Label(
    top, 
    text="", 
    font=("Helvetica", 12, "bold"), 
    bg="#b0e0e6", 
    fg="#333333"
)
label_hasil.pack(pady=5)


