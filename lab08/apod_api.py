import requests
from datetime import datetime

API_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "UkdydEVbXqkwhmrSq7btbT0ppbfObB7dQcYSgHrz"  

def get_apod(date=None):
    """
    Fetches the Astronomy Picture of the Day (APOD) for a specific date.
    
    :param date: A string in the format 'YYYY-MM-DD' or None for today's date.
    :return: A JSON object with APOD data.
    """
    params = {
        'api_key': API_KEY,
        'date': date or datetime.now().strftime('%Y-%m-%d')
    }
    response = requests.get(API_URL, params=params)
    response.raise_for_status() 
    return response.json()
