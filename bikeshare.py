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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("choose the city name (chicago , new york city , washington) :").lower()
    while city not in CITY_DATA.keys():
        print("please enter a valiid city ")
        city = input("choose the city name (chicago , new york city , washington) :").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months= ["january","february","march","april","may","june","all"]
    while True :
        month = input ("choose month : (all,january,february,march,april,may,june)").lower()
        if month in months :
            break
        else :
            print ("invalid input")
            

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["sunday","monday","tuesday","wednsday","thursday","friday","satarday","all"]
    while True:
        day = input("choose a day :(sunday,monday,tuesday,wednsday,thursday,friday,satarday,all) ").lower()
        if day in days :
            break
        else:
            print ("invalid input")

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']= df['Start Time'].dt.month
    df['day_of_week']= df['Start Time'].dt.weekday_name
    df['start hour']= df['Start Time'].dt.hour
    
    if month != "all":
        months= ["january","february","march","april","may","june"]
        month = months.index(month) +1
        df = df[df['month']==month]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('the most common month : {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('the most common day :{}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('the most common start hour :{}'.format(df['start hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("the most common start station :{}" .format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("the most common end station :{}".format(df["End Station"].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df["route"]= df["Start Station"]+","+ df["End Station"]
    print ("most route :{}".format(df["route"].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time :", (df["Trip Duration"].sum()).round())
    

    # TO DO: display mean travel time
    print("mean travel time :", (df['Trip Duration'].mean()).round())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df["User Type"].value_counts().to_frame())

    # TO DO: Display counts of gender
    if city != 'washington':
        print(df["Gender"].value_counts().to_frame())

    # TO DO: Display earliest, most recent, and most common year of birth
        print("most common year of birth ",int(df["Birth Year"].mode()[0]))
        print("most recent year of birth ",int(df["Birth Year"].max()))
        print("most earlist year of birth ",int(df["Birth Year"].min()))
    else :
        print("there is no data")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
def dispaly_data(df):
    """Displays data used."""
    print ('\nRaw data is available to check ...\n')
    index=0
    user_input=input ("Do you like to display 5 rows of row data ? enter yes or no ").lower()
    if user_input not in ['yes','no']:
        print ('please choose yes or no')
        user_input=input ("Do you like to display 5 rows of row data ? enter yes or no ").lower()
    elif user_input != 'yes':
        print('Thank you')
    else :
        while index+5 < df.shape[0]:
            print(df.iloc[index:index+5])
            index +=5
            user_input=input("Do you like to display 5 more rows of row data ? enter yes or no ").lower()
            if user_input != 'yes':
                print('Thank you')
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        dispaly_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
