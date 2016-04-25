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
	timecount = (df[end_time:begin_time]/capacity).to_dict()['count'].items()
	timecount = sorted(timecount,key=lambda x: x[0])
	for (key, value) in  timecount:
		days.append(key.time())#.strftime("%H:%M"))
		totals.append(value)
	plt.scatter(days,totals)
	plt.plot(days,totals)
	plt.show()

total_usage('dining','john_jay','2016-4-20 11:00:00','2016-4-20 14:00:00')


def average_total():
	alllibrary = pd.read_csv('../output/alllibrary.csv', index_col='t')
	alllibrary.index = pd.to_datetime(alllibrary.index)
	days = []
	totals = []
	# capacity = df.max()
	timecount = alllibrary.groupby(alllibrary.index.hour).mean().to_dict()['count'].items()
	timecount = sorted(timecount,key=lambda x: x[0])
	for (key, value) in  timecount:
		days.append(key)#.strftime("%H:%M"))
		totals.append(value)
	plt.scatter(days,totals)
	plt.plot(days,totals)
	plt.show()

def average_butler():
	alllibrary = pd.read_csv('../output/alllibrary.csv', index_col='t')
	alllibrary.index = pd.to_datetime(alllibrary.index)
	butlers = ["Butler Library 2", "Butler Library 3", "Butler Library 4", "Butler Library 5", "Butler Library 6","Butler Library stk"]
	for butler in butlers:
		hours = []
		totals = []
		thisbutler = alllibrary[alllibrary['location'] == butler.replace(' ','_')]
		timecount = thisbutler.groupby(thisbutler.index.hour).mean().to_dict()['count'].items()
		timecount = sorted(timecount,key=lambda x: x[0])
		for (key, value) in  timecount:
			hours.append(key)
			totals.append(value)
		plt.scatter(days,totals)
		plt.plot(days,totals, label= butler)
	plt.legend(loc='upper left')
	plt.show()


