# 📘 Belajar OOP (Object Oriented Programming)
Repository ini berisi dokumentasi dan latihan pribadi saya dalam mempelajari **Object Oriented Programming (OOP)** menggunakan bahasa **Python**.
Melalui project sederhana ini, saya belajar konsep dasar OOP seperti:

* Class dan Object
* Inheritance (Pewarisan)
* Method
* Constructor (`__init__`)
* Encapsulation sederhana

---

## 🎯 Tujuan Project

✅ Memahami konsep dasar OOP
✅ Membuat program manajemen data siswa sederhana
✅ Melatih logika pemrograman Python
✅ Latihan membuat class turunan (inheritance)

---

## 🧩 Penjelasan Program

Program ini mensimulasikan sistem data siswa sederhana.

### 🔹 Class Utama: `Siswa`

Class ini berisi:

* Nama siswa
* Kelas
* Nilai
* Method untuk menentukan status nilai

Kategori Status:

| Nilai | Status      |
| ----- | ----------- |
| ≥ 98  | Terbaik     |
| ≥ 88  | Bagus       |
| ≥ 75  | Cukup       |
| < 75  | Tidak Lulus |

---

### 🔹 Class Turunan: `No_Siswa`

Merupakan turunan dari class `Siswa`, dengan tambahan:

* Nomor Absen
* Gender
* Method untuk menampilkan info lengkap siswa

---

## ▶️ Cara Menjalankan Program

1. Pastikan Python sudah terinstall
2. Jalankan file Python:

```
python oop.py
```

3. Saat program berjalan, masukkan:

```
ya
```

atau

```
tidak
```

---

## 🖥️ Contoh Output Program

```
=============================
Nama: Kevin Triputra Sucipto
Gander: laki-laki
Kelas: XII TJKT 4
No absen: 1
Nilai: 100
Status: Terbaik
```

---

## 📂 Struktur Program

```
Belajar-oop/
│
├── oop.py
└── README.md
```

---
## 🚀 Pengembangan Kedepan
Rencana pengembangan project:

* Input data siswa manual
* Simpan data ke file (JSON / Database)
* Tambah menu CLI
* GUI sederhana (Tkinter / Web)
---
## ⭐ Catatan
Project sangat ini dibuat untuk tujuan belajar dan eksplorasi OOP dasar saya.
