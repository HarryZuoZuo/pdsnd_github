import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ["all", "january", "february", "march", "april", "may", "june"]

DAY_DATA = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

CITIES_DATA = ['chicago', 'new york', 'washington']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Can be all or specific
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
       city = input('Which city to look at? Chicago, New York or Washington?').lower()
       if city.lower() in CITIES_DATA:
           break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich month? all, january, february, ... , june?\n')
        month = month.lower()
        try:
            MONTH_DATA.index(month)
        except:
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhich day? all, monday, tuesday, ... sunday?\n')
        day = day.lower()
        try:
            DAY_DATA.index(day)
        except:
            continue
        else:
            break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['start_time'] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df["start_time"].dt.month
    df['day_of_week'] = df["start_time"].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df["month"] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df["month"].mode()[0]
    print("The most frequent month of travel is {}.".format(MONTH_DATA[common_month].title()))

    # TO DO: display the most common day of week

    common_day_of_week = df["day_of_week"].mode()[0]
    print("The most frequent day of week of travel is: {}.".format(common_day_of_week))

    # TO DO: display the most common start hour

    common_start_hour = df["start_time"].mode()[0]
    print("The most frequent start hour of travel is: {}.".format(str(common_start_hour)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print("The most commonly used start station is: {}.".format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print("The most commonly used end station is: {}.".format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    common_combination = (df["Start Station"] + "-" + df["End Station"]).mode()[0]
    print("The most frequent combination of start station and end station trip is : {}.".format( str(common_combination.split("-"))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("The total travel time is: {}.".format(str(total_travel_time)))

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("The mean travel time is: {}.".format(str(mean_travel_time)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df["User Type"].value_counts()
    print("The counts of user types is: {}.".format(str(count_user_types)))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
    # TO DO: Display counts of gender
        count_gender = df["Gender"].value_counts()
        print("The counts of gender is: {}.".format(str(count_gender)))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df["Birth Year"].min()
        print("The Earliest birth is: {}.".format(earliest_birth))
        most_recent_birth = df["Birth Year"].max()
        print("The most recent birth is: {}.".format(most_recent_birth))
        most_common_birth = df["Birth Year"].mode()[0]
        print("The most common birth year is: {}.".format(most_common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    start_counter = 0
    end_counter = 5
    data_size = len(df.index)

    while start_counter < data_size:
        raw_data = input("\nWould you like to see 5 lines of data?\n")
        if raw_data.lower() == "yes":
            print("\nDisplaying 5 rows of data.\n")

            if end_counter > data_size:
                end_counter = data_size
            print(df.iloc[start_counter:end_counter])
            start_counter += 5
            end_counter += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
