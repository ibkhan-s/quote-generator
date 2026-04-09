import streamlit as st
import random

# Page config
st.set_page_config(page_title="Random Quote Generator", page_icon="💬")

# Title
st.title("💬 Random Quote Generator")

# List of quotes
quotes = [
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "Don't let yesterday take up too much of today. – Will Rogers",
    "It's not whether you get knocked down, it's whether you get up. – Vince Lombardi",
    "If you are working on something exciting, it will keep you motivated. – Steve Jobs",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Do what you can with all you have, wherever you are. – Theodore Roosevelt"
]

# Button to generate quote
if st.button("Generate Quote 🎲"):
    quote = random.choice(quotes)
    st.success(quote)

# Optional footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")