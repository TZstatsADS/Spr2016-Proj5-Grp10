import pandas as pd


# df = pd.read_csv('../output/john_jay.csv', index_col='t')

# df.index = pd.to_datetime(df.index)

# john_jay_fall_2015 = df['2015-12-23':'2015-9-8']

# john_jay_fall_2015.to_csv("../output/john_jay_fall_2015.csv")

#     S: 1/20/2015 - 5/15/2015

def split_sem(placename):
	df = pd.read_csv('../output/' + placename + '.csv',index_col = 't')
	df.index = pd.to_datetime(df.index)
	fall_2014 = df['2014-12-19':'2014-9-2']
	spr_2015 =  df['2015-5-15':'2015-1-20']
	fall_2015 = df['2015-12-23':'2015-9-8']
	fall_2014.to_csv('../output/' + placename + '_fall_2014.csv')
	spr_2015.to_csv('../output/' + placename + '_spr_2015.csv')
	fall_2015.to_csv('../output/' + placename + '_fall_2015.csv')

split_sem('john_jay')
split_sem('jjs')
split_sem('lerner3')
split_sem('lerner4')
