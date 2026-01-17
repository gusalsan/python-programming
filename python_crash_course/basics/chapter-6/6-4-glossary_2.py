new_concepts = {"string": "cadena de carácteres", 
                "int": "número entero", 
                "float": "número decimal", 
                "loop": "for number in numbers", 
                "tuples": "listas inmutables", 
                "dictionary": "values and keys",
                "get function": "for know if we have a value",
                "del function": "for delete something"
                }
for concept, definition in new_concepts.items():
    print(f"\n{concept.title()}:")
    print(f"{definition}\n")