import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def week_total(typeofplace, placename, semester):
	df = pd.read_csv('../output/' + typeofplace + '/' + placename + '_' + semester + '.csv', index_col='t')
	df.index = pd.to_datetime(df.index)
	days = []
	totals = []
	for key, value in df.groupby(df.index.dayofweek).sum().to_dict()['count'].items():
		days.append(key)
		totals.append(value)
	ind = np.arange(len(days))
	width = 0.35 
	fig, ax = plt.subplots()
	rects1 = ax.bar(ind, totals, width, color='r')
	ax.set_ylabel('Totals')
	ax.set_title('Total students per day of the week')
	ax.set_xticks(ind + width)
	ax.set_xticklabels(days)
	plt.show()

week_total('dining','john_jay','fall_2015')




def hour_total(typeofplace, placename, semester):
	df = pd.read_csv('../output/' + typeofplace + '/' + placename + '_' + semester + '.csv', index_col='t')
	df.index = pd.to_datetime(df.index)
	hours = []
	totals = []
	for key, value in df.groupby(df.index.hour).sum().to_dict()['count'].items():
		hours.append(key)
		totals.append(value)
	ind = np.arange(len(hours))
	width = 0.35 
	fig, ax = plt.subplots()
	rects1 = ax.bar(ind, totals, width, color='r')
	ax.set_ylabel('Totals')
	ax.set_title('Total students per hour of the day')
	ax.set_xticks(ind + width)
	ax.set_xticklabels(hours)
	plt.show()

hour_total('dining','john_jay','fall_2015')




def total_usage(typeofplace, placename,begin_time,end_time):
	df = pd.read_csv('../output/' + typeofplace + '/' + placename + '.csv', index_col='t')
	df.index = pd.to_datetime(df.index)
	days = []
	totals = []
	capacity = df.max()
	# newdf = df[end_time:begin_time]
	timecount = (df[end_time:begin_time]/capacity).to_dict()['count'].items()
	timecount = sorted(timecount,key=lambda x: x[0])
	for (key, value) in  timecount:
		days.append(key.time().strftime("%H:%M"))
		totals.append(value)
	ind = np.arange(len(days))
	width = 0.35 
	fig, ax = plt.subplots()
	rects1 = ax.bar(ind, totals, width, color='r')
	ax.set_ylabel('Percent Full')
	ax.set_title('How Full is ' + placename)
	ax.set_xticks(ind + width)
	ax.set_xticklabels(days)
	plt.show()

total_usage('dining','john_jay','2016-4-20 11:00:00','2016-4-20 14:00:00')



