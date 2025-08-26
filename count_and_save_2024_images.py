from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime

# Setup Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Vai al profilo
driver.get("https://www.instagram.com/ig_visitsicily/")
input("🔐 Fai login e accetta i cookie, poi premi INVIO nel terminale per iniziare...")

# Scrolla per caricare post
post_links = set()
scroll_pause = 2
scrolls = 0

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause)
    links = driver.find_elements(By.TAG_NAME, 'a')
    for link in links:
        href = link.get_attribute('href')
        if href and '/p/' in href:
            post_links.add(href)
    scrolls += 1
    print(f"🌀 Scroll {scrolls} - Post trovati: {len(post_links)}")
    if scrolls >= 300:
        print("✅ Scroll massimo raggiunto.")
        break

# Analizza i post raccolti
count_2024 = 0
post_2024_links = []

print("🔍 Inizio analisi post...")

for i, link in enumerate(post_links):
    try:
        driver.get(link)

        # Aspetta che la data sia disponibile
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "time")))
        time.sleep(2)

        # Escludi se è video
        try:
            driver.find_element(By.TAG_NAME, 'video')
            print(f"🎥 [{i+1}] Video saltato")
            continue
        except:
            pass

        # Estrai la data
        time_elem = driver.find_element(By.TAG_NAME, 'time')
        date_str = time_elem.get_attribute('datetime')
        post_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")

        if post_date.year == 2024:
            count_2024 += 1
            post_2024_links.append(link)
            print(f"✅ [{i+1}] Immagine 2024 trovata: {post_date.date()}")
        else:
            print(f"📅 [{i+1}] Non 2024: {post_date.date()}")

    except Exception as e:
        print(f"⚠️ Errore su post {i+1}: {e}")
        continue

# Salva i risultati
with open("ig_visitsicily_2024_images.txt", "w") as f:
    for link in post_2024_links:
        f.write(link + "\n")

print(f"\n🎯 Totale immagini del 2024: {count_2024}")
print("✅ Link salvati in ig_visitsicily_2024_images.txt")
print("📌 Il browser resta aperto per verifica manuale.")

