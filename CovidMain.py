from Covid19Pred import CovidPrediction
import sys

obj = CovidPrediction()

filename = sys.argv[1]
test_file = sys.argv[2]

symptoms = obj.csv_to_dict(test_file)
obj.main(filename, symptoms)
