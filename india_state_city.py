#!/usr/bin/python

import customPRG

dataset = {}
country = 'India'
union_terr = {'Andaman and Nicobar', 'Chandigarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi', 'Lakshadweep', 'Puducherry'}

##Reading and organizing state and city data in a dictionary.
def read_database_csv():
    try:
        with open('india-state-city-database-list.csv', 'r') as csvfile:        ##This csv file has been found online. Data for 'Telangan' has been manually added though.
            for line in csvfile:
                file_state = line.split(",")[0].strip().replace('"', '')
                if file_state == 'State/Union Territory':
                    continue
                if len(line.split(",")) > 1:
                    file_city = line.split(",")[1].strip().replace('"', '')
                    dataset[file_state].append(file_city)
                elif len(line.split(",")) == 1:
                    dataset[file_state] = []
        return True
    except:
        print ("Database file loading error.")
        return False

##The data source csv file includes both states and union territories. Union territories are removed.
def remove_ut():
    for ut in union_terr:
        del dataset[ut]
    
##Get two random city indexes for the city list.
def get_random_city(state):
    limit = len(dataset[state])
    cmsm = customPRG.customMSM()
    sel1 = cmsm.random(limit)
    sel2 = cmsm.random(limit)
    if sel1 == sel2:
        sel2 = cmsm.random(limit-1)
        if sel2 >= sel1:
            sel2 += 1
    return sel1, sel2
    
##Write output to csv file.
def output_to_file(sel1, sel2, state):
    #print (dataset[state][sel1], dataset[state][sel2], state)
    rec_no = 1
    try:
        with open('output.csv', 'r') as outputcsv:
            reader = outputcsv.readlines()
            rec_no = int(reader[-1].split(",")[0]) + 1
        with open('output.csv', 'a') as outputcsv:
            outputcsv.write('{0}, {1}, {2}, {3}\n'.format(rec_no, country, state, dataset[state][sel1]))
            outputcsv.write('{0}, {1}, {2}, {3}\n'.format(rec_no+1, country, state, dataset[state][sel2]))
    except:
        with open('output.csv', 'w') as outputcsv:
            outputcsv.write("Record No, Country, State, City\n")
            outputcsv.write('{0}, {1}, {2}, {3}\n'.format(rec_no, country, state, dataset[state][sel1]))            
            outputcsv.write('{0}, {1}, {2}, {3}\n'.format(rec_no+1, country, state, dataset[state][sel2]))
    
def function(State):
    sel1, sel2 = get_random_city(State)
    output_to_file(sel1, sel2, State)
    

#read_database_csv()
#function('Goa')
    
if read_database_csv():
    remove_ut()
    for st in dataset.keys():
        if len(dataset[st]) == 0:
            print ("Record for state '{0}' not found.".format(st))
            continue
        print ("Finished State -> {0}".format(st))
        function(st)
