# Created by Nikolai Tiugaev for TumoLabs.
# Task 1. Mad Libs.
# Mad Libs is a game with a basic story template that has blank spaces which need to be filled by the user.
# The fun part is that the user inputs words without knowing the story ahead of time.


# introducing templates and dictionary of marks.
TEMPLATES: tuple = (
    '''
It was about {0} {1} ago when I arrived at the hospital in a {2}. 
The hospital is a/an {3} place, there are a lot of {4} {5} here. 
There are nurses here who have {6} {7}. 
If someone wants to come into my room I told them that they have to {8} first. 
I’ve decorated my room with {9} {10}. 
Today I talked to a doctor and they were wearing a {11} on their {12}. 
I heard that all doctors {8} {13} every day for breakfast. 
The most {14} thing about being in the hospital is the {15} {5}!
''',
    '''
This weekend I am going camping with {0}. 
I packed my lantern, sleeping bag, and {1}. I am so {2} to {3} in a tent. 
I am {4} we might see a(n) {5}, I hear they’re kind of dangerous. 
While we’re camping, we are going to hike, fish, and {6}. 
I have heard that the {7} lake is great for {8}. 
Then we will {9} hike through the forest for {10} {11}. 
If I see a {7} {5} while hiking, I am going to bring it home as a pet! 
At night we will tell {10} {12} stories and roast {13} around the campfire!!
''',
    '''
Dear {0}, I am writing to you from a {1} castle in an enchanted forest. 
I found myself here one day after going for a ride on a {2} {3} in {4}. 
There are {5} {6} and {7} {8} here! 
In the {9} there is a pool full of {10}.
I fall asleep each night on a {11} of {12} and dream of {13} {14}. 
It feels as though I have lived here for {15} {16}. 
I hope one day you can visit, although the only way to get here now is {17} on a {18} {19}!
'''
)

DICT_OF_VARIABLES: dict = {
    1: (
        'Number', 'Measure of time', 'Mode of Transportation', 'Adjective', 'Another Adjective', 'Noun',
        'Color', 'Part of the Body', 'Verb', 'Another Number', 'Another Noun', 'Another Noun',
        'Another Part of the Body', 'Another Noun', 'Another Adjective', 'Silly Word'
        ),
    2: ('Proper Noun (Person’s Name)', 'Noun', 'Adjective (Feeling)', 'Verb', 'Another Adjective (Feeling)', 'Animal',
        'Another Verb', 'Color', 'Verb (ending in ing)', 'Adverb (ending in ly)', 'Number', 'Measure of Time',
        'Silly Word', 'Another Noun'
        ),
    3: ('Proper Noun (Person’s Name)', 'Adjective', 'Color', 'Animal', 'Place', 'Another Adjective',
        'Magical Creature (Plural)', 'Another Adjective', 'Another Magical Creature (Plural)', 'Room in a House',
        'Noun', 'Another Noun', 'Another Noun (Plural)', 'Another Adjective', 'Another Noun (Plural)', 'Number',
        'Measure of time', 'Verb (ending in ing)', 'Another Adjective', 'Another Noun'
        ),
}


# action starts here.
values_list: list = []    # to store the users words.

# loop goes until is not interrupted by 'q'.
while True:
    num_templ: str = input('Input number of template (1 or 2 or 3) or q to quit: ')

    # if input is 'q' then quit the game.
    if num_templ == 'q':
        print('The game was stopped! Goodbye!')
        break

    # if input is not correct then user tries again.
    if num_templ not in {'1', '2', '3'}:
        print('Your input is not correct! Try again!')
        continue

    # if user is here, it means he's chosen correct template.
    print(f"You've chosen template {num_templ}. Now input the words. To interrupt input q.")

    # loop through all marks of chosen template. we are receiving inputs from user.
    for var in DICT_OF_VARIABLES[int(num_templ)]:
        input_check: str = input(f'Input {var}: ')

        # if user's input is 'q' then he goes back by 1 step.
        if input_check == 'q':
            values_list.clear()     # don't forget to clean the storage.
            break

        # storing of data.
        values_list.append(input_check)

    # if loop wasn't interrupted then all data are collected, we can print the story.
    else:
        print('This is your story:')
        print(TEMPLATES[int(num_templ) - 1].format(*values_list))   # unpacking list of data to template by 'format'.
        values_list.clear()     # don't forget to clean the storage.

# end of program.
