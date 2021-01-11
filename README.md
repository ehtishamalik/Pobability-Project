# Probability and Random Variables CEP

## 1) Symptom Based Covid-19 Detection 
Command-line syntax:   
      python Covid19_Pred.py Symptom_data_file.csv Patient_Symptom_file.csv  
###### Input Parameters:   
a) Covid-19 sysmptom and test data   
   i) Infected/Not Infected  (Yes/No)   
   ii) Dry Cough (0.25/0.5/0.75/2  Mild -> Severe)   
   iii) High Fever (0.25/0.5/0.75/2  Mild -> Severe)   
   iv) Sore Throat (0.25/0.5/0.75/2  Mild -> Severe)   
   v) Difficulty Breathing  ( 0/1 -> No/Yes)    
b) Patient symptom data for prediction   
   i) Dry Cough (0.25/0.5/0.75/2  Mild -> Severe)    
   ii) High Fever (0.25/0.5/0.75/2  Mild -> Severe)     
   iii) Sore Throat (0.25/0.5/0.75/2  Mild -> Severe)     
   iv) Difficulty Breathing ( 0/1 -> No/Yes)    
###### Output:   
Infected/Not Infected   

## Description: 
Thie Covid19 Prediction tools uses Bayesian Probability Model to predict Covid19 Infection with symptoms based on past data.
## 2) City lockdown recommendation   
Command-line syntax:     
      python Lockdown_Pred.py City_data_file.csv   
###### Input Parameters:   
a) City Data:-   
   Various data of multiple cities    
   i) Population (Number of people living in the city. No prefix)    
   ii) Demographics  (Scaled 0.5-1 Young/Old)   
   iii) Population Density (Scaled 1-5 Sparse -> Dense)   
   iv) Infections in Neighbouring cities (1/2/3 ->None/In 1 city/In multiple cities)   
   v) Health Provider Standard (Scaled 1-5 Worst -> Best)    
   vi) Infection rate (Infection Rate)   
   vii) Past Outbreaks (0.5/1 Yes/No)      
          
###### Output:        
Names of cities to lockdown for preventing virus outbreak    

## Description
The Lockdown recommendation tool uses past data to generate a score for each city and recommends lockdown of cities above mean score.
