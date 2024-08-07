# Sign Language Translation API

This is a basic backend API service for a sign language translation tool. It simulates translation from English to French using a predefined dictionary.

## API Documentation

### Endpoint

#### POST /translate

- **Description:** Translates the provided text input from English to French.
- **HTTP Method:** POST
- **Request Format:** JSON

  ```json
  {
    "text": "hello"
  }
- **Response Format:** JSON

  ```json
  {
  "status": "success",
  "original_text": "hello",
  "translated_text": "bonjour"
  }

#### Error Responses:

- 400 Bad Request: Returned if the input is invalid or the text field is missing.

  ```json
  {
    "error": "Invalid input. The \"text\" field is required."
  }

- 500 Internal Server Error: Returned if an unexpected error occurs on the server.

  ```json
  {
    "error": "Internal Server Error: Please try again later."
  }


## Example Request

  ```bash
  curl -X POST http://127.0.0.1:5000/translate -H "Content-Type: application/json" -d '{"text": "Hello"}'

