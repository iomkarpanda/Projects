import os
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import google.generativeai as genai

# --- Gemini configuration ---
genai.configure(api_key="AIzaSyB8BfZRSj10jDnra04WOTtcoylNTjM0Dts")
model = genai.GenerativeModel("gemini-1.5-flash")  # can change to pro if quota allows

# --- Scrape Flipkart product ---
def scrape_flipkart(url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(3)

    try:
        title = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "B_NuCI"))
        ).text
    except:
        title = "No Title"

    try:
        current_price = driver.find_element(By.CLASS_NAME,'Nx9bqj').text
    except:
        current_price = "No Price"

    try:
        actual_price = driver.find_element(By.CLASS_NAME,"yRaY8j").text
    except:
        actual_price = "No Actual Price"

    try:
        rating = driver.find_element(By.CLASS_NAME,"XQDdHH").text
    except:
        rating = "No Rating"

    driver.quit()
    return {"title": title, "current_price": current_price, "actual_price": actual_price, "rating": rating}

# --- Generate post using Gemini ---
def generate_post_with_gemini(product, affiliate_link):
    prompt = f"""
You are a social media content writer. Create a short, engaging, emoji-rich post in bullet points under 280 characters for this Flipkart product:

Title: {product['title']}
Actual Price: {product['actual_price']}
Current Price: {product['current_price']}
Rating: {product['rating']}
Affiliate Link: {affiliate_link}

Requirements:
- Emojis like 🔥, 💻, ⚡, 🎯
- Highlight key features
- Call to action (e.g., "Don't miss this deal!")
- Ready to post on Twitter/X
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # fallback if Gemini quota is exceeded
        fallback_post = f"""
🔥 {product['title']} 🔥

• Current Price: {product['current_price']} ⚡
• Actual Price: {product['actual_price']}
• Rating: {product['rating']} ⭐
• Key Features: Highlight main features 🎯

Grab yours now! ➡️ {affiliate_link}
"""
        return fallback_post.strip()

# --- Telegram bot handler ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "flipkart.com" in text.lower():  # detect Flipkart links
        await update.message.reply_text("Processing product, please wait... ⏳")
        product = scrape_flipkart(text)
        post_text = generate_post_with_gemini(product, text)
        await update.message.reply_text(post_text)

# --- Main bot setup ---
if __name__ == "__main__":
    app = ApplicationBuilder().token("8324862269:AAEA4U6urK4b0Y1HYfuBeOf4QSuhJ_c_Ick").build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()
