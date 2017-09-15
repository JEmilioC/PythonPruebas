import json

with open('ej.json') as jsonEscuela:
    data=json.load(jsonEscuela)

print(data['alumnos'])
