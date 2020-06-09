# consuming-swapi-with-flask
Consuming the swapi.dev API using Flask without helper libraries

## Task specification
 People page: Display a table with the characters info:

  - Allow pagination

  - Allow order by Name, Gender, Mass and Height 

  - Allow filter by Film, Startship, Vehicles and Planets

Starship page: Display a table with the starships info 
  - Calculate the starship score (hyperdrive_rating dividido / cost_in_credits)
  - Order the data by the starship score (descending)

## Requirements:
Python >=3.6
All the other dependecies are listed in requirements.txt 

Run:
```
pip install -r requirements.txt

```
- Docker deploy 
- Add unit tests
- Make requests asynchronously
- Document code
- Improve error handling
