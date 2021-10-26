import json
from difflib import SequenceMatcher, get_close_matches
data = json.load(open("data.json"))
word_input = input("Enter the word:  ").lower()

# def find_word(word):
#     for key in data.keys():
#         if word == key:
#             return data[word]
#         else:
#             return "The word seems made-up. Or, is beyond the scope of this dictionary"


def find_word(word):
    if word in data:
        return data[word]
    elif word not in data:
        matched_word = get_close_matches(word_input, data.keys())[0]
        return(f'It seems you mistyped the word. Maybe you meant {matched_word}\n {data[matched_word]}')
    else:
        return "The word seems made-up. Or, is beyond the scope of this dictionary"


print(find_word(word_input))
