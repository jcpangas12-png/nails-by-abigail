import streamlit as st
import urllib.parse
from datetime import datetime

# Set up a clean mobile interface matching her premium aesthetic
st.set_page_config(page_title="Nails By Abigail", page_icon="💅", layout="centered")

st.title("💅 Nails By Abigail - Booking Portal")
st.write("Select your services, choose a date, and book your spot via WhatsApp!")

# 1. Services and Prices taken exactly from Abby's price list
services = {
    "Extensions": 170,
    "Overlay (Rubber Base / Builder Gel)": 120,
    "Mini Pedicure": 100,
    "Removal": 65
}

# 2. Service Selection
st.subheader("1. Select Core Services")
selected_services = []
total_amount = 0

for service, price in services.items():
    checked = st.checkbox(f"{service} — R{price}")
    if checked:
        selected_services.append(service)
        total_amount += price

st.markdown(f"### **Estimated Total: R{total_amount}**")

# 3. Appointment Details
st.subheader("2. Your Details & Preferred Time")
name = st.text_input("Your Full Name")
date_selected = st.date_input("Preferred Date", min_value=datetime.today())
time_selected = st.time_input("Preferred Time")

# 4. The Magic Booking Button
if st.button("💖 Request Spot via WhatsApp"):
    if not name or len(selected_services) == 0:
        st.error("Please provide your name and select at least one service!")
    else:
        # Format a highly professional appointment text
        booking_text = f"*New Appointment Request for Nails By Abigail* 💅\n\n"
        booking_text += f"*Client Name:* {name}\n"
        booking_text += f"*Date:* {date_selected.strftime('%d %B %Y')}\n"
        booking_text += f"*Preferred Time:* {time_selected.strftime('%H:%M')}\n\n"
        
        booking_text += "*Requested Services:*\n"
        for service in selected_services:
            booking_text += f"- {service}\n"
        
        booking_text += f"\n*Estimated Total:* R{total_amount}\n\n"
        booking_text += "Please confirm if this slot is available! ✨"
        
        # URL encode the text string for the WhatsApp link
        encoded_message = urllib.parse.quote(booking_text)
        
        # Abby's direct WhatsApp number formatted for the web API
        whatsapp_number = "27615113707" 
        whatsapp_url = f"https://wa.me{whatsapp_number}?text={encoded_message}"
        
        st.success("Booking request compiled perfectly!")
        st.markdown(f"[👉 Click Here to Open WhatsApp & Send to Abby]({whatsapp_url})")
