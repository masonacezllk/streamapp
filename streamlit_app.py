import streamlit as st

col1, col2 = st.columns(2)

with col1:
   st.header("前中后排定义")
   with st.container():
      st.checkbox("前排")
      st.checkbox("中排")
      st.checkbox("后排")

with col2:
   st.header("位置定义")
   with st.container():
      st.checkbox("靠背")
      st.checkbox("坐垫")
      st.checkbox("地板")

