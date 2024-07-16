import csv
# make a set of all stories, this prevents duplicates
stories = set()

# opens the input file
with open('exercise_input.csv', 'r') as input_file:
    # reads the csv file and
    # puts the entries in a list of dictionaries
    input = csv.DictReader(input_file)

    # iterates over each entry in the file
    for entry in input:
        print(entry)
