def make_album(artist_name, album_title, number_songs=None):
    album = {"artist": artist_name, "album": album_title}
    if number_songs:
        album["number of songs: "] = number_songs
    return album

ecdl = make_album("el canto del loco", "zapatillas")
print(ecdl)

pignoise = make_album("pignoise", "los hombres de paco")
print(pignoise)

julio_iglesias = make_album("julio iglesias", "quijote")
print(julio_iglesias)

mana = make_album("mana", "labios compartidos", 12)
print(mana)