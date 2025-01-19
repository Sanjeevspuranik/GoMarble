# GoMarble

GoMarble is a project that implements an API server capable of extracting reviews information from product pages such as Shopify and Amazon. The API dynamically identifies CSS elements for reviews, handles pagination, and retrieves all reviews using browser automation and LLM integration.

## Requirements

- Python 3.8+
- pip (Python package installer)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Sanjeevspuranik/GoMarble.git
   cd GoMarble
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
   
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Download and configure ChromeDriver:

   To run the Selenium-based automation, you'll need to have ChromeDriver installed. You can download it from the official ChromeDriver website.
   
   After downloading ChromeDriver, follow these steps:
   
   For Windows:
      Extract the chromedriver.exe file to a folder.
      Add the path to the chromedriver.exe file to your system's PATH environment variable or specify the full path to it in the code.

   For macOS/Linux:
      Extract the chromedriver file to a directory of your choice.
      Add the directory to your system's PATH or specify the full path in the code.
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def extract_reviews(url: str):
    try:
        path = r"C:\Users\SANJEEVSPURANIK\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe" # Change this path to local ChromeDriver path
        service = Service(executable_path=path)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run Chrome in headless mode
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=service, options=options)
        
        print(f"Opening URL: {url}")
```
## Running the Project
Start the API server using Uvicorn:
   ```bash
   uvicorn app:app --reload
   ```
## Access the API:

The API will be available at http://localhost:8000. You can use tools like Postman or curl to interact with the API.


## Usage
Extract Reviews:

To extract reviews from a product page, send a GET request to ```http://localhost:8000/api/reviews?page={enter_your_url_here}``` with the URL of the product page in the request body.

```json
{
  "url": "https://www.example.com/product-page"
}
```
## Note
Make sure to remove the quotation marks from the URL before accessing the API.

## Response:

The API will return a JSON response with the extracted reviews.

```json
{
  "reviews": [
  {
      "author": "John Doe",
      "rating": 5,
      "comment": "Great product!"
    },
    ...
  ]
}
```
