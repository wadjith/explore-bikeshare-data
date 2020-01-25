import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    while True:
        print('Would you like to see data for which city (Chicago, New York City, or Washington) ?')
        city = input('').lower()
        if (city in cities):
            break
        else:
            print("City's name should be {}".format(cities))

    # get user input for month (all, january, february, ... , june)
    month_values = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    print()
    while True:
        print('Would you like to filter data by which month (all, january, february, ... , june)?')
        month = input('').lower()
        if(month in month_values):
            break
        else:
            print("Month's value should be {}".format(month_values))

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_values = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    print()
    while True:
        print('Would you like to filter data by which day of week (all, monday, tuesday, ... sunday)?')
        day = input('').lower()
        if(day in day_values):
            break
        else:
            print("Day's value should be {}".format(day_values))

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    cmonth = df['month'].mode()[0]
    print()
    print("What is the most common month of travel ?")
    print(months[cmonth - 1])

    # display the most common day of week
    cday = df['day_of_week'].mode()[0]
    print()
    print("What is the most common day of week of travel ?")
    print(cday)

    # display the most common start hour
    chour = df['hour'].mode()[0]
    print()
    print("What is the most common start hour of travel ?")
    print(chour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    cstart = df['Start Station'].mode()[0]
    print()
    print("What is the most commonly used start station for travel ?")
    print(cstart)

    # display most commonly used end station
    cend = df['End Station'].mode()[0]
    print()
    print("What is the most commonly used end station for travel ?")
    print(cend)

    # display most frequent combination of start station and end station trip
    #2.a Combine Start Station and End Station to create new columns
    df['Path'] = df['Start Station']+ " To " + df['End Station']
    cpath = df['Path'].mode()[0]
    print()
    print("What is the most common trip from start to end ? ")
    print(cpath)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print()
    print("What is the total travel time ?")
    print(total_time)

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print()
    print("What is the mean travel time ?")
    print(mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print()
    print("What is the breakdown of users ?")
    print(user_types)

    # Display counts of gender
    print()
    print('What is the breakdown of gender ?')
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print('There is no Gender information about users in the data of the city')

    # Display earliest, most recent, and most common year of birth
    print()
    print('What is the oldest, youngest, and most popular year of birth respectively ?')
    if 'Birth Year' in df:
        birth_year = (df['Birth Year'].min(), df['Birth Year'].max(), df['Birth Year'].mode()[0])
        print(birth_year)
    else:
        print('Information about year of birth is not collected for the city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def print_next_5lines(df, start = 0):
    """
    Dislay the next five lines of dataframe df

    Args:
        (dataframe) df - the dataframe from which lines will be displayed
        (int) start - the first index of line to displayed

    """

    # The last index of lines to displayed.
    end = start + 5
    # get a subset of the dataframe from line = start to line = end-1
    data = df.iloc[start:end, :].copy()
    # number of rows in the dataset
    nb_row = df.shape[0]

    # removes unnecessary columns in the new dataframe
    data.drop('Path', axis = 1, inplace = True)
    data.drop('month', axis = 1, inplace = True)
    data.drop('day_of_week', axis = 1, inplace = True)
    data.drop('hour', axis = 1, inplace = True)

    # list of columns of the dataframe
    data_columns = data.columns
    # list of lines of values within data.
    data_values = data.values

    # Print the list of dictionnary
    print('SHOWING RAW DATA FROM LINE {} TO {} OVER {} ROWS'.format(start, end-1, nb_row))
    print('-'*60)

    for  i in range(5):
        print()
        # get a line of value as a list
        line_value = data_values[i]
        j = 0
        # loop over data_columns an line_value to fill the dictionnary
        for k in data_columns:
            print('{} = {}'.format(k, line_value[j]))
            j += 1


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print()
        print("THESE ARE STATISTICS ABOUT THE CITY OF {}".format(city.upper()))
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        start = 0
        while True:
            # By default we display 5 lines of raw data
            print()
            print_next_5lines(df, start)
            start += 5
            print()
            view = input('\nWould you like to view more individual trip data? Enter yes or no.\n')
            if view.lower() != 'yes':
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
