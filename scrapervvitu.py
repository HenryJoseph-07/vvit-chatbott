from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time, os, re

BASE_URL = "https://www.vvitu.ac.in"
OUTPUT_DIR = "data"
MAX_PAGES = 100
ALLOWED_DOMAINS = ["www.vvitu.ac.in", "vvitu.ac.in"]

def clean_text(soup):
    for tag in soup(['script','style','noscript','iframe']):
        tag.decompose()
    for tag in soup(['nav','footer','header']):
        tag.decompose()
    for tag in soup.find_all(True, {'class': re.compile(r'nav|menu|footer|header|sidebar|breadcrumb|social|cookie|popup|banner', re.I)}):
        tag.decompose()
    for tag in soup.find_all(True, {'id': re.compile(r'nav|menu|footer|header|sidebar|breadcrumb|social|cookie|popup|banner', re.I)}):
        tag.decompose()
    raw = soup.get_text(separator='\n', strip=True)
    lines = [l.strip() for l in raw.splitlines() if l.strip()]
    seen = set()
    unique = []
    for line in lines:
        if line not in seen:
            seen.add(line)
            unique.append(line)
    return '\n'.join(unique)

def is_valid_url(url):
    try:
        parsed = urlparse(url)
        return (
            parsed.netloc in ALLOWED_DOMAINS and
            not url.endswith(('.jpg','.jpeg','.png','.gif','.zip','.mp4','.doc','.docx','.pdf')) and
            '#' not in url and '?' not in url
        )
    except:
        return False

def safe_filename(url, index):
    slug = url.replace(BASE_URL,'').replace('/','_').strip('_')
    slug = re.sub(r'[\\/*?:"<>|]','',slug)
    return f"vvitu_{index}_{slug[:60] if slug else 'homepage'}.txt"

def crawl():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--log-level=3')
    options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.set_page_load_timeout(15)

    visited = set()
    to_visit = [BASE_URL]
    saved = 0

    print(f"Starting crawl on {BASE_URL}...\n")

    while to_visit and len(visited) < MAX_PAGES:
        url = to_visit.pop(0)
        if url in visited:
            continue

        try:
            driver.get(url)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            time.sleep(3)

            visited.add(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            text = clean_text(soup)

            line_count = len([l for l in text.splitlines() if l.strip()])
            if line_count >= 5:
                filepath = os.path.join(OUTPUT_DIR, safe_filename(url, saved+1))
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(f"Source: {url}\n\n{text}")
                saved += 1
                print(f"[{saved}] Saved ({line_count} lines): {url}")
            else:
                print(f"[skip] {url}")

            for a in driver.find_elements(By.TAG_NAME, 'a'):
                try:
                    href = a.get_attribute('href')
                    if href and is_valid_url(href) and href not in visited:
                        to_visit.append(href)
                except:
                    continue

        except Exception as e:
            print(f"Skipped {url} — {e}")
            continue

    driver.quit()
    print(f"\nDone. {saved} pages saved to /{OUTPUT_DIR} folder.")

if __name__ == "__main__":
    crawl()