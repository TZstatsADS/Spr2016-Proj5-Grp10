import pandas as pd

def csv_to_df(output_path, location_name):
    '''
    -given path to your output folder and the name of the location, returns a df of that csv
    '''
    df = pd.read_csv(output_path + location_name.replace(' ', '_') + '.csv', index_col='t')
    return df

output_path = '/home/max/Documents/finalproject-p5-team10-master/output/'

jjs = csv_to_df(output_path, 'jjs')
jjs[:460].plot() # if this doesn't work, type same command in command line, shows past 5 days at jjs
# see output folder for this sample figure
