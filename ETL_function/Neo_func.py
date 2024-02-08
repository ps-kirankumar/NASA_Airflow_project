import requests
import pandas as pd
from datetime import datetime

def fetch_neo_data():
    """
    Fetches NEO (Near-Earth Object) data from the NASA NEO API.

    Parameters:
        api_key (str): NASA API key.
        page_limit (int): Number of pages to fetch (each page contains 20 items).

    Returns:
        pandas.DataFrame: DataFrame containing NEO data.
    """
    # Define the API endpoint URL
    api_url = 'https://api.nasa.gov/neo/rest/v1/neo/browse'

    # Initialize list to store all data
    all_neo_data = []

    # Construct the API request with the provided API key
    params = {'api_key': 'your_key'}

    # Loop through the specified number of pages
    for page_number in range(5):
        params['page'] = page_number + 1  # Adjust the page number in the request here it is 5 because I took 100 rows from api

        # Send the API request for this page
        response = requests.get(api_url, params=params)

        # Parse the JSON response for this page
        page_data = response.json()

        # Extract relevant data fields from the response for this page
        for neo in page_data['near_earth_objects']:
            # Extracting closest approach date and formatting it as date
            closest_approach_date_full = neo['close_approach_data'][0]['close_approach_date_full']
            closest_approach_date = datetime.strptime(closest_approach_date_full, '%Y-%b-%d %H:%M')

            # Extracting other relevant fields
            estimated_diameter_km_max = neo['estimated_diameter']['kilometers']['estimated_diameter_max']
            velocity = neo['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']

            all_neo_data.append([
                neo['id'],
                neo['name'],
                neo['absolute_magnitude_h'],
                estimated_diameter_km_max,
                neo['is_potentially_hazardous_asteroid'],
                closest_approach_date,
                velocity,
            ])

    # Convert the collected data into a DataFrame
    df = pd.DataFrame(all_neo_data, columns=['id', 'name', 'magnitude', 'diameter', 'hazardous', 'closest_approach_date', 'velocity'])
    return df # This data frame can also be stored into cloud such as AWS S3 and can be accessed from there.


