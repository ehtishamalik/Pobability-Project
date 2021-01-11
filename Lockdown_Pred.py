import pandas
import sys
#Read from csv to a pandas dataframe
def read_data(filename):
    Data = pandas.read_csv(filename, sep=",")
    return Data

def main(filename):
    tmpdf=read_data(filename)
    City_List=tmpdf.values.tolist() #dataframe to list
    mean_index=0 #Initialize Mean_Index
    max_index=0.001 #Initialize max_index
    for index,_ in enumerate(City_List):
        city_index= (City_List[index][1] * City_List[index][2] * City_List[index][3] * City_List[index][7]  )
        city_index= city_index/ (City_List[index][4] * City_List[index][6]  )
        City_List[index].append(city_index)
        if city_index > max_index: #Check and update max index
            max_index=city_index

    #Normalize city_index/score
    for index,_ in enumerate(City_List):
        City_List[index][-1]=City_List[index][-1]/ max_index
        mean_index=mean_index+ City_List[index][-1]
    mean_index=mean_index/len(City_List)
    
    lockdown=[] #List to store name of cities recommended to lockdown
    for index,_ in enumerate(City_List):
        if City_List[index][8] >mean_index:
            lockdown.append(City_List[index][0]) #Add to lockdown list
    print('The recommended cities for complete lockdown are City ' + ', '.join('%s' % s for s in lockdown))

if __name__ == "__main__":
    filename=sys.argv[1]
    main(filename)
    