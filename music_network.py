import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# 페이지 설정
st.title("클래식 음악 작곡가 연관관계")

# 그래프 생성
G = nx.Graph()

# 작곡가 노드 추가
composers = {
    "바흐": {"year": "1685-1750", "color": "#FF9999"},
    "베토벤": {"year": "1770-1827", "color": "#99FF99"},
    "모차르트": {"year": "1756-1791", "color": "#9999FF"},
    "쇼팽": {"year": "1810-1849", "color": "#FFFF99"}
}

# 노드 추가
for composer, data in composers.items():
    G.add_node(composer, year=data["year"])

# 연관관계 추가 (weight는 영향력의 강도)
relationships = [
    ("바흐", "베토벤", {"weight": 3, "description": "바흐의 평균율 클라비어가 베토벤의 피아노 소나타에 영향"}),
    ("바흐", "모차르트", {"weight": 4, "description": "모차르트가 바흐의 대위법을 연구하고 발전시킴"}),
    ("모차르트", "베토벤", {"weight": 5, "description": "베토벤이 모차르트의 작품을 깊이 연구"}),
    ("베토벤", "쇼팽", {"weight": 3, "description": "베토벤의 피아노 소나타가 쇼팽의 작품에 영향"}),
]

G.add_edges_from([(r[0], r[1]) for r in relationships])

# 그래프 그리기
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)

# 노드 그리기
nx.draw_networkx_nodes(G, pos, 
                      node_color=[composers[node]["color"] for node in G.nodes()],
                      node_size=2000)

# 엣지 그리기
nx.draw_networkx_edges(G, pos, width=2)

# 레이블 추가
nx.draw_networkx_labels(G, pos, font_size=10, font_family='NanumGothic')

# Streamlit에 그래프 표시
st.pyplot(plt)

# 연관관계 설명
st.subheader("작곡가 간의 연관관계")
for r in relationships:
    st.write(f"**{r[0]}** → **{r[1]}**: {r[2]['description']}")

# 작곡가 정보
st.subheader("작곡가 정보")
for composer, data in composers.items():
    st.write(f"**{composer}** ({data['year']})") 