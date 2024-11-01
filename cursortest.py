import streamlit as st
from datetime import datetime

st.title("Multi-Language Disney Time")

# 캐릭터 이미지 경로
character_images = {
    "미키마우스": "images/mickey.jpg",
    "미니마우스": "images/minnie.jpg",
    "도날드 덕": "images/donald.jpg"
}

# 다국어 메시지 설정
time_messages = {
    "미키마우스": {
        "한국어": "하하! 안녕! 지금 시간은 {} 이야!",
        "영어": "Ha ha! Hi! The time is {}!",
        "독일어": "Ha ha! Hallo! Die Zeit ist {}!",
        "프랑스어": "Ha ha! Bonjour! Il est {}!",
        "중국어": "哈哈！你好！现在是 {} ！",
        "터키어": "Ha ha! Merhaba! Saat {}!",
        "아랍어": "!{} هاها! مرحبا! الوقت الآن"
    },
    "미니마우스": {
        "한국어": "안녕하세요~ 현재 시각은 {} 랍니다!",
        "영어": "Hello~ The current time is {}!",
        "독일어": "Hallo~ Die aktuelle Zeit ist {}!",
        "프랑스어": "Bonjour~ L'heure actuelle est {}!",
        "중국어": "你好～现在的时间是 {} ！",
        "터키어": "Merhaba~ Şu anki saat {}!",
        "아랍어": "!{} مرحباً~ الوقت الحالي هو"
    },
    "도날드 덕": {
        "한국어": "꽥! 지금이 {} 이라고!",
        "영어": "Quack! It's {} now!",
        "독일어": "Quak! Es ist jetzt {}!",
        "프랑스어": "Coin! Il est {} maintenant!",
        "중국어": "嘎！现在是 {} ！",
        "터키어": "Vak! Şimdi saat {}!",
        "아랍어": "!{} كواك! الساعة الآن"
    }
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

# 모든 언어로 메시지 표시
st.subheader("🌍 다국어 시간 안내")
for language, message in time_messages[character].items():
    # 언어별 이모지 설정
    emoji = {
        "한국어": "🇰🇷",
        "영어": "🇺🇸",
        "독일어": "🇩🇪",
        "프랑스어": "🇫🇷",
        "중국어": "🇨🇳",
        "터키어": "🇹🇷",
        "아랍어": "🇸🇦"
    }
    
    # 메시지 표시 (이모지와 함께)
    st.write(f"{emoji[language]} {language}: {message.format(current_time)}")
