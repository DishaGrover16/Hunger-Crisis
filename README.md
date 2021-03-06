# Hunger-Crisis
Food wastage is a massive problem. About **40%** of the food produced is wasted every year. One of the most common occurrences leading to food wastage is due to overflowing plates and food that ultimately goes into trash cans, be it buffet spreads or individual orders.

## Proposed Solution
A regression modal predicting how much a particular person should consume according to his daily food consuming habits and data features like age, height, weight etc in order to determine the quantity of food required by the person so that food is not wasted at eateries and cafe's.

## Data-set Description
The dataset contains information about daily food quantity required by a person and physical parameters of that person.
Data was collected via Google forms.
The dataset contains 482 rows and has following 14 Data features -

- Timestamp (Catagorical)
- Name(Catagorical)
- Gender(Numeric)
- Age(in years)(Numeric)
- Height(in cm) (Numeric)
- Weight(in kgs) (Numeric)
- Health Issues(if any)(Catagorical)
- How many servings of rice do you eat at a restaurant (Numeric)
- How many bowls of vegetables you eat(Numeric)
- How many slices of pizza would you prefer in restaurants
- How many burgers would you prefer(Numeric)
- How many beverages would you consume in a eatery?(Numeric)
- How many pieces of meat you are likely to consume?(Numeric)
- How much quantity of sea food would you prefer in hotels?(Numeric)

### Visualising the dataframes
- Raw Data
<img src= "assets/raw_data.PNG">

- Pre-Processed Data
<img src= "assets/pre-processed_data.PNG">

## Installation 
- Cloning the Repository: 

        git clone https://github.com/DishaGrover16/Hunger-Crisis
        
- Entering the directory: 

        cd Hunger-Crisis
        
- Setting up the Python Environment with dependencies:

        pip install -r requirements.txt

- Running the web app:

        streamlit run main.py
        
## Demonstration
![](assets/demo.gif)

Check out the notebook <a href="https://nbviewer.jupyter.org/github/DishaGrover16/Hunger-Crisis/blob/main/Notebook/Hunger_crisis_.ipynb">here</a>.

<hr>
This project has been developed by <a href="https://github.com/tissyamalik">Tissya Malik </a>and <a href="https://github.com/DishaGrover16">Disha Grover</a>.

