def make_album(artist_name, album_title, number_songs=None):
    album = {"artist": artist_name, "album": album_title}
    if number_songs:
        album["number of songs: "] = number_songs
    return album

while True:
    artist_question = input("What its your favourite artist?\n")
    album_question = input("And their favourite album?\n")
    exit = "If you want to exit, press 0 two times"
    print(make_album(artist_question, album_question))
    print(exit)
    if artist_question == "0":
        break
    if album_question == "0":
        break