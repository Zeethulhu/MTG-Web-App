''' This script will grab data from https://api.magicthegathering.io and save it
to a local JSON file.

It is worth noting that the API returns 100 records per request and has a limit
of 5000 requests per hour


'''


# built-in libraries
import json
import pickle
import os.path


# third party libraries
from mtgsdk import Card


# Global variables
PICKLED_CARDS = 'mtg_card_data.pickle'
JSON_OUTPUT = 'mtg_card_data.json'


# testing if the pickle file exists and use that instead of using the mtgsdk
# to download the card data from the internet API.
if os.path.isfile(PICKLED_CARDS):
    print("Found pickle file of card data {}".format(PICKLED_CARDS))
    print("loading file...")
    with open(PICKLED_CARDS, 'rb') as fileobj:
        cards = pickle.load(fileobj)

else:
    print("Grabbing card data from internet API. This may take a few minutes.")
    cards = Card.all()
    print("Saving card data to pickle file {}".format(PICKLED_CARDS))
    with open(PICKLED_CARDS, 'wb') as fileobj:
        pickle.dump(cards, fileobj)


# counting the number of cards.
len(cards)


# creating dictionary that will be converted to JSON.
# cards_dict = {'cards' : []}
cards_dict = []


for mtg_card in cards:
    # cards_dict['cards'].append(mtg_card.__dict__)
    cards_dict.append(mtg_card.__dict__)

print("Dumping data as JSON file: {}".format(JSON_OUTPUT))
with open(JSON_OUTPUT, "w") as write_file:
    json.dump(cards_dict, write_file)


