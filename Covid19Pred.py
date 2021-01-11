# importing pandas module to read csv file.
import pandas
import sys
#Readig data from csv to a dataframe
def read_data(filename):
    Data = pandas.read_csv("data.csv", sep=",")
    # reading data files using pandas 
    Data
    return Data

#Separating data based on a given label in a given column
def Separate_data(Data,label,column):
    Sep_Data=Data[Data[Data.columns[column]] == label]
    return Sep_Data

def main(filename,symptoms):
    Data=read_data(filename)
    # seperating data infected with Corona
    Data_Inf = Separate_data(Data,"Yes",0)
    # Displaying output of infected people
    Data_Inf
    
    # seperating data not infected with Corona
    Data_NInf = Separate_data(Data,"No",0)
    # Displaying output of infected people
    Data_NInf

   # Declaring dictionaries to store data
    # This dictionary with store the count of symptoms of data with infected people 
    Count_Inf = {}
    # This dictionary with store the count of symptoms of data with non infected people
    Count_NInf = {}

    # Calculating the count of symptoms in data of infected and non infected people
    for key, data in symptoms.items():
        # Gives the count of key from data of infected people
        count = list(Data_Inf[key]).count(data)
        Count_Inf[key] = count
    
        # Gives the count of key from data of non infected people
        count = list(Data_NInf[key]).count(data)
        Count_NInf[key] = count
    
    # Displaying values in dictionary of infected people
    Count_Inf
    # Displaying values in dictionary of non infected people
    Count_NInf

    # The list will store the probabilities of infected people
    AllProbabilitiesWithInfected =  []
    
    # The list will store the probabilities of non infected people
    AllProbabilityWithNonInfected =  []

    # total number of peoples we have in overall data
    Num_Total = len(list(Data['infected with covid']))

    # total number of peoples infected with Covid
    Num_Inf = len(list(Data_Inf['infected with covid']))

    # Probability of people infected with Corona
    Prob_Prior_Inf = Num_Inf/Num_Total
    Prob_Prior_Inf

    # Appending p_c to list
    AllProbabilitiesWithInfected.append(Prob_Prior_Inf)

    # Calculating the probaility of symptoms given that you are infected with Corona
    for key, data in Count_Inf.items():
        AllProbabilitiesWithInfected.append(data/Num_Inf)
    
    # Displaying the probaility given that you are infected with Corona
    AllProbabilitiesWithInfected

    # total number of peoples not infected with Covid
    Num_NInf = len(list(Data_NInf['infected with covid']))

    # Probability of people not infected with Corona
    ProbabilityOfPeopleNotInfected = Num_NInf/Num_Total
    ProbabilityOfPeopleNotInfected

    # Appending p_c to list
    AllProbabilityWithNonInfected.append(ProbabilityOfPeopleNotInfected)

    # Calculating the probaility of symptoms given that you are not infected with Corona
    for key, data in Count_NInf.items():
        AllProbabilityWithNonInfected.append(data/Num_NInf)
    
    # Displaying the probaility given that you are not infected with Corona
    AllProbabilityWithNonInfected

    # Multiplying the probailities given that you are infected with Corona
    Prob_Inf = 1.0
    for i in AllProbabilitiesWithInfected:
        if (i == 0): # if probaility of any symptom is equal to zero
            i = 0.01   # replace it with 0.01
        Prob_Inf = Prob_Inf*i
    Prob_Inf

    # Multiplying the probailities given that you are not infected with Corona
    Prob_NInf = 1.0
    for i in AllProbabilityWithNonInfected:
        if (i == 0): # if probaility of any symptom is equal to zero
            i = 0.01   # replace it with 0.01
        Prob_NInf = Prob_NInf*i
    Prob_NInf

    #Normalize Probabilities
    TotalProbability = Prob_Inf + Prob_NInf
    Normalized_Prob_Inf = Prob_Inf/TotalProbability
    Normalized_Prob_NInf = Prob_NInf/TotalProbability

    Normalized_Prob_Inf 

    Normalized_Prob_NInf

    Normalized_Prob_Inf +Normalized_Prob_NInf

    # Displaying the Final result
    if ( Normalized_Prob_Inf >Normalized_Prob_NInf):
        print("Infected with COVID-19.")
    else:
        print("Not infected with COVID-19.")
    
if __name__ == "__main__":
    filename=sys.argv[1]
    in_row=list(map(float, sys.argv[2:]))
    symptoms  = {'Dry Cough': in_row[0], 'High Fever': in_row[1], 'Sore Throat':in_row[2], 'Difficulty in breathing': in_row[3]}
    main(filename,symptoms)