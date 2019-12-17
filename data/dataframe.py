import pandas as pd
data = pd.read_csv("small_vocab_fr", delimiter = "\n", header = None)
print(data.head())
data = data[0:50000]
data.to_csv("50k_fr_data.csv", index= False)
#convert csv to text file
import csv
csv_file = '50k_fr_data.csv'
txt_file = 'fr_50k.txt'
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()
    print(my_output_file)