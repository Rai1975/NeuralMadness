import csv

def txt_to_csv(delimiter, txt_file_path, csv_file_path):
    with open(txt_file_path, 'r') as txt_file, open(csv_file_path, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Read and process each line from the TXT file
        for line in txt_file:
            parts = line.strip().split(delimiter)       # Split the line by the delimiter (e.g., tab)

            if len(parts) == 2:
                print(parts)
                csv_writer.writerow((parts))              # Ensure the line has exactly two parts


if __name__ == "__main__":
    txt_file_path = r'C:\Users\User\projects\NeuralNetwork\data\tnn_train.txt'
    csv_file_path = r'C:\Users\User\projects\NeuralNetwork\data\tnn_train.csv'

    txt_to_csv(delimiter='\t', txt_file_path=txt_file_path, csv_file_path=csv_file_path)
    print("Done!")