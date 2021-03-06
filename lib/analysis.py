import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def dayofweek_int_to_str(dayofweek):
	day_num_to_str = { 0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thur', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
	return day_num_to_str[dayofweek]
    
    
def week_total(typeofplace, placename, semester):
	df = pd.read_csv('../output/' + typeofplace + '/' + placename + '_' + semester + '.csv', index_col='t')
	df.index = pd.to_datetime(df.index)
	days = []
	totals = []
	for key, value in df.groupby(df.index.dayofweek).sum().to_dict()['count'].items():
		days.append(dayofweek_int_to_str(key))
		totals.append(value)
	ind = np.arange(len(days))
	width = 0.35 
	fig, ax = plt.subplots()
	rects1 = ax.bar(ind, totals, width, color='r')
	ax.set_ylabel(semester + ' Aggregate Occupancy')
	ax.set_title('Total Occupancy of ' + placename + ' during ' + semester)
	ax.set_xticks(ind + width)
	ax.set_xticklabels(days)
	# plt.show()
	fig.savefig('week_total.png')
	plt.close(fig)		

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
	# plt.show()
	fig.savefig('hour_total.png')
	plt.close(fig)		

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
		days.append(key)
		totals.append(value)
	days = [(i-min(days)).total_seconds()/60 for i in days]
	plt.scatter(days,totals)
	plt.plot(days,totals)
	# plt.show()
	plt.savefig('total_usage.png')
	plt.close()		

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
	# plt.show()
	plt.savefig('average_total.png')
	plt.close()		

average_total()


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
		plt.scatter(hours,totals)
		plt.plot(hours,totals, label= butler)
	plt.legend(loc='upper left')
	# plt.show()
	plt.savefig('average_butler.png')
	plt.close()		
average_butler()

def average_dining():
	alldining = pd.read_csv('../output/alldining.csv', index_col='t')
	alldining.index = pd.to_datetime(alldining.index)
	halls = dining = ["jjs","john jay","lerner3","lerner4"]
	for hall in halls:
		hours = []
		totals = []
		thishall = alldining[alldining['location'] == hall.replace(' ','_')]
		timecount = thishall.groupby(thishall.index.hour).mean().to_dict()['count'].items()
		timecount = sorted(timecount,key=lambda x: x[0])
		for (key, value) in  timecount:
			hours.append(key)
			totals.append(value)
		plt.scatter(hours,totals)
		plt.plot(hours,totals, label= hall)
	plt.legend(loc='upper left')
	# plt.show()
	plt.savefig('average_dining.png')
	plt.close()		
average_dining()




