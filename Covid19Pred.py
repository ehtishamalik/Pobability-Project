# importing pandas module to read csv file.
import pandas
import sys
from csv import DictReader  # For creating dict from csv file


class CovidPrediction:

    def __init__(self):
        self.Data = pandas.DataFrame

    # Reading data from csv to a dataframe
    def read_data(self, filename):
        # reading data files using pandas
        self.Data = pandas.read_csv(filename, sep=",")

    # Reading from csv to dictionary
    def csv_to_dict(self, test_file):
        file = open(test_file, "r")
        reader = DictReader(file)
        labels = list(reader)[0]
        dict_in = dict(labels)
        return dict_in

    # Separating data based on a given label in a given column
    def Separate_data(self, Data, label, column):
        Sep_Data = Data[Data[Data.columns[column]] == label]
        return Sep_Data

    # main function to predict values
    def main(self, filename, symptoms):
        self.read_data(filename)
        # seperating data infected with Corona
        Data_Inf = self.Separate_data(self.Data, "Yes", 0)
        # Displaying output of infected people
        # Data_Inf

        # seperating data not infected with Corona
        Data_NInf = self.Separate_data(self.Data, "No", 0)
        # Displaying output of infected people
        # Data_NInf

        # Declaring dictionaries to store data
        # This dictionary will store the count of symptoms of data with infected people
        Count_Inf = {}
        # This dictionary will store the count of symptoms of data with non infected people
        Count_NInf = {}

        # Calculating the count of symptoms in data of infected and non infected people
        for key, data in symptoms.items():
            # Gives the count of key from data of infected people
            count = list(Data_Inf[key]).count(float(data))
            Count_Inf[key] = count

            # Gives the count of key from data of non infected people
            count = list(Data_NInf[key]).count(float(data))
            Count_NInf[key] = count

        # The list will store the probabilities of infected people
        AllProbabilitiesWithInfected = []

        # The list will store the probabilities of non infected people
        AllProbabilityWithNonInfected = []

        # total number of peoples we have in overall data
        Num_Total = len(list(self.Data['infected with covid']))

        # total number of peoples infected with Covid
        Num_Inf = len(list(Data_Inf['infected with covid']))

        # Probability of people infected with Corona
        Prob_Prior_Inf = Num_Inf / Num_Total
        # Appending p_c to list
        AllProbabilitiesWithInfected.append(Prob_Prior_Inf)

        # Calculating the probaility of symptoms given that you are infected with Corona
        for key, data in Count_Inf.items():
            AllProbabilitiesWithInfected.append(data / Num_Inf)

        # total number of peoples not infected with Covid
        Num_NInf = len(list(Data_NInf['infected with covid']))

        # Probability of people not infected with Corona
        ProbabilityOfPeopleNotInfected = Num_NInf / Num_Total

        # Appending ProbabilityOfPeopleNotInfected to list AllProbabilityWithNonInfected
        AllProbabilityWithNonInfected.append(ProbabilityOfPeopleNotInfected)

        # Calculating the probaility of symptoms given that you are not infected with Corona
        for key, data in Count_NInf.items():
            AllProbabilityWithNonInfected.append(data / Num_NInf)

        # Displaying the probaility given that you are not infected with Corona

        # Multiplying the probailities given that you are infected with Corona
        Prob_Inf = 1.0
        for i in AllProbabilitiesWithInfected:
            if i == 0:  # if probaility of any symptom is equal to zero
                i = 0.01  # replace it with 0.01
            Prob_Inf = Prob_Inf * i

        # Multiplying the probailities given that you are not infected with Corona
        Prob_NInf = 1.0
        for i in AllProbabilityWithNonInfected:
            if i == 0:  # if probaility of any symptom is equal to zero
                i = 0.01  # replace it with 0.01
            Prob_NInf = Prob_NInf * i

        # Normalize Probabilities
        TotalProbability = Prob_Inf + Prob_NInf
        Normalized_Prob_Inf = Prob_Inf / TotalProbability
        Normalized_Prob_NInf = Prob_NInf / TotalProbability

        # Displaying the Final result
        if Normalized_Prob_Inf > Normalized_Prob_NInf:
            print("\nInfected with COVID-19.\n")
        else:
            print("\nNot infected with COVID-19.\n")
