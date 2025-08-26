import random
import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

# Keywords da escludere
ban_words = ['sicily', 'sicilia', 'travel', 'discover', 'tour']
ban_hashtags = ['#adv']

# Leggi tutti i link dal file
with open("sicily_all_links.txt", "r") as f:
    all_links = [line.strip() for line in f if line.strip()]

print(f"🔗 Trovati {len(all_links)} link totali nel file.")

# Setup Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Login manuale
driver.get("https://www.instagram.com")
input("🔐 Fai login e accetta i cookie, poi premi INVIO nel terminale per iniziare...")

valid_links = []
consecutive_image_errors = 0

# Crea cartelle per output
os.makedirs("1_post_idonei", exist_ok=True)
os.makedirs("2_link_scelti", exist_ok=True)

for idx, link in enumerate(all_links):
    print(f"\n🔗 [{idx+1}] Analizzo: {link}")
    try:
        driver.get(link)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "time")))
        time.sleep(3)

        # Escludi video
        try:
            driver.find_element(By.TAG_NAME, 'video')
            print("🎥 Video rilevato. Saltato.")
            continue
        except:
            pass

        # Estrai username
        try:
            username_elem = driver.find_element(By.XPATH, '//header//a[contains(@href, "/")]')
            username = username_elem.get_attribute("href").split("/")[-2].lower()
            if any(word in username for word in ban_words):
                print(f"🚫 Username con parole vietate: {username}. Saltato.")
                continue
        except:
            try:
                # Metodo alternativo: cerca elementi a sinistra dell’intestazione
                username_elem_alt = driver.find_element(By.XPATH, '//a[contains(@href, "/") and not(contains(@href, "/p/"))]')
                username = username_elem_alt.get_attribute("href").split("/")[-2].lower()
                print(f"ℹ️ Username trovato con metodo alternativo: {username}")
            except:
                print("⚠️ Impossibile leggere l’username con nessun metodo. Post saltato.")
                continue

        # Estrai caption
        try:
            caption_elem = driver.find_element(By.XPATH, '//div[@role="button"]/../../..//span')
            caption = caption_elem.text.lower()
            if any(tag in caption for tag in ban_hashtags):
                print("🚫 Hashtag vietato trovato (#adv). Saltato.")
                continue
        except:
            caption = ""

        # Estrai data e verifica sia 2024
        try:
            time_elem = driver.find_element(By.TAG_NAME, 'time')
            date_str = time_elem.get_attribute("datetime")
            post_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
            if post_date.year != 2024:
                print(f"📅 Anno non valido: {post_date.year}. Saltato.")
                continue
        except Exception as e:
            print(f"⚠️ Errore nella data: {e}")
            continue

        # Trova immagine (anche per caroselli)
        try:
            img_elems = driver.find_elements(By.XPATH, '//img')
            img_url = None
            for img in img_elems:
                src = img.get_attribute("src")
                if src and "instagram.com" in src and "scontent" in src:
                    img_url = src
                    break
            if not img_url:
                for img in img_elems:
                    src = img.get_attribute("src")
                    if src and src.startswith("https"):
                        img_url = src
                        break
            if not img_url:
                print("⚠️ Nessuna immagine trovata. Saltato.")
                continue
        except Exception as e:
            print(f"⚠️ Errore nel trovare immagine: {e}")
            continue

        # valid_links.append((link, img_url))
        # print("✅ Post idoneo aggiunto.")
        # if len(valid_links) >= 1000:
        #     print("🎯 Raggiunti 1000 post idonei. Fine.")
        #     break
        # Check per errore 429
        if "429" in driver.page_source or "This page isn’t working" in driver.page_source:
            print("⛔ Errore 429 (Too Many Requests) - Accesso temporaneamente bloccato.")
            consecutive_image_errors += 1
            if consecutive_image_errors >= 5:
                print("🚨 Blocco rilevato 5 volte di fila. Script interrotto.")
                break
            continue
        else:
            consecutive_image_errors = 0  # resetta se va tutto bene

    except Exception as e:
        print(f"⚠️ Errore generale al post {idx+1}: {e}")
        continue

# Salva tutti i link idonei
with open("1_post_idonei/filtered_links.txt", "w") as f:
    for link in valid_links:
        f.write(link + "\n")

# Seleziona 200 a caso e salvali
selected = random.sample(valid_links, min(200, len(valid_links)))
with open("2_link_scelti/final_selected_links.txt", "w") as f:
    for link in selected:
        f.write(link + "\n")

print(f"\n✅ Totale post idonei: {len(valid_links)}")
print(f"🎯 Link scelti casualmente: {len(selected)}")
print("📁 Salvati in '1_post_idonei/filtered_links.txt' e '2_link_scelti/final_selected_links.txt'")
driver.quit()

