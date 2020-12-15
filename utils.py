import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier


def convert_to_MPH(strava_df):
    for i in range(len(strava_df["Average Speed"])):
        strava_df.iloc[i, 10] = float(strava_df.iloc[i, 10]) * 2.23694
        strava_df.iloc[i, 9] = float(strava_df.iloc[i, 9]) * 2.23694

        
def bar_chart(x, y, title, size, attribute):
    '''
    Description: Takes in two columns/lists and plots them to a bar graph.
    Also uses the title parameter to label the graph.
    '''
    if size == "big":
        plt.figure(figsize = (20,10))
    else:
        plt.figure()
    plt.xlabel("Date")
    plt.xticks(rotation=45)
    if attribute == "Average Speed":
        plt.bar(x, y, width = .5, color = "#FC4C02", edgecolor = "black") # color is strava red
        plt.ylabel("Speed MPH")
        plt.ylim([8.2, 9.5])
    elif attribute == "Temperature":
        plt.ylabel("Temperature in Fahrenheit")
        plt.bar(x, y, width = .5, color = "#87ceeb", edgecolor = "black")
    elif attribute == "Max Speed":
        plt.bar(x, y, width = .5, color = "#FC4C02", edgecolor = "black") # color is strava red
        plt.ylabel("Speed MPH")
        plt.ylim([10, 15.5])  
    plt.title(title)
    for a, b in enumerate(y):
        plt.text(a - .25, b + .01, str("{:.2f}".format(b)))
    plt.show()  



def plot_box_plot(strava_df):
    plt.figure()
    plt.ylabel("Average Speed in MPH")
    plt.title("Box and Whiskers Plot Showing Data Spread")
    plt.boxplot(strava_df["Average Speed"], notch = True)
    plt.show()
    
def print_songs(Date, strava_df, spotify_df, og_strava_df):
    date_index = -1
    for i in range(len(strava_df)):
        if Date == strava_df.iloc[i,1].split(",")[0]:
            date_index = i
    if date_index == -1:
        print("That's not a valid date, the valid dates are displayed on the x-axis on the graphs above")
        print("All dates must be two atleast two integers, so 09 instead of 9")
    else:
        string_time = og_strava_df.iloc[date_index,1].split(", ")[2]
        start_time_list = string_time.split(":")
        start_time = (int(start_time_list[0]) * 60 * 60) + (int(start_time_list[1]) * 60) + int(start_time_list[2]) - 120
        moving_time = int(strava_df.iloc[date_index, 7])
        end_time = start_time + moving_time + 120
    
        # print(spotify_df)
    
        for i in range(len(spotify_df)):
            # grabbing the date and time to format them to match the strava date and time
            # Like Oct 6 and by seconds instead of by hour:minute
            date_time = spotify_df.iloc[i,0].split(" ")
            date = date_time[0]
            time = date_time[1]
            cleaned_time = int(time.split(":")[0]) * 60 * 60 + int(time.split(":")[1]) * 60

            year_month_day = date.split("-")
            month = year_month_day[1]
            day = year_month_day[2]
            #print(month, day)
            cleaned_date = ""
            if month == "10":
                cleaned_date = "Oct " + day
            elif month == "11":
                cleaned_date = "Nov " + day
            elif month == "12":
                cleaned_date = "Dec " + day
            
            #song_title_ser = pd.Series(dtype=str)
            #song_artist_ser = pd.Series(dtype=str)
            if cleaned_date == Date:
                if cleaned_time >= start_time and cleaned_time <= end_time:              
                    print("Song:", spotify_df.iloc[i,2]) 
                    print("Artist:", spotify_df.iloc[i,1])
                    print()
                
def plot_decision_tree(clf, X):
    plt.figure(figsize=(15,15))
    tree.plot_tree(clf, feature_names=X.columns, class_names = {2: "pop", 1: "rap", 0: "folk"}, filled=True)
    plt.show()                
