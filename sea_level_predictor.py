import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x=data["Year"], y=data["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    slope, intercept, r, p, std_err =linregress(data["Year"], data["CSIRO Adjusted Sea Level"])

    years_range = list(range(int(data["Year"].min()), 2051))
    first_prediction = [slope * year + intercept for year in years_range]

    ax.plot(years_range, first_prediction)

    # Create second line of best fit
    recent_data = data[data["Year"]>= 2000]

    slope2, intercept2, r, p, std_err = linregress(
        recent_data["Year"], recent_data["CSIRO Adjusted Sea Level"]
    )

    years_recent= list(range(2000, 2051))
    second_prediction = [slope2*year+ intercept2 for year in years_recent]

    ax.plot(years_recent, second_prediction)

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

