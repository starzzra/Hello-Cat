import streamlit as st

st.title("🩷 Greetings! welcome to my very first app <3")
st.write(
    "Because this was my first app, Let me introduce myself first so you can know me better! Im Daneera Meijandini Ariestya from X-F :D"
)

st.title("Aplikasi Sederhana") 
st.header("Aplikasi Mengecek Nilai Genap/Ganjil") 
angka = st.number_input("Tulis Sebuah Angka:", value=0, step=1) 


if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap") 
else:
    st.write(f"{angka} adalah Bilangan Ganjil") 
