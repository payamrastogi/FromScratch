from csv import reader 

#load a CSV file
def load_csv(filename):
    file = open(filename, "r")
    lines = reader(file)
    dataset = list(lines)
    return dataset

#filename = 'pima_diabetes.csv'
#dataset = load_csv(filename)
#print('loaded data file {0} with {1} rows and {2} columns'.format(filename, len(dataset), len(dataset[0])))

#load a CSV file without empty lines
def load_csv_without_empty_lines(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

# filename = 'pima_diabetes.csv'
# dataset = load_csv_without_empty_lines(filename)
# print('loaded data file {0} with {1} rows and {2} columns'.format(filename, len(dataset), len(dataset[0])))
# print(dataset[0])

def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

# filename = 'pima_diabetes.csv'
# dataset = load_csv_without_empty_lines(filename)
# print('loaded data file {0} with {1} rows and {2} columns'.format(filename, len(dataset), len(dataset[0])))
# print(dataset[0])
#convert string columns to float
# for i in range(len(dataset[0])):
#     str_column_to_float(dataset, i)

# print(dataset[0])


def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup

filename = 'iris.csv'
dataset = load_csv_without_empty_lines(filename)
print('loaded data file {0} with {1} rows and {2} columns'.format(filename, len(dataset), len(dataset[0])))
print(dataset[0])
lookup = str_column_to_int(dataset, 4)
print(dataset[0])
print(lookup)