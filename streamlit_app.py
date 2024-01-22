import streamlit as st

container = st.container(border=True)
container.write(st.checkbox("前排")
st.write("This is outside the container")

# Now insert some more in the container
container.write("This is inside too")
