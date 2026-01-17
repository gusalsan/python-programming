rivers = {"Miño": "Spain and Portugal", "Nile": "Egypt", "Amazonas": "Perú, Colombia and Brasil"}
for river, country in rivers.items():
    print(f"You can't swim in {river} river which is situated on {country}")
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)