import requests as req
import json
import pandas as pd

def process_page_data(url):
    '''
    -gets the next page in the Density API and extracts time and number of people
    connected to wifi for that page.
    -returns tuple of (page data as dataframe, next page url)
    '''
    page = req.get(url)
    content = json.loads(page.content) # load API's json content

    page_df = pd.DataFrame(content['data']).loc[:,['client_count','dump_time']]
    page_df.dump_time = pd.to_datetime(page_df.dump_time)
    page_df = page_df.set_index('dump_time') # get num on wifi and time of measure
    page_df.index = page_df.index.rename('t')
    page_df.columns = ['count']
    next_page = content['next_page'] # get url for next page
    return (page_df, next_page)

def scrape_location_data(location_name, location_id, yr_1, m_1, d_1, h_1, min_1, yr_f, m_f, d_f, h_f, min_f):
    '''
    -for a building's location id (provided by ADI Density) and
    starting year, month, day, hour (HH), minute (MM) (24 hour time) and
    ending year, month, day, hour (HH), minute (MM) (24 hour time)
    returns a dataframe with the index datetime of measure and value count people on wifi
    '''

    t_1 = str(yr_1) + '-' + str(m_1) + '-' + str(d_1) + 'T' + str(h_1) + ':' + str(min_1)
    t_f = str(yr_f) + '-' + str(m_f) + '-' + str(d_f) + 'T' + str(h_f) + ':' + str(min_f)
    url = "http://density.adicu.com/window/" + t_1 + "/" + t_f + "/group/" + location_id + "?auth_token=HMOPZA257UIFUJKIDTAKAV0F1D6CG23A"

    page = req.get(url) # get first page content
    content = json.loads(page.content)

    next_page = content['next_page'] # get url for next page
    page_data = pd.DataFrame(content['data']).loc[:,['client_count','dump_time']] # get data for this page
    page_data.dump_time = pd.to_datetime(page_data.dump_time) # convert time on page to datetime
    location_df = page_data.set_index('dump_time') # set as index
    location_df.index = location_df.index.rename('t') # rename index
    location_df.columns = ['count'] # rename column
    page_count = 1
    while next_page is not None: # do it until there is no url for a next page
        print 'scraping page ' + str(page_count) + ' for ' + location_name
        page_count += 1
        (next_df, next_page) = process_page_data(next_page)
        location_df = location_df.append(next_df) # add each page's data to the total
    return location_df

def get_all_data(output_path, yr_1, m_1, d_1, h_1, min_1, yr_f, m_f, d_f, h_f, min_f):
    '''
    -gets all of the data across all locations in the dictionary below for input time.
    -returns in form: {'location name' : location_df, ... , 'location_name': location_df}
    -saves csv to path_out + 'location_name.csv'

    -the building ids can be found here:   http://density.adicu.com/docs/building_info
        -NOTE: FARTHEST BACK FULL DAY OF DATA IS JUNE 28 2014
            -Data is accessible every 15 minutes in real time

    this is the highest level run function for the scraper
    '''

    building_to_location_id_dic = {'john jay': '125',
                                    'jjs': '155'
#                                    'lerner3': '152', 'lerner4': '153'
                    }
    location_data_dic = {}
    for location_name, location_id in building_to_location_id_dic.iteritems():
        print "working on " + location_name
        location_data = scrape_location_data(location_name, location_id, yr_1, m_1, d_1, h_1, min_1, yr_f, m_f, d_f, h_f, min_f)
        location_data_dic[location_name] = location_data
        location_data.to_csv(output_path + location_name.replace(' ', '_') + '.csv')
    return location_data_dic

output_path = '/home/max/Documents/finalproject-p5-team10-master/output/'
all_locations_data_dic = get_all_data(output_path, 2014, 8, 10, 12, 00, 2016, 4, 23, 01, 00)
