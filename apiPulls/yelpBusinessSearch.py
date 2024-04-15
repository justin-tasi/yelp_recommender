import csv
import requests
import os

# Define your API endpoint and parameters
url = 'https://api.yelp.com/v3/businesses/search'
headers = {
    'Authorization': 'Bearer YOUR_API_KEY',  # Replace YOUR_API_KEY with your actual API key
}

# Define your query parameters
params = {
    'location': 'Hawaii',
    'limit': 50,
    'offset': 0,
    'term': 'food'
}

# Initialize a list to store all restaurants
all_restaurants = []

# Maximum number of restaurants to retrieve
max_restaurants = 2000

# Make multiple GET requests to retrieve all restaurants
while len(all_restaurants) < max_restaurants:
    # Make the GET request to the Yelp API
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract restaurants from the response
        restaurants = data['businesses']
        # Add restaurants to the list
        all_restaurants.extend(restaurants)
        # Check if there are more restaurants to retrieve
        if len(restaurants) < params['limit']:
            break  # No more restaurants to retrieve
        else:
            # Increment the offset for the next request
            params['offset'] += params['limit']
    else:
        # If the request was not successful, print an error message
        print('Error:', response.status_code)
        break

# Define the path to save the CSV file on your desktop
desktop_path = r'C:\Users\justin\Desktop'
csv_file_path = os.path.join(desktop_path, 'yelp_restaurants.csv')

# Define field names for the CSV file
field_names = [
    'Name', 'ID', 'Rating', 'Price', 'Categories', 'Location', 'City', 'State',
    'ZIP Code', 'Country', 'Latitude', 'Longitude', 'Phone', 'URL', 'Review Count',
    'Opening Hours', 'Transactions', 'Special Hours'
]

# Write the retrieved data to the CSV file
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    for restaurant in all_restaurants:
        writer.writerow({
            'Name': restaurant['name'],
            'ID': restaurant['id'],
            'Rating': restaurant['rating'],
            'Price': restaurant.get('price', 'N/A'),
            'Categories': ', '.join(category['title'] for category in restaurant['categories']),
            'Location': restaurant['location']['address1'],
            'City': restaurant['location']['city'],
            'State': restaurant['location']['state'],
            'ZIP Code': restaurant['location']['zip_code'],
            'Country': restaurant['location']['country'],
            'Latitude': restaurant['coordinates']['latitude'],
            'Longitude': restaurant['coordinates']['longitude'],
            'Phone': restaurant.get('phone', 'N/A'),
            'URL': restaurant['url'],
            'Review Count': restaurant['review_count'],
            'Opening Hours': restaurant.get('hours', 'N/A'),
            'Transactions': ', '.join(restaurant.get('transactions', [])),
            'Special Hours': restaurant.get('special_hours', 'N/A')
        })

print(f'Data has been written to {csv_file_path}')
