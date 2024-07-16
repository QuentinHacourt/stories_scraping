import csv

# make a set of all stories, this prevents duplicates
stories = set()
# list of story entries
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

    # make dictionaries out of unique story titles
    # for now every story has an empty set of voters
    for story in stories:
        story_entry = {
            "title": story,
            "voters": set(),
        }
        story_entries.append(story_entry)

    # add names to list of voter of stories if they voted for this story
    for entry in input:
        for story in story_entries:
            if (entry['User story 1'] == story['title'] or
                entry['User story 2'] == story['title'] or
                entry['User story 3'] == story['title'] or
                entry['User story 4'] == story['title'] or
                entry['User story 5'] == story['title']):
                story['voters'].add(entry['Your name'])

# sort the entries (from most votes to least votes)
sorted_story_entries = sorted(story_entries, key=lambda d: len(d['voters']), reverse=True)

# pretty print all entries one by one
for story_entry in sorted_story_entries:
    print("title: {}, voters: {}, voter-count: {}".format(story_entry['title'], ", ".join(story_entry['voters']), len(story_entry['voters'])))
