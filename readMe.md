# Yelp Restaurant Recommender System

## How It Works

### Data Loading and Preprocessing:

- The script loads restaurant data from the CSV file 'yelp_restaurants.csv'.
- It preprocesses the categories by joining them into a single string.

### Vectorization and Similarity Calculation:

- Utilizing scikit-learn, it vectorizes the categories using CountVectorizer.
- Computes the cosine similarity matrix based on the vectorized categories.

### Recommendation Function:

- Defines a function `recommend_restaurant` to recommend similar restaurants.
- Calculates similarity scores between the input restaurant and all others.
- Returns the top 5 most similar restaurants.

### Streamlit Web Interface:

- Sets up the Streamlit web interface with a title and input field for the user to enter a restaurant name.
- Upon clicking the recommendation button, it calls the recommendation function and displays the top 5 recommended restaurants along with their ratings.
- Generates a map using Folium to visualize the recommended restaurants' locations with markers.

## Instructions

### Yelp Fusion API Data Retrieval Script

**1. API Setup:**
   - Replace `'YOUR_API_KEY'` in the `headers` dictionary with your actual Yelp API key.

**2. Query Parameters:**
   - Adjust the `params` dictionary to specify the location (`'location'`), limit (`'limit'`), and search term (`'term'`) for retrieving restaurant data.

**3. Maximum Restaurants:**
   - Modify `max_restaurants` variable to set the maximum number of restaurants to retrieve.

**4. Execution:**
   - Run the script to retrieve restaurant data from the Yelp Fusion API.
   - The retrieved data will be saved as a CSV file named `'yelp_restaurants.csv'` on your desktop.

---

### Restaurant Recommender Web Interface Script

**1. Data Loading:**
   - Ensure the CSV file path (`file_path`) in the script points to the location of the generated `'yelp_restaurants.csv'` file from the previous script.

**2. Streamlit Setup:**
   - Run the script to launch the Streamlit web interface.

**3. Input Restaurant Name:**
   - Enter the name of a restaurant you like in the text input field.
   - By default, `'Leonard's Bakery'` is pre-filled as an example.

**4. Recommendation:**
   - Click the `'Recommend 🎉'` button to trigger the recommendation process.

**5. View Recommendations:**
   - The web interface will display the top 5 recommended restaurants similar to the input restaurant along with their ratings.

**6. Map Visualization:**
   - Below the recommendations, a map showing the recommended restaurants' locations will be displayed.
   - Each restaurant will be represented by a marker on the map.
