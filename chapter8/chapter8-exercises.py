# 8-1 Messages
"""
def display_message():
    print('I am learning about functions')

display_message()
"""

# 8-2 Favorite Book
"""
title = 'alice in wonderland'

def favorite_book(title):
    print(f'One of my favorite books is {title.title()}')

favorite_book(title)
"""

# 8-3 T-Shirt 
"""
def make_shirt(size):
    print(f'the shirt size is a {size}')

make_shirt('large')
"""

# 8-4 Large Shirts
"""
def make_shirt(large, medium, all_size):
    print(f'{large}{medium}', f'{all_size}')

make_shirt(large='I Love Python', medium='I Love Python', all_size='Other Message')
"""

# 8-5 Cities
"""
def describe_city(country = 'US', city = 'US'):
    print(f'{city} is in {country}')

describe_city('US','Seattle')
describe_city('Germany','Manassas')
describe_city('US','DC')
"""

# 8-7 Albums
"""
def make_album(artist, album, tracks=''):
    if tracks: 
        album_dict = {
            'artist': artist.title(),
            'album': album.title(),
            '# of songs': tracks
        }
    else:
        album_dict = {
            'artist': artist.title(),
            'album': album.title(),
        }
    return album_dict

artistMsg = "Enter an artist: "
albumMsg = "Enter an album made by the artist you just entered: "

trackMsg = input("Would you like to add the number of tracks to this entry? (yes/no) ")

if trackMsg == 'yes':
    trackPrompt = "Enter the number of tracks: "
    album = make_album(
        input(artistMsg),
        input(albumMsg), 
        tracks=input(trackPrompt))
else:
    album = make_album(input(artistMsg),input(albumMsg))

print(album)

trackMsg = input("Would you like to add the number of tracks to this entry? (yes/no) ")

if trackMsg == 'yes':
    trackPrompt = "Enter the number of tracks: "    
    album = make_album(
        input(artistMsg),
        input(albumMsg), 
        tracks=input(trackPrompt))
else:
    album = make_album(input(artistMsg),input(albumMsg))

print(album)

trackMsg = input("Would you like to add the number of tracks to this entry? (yes/no) ")

if trackMsg == 'yes':
    trackPrompt = "Enter the number of tracks: "
    album = make_album(
        input(artistMsg),
        input(albumMsg), 
        tracks=input(trackPrompt))
else:
    album = make_album(input(artistMsg),input(albumMsg))

print(album)

if __name__ == '__main__':
    pass
"""

# 8-8 User Albums
"""
def make_album(artist, album, tracks=''):
    if tracks: 
        album_dict = {
            'artist': artist.title(),
            'album': album.title(),
            '# of songs': tracks
        }
    else:
        album_dict = {
            'artist': artist.title(),
            'album': album.title(),
        }
    return album_dict

artistPrompt = "Enter an artist: "
albumPrompt = "Enter an album from that artist: "
tracksPrompt = "How many tracks does that album have?"


while True:
    print("(Type 'quit' at anytime to exit the program)")
    artist = input(artistPrompt)

    if artist == 'quit':
        break

    album = input(albumPrompt)

    if album == 'quit': 
        break

    trackResponse = input("Would you like to add the number of tracks to this entry? (yes/no) ")

    if trackResponse == 'quit':
        break
    elif trackResponse == 'yes':
        tracks = input(tracksPrompt)
        print(make_album(artist, album, tracks))
    else:
        print(make_album(artist, album))
"""

# 8-9 Messages
"""
texts = ['hewwo :3', 'suh cuh', 'thats what im saying']

def show_messages(texts):
    for text in texts:
        print(text)

show_messages(texts)
"""

# 8-10 Sending Messages
"""
def show_messages(queued_texts, sent_texts):
    while queued_texts:
        current_text = queued_texts.pop()
        print(f" Sending text: {current_text}")
        sent_texts.append(current_text)

def sent_messages(sent_texts):
    print("Text has been sent:")
    for finished_texts in sent_texts:
        print(finished_texts)

queued_texts = ['hewwo :3', 'suh cuh', 'thats what im saying']
sent_texts = []

show_messages(queued_texts, sent_texts)
sent_messages(sent_texts)
"""

# 8-11 Archived Messages
"""
def show_messages(queued_texts, sent_texts):
    while queued_texts:
        current_text = queued_texts.pop()
        print(f" Sending text: {current_text}")
        sent_texts.append(current_text)

def sent_messages(sent_texts):
    print("\nText that have been sent:")
    for finished_texts in sent_texts:
        print(finished_texts)

queued_texts = ['hewwo :3', 'suh cuh', 'thats what im saying']
sent_texts = []

show_messages(queued_texts[:], sent_texts)
sent_messages(sent_texts)
print(queued_texts, sent_texts)
"""


# 8-12 Sandwiches
"""
"""

def sandwich(*toppings):
    print(f"\n Making a sandwich with: ")
    for topping in toppings:
        print(f"- {topping}")

sandwich('roast beef','lettuce','mayo')
sandwich('ham','turkey', 'mustard')
sandwich('bbq', 'chicken')

    

