students = [
    {"name": "Hermione", "House": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "House": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "House": "Gryffindor", "patronus": "Jack Russell terrir"},
    {"name": "Draco", "House": "Slytherin", "patronus": "None"},
]
for student in students:
    print(student["name"], student["House"], student["patronus"], sep=", ")