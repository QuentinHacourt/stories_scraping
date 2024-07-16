import csv

# make a set of all stories, this prevents duplicates
stories = set()
#
story_entries = []

# opens the input file
with open('exercise_input.csv', 'r') as input_file:
    # reads the csv file and
    # puts the entries in a list of dictionaries
    input = list(csv.DictReader(input_file))

    # iterates over each entry in the file
    for entry in input:
        # adds the story names from all the "User story" columns
        stories.update({
            entry['User story 1'],
            entry['User story 2'],
            entry['User story 3'],
            entry['User story 4'],
            entry['User story 5'],
        })

    for story in stories:
        story_entry = {
            "title": story,
            "voters": set(),
            "vote-count": 0
        }
        story_entries.append(story_entry)

    for entry in input:
        for story in story_entries:
            if (entry['User story 1'] == story['title'] or
                entry['User story 2'] == story['title'] or
                entry['User story 3'] == story['title'] or
                entry['User story 4'] == story['title'] or
                entry['User story 5'] == story['title']):
                story['vote-count'] += 1
                story['voters'].add(entry['Your name'])


print(story_entries)
