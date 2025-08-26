from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://www.instagram.com/explore/tags/sicily2024/"
driver.get(url)
input("🔐 Fai login, accetta i cookie e premi INVIO qui per iniziare...")

post_links = set()
scroll_pause = 2
scroll_round = 0

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause)
    links = driver.find_elements(By.TAG_NAME, 'a')
    for link in links:
        href = link.get_attribute('href')
        if href and '/p/' in href:
            post_links.add(href)
    scroll_round += 1
    print(f"🌀 Scroll {scroll_round} - Link raccolti: {len(post_links)}")
    if scroll_round >= 300:
        break

with open("sicily_all_links.txt", "w") as f:
    for link in post_links:
        f.write(link + "\n")

print("✅ Link salvati in sicily_all_links.txt")
driver.quit()
