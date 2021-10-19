import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asking user to insert the name of city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    cities= ['chicago', 'new york city','washington']
    months=['january','february','march', 'april', 'may', 'june','all']
    days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
    while True:
            try:
                city=cities.index(input('which city would you like to see its data chicago, new york city or washington? ').lower())
                break
            except:
                print("Typing error, please try again and type city name :chicago, new york city or washington!")
    while True:
        try:
            filtration=input("would you like to filter data by month and day or not at all? type yes or no! ").lower()
            if filtration=="no":
                day=7
                month=6
                break

            elif filtration =='yes':
                while True:
                        try:
                            month=months.index(input('please type name of the month or select all: ').lower())
                            break
                        except ValueError:
                            print("Typing error, please try again and type the name of month. ")
                while True:
                        try:
                            day=days.index(input('please insert name of the day or select all: ').lower())
                            break
                        except ValueError:
                            print("Typing error, please try again and type the name of day. ")
                break
            else:
                chosen=['yes','no']
                filtration=chosen.index(filtration)
        except:
            print("Please type yes or no.")

    city=cities[city]
    month=months[month]
    day=days[day]

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Input:
        (str) city - name of the city to analyze.
        (str) month - name of the month to filter by, or "all" to apply no month filter.
        (str) day - name of the day of week to filter by, or "all" to apply no day filter.

    Return:
        df - DataFrame containing city data filtered by month and day.
    """
    df=pd.read_csv(CITY_DATA[city])
    df["Start Time"]=pd.to_datetime(df["Start Time"])
    df["Month"]=df["Start Time"].dt.month
    df['Day'] = df['Start Time'].dt.day_name()

    month=month.title()
    day=day.title()
    if month != "All":
        months = ['January', 'February', 'March', 'April', 'May', 'June',"All"]
        month = months.index(month) + 1
        df = df[df['Month'] == month]
        month=months[month-1]
    if day != 'All':
        df=df[df["Day"]==day]
    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    Input:
        df - DataFrame containing city data filtered by month and day.
    Output:
        the most common month, the most common day of week, and the most common start hour.
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df["Start Time"]=pd.to_datetime(df["Start Time"])
    df["Month"]=df["Start Time"].dt.month
    df["Day"]=df["Start Time"].dt.day_name()
    df["Hour"]=df["Start Time"].dt.hour
    common_month=df["Month"].mode()[0]
    common_day=df["Day"].mode()[0]
    common_hour=df["Hour"].mode()[0]

    print('The common month is ',common_month)
    print('The common day is ',common_day)
    print('The common hour is ',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.

    Input:
        df - DataFrame containing city data filtered by month and day.

    Output: the most commonly used start station, the most commonly used end station,
            the most frequent combination of start station and end station trip.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    common_start_station=df["Start Station"].mode()[0]
    print("The common Start Station is ",common_start_station )
    common_end_station=df["End Station"].mode()[0]
    print("The common End Station is ",common_end_station )
    df["Freq_Station"]=df["Start Station"] + " : " +df["End Station"]
    common_freq_station=df["Freq_Station"].mode()[0]
    print("Common Frequant Station is ",common_freq_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.

    Input:
        df - DataFrame containing city data filtered by month and day.

    Output: total travel time, mean travel time.

    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_trip_duration=df["Trip Duration"].sum()
    print("The total travel time is: ",total_trip_duration)
    trip_duration_avrege=df["Trip Duration"].mean()
    print ('The mean travel time is: ',trip_duration_avrege)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """
    Displays statistics on bikeshare users.

    Input:
        df - DataFrame containing city data filtered by month and day
        (str) city.

    Output: counts of user types, counts of gender, the earliest year of birth,
            the most recent year of birth, and the most common year of birth.

    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    User_counts=df["User Type"].value_counts()
    print("The counts of user types is: ",User_counts)
    if city=="chicago" or city=="new york city":
        Gender_counts=df["Gender"].value_counts()
        print("The counts of gender is: ",Gender_counts)
        min_year= df['Birth Year'].min()
        print("The earliest year of birth is: ",int(min_year))
        recent_year= df['Birth Year'].max()
        print("The most recent year of birth is: ",int(recent_year))
        common_year= df["Birth Year"].mode()[0]
        print("The most common year of birth is: ",int(common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)


        start_num = 0
        show_data = input('\nWould you like to display 5 rows of individual trip data? Enter yes or no: ')
        if show_data.lower() == "yes":
            print(df.iloc[start_num:start_num+ 5])
            start_num+=5
            while True:
                    try:
                        display = input("would you like to continue?:  ").lower()
                        if display=="yes":
                            print(df.iloc[start_num:start_num+ 5])
                            start_num+=5
                        elif display=="no":
                            break
                        else:
                            chose=['yes','no']
                            filtr=chose.index(filtr)
                    except:
                        print("Please type yes or no: ")

        restart = input('\nWould you like to restart? Enter yes or no: ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
