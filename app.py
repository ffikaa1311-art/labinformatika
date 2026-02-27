import streamlit as st
import pandas as pd

st.title("🔍 Cek Data Sertifikat Asprak")

# Membaca data dari folder csv_exports
try:
    # Menggunakan path yang sesuai dengan struktur foldermu
    df = pd.read_csv("docs.csv")
    
    kode_input = st.text_input("Masukkan Kode Sertifikat:")

    if kode_input:
        # Mencari data yang kodenya cocok
        hasil = df[df['Kode'] == kode_input]
        
        if not hasil.empty:
            st.success("Data Ditemukan!")
            st.write(f"**NIM:** {hasil['NIM'].values[0]}")
            st.write(f"**Nama:** {hasil['Nama'].values[0]}")
            st.write(f"**Semester:** {hasil['Semester'].values[0]}")
            st.write(f"**Mata Kuliah:** {hasil['Matakuliah'].values[0]}")
        else:
            st.error("Kode tidak terdaftar. Pastikan huruf besar/kecil sesuai.")
except Exception as e:
    st.error("Pastikan file 'docs.csv' sudah ada di dalam folder 'csv_exports'")