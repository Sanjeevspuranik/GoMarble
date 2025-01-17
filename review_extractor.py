from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def extract_reviews(url: str):
    try:
        path = r"C:\Users\SANJEEVSPURANIK\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe"
        service = Service(executable_path=path)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run Chrome in headless mode
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=service, options=options)
        
        print(f"Opening URL: {url}")
        driver.get(url)
        
        # Check if the page loaded correctly
        print(f"Page title: {driver.title}")

        containers = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//span[@class="cr-widget-FocalReviews"]/div/div/div[3]/div[3]/ul/li'))
        )

        Titles = []
        Stars = []
        Date_locations = []
        Usernames = []
        Bodies = []

        for container in containers:
            try:
                title = container.find_element(
                    by="xpath", value="./span/div/div/div[2]/h5/a/span[2]").text
                Titles.append(title)
            except Exception as e:
                print(f"Error fetching title: {e}")
                title = None

            try:
                star = container.find_element(
                    by="xpath", value="./span/div/div/div[2]/h5/a/i/span").get_attribute("innerHTML")
                Stars.append(star)
            except Exception as e:
                print(f"Error fetching star: {e}")
                star = None

            try:
                date_location = container.find_element(
                    by="xpath", value="./span/div/div/span").get_attribute("innerHTML")
                Date_locations.append(date_location)
            except Exception as e:
                print(f"Error fetching date_location: {e}")
                date_location = None

            try:
                username = container.find_element(
                    by="xpath", value="./span/div/div/div/a/div[2]/span").text
                Usernames.append(username)
            except Exception as e:
                print(f"Error fetching username: {e}")
                username = None

            try:
                body = container.find_element(
                    by="xpath", value="./span/div/div/div[4]/span/div/div/span").text
                Bodies.append(body)
            except Exception as e:
                print(f"Error fetching body: {e}")
                body = None

        driver.close()

        data = pd.DataFrame(
            {
                'Titles': Titles,
                'Ratings': Stars,
                'Profile': Usernames,
                'Review': Bodies,
                'Date_location': Date_locations
            }
        )

        formatted_data = {
            'reviews_count': len(data),
            'reviews': [
                {
                    'Username': row['Profile'],
                    'Ratings': row['Ratings'],
                    'Title': row['Titles'],
                    'Review': row['Review'],
                    'Date_Location': row['Date_location']
                }
                for index, row in data.iterrows()
            ]
        }

        return formatted_data
    
    except Exception as e:
        return {'message': f'Error occurred while fetching data: {e}'}