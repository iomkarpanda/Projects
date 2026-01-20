from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import google.generativeai as genai


#configure with api key
genai.configure(api_key='AIzaSyB8BfZRSj10jDnra04WOTtcoylNTjM0Dts')
models = genai.GenerativeModel('gemini-1.5-flash')

# Setting up Headless Mode
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# Getting Details of Product
driver.get("https://fkrt.cc/g9l2K7U")


title = driver.title   #Getting Product Title
current_price = driver.find_element(By.CLASS_NAME,'Nx9bqj').text #Getting details of current price
actual_price = driver.find_element(By.CLASS_NAME,"yRaY8j").text
rating = driver.find_element(By.CLASS_NAME,"XQDdHH").text
img_element = driver.find_element(By.CLASS_NAME,'DByuf4')
# url = 'https://fktr.in/1YlHmV5'

image_url = img_element.get_attribute('src')
#Generation of text
response = models.generate_content(f"""
                                  You are a content writer. I will give you product details scraped from Flipkart. 
Your task is to generate an attractive, engaging, and concise description/post in bullet points and whole content should be in 280 characters including spaces and line breaks and embed the image url.

Product Details:
Title: {title}
Actaul Price: {actual_price}
Current Price:{current_price}
Rating: {rating}

image_url:{image_url}

Requirements:
1. Write in an engaging tone with emojis (🔥, 💻, ⚡, 🎯).
2. Highlight key features and benefits.
3. Mention price attractively.
4. Make it suitable for a short social media post (Twitter/X thread or Instagram caption).
5. End with a call to action (e.g., "Don’t miss this deal!" or "Check it out now!").
  """)
print(response.text)

# print(title)
# print(current_price.text)
# print(actual_price.text)
# print(rating.text)


# driver.quit()