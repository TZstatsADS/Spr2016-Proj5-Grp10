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

buildings = ["Architectural and Fine Arts Library 1", "Architectural and Fine Arts Library 2", "Architectural and Fine Arts Library 3", "Butler Library 2", "Butler Library 3", "Butler Library 4", "Butler Library 5", "Butler Library 6","Butler Library stk", "Starr East Asian Library", "Lehman Library 2", "Lehman Library 3", "Science and Engineering Library","Uris"]
for build in buildings:
	split_sem(build.replace(' ','_'))


# split_sem('john_jay')
# split_sem('jjs')
# split_sem('lerner3')
# split_sem('lerner4')
