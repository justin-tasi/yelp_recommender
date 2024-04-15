import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the data
file_path = 'C:\\Users\\justin\\Desktop\\yelp_restaurants.csv'
data = pd.read_csv(file_path)

# Preprocess the categories
data['Categories'] = data['Categories'].apply(lambda x: ' '.join(x.split(', ')))

# Create a count vectorizer
vectorizer = CountVectorizer()

# Fit and transform the categories
category_matrix = vectorizer.fit_transform(data['Categories'])

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(category_matrix, category_matrix)

# Function to recommend restaurants based on category
def recommend_restaurant(name, cosine_sim=cosine_sim):
    # Get the index of the restaurant that matches the name
    idx = data[data['Name'] == name].index[0]

    # Get the pairwsie similarity scores of all restaurants with that restaurant
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the restaurants based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top 5 most similar restaurants
    sim_scores = sim_scores[1:6]

    # Get the restaurant indices
    restaurant_indices = [i[0] for i in sim_scores]

    # Return the top 5 most similar restaurants
    return data.iloc[restaurant_indices]

# Streamlit web interface
st.set_page_config(page_title='Restaurant Recommender', page_icon=":hamburger:")
st.title('Restaurant Recommender')
st.markdown("---")

restaurant_name = st.text_input('I like this restaurant but I wanna try something new', 'Leonard\'s Bakery')

if st.button('Recommend 🎉'):
    recommended_restaurants = recommend_restaurant(restaurant_name)
    st.subheader(f"Recommended restaurants similar to '{restaurant_name}':")
    counter = 1
    for index, restaurant in recommended_restaurants.iterrows():
        st.write(f"{counter}. 📍 **{restaurant['Name']}** - Rating: {restaurant['Rating']}")
        counter += 1

    # Create a map
    st.subheader('🗺️ Map of Recommended Restaurants')
    m = folium.Map(location=[21.3069, -157.8583], zoom_start=10)

    # Add markers for recommended restaurants
    marker_cluster = MarkerCluster().add_to(m)
    for index, restaurant in recommended_restaurants.iterrows():
        folium.Marker(location=[restaurant['Latitude'], restaurant['Longitude']],
                      popup=f"{restaurant['Name']} - Rating: {restaurant['Rating']}").add_to(marker_cluster)

    # Display the map
    folium_static(m)
