import tkinter as tk
import sqlite3
from tkinter import messagebox

# Create a connection to the SQLite database
conn = sqlite3.connect('Nilai.db')
c = conn.cursor()

# Create the table
c.execute('''
    CREATE TABLE IF NOT EXISTS nilai_siswa (
        id INTEGER PRIMARY KEY,
        nama_siswa TEXT,
        biologi INTEGER,
        fisika INTEGER,
        inggris INTEGER,
        prediksi_fakultas TEXT
    )
''')

# Function to insert data into the database
def submit_data():
    nama = entry_nama.get()
    bio = int(entry_biologi.get())
    fis = int(entry_fisika.get())
    ing = int(entry_inggris.get())

    # Determine the highest score and set the faculty prediction
    if bio > fis and bio > ing:
        prediksi = "Kedokteran"
    elif fis > bio and fis > ing:
        prediksi = "Teknik"
    else:
        prediksi = "Bahasa"

    # Insert data into the database
    c.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama, bio, fis, ing, prediksi))
    conn.commit()

# Create the GUI
root = tk.Tk()
root.title("Prediksi Fakultas")
root.geometry("500x500")
root.resizable(False,False)

# Label Judul
label_judul = tk.Label(root, text="Prediksi Fakultas", font=("Times",14,"bold"))
label_judul.pack(pady=20)

# Buat Frame inputan
frame_input = tk.LabelFrame(root, labelanchor="n",pady=10, padx=10)
frame_input.pack()

# Label nama siswa
label_nama = tk.Label(frame_input, text="Nama Siswa")
label_nama.grid(row=0, column=0, pady=10)
entry_nama = tk.Entry(frame_input)
entry_nama.grid(row=0, column=1)

# Label Nilai biologi
label_biologi = tk.Label(frame_input, text="Nilai Biologi")
label_biologi.grid(row=1, column=0, pady=10)
entry_biologi = tk.Entry(frame_input)
entry_biologi.grid(row=1, column=1)

# Label fisika
label_fisika = tk.Label(frame_input, text="Nilai Fisika")
label_fisika.grid(row=2, column=0, pady=10)
entry_fisika = tk.Entry(frame_input)
entry_fisika.grid(row=2, column=1)

# Label bahasa inggris
label_inggris = tk.Label(frame_input, text="Nilai Inggris")
label_inggris.grid(row=3, column=0, pady=10)
entry_inggris = tk.Entry(frame_input)
entry_inggris.grid(row=3, column=1)

# Tombol Hasil
# Label Hasil

def submit_wrapper():
    submit_data()
    messagebox.showinfo("Info", "Data berhasil disimpan")

submit_button = tk.Button(root, text="Submit", command=submit_wrapper)
submit_button.pack(pady=10)

frame_hasil = tk.LabelFrame(root,labelanchor="n", padx=10,pady=10)
frame_hasil.pack_forget()


# Jalankan Aplikasi
root.mainloop()