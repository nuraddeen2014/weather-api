# Weather API - Complete Documentation

## Overview

This Django REST API project provides integration with multiple external APIs to serve data about animals, entertainment, geographical information, and demographic predictions. The application follows RESTful principles and uses Django REST Framework (DRF) for API management.

---

## Project Structure

```
weather_api/
├── api/
│   ├── services/           # External API integration modules
│   │   ├── dog_api.py      # Dog image fetching service
│   │   ├── cat_api.py      # Cat image fetching service
│   │   ├── joke_api.py     # Joke fetching service
│   │   ├── advice_api.py   # Advice fetching service
│   │   ├── age_prediction_api.py    # Age prediction service
│   │   ├── country_data.py          # Country information service
│   │   └── country_universities_api.py  # University lookup service
│   ├── views.py            # API endpoint handlers
│   ├── serializers.py      # Request/response validation and formatting
│   ├── models.py           # Database models (currently empty)
│   ├── urls.py             # URL routing configuration
│   └── ...
├── weather_api/            # Django project settings
└── manage.py              # Django management utility
```

---

## Services Documentation

### 1. Dog API Service (`api/services/dog_api.py`)

**Purpose:** Fetches random dog images from the Dog CEO API.

**External API:** `https://dog.ceo/api/breeds/image/random`

**Function:** `dog_api()`
- **Returns:** `str` - URL to a random dog image
- **Timeout:** 5 seconds
- **Exception Handling:** Raises `requests.exceptions.RequestException` on failure

**Example Output:**
```json
"https://images.dog.ceo/breeds/affenpinscher/n02110063_10697.jpg"
```

---

### 2. Cat API Service (`api/services/cat_api.py`)

**Purpose:** Fetches random cat images with metadata from The Cat API.

**External API:** `https://api.thecatapi.com/v1/images/search`

**Function:** `cat_image()`
- **Returns:** `list` - List of dictionaries containing cat image data
- **Data Fields:** `url`, `width`, `height`, `id`, etc.
- **Timeout:** 5 seconds

**Example Output:**
```json
[
  {
    "url": "https://cdn2.thecatapi.com/images/abc123.jpg",
    "width": 1920,
    "height": 1080,
    "id": "abc123"
  }
]
```

---

### 3. Joke API Service (`api/services/joke_api.py`)

**Purpose:** Fetches random jokes in setup/punchline format.

**External API:** `https://official-joke-api.appspot.com/random_joke`

**Function:** `joke_api()`
- **Returns:** `dict` - Joke data with setup and punchline
- **No timeout specified** (uses default)
- **Exception Handling:** Raises `requests.exceptions.RequestException`

**Example Output:**
```json
{
  "setup": "Why don't scientists trust atoms?",
  "punchline": "Because they make up everything!",
  "type": "general",
  "id": 12345
}
```

---

### 4. Advice API Service (`api/services/advice_api.py`)

**Purpose:** Fetches random life advice and motivational quotes.

**External API:** `https://api.adviceslip.com/advice`

**Function:** `advice_api()`
- **Returns:** `dict` - Advice data with a 'slip' object containing advice text
- **Timeout:** 5 seconds
- **Exception Handling:** Raises `requests.exceptions.RequestException`

**Example Output:**
```json
{
  "slip": {
    "advice": "Don't wait for opportunity. Create it.",
    "slip_id": 67890
  }
}
```

---

### 5. Age Prediction API Service (`api/services/age_prediction_api.py`)

**Purpose:** Predicts a person's age based on their name using statistical analysis.

**External API:** `https://api.agify.io/`

**Function:** `age_prediction_api(name)`
- **Parameter:** `name` (str) - Person's name
- **Returns:** `dict` - Age prediction data
- **Data Fields:** `name`, `age`, `count`
- **Timeout:** 5 seconds

**Example Output:**
```json
{
  "name": "Michael",
  "age": 45,
  "count": 50000
}
```

**Note:** `age` may be `null` if no data is available for the name.

---

### 6. Country Data API Service (`api/services/country_data.py`)

**Purpose:** Fetches comprehensive country information from REST Countries API.

**External API:** `https://restcountries.com/v3.1/name/{country}`

**Function:** `country_data(country)`
- **Parameter:** `country` (str) - Country name (e.g., 'France', 'Japan')
- **Returns:** `list` - List of matching country objects
- **Timeout:** 5 seconds
- **Common Fields:** `name`, `capital`, `population`, `region`, `flag`, `area`, `currencies`, `languages`

**Example Output:**
```json
[
  {
    "name": {
      "common": "France",
      "official": "French Republic"
    },
    "capital": ["Paris"],
    "population": 67970000,
    "region": "Europe",
    "flag": "🇫🇷",
    "area": 643801,
    "currencies": {
      "EUR": {
        "name": "Euro",
        "symbol": "€"
      }
    }
  }
]
```

---

### 7. Country Universities API Service (`api/services/country_universities_api.py`)

**Purpose:** Fetches list of universities in a specific country.

**External API:** `http://universities.hipolabs.com/search`

**Function:** `country_universities_api(country)`
- **Parameter:** `country` (str) - Country name
- **Returns:** `list` - List of university objects
- **Data Fields:** `name`, `country`, `web_pages`, `domains`, `alpha_two_code`
- **Timeout:** 5 seconds

**Example Output:**
```json
[
  {
    "name": "University of Paris",
    "country": "France",
    "web_pages": ["http://www.uparis.fr"],
    "domains": ["uparis.fr"],
    "alpha_two_code": "FR"
  },
  {
    "name": "Sorbonne University",
    "country": "France",
    "web_pages": ["http://www.sorbonne-universite.fr"],
    "domains": ["sorbonne-universite.fr"],
    "alpha_two_code": "FR"
  }
]
```

---

## API Endpoints Documentation

### 1. Random Dog Image
- **Endpoint:** `GET /api/dog/`
- **View Function:** `random_dog()`
- **Description:** Returns a random dog image URL
- **Query Parameters:** None
- **Response (Success - 200):**
  ```json
  {
    "image_url": "https://images.dog.ceo/breeds/..."
  }
  ```
- **Response (Error - 503):**
  ```json
  {
    "error": "Failed to fetch Dog"
  }
  ```

---

### 2. Random Cat Image
- **Endpoint:** `GET /api/cat/`
- **View Function:** `get_cat_image()`
- **Description:** Returns a random cat image with metadata
- **Query Parameters:** None
- **Response (Success - 200):**
  ```json
  {
    "image_url": "https://cdn2.thecatapi.com/images/...",
    "width": 1920,
    "height": 1080
  }
  ```
- **Response (Error - 503):**
  ```json
  {
    "error": "Error fetching url"
  }
  ```

---

### 3. Random Joke
- **Endpoint:** `GET /api/joke/`
- **View Function:** `get_random_joke()`
- **Description:** Returns a random joke in setup/punchline format
- **Query Parameters:** None
- **Response (Success - 200):**
  ```json
  {
    "setup": "Why did the scarecrow win an award?",
    "punchline": "He was outstanding in his field."
  }
  ```

---

### 4. Random Advice
- **Endpoint:** `GET /api/advice/`
- **View Function:** `get_random_advice()`
- **Description:** Returns random life advice
- **Query Parameters:** None
- **Response (Success - 200):**
  ```json
  {
    "advice": "The best time to plant a tree was 20 years ago. The second best time is now."
  }
  ```

---

### 5. Age Prediction
- **Endpoint:** `GET /api/age/`
- **View Function:** `get_age_prediction()`
- **Description:** Predicts age based on name
- **Query Parameters:**
  - `name` (required): Person's name
- **Example Request:** `/api/age/?name=Michael`
- **Response (Success - 200):**
  ```json
  {
    "name": "Michael",
    "predicted_age": 45
  }
  ```
- **Validation:** Uses `AgeQuerySerializer` to validate input

---

### 6. Country Information
- **Endpoint:** `GET /api/country/`
- **View Function:** `get_country_data()`
- **Description:** Returns comprehensive country information
- **Query Parameters:**
  - `name` (required): Country name
- **Example Request:** `/api/country/?name=Italy`
- **Response (Success - 200):**
  ```json
  {
    "name": "Italy",
    "capital": "Rome",
    "population": 58940540,
    "flag": "🇮🇹",
    "region": "Europe"
  }
  ```
- **Validation:** Uses `CountryDetailSerializer` to validate output data

---

### 7. Country Universities (Basic)
- **Endpoint:** `GET /api/universities/`
- **View Function:** `get_country_universities()`
- **Description:** Returns list of universities in a country (manually formatted)
- **Query Parameters:**
  - `country` (required): Country name
- **Example Request:** `/api/universities/?country=France`
- **Response (Success - 200):**
  ```json
  {
    "country": "France",
    "universities": [
      {
        "name": "University of Paris",
        "website": "http://www.uparis.fr"
      },
      {
        "name": "Sorbonne University",
        "website": "http://www.sorbonne-universite.fr"
      }
    ]
  }
  ```
- **Validation:** Uses `CountryUniversitiesQuerySerializer`

---

### 8. Country Universities (Serialized - Professional)
- **Endpoint:** `GET /api/universities/pro/`
- **View Function:** `get_pro_country_universities()`
- **Description:** Returns list of universities in a country (using DRF serializer for formatting)
- **Query Parameters:**
  - `country` (required): Country name
- **Example Request:** `/api/universities/pro/?country=United%20Kingdom`
- **Response (Success - 200):**
  ```json
  {
    "country": "United Kingdom",
    "universities": [
      {
        "name": "University of Oxford",
        "website": "http://www.ox.ac.uk"
      },
      {
        "name": "University of Cambridge",
        "website": "http://www.cam.ac.uk"
      }
    ]
  }
  ```
- **Validation:** Uses `CountryUniversitiesQuerySerializer` and `CountryUniversitiesSerializer`

**Difference from `/api/universities/`:**
- Uses `CountryUniversitiesSerializer` for data formatting
- Provides better error handling and validation
- Follows DRF best practices for serialization

---

## Serializers Documentation

### Query/Input Serializers

**CountryQuerySerializer**
- Validates `name` parameter for country lookups
- Required field: `name`

**AgeQuerySerializer**
- Validates `name` parameter for age prediction
- Required field: `name`

**CountryUniversitiesQuerySerializer**
- Validates `country` parameter for university lookups
- Required field: `country` (min_length: 1)

### Response Serializers

**CountryDetailSerializer**
- Formats country information responses
- Fields: `name`, `capital`, `population`, `flag`, `region`

**UniversitySerializer**
- Formats individual university data
- Uses `SerializerMethodField` to extract primary website from `web_pages` list
- Fields: `name`, `website`

**CountryUniversitiesSerializer**
- Combines country name with list of universities
- Overrides `to_representation()` for custom formatting
- Fields: `country`, `universities`

---

## Error Handling

All endpoints implement consistent error handling:

1. **Request Validation Errors (400):**
   - Missing required query parameters
   - Invalid parameter types
   - Returns validation error messages from serializers

2. **Service Unavailable (503):**
   - External API failures
   - Network timeout
   - JSON parsing errors
   - Returns descriptive error message

3. **Exception Handling:**
   - Generic `Exception` catches for unexpected errors
   - `requests.exceptions.RequestException` for HTTP-related issues

---

## Best Practices Implemented

1. **Timeout Settings:**
   - Most services implement 5-second timeout to prevent hanging requests
   - Prevents resource exhaustion from slow external APIs

2. **Serializer Validation:**
   - Input validation using DRF serializers
   - Output validation ensures correct response structure
   - `raise_exception=True` for immediate error feedback

3. **Error Responses:**
   - Consistent error response format
   - Appropriate HTTP status codes (200 for success, 503 for service errors)
   - Descriptive error messages

4. **External API Integration:**
   - Each service in a separate module for maintainability
   - Clear separation of concerns between data fetching and response formatting
   - Reusable service functions

5. **Documentation:**
   - Comprehensive docstrings for all functions
   - Module-level documentation explaining purpose and context
   - Usage examples in docstrings

---

## Usage Examples

### Fetching a Dog Image
```bash
curl http://localhost:8000/api/dog/
```

### Predicting Age
```bash
curl "http://localhost:8000/api/age/?name=Sarah"
```

### Getting Country Information
```bash
curl "http://localhost:8000/api/country/?name=Germany"
```

### Finding Universities
```bash
curl "http://localhost:8000/api/universities/?country=Canada"
```

---

## Dependencies

- **Django:** Web framework
- **Django REST Framework:** REST API development
- **requests:** HTTP client for external API calls

---

## Notes

- The project name "weather_api" is legacy; it now serves multiple types of data
- Models are currently not utilized (no database operations)
- All data is fetched from external APIs in real-time
- Responses are not cached; each request fetches fresh data
