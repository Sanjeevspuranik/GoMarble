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
