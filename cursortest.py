import streamlit as st
from datetime import datetime

st.title("My Streamlit App")

# 이미지 경로 설정
character_images = {
    "미키마우스": "images/mickey.jpg",
    "미니마우스": "images/minnie.jpg",
    "도날드 덕": "images/donald.jpg"
}

# 디즈니 캐릭터 선택
character = st.selectbox(
    "좋아하는 캐릭터를 선택하세요",
    ["미키마우스", "미니마우스", "도날드 덕"]
)

# 선택된 캐릭터 이미지 표시
st.image(character_images[character], width=300, caption=character)

# 현재 시간 표시
current_time = datetime.now().strftime("%H:%M:%S")

# 캐릭터별 메시지
if character == "미키마우스":
    st.write(f"하하! 안녕! 지금 시간은 {current_time} 이야!")
elif character == "미니마우스":
    st.write(f"안녕하세요~ 현재 시각은 {current_time} 랍니다!")
else:  # 도날드 덕
    st.write(f"꽥! 지금이 {current_time} 이라고!")
