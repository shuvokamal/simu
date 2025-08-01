import streamlit as st

st.set_page_config(page_title="🔓 Unlock the Revolution", layout="centered")
st.title("🎬 Crisis President is Waiting...")

# Password input
password = st.text_input("শ্লোগানটা কি যেন?", type="password")

# If password is correct
if password == "1234":
    st.success("✅ ১২৩৪... সিমু নাসেরের...")

    # Display local GIF
    with open("simu.gif", "rb") as f:
        gif_bytes = f.read()
        st.image(gif_bytes, caption="👔 Your President in Action", use_column_width=True)

elif password:
    st.error("❌ ভুল শ্লোগান. Try again!")
