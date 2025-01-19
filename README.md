Your updated README looks great! Here's the complete file with the necessary changes:

### README.md

```markdown
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

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

1. **Start the API server:**

   ```bash
   python app.py
   ```

2. **Access the API:**

   The API will be available at `http://localhost:5000`. You can use tools like Postman or curl to interact with the API.

## Usage

- **Extract Reviews:**

  To extract reviews from a product page, send a POST request to `http://localhost:5000/api/reviews?page={enter_your_url_here}` with the URL of the product page in the request body.

  ```json
  {
    "url": "https://www.example.com/product-page"
  }
  ```

- **Response:**

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

## Note

Make sure to remove the quotation marks from the URL before accessing the API.

## Explanation

- **Browser Automation:** The project uses Selenium to automate browser actions and navigate through product pages.
- **LLM Integration:** Large Language Models (LLMs) are used to dynamically identify CSS elements for reviews.
- **Pagination Handling:** The API handles pagination to ensure all reviews are retrieved.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
```

### requirements.txt

```plaintext
Flask==2.0.1
selenium==3.141.0
requests==2.25.1
beautifulsoup4==4.9.3
```

Feel free to ask if you need any more details or further assistance!
