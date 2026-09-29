import streamlit as st
import pandas as pd

st.set_page_config(page_title="생산 현황 대시보드", page_icon="🔋")
st.title("🔋 생산 현황 대시보드 (샘플)")
st.caption("세방전지 AX 전문가 과정 실습용 대시보드입니다.")

name = st.text_input("이름을 입력하세요")
if name:
    st.success(f"{name}님, 환영합니다!")

df = pd.DataFrame({
    "월": ["1월", "2월", "3월", "4월", "5월", "6월"],
    "생산량": [120, 135, 150, 142, 160, 171],
})
st.subheader("월별 생산량")
st.metric("생산량 합계", f"{df['생산량'].sum():,}")
st.bar_chart(df, x="월", y="생산량")
st.dataframe(df, hide_index=True)
