#pip install openai

import openai
from selenium import webdriver
import time

# Set up OpenAI API Key (Replace with your actual API key)
openai.api_key = "your_openai_api_key_here"

# Function to generate comments using OpenAI
def generate_comment(text):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the appropriate engine
        prompt=f"Generate a comment based on the following content: {text}",
        max_tokens=60
    )
    comment = response.choices[0].text.strip()
    return comment

# Set up Selenium WebDriver (Ensure the path to your WebDriver is correct)
driver_path = 'path/to/chromedriver'  # Update this with your actual ChromeDriver path
driver = webdriver.Chrome(executable_path=driver_path)

# Open a webpage (Example: Amazon product page)
driver.get('https://www.amazon.com/dp/B08N5WRWNW')  # Replace with your target URL

# Wait for the page to load
time.sleep(5)

# Scrape content (e.g., product description or reviews)
# Adjust the selector to target the right element
content_element = driver.find_element('id', 'productDescription')  # Adjust the locator method
product_description = content_element.text

# Generate a comment using the scraped content
generated_comment = generate_comment(product_description)
print("Generated Comment:", generated_comment)

# Optionally, post the generated comment on the website (example below)

# Find comment box (this would be website-specific)
# comment_box = driver.find_element('id', 'comment_box_id')  # Adjust the selector
# comment_box.send_keys(generated_comment)  # Enter the generated comment
# submit_button = driver.find_element('id', 'submit_button_id')  # Adjust the selector
# submit_button.click()  # Submit the comment

# Close the browser after task is complete
driver.quit()