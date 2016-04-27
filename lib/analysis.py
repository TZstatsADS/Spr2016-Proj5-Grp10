import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import statsmodels.api as sm
import scrape_density_api as scraper
from sklearn.svm import SVR
import easygui as eGUI



def dayofweek_int_to_str(dayofweek):
    day_num_to_str = { 0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thur', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
    return day_num_to_str[dayofweek]


def df_to_weekday_dic(df):
    weekday_col = []
    weekday_dic = {}
    for dayofweek_int in df.index.dayofweek:
        weekday_col.append(dayofweek_int_to_str(dayofweek_int))
    df['weekday'] = pd.Series(weekday_col, index=df.index)
    df = df.sort_index()
    grouped_day = df.groupby('weekday')
    for weekday, weekday_df in grouped_day:
        weekday_df = weekday_df.drop('weekday', 1)
        weekday_dic[weekday] = weekday_df
    return weekday_dic


def count_series_by_weekday_dic(placename, semester, df = None):
    if df is None:
        df = pd.read_csv('/home/max/Documents/finalproject-p5-team10-master/output/dining/' + placename + '_' + semester + '.csv', index_col='t')
    df.index = pd.to_datetime(df.index)
    weekday_dic = df_to_weekday_dic(df)
    weekday_series_dic = {}
    for weekday, weekday_df in weekday_dic.items():
        date_series_dic = {}
        grouped_date = weekday_df.groupby(weekday_df.index.date)
        for date, date_df in grouped_date:
            date_series = pd.Series(date_df['count'])
            date_series.index = date_series.index.time
            date_series_dic[date] = date_series
        date_series_df = pd.DataFrame(date_series_dic)
        date_series_df.index = date_series_df.index.rename('t')
        weekday_series_dic[weekday] = date_series_df
    return weekday_series_dic


def trim_df_by_daily_count(df, count_threshold):
    sum_count_series = df.sum().sort_values()
    to_drop = []
    for date in sum_count_series.index:
        sum_count = sum_count_series.loc[date]
        if sum_count < count_threshold:
            to_drop.append(date)
    new_df = df.drop(to_drop, 1)
    return new_df


def extract_open_hours(placename, weekday_series_dic):
    '''
    cut only 10:00 - 22:00 for open hours
    JJs:
        Sun - Thu : 12:00 - 01:00
        Fri - Sat : 12:00 - 20:00
    John Jay:
        Mon - Thu :
            11:00 - 15:00 &
            17:00 - [20:00]<->[fall_2015 -> 21:00]
        Sun :
            10:00 - 15:00 &
            17:00 - [20:00]<->[fall_2015 -> 21:00]
    '''
    sliced_dic = {}
    if placename == 'jjs':
        for weekday, date_series_df in weekday_series_dic.items():
            mask = (date_series_df.index >= datetime.time(11,0)) & (date_series_df.index <= datetime.time(23,0))
            sliced_df = date_series_df.loc[mask]
            sliced_dic[weekday] = trim_df_by_daily_count(sliced_df, 800)
    elif placename == 'john_jay':
        for weekday, date_series_df in weekday_series_dic.items():
            if (weekday == 'Fri') or (weekday == 'Sat'):
                continue ## IF col count < THRESH drop it
            mask = (date_series_df.index >= datetime.time(9,0)) & (date_series_df.index <= datetime.time(21,0))
            sliced_df = date_series_df.loc[mask]
            sliced_dic[weekday] = trim_df_by_daily_count(sliced_df, 2000)
    return sliced_dic

def hodrick_prescott_filter(date_series):
    filtered_series = sm.tsa.filters.hpfilter(date_series, lamb=.1)[1]
    return filtered_series

def hp_filter_weekday_dic(weekday_dic):
    filtered_dic = {}
    for weekday, date_series_df in weekday_dic.items():
        weekday_dic = {}
        for date in date_series_df.columns:
            series = date_series_df[date]
            series = hodrick_prescott_filter(series)
            weekday_dic[date] = series
        weekday_df = pd.DataFrame(weekday_dic)
        filtered_dic[weekday] = weekday_df.dropna(axis=1, thresh = 15)
    return filtered_dic

def write_dhall_filtered(placename, semester, weekday_series_dic=None):
    if weekday_series_dic is None:
        weekday_series_dic = count_series_by_weekday_dic(placename, semester)
        weekday_series_dic = extract_open_hours(placename, weekday_series_dic)
    filtered_series_dic = hp_filter_weekday_dic(weekday_series_dic)
    df = pd.concat(filtered_series_dic.values(), axis = 1)
    df = df.reindex_axis(sorted(df.columns), axis=1)
    try:
        pd.read_csv('/home/max/Documents/finalproject-p5-team10-master/output/dining/filtered_' + placename + '_' + semester + '.csv')
        print 'file already found, not writing filtered for ' + placename + ' ' + semester
    except:
        df.to_csv('/home/max/Documents/finalproject-p5-team10-master/output/dining/filtered_' + placename + '_' + semester + '.csv')
        print 'no preexisting file found, wrote filtered for ' + placename + ' ' + semester
    return df

def read_filtered_csv(placename, semester):
    try:
        filtered = pd.read_csv('/home/max/Documents/finalproject-p5-team10-master/output/dining/filtered_' + placename + '_' + semester + '.csv', index_col = 't')
        print 'file already found, not writing filtered for ' + placename + ' ' + semester
    except:
        semester_data = pd.read_csv('/home/max/Documents/finalproject-p5-team10-master/output/dining/' + placename + '_' + semester + '.csv', index_col = 't')
        semester_data_dic = count_series_by_weekday_dic(placename, semester, df=semester_data)
        semester_data_dic = extract_open_hours(placename, semester_data_dic)
        filtered = write_dhall_filtered(placename, semester, weekday_series_dic=semester_data_dic)
        print 'no preexisting file found, wrote filtered for ' + placename + ' ' + semester
    filtered.columns = pd.to_datetime(filtered.columns)
    filtered.columns = [x.date() for x in filtered.columns]
    grouped_filtered = filtered.groupby(lambda x: x.weekday(), axis=1)
    filtered_weekday_dic = {}
    for weekday, weekday_filtered_df in grouped_filtered:
        weekday_filtered_df.index = pd.to_datetime(weekday_filtered_df.index)
        weekday_filtered_df.index = [x.time() for x in weekday_filtered_df.index]
        filtered_weekday_dic[dayofweek_int_to_str(weekday)] = weekday_filtered_df
    return filtered_weekday_dic

def load_all_current(placename, semester, points_to_predict = 1):
    weekday = dayofweek_int_to_str(datetime.datetime.now().weekday())
    print 'starting scraping'
    current_data = scraper.get_current_data(placename)
    print 'done scraping'
    prior_filtered = read_filtered_csv(placename, semester)
    weekday_series_df = prior_filtered[weekday]
    current_data.index = [x.time() for x in current_data.index]
    current_data.columns = [datetime.datetime.now().date()]
    last_measure = current_data.index[-1]
    first = weekday_series_df.index[0]
    trimmed_prior = weekday_series_df.loc[first:(datetime.datetime.combine(datetime.datetime.today(),last_measure)+datetime.timedelta(minutes=15*points_to_predict)).time()]
    trimmed_current = current_data.loc[first:last_measure]
    return trimmed_current, trimmed_prior, weekday_series_df

c, f, w = load_all_current('john_jay', 'spr_2016')

def forecast_master(c,f,w, points_to_predict=19):
    to_predict = np.array(c).T
    new_to_predict = list(to_predict[0])
    for i in range(0, points_to_predict - 1):
        filtered_X = []
        next_X = []
        for old_date in w.columns:
            filtered_X.append(w[old_date].iloc[:len(to_predict[0])])
            next_X.append(w[old_date].iloc[len(to_predict[0])])
        clf = SVR(kernel = 'linear', C=1e3)
        clf.fit(filtered_X, next_X)
        new_to_predict.append(clf.predict(to_predict)[0])
        next_X.append(w[old_date][-1])
        print new_to_predict
        to_predict = np.array([new_to_predict])
    return pd.Series(to_predict[-1], index=w.index[:len(to_predict[-1])])

def predict():
    msg ="Which dining hall do you want to explore?"
    title = "Where 2 Eat"
    dhalls = ["john_jay", "jjs"]
    dhall = eGUI.choicebox(msg, title, dhalls)
    msg = "How many half-hours do you want to glance into the future?"
    integer = eGUI.integerbox(msg, title, default = '2')
    points_to_predict = int(integer)*2
    c, f, w = load_all_current(dhall, 'spr_2016')
    predicted = forecast_master(c, f, w, points_to_predict)
    f.iloc[:len(predicted)].plot()
    plt.plot(predicted.index, predicted.values, color='black', linewidth=1., linestyle='dashed')
    plt.plot(c.index, c.values, color='blUe', linewidth=2.)
    plt.show()
    return predicted
p = predict()
plt.plot(p.index, p.values, color='black', linewidth=1., linestyle='dashed')
plt.plot(c.index, c.values, color='blue', linewidth=2.)
plt.show()
