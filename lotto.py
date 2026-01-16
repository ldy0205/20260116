import streamlit as st
import random
import datetime

#로또 번호 생성 함수
st.title("로또 번호 생성기")

def generate_lotto_numbers():
    lotto=set()
    while len(lotto) < 6:
        number=random.randint(1, 46)
        lotto.add(number)
    return lotto

if st.button("로또 번호 생성하기"):
   for i in range(1,6):
       st.subheader(f"추천 로또 번호 {i}: {generate_lotto_numbers()}")
       st.write("생성된 시간:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))