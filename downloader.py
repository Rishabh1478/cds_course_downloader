from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from waiter import waiter
from tqdm import tqdm
import os

def downloader(link, folder_name, file_name):
    # Set up the Selenium driver (e.g., ChromeDriver)
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    opt.add_argument('--disable-gpu')
    opt.add_argument('--no-sandbox')
    opt.add_argument('--disable-dev-shm-usage')
    opt.add_argument('--log-level=3')
    opt.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36')
    driver = webdriver.Chrome(options=opt)

    # Navigate to the webpage (log in if necessary)
    driver.get(link)

    # Locate the media element (e.g., an image)
    waiter(driver, '//video[@id="vjs_video_3_html5_api"]')
    media_element = driver.find_element(By.XPATH, '//video[@id="vjs_video_3_html5_api"]')  # Adjust the locator as needed

    # Extract the media URL
    media_url = media_element.get_attribute('src')

    # Extract cookies
    cookies = driver.get_cookies()

    # Convert cookies to a dictionary
    cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}

    # Extract headers (if needed, this is a basic example)
    headers = {
        'User-Agent': driver.execute_script("return navigator.userAgent;"),
        'Referer': driver.current_url  # Example of adding Referer header
    }

    # Close the driver
    driver.quit()
    if os.path.isdir(rf'downloads\{folder_name}'):
        pass
    else:
        os.makedirs(rf'downloads\{folder_name}')
    
    response = requests.get(media_url, headers=headers, cookies=cookies_dict)
    # Save the media to a file
    if response.status_code == 200:
        with open(fr'downloads/{folder_name}/{file_name}.mp4', 'wb') as file:
            file.write(response.content)
        print(f"{file_name} downloaded successfully.")
    else:
        print("Failed to download media.")

# downloader('https://us06web.zoom.us/rec/share/2q0V276gXFvyBcNvBvUXHt1w-VLzmKFGOVX3PyuCJkuwkWMw6eo-pCInSo3S3fQT.SlqRJTRRLoauxwwx', 'Geo', '1. Apna Desh - Indian Geo intro + Plains')