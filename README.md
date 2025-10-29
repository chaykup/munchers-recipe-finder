# Munchers Recipe Finder

This project allows you to find recipes based on the main ingredient you have available. The app features React tile-based recipe browsing and embedded YouTube videos. This app is compatible to desktop and smartphone interfaces.

## Features

- **Search by Ingredient**: Enter main ingredient to discover recipes
- **Tile-Based Browsing**: View all recipes in the database that use the provided main ingredient
- **Detailed Recipe View**: Click any tile to see cooking instructions and watch youtube tutorial if available

## Requirements
- Python 3.12+
- See `requirements.txt` for dependencies

## Setup Instructions

### 1. Fork and clone this repository
```bash
git clone <your-repo-url>
cd munchers-recipe-finder
```

### 2. (Optional) Create and activate virtual environment

**macOS/Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Create a `.env` file in the root directory:
```bash
API_KEY=your_api_key_here
```

You can get a free API key from [TheMealDB](https://www.themealdb.com/api.php).

### 5. Run the application
```bash
python3 main.py
```

The application will be available at `http://localhost:8000`

## API Endpoints

### Search Recipes
```
GET /api/recipes/search?ingredient=chicken
```

**Response:**
```json
{
  "recipes": [
    {
      "id": "52940",
      "name": "Brown Stew Chicken",
      "image": "https://www.themealdb.com/images/media/meals/sypxpx1515365095.jpg"
    }
  ]
}
```

### Get Recipe Details
```
GET /api/recipes/52940
```

**Response:**
```json
{
  "id": "52940",
  "name": "Brown Stew Chicken",
  "image": "https://...",
  "instructions": "...",
  "youtube": "https://www.youtube.com/watch?v=...",
  "category": "Chicken",
  "area": "Jamaican"
}
```

## Technologies Used

- **Backend**: Flask, Python
- **Frontend**: React, Vanilla JavaScript
- **API**: TheMealDB API
- **Server**: Waitress (WSGI server)
