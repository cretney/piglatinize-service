import requests

with open('strings_to_piglatinize.txt') as string_file:
    strings = [line.rstrip() for line in string_file]
for string in strings:
    response = requests.get(f'http://localhost:8001/piglatinize/?text={string}')
    print(response.json())
