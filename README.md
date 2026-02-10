# Weather API

A Django REST API that integrates with multiple external APIs to provide data about animals, entertainment, geography, and demographics.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Services](#services)
- [Error Handling](#error-handling)
- [Documentation](#documentation)
- [Contributing](#contributing)

---

## Features

- 🐕 **Dog Images** - Fetch random dog photos
- 🐱 **Cat Images** - Get random cat pictures with metadata
- 😂 **Jokes** - Retrieve random jokes in setup/punchline format
- 💡 **Life Advice** - Get motivational quotes and wisdom
- 🎂 **Age Prediction** - Predict age based on names
- 🌍 **Country Info** - Fetch comprehensive country data
- 🎓 **Universities** - Search universities by country

---

## Tech Stack

- **Framework**: Django 3.x+
- **API**: Django REST Framework (DRF)
- **Python**: 3.8+
- **External APIs**: 7 third-party integrations
- **Package Manager**: pip

---

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd weather_api
```

### 2. Create Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Start Development Server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

---

## Quick Start

### Fetch a Random Dog Image
```bash
curl http://localhost:8000/api/dog/
```

**Response:**
```json
{
  "image_url": "https://images.dog.ceo/breeds/..."
}
```

### Predict Someone's Age
```bash
curl "http://localhost:8000/api/age/?name=Michael"
```

**Response:**
```json
{
  "name": "Michael",
  "predicted_age": 45
}
```

### Get Country Information
```bash
curl "http://localhost:8000/api/country/?name=France"
```

**Response:**
```json
{
  "name": "France",
  "capital": "Paris",
  "population": 67750000,
  "flag": "🇫🇷",
  "region": "Europe"
}
```

### Find Universities in a Country
```bash
curl "http://localhost:8000/api/universities/?country=Germany"
```

**Response:**
```json
{
  "country": "Germany",
  "universities": [
    {
      "name": "University of Berlin",
      "website": "http://www.tu-berlin.de"
    },
    ...
  ]
}
```

---

## API Endpoints

| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|-----------|
| GET | `/api/dog/` | Random dog image | None |
| GET | `/api/cat/` | Random cat image | None |
| GET | `/api/joke/` | Random joke | None |
| GET | `/api/advice/` | Random life advice | None |
| GET | `/api/age/` | Predict age from name | `name` (required) |
| GET | `/api/country/` | Country information | `name` (required) |
| GET | `/api/universities/` | University list (basic) | `country` (required) |
| GET | `/api/universities/pro/` | University list (serialized) | `country` (required) |

For detailed endpoint documentation, see [API_DOCUMENTATION.md](API_DOCUMENTATION.md).

---

## Project Structure

```
weather_api/
├── api/
│   ├── services/                      # External API integrations
│   │   ├── dog_api.py
│   │   ├── cat_api.py
│   │   ├── joke_api.py
│   │   ├── advice_api.py
│   │   ├── age_prediction_api.py
│   │   ├── country_data.py
│   │   └── country_universities_api.py
│   ├── views.py                       # API endpoint handlers
│   ├── serializers.py                 # Request/response validation
│   ├── urls.py                        # URL routing
│   ├── models.py                      # Database models
│   ├── admin.py                       # Django admin config
│   └── tests.py                       # Test suite
├── weather_api/                       # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py                          # Django management utility
├── requirements.txt                   # Python dependencies
├── db.sqlite3                         # SQLite database
└── README.md                          # This file
```

---

## Services

The project integrates with 7 external APIs:

### 1. Dog CEO API
- **Endpoint**: `https://dog.ceo/api/breeds/image/random`
- **Service**: [api/services/dog_api.py](api/services/dog_api.py)
- **Purpose**: Fetch random dog images

### 2. The Cat API
- **Endpoint**: `https://api.thecatapi.com/v1/images/search`
- **Service**: [api/services/cat_api.py](api/services/cat_api.py)
- **Purpose**: Fetch random cat images with metadata

### 3. Official Joke API
- **Endpoint**: `https://official-joke-api.appspot.com/random_joke`
- **Service**: [api/services/joke_api.py](api/services/joke_api.py)
- **Purpose**: Fetch random jokes

### 4. Advice Slip API
- **Endpoint**: `https://api.adviceslip.com/advice`
- **Service**: [api/services/advice_api.py](api/services/advice_api.py)
- **Purpose**: Fetch life advice and quotes

### 5. Agify.io API
- **Endpoint**: `https://api.agify.io/`
- **Service**: [api/services/age_prediction_api.py](api/services/age_prediction_api.py)
- **Purpose**: Predict age based on names

### 6. REST Countries API
- **Endpoint**: `https://restcountries.com/v3.1/name/`
- **Service**: [api/services/country_data.py](api/services/country_data.py)
- **Purpose**: Fetch comprehensive country information

### 7. Hipolabs Universities API
- **Endpoint**: `http://universities.hipolabs.com/search`
- **Service**: [api/services/country_universities_api.py](api/services/country_universities_api.py)
- **Purpose**: Search universities by country

---

## Error Handling

### Response Status Codes

- **200 OK** - Request successful
- **400 Bad Request** - Invalid query parameters or missing required fields
- **503 Service Unavailable** - External API failure or timeout

### Error Response Format

```json
{
  "error": "Descriptive error message"
}
```

### Example Error Response

```bash
curl "http://localhost:8000/api/age/?wrongparam=value"
```

**Response (400):**
```json
{
  "name": ["This field is required."]
}
```

---

## Documentation

The project includes comprehensive documentation:

- **[API_DOCUMENTATION.md](API_DOCUMENTATION.md)** - Complete API reference with detailed endpoint specifications and service documentation
- **[DOCUMENTATION_SUMMARY.md](DOCUMENTATION_SUMMARY.md)** - Quick reference guide for documentation structure
- **[DOCUMENTATION_OVERVIEW.md](DOCUMENTATION_OVERVIEW.md)** - Navigation guide and lookup table

### Code Documentation

All code files include:
- Module-level docstrings
- Function/class docstrings with parameters and return types
- Usage examples
- Exception documentation
- Inline comments for complex logic

---

## Development

### Running Tests
```bash
python manage.py test
```

### Code Style
This project follows PEP 8 Python style guidelines.

### Creating New Endpoints

1. Create a service in `api/services/` if integrating an external API
2. Create a serializer in `api/serializers.py` for validation
3. Add a view function in `api/views.py`
4. Register the route in `api/urls.py`
5. Add comprehensive documentation

---

## Contributing

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes and test them
3. Commit with descriptive messages: `git commit -m "Add descriptive message"`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request

---

## Notes

- The project name "weather_api" is legacy; it now serves multiple data types
- All data is fetched in real-time from external APIs (no caching)
- Each request includes a 5-second timeout for external API calls
- Database models are not currently utilized
- Built with Django REST Framework best practices

---

## Support

For issues, questions, or suggestions, please open an issue on the repository.

---

## License

This project is open source.
