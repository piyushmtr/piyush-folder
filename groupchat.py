import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import time

# --- GOOGLE SHEET SETUP ---
# Share your Google Sheet with your service account email
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", SCOPE)
client = gspread.authorize(CREDS)
sheet = client.open("PiyushChatApp").sheet1  # Use your sheet name

# --- UI ---
st.set_page_config("Chat App by Piyush", layout="centered")
st.title("💬 Chat App")
st.markdown("### 👋 A warm welcome from Piyush!")

name = st.text_input("Enter your name:")
message = st.text_input("Type your message:")

# --- Send message ---
if st.button("Send"):
    if name and message:
        sheet.append_row([name, message, time.strftime("%H:%M:%S")])
        st.success("Message sent!")
        st.experimental_rerun()
    else:
        st.warning("Please enter both name and message.")

# --- Display chat ---
st.markdown("---")
st.subheader("📢 Chat Room")

data = sheet.get_all_records()
if data:
    df = pd.DataFrame(data)
    for i in range(len(df)):
        st.markdown(f"**{df.iloc[i]['name']}** ({df.iloc[i]['time']}): {df.iloc[i]['message']}")
else:
    st.write("No messages yet.")

