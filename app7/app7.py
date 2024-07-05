import streamlit as st
import plotly.express as px
from backend_app7 import get_data

# Add the slider and inout boxes
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, 
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
    
if place:
    # Get the data
    data = get_data(place, days)

    if option == "Temperature":
        temperatures = [dicti["main"]["temp"] / 10 for dicti in data]
        dates = [dicti["dt_txt"] for dicti in data]
        # Create a temperature plot
        figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperatures (C)"})
        st.plotly_chart(figure)
        
    if option == "Sky":
        images = {"Clear": "app7/images/clear.png", "Clouds": "app7/images/cloud.png", 
                  "Rain": "app7/images/rain.png", "Snow": "app7/images/snow.png"}
        sky_conditions = [dicti["weather"][0]["main"] for dicti in data]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=115)
        
