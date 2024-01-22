import numpy as np
import streamlit as st

with st.container(border=True):
   check1 = st.checkbox('前排')
   check2 = st.checkbox('中间')
   check3 = st.checkbox('后排')

if check1:
    st.write('前排!')
if check2:
    st.write('中间!')
if check3:
    st.write('后排!')

with st.container(border=True):
   check1 = st.checkbox('前排')
   check2 = st.checkbox('中间')
   check3 = st.checkbox('后排')
st.write("This is outside the container")
