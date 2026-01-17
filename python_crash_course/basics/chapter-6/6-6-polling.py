favorite_languages = {"jen": "python",
                      "sarah": "c", 
                      "edward": "rust", 
                      "phil": "python"
                      }
take_poll = ["jen", "sarah"]
not_take_poll = ["edward", "phill"]
for person, language in favorite_languages.items():
    if person in take_poll:
        print(f"Thanks for learn {language}, {person}")
    else:
        print(f"You must study {language}, {person}")