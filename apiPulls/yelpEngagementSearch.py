# This script doesn't work afaik. It's mean't to pull views of a Yelp page, etc.

import requests

# Define your API endpoint and parameters
url = 'https://api.yelp.com/v3/businesses/engagement'
headers = {
    'Authorization': 'Bearer YOUR_API_KEY',  # Replace YOUR_API_KEY with your actual API key
}

# Define the Yelp business ID for the business you want to get engagement metrics for
business_id = 'xHpTs2y1oR4asEHhLeh4Cg'  # Replace YOUR_BUSINESS_ID with the actual Yelp business ID

# Make the GET request to the Yelp API
response = requests.get(f'{url}/{business_id}', headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Print engagement metrics data for the business
    print('Total page views:', data['total_page_views'])
    print('Total photo views:', data['total_photo_views'])
    print('Total Yelp searches:', data['total_yelp_searches'])
    print('---')
else:
    # If the request was not successful, print an error message
    print('Error:', response.status_code)