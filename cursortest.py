import streamlit as st
from datetime import datetime

st.title("My Streamlit App")
st.write("Hello IS IT OK OK OK?")
st.write("연동테스트에 성공하였다")

# 달력 추가
selected_date = st.date_input(
    "날짜를 선택하세요",
    datetime.now(),  # 기본값으로 오늘 날짜 설정
)

# 선택된 날짜 표시
st.write("선택하신 날짜:", selected_date)
