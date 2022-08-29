def make_album(artist, title):
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('Nirvana', 'Nevermind')
print(album)

album = make_album('Musikang Bayan', 'Rosas ng Digma')
print(album)

album = make_album('Linkin Park', 'Minutes to Midnight')
print(album)