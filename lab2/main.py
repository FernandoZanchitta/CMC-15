import pandas as pd
from functions import *
import json

# Read the data from the CSV file
data = pd.read_csv('republican_democrat.csv')
from functions import *
#splitting the data into train and test
train_data, test_data = split_data(data, 0.8)
result_tree = id3(train_data, 'Target')
print(json.dumps(result_tree, indent=4))
#test the tree
accuracy = evaluate(result_tree, test_data, 'Target')

print("Accuracy: ", accuracy)


