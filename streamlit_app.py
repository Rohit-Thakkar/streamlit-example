import streamlit as st
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier

# Load the Titanic dataset (replace 'dataset.csv' with the actual filename)
df = pd.read_csv('dataset.csv')

st.title("Titanic Survival Prediction")

# Sidebar for user input
st.sidebar.header("User Input")

# Allow the user to select a passenger by index
passenger_index = st.sidebar.number_input("Select Passenger Index", min_value=0, max_value=len(df) - 1, value=0)

# Display the details of the selected passenger
if 'df' in locals():
    st.sidebar.write("Selected Passenger:")
    st.sidebar.write(df.iloc[passenger_index])

# Create a section for data exploration
st.header("Data Exploration")

# Display a bar chart of passenger class distribution
if 'df' in locals():
    st.subheader("Passenger Class Distribution")
    class_counts = df['Pclass'].value_counts()
    st.bar_chart(class_counts)

# Create a section for prediction
st.header("Survival Prediction")

# Show a form to input features for prediction
if 'df' in locals():
    st.subheader("Enter Passenger Information for Prediction")
    pclass = st.selectbox("Passenger Class", (1, 2, 3))
    sex = st.selectbox("Sex", ('male', 'female'))
    sibsp = st.number_input("SibSp", min_value=0)
    parch = st.number_input("Parch", min_value=0)

    # Preprocess the selected features
    features = [pclass, sex, sibsp, parch]
    features = pd.get_dummies(pd.Series(features)).values.reshape(1, -1)

    # Train a Random Forest model (you can replace this with your trained model)
    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
    # Load your pre-trained model here
    # model = joblib.load('your_model.pkl')
    X = pd.get_dummies(df[['Pclass', 'Sex', 'SibSp', 'Parch']])
    y = df['Survived']
    model.fit(X, y)

    # Make a prediction
    prediction = model.predict(features)[0]

    st.write("Prediction: ", "Survived" if prediction == 1 else "Did Not Survive")



'''from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:



with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))'''
