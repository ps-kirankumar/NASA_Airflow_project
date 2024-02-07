Removing Unnecessary Columns:

In the Python script, certain columns from the retrieved data are excluded to focus only on relevant information. These columns include 'links', 'name_limited', and 'neo_reference_id', which are not required for the project.
Extracting Relevant Data:

The relevant data fields extracted from the NASA API response include:
id: The unique identifier for each near-Earth object (NEO).
name: The name of the NEO.
absolute_magnitude_h: The absolute magnitude of the NEO.
estimated_diameter_km_max: The maximum estimated diameter of the NEO in kilometers.
is_potentially_hazardous_asteroid: A boolean indicating whether the NEO is potentially hazardous.
closest_approach_date: The date and time of the closest approach of the NEO to Earth, formatted as '%Y-%m-%d %H:%M'.
velocity: The velocity of the NEO at the time of closest approach in kilometers per hour.
Instructions for Accessing Data from the NASA API:
API Endpoint:

The data is obtained from the NASA Near-Earth Object Web Service API.
The API endpoint URL is https://api.nasa.gov/neo/rest/v1/neo/browse.
API Key:

To access the API, you need to obtain an API key from NASA. You can sign up for an API key at the NASA API Portal.
Requesting Data:

The Python requests library is used to send a GET request to the API endpoint.
The API key is passed as a parameter in the request to authenticate the request.
Parsing JSON Response:

Once the request is successful (status code 200), the JSON response from the API is parsed using the response.json() method.
Extracting Relevant Fields:

Relevant data fields are extracted from the JSON response, including NEO ID, name, absolute magnitude, estimated diameter, hazard status, closest approach date, and velocity.
Writing Data to CSV:

The extracted data is then written to a CSV file (NASA.csv) for further analysis or visualization.
