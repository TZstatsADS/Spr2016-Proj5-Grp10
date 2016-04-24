import pandas as pd


libraries = ["Architectural and Fine Arts Library 1", "Architectural and Fine Arts Library 2", "Architectural and Fine Arts Library 3", "Butler Library 2", "Butler Library 3", "Butler Library 4", "Butler Library 5", "Butler Library 6","Butler Library stk", "Starr East Asian Library", "Lehman Library 2", "Lehman Library 3", "Science and Engineering Library","Uris"]
dining = ["jjs","john jay","lerner3","lerner4"]

alldining = pd.read_csv('../output/dining/' + dining[0].replace(' ', '_') + '.csv',index_col = 't')
alldining["location"] = dining[0].replace(' ', '_')
for hall in dining[1:]:
	newdf = pd.read_csv('../output/dining/' + hall.replace(' ','_') + '.csv',index_col = 't')
	newdf["location"] = hall.replace(' ','_')
	alldining = pd.concat([alldining,newdf])
alldining.index = pd.to_datetime(alldining.index)
alldining.to_csv('../output/alldining.csv')


alllibrary = pd.read_csv('../output/libraries/' + libraries[0].replace(' ', '_') + '.csv',index_col = 't')
alllibrary["location"] = libraries[0].replace(' ', '_')
for hall in libraries[1:]:
	newdf = pd.read_csv('../output/libraries/' + hall.replace(' ','_') + '.csv',index_col = 't')
	newdf["location"] = hall.replace(' ','_')
	alllibrary = pd.concat([alllibrary,newdf])
alllibrary.index = pd.to_datetime(alllibrary.index)
alllibrary.to_csv('../output/alllibrary.csv')



