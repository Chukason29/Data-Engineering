import json

# use the json.loads() to convert JSON string to a python object
#use json.dump() to convert a python object to a JSON string

x =  '{ "name":"John", "age":30, "city":"New York"}' #JSON string
value = json.loads(x)
print(f"{value} is a {type(value)}") #returns a dictionary

y = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

jsonValue = json.dumps(y)
print(f"{jsonValue} is a {type(jsonValue)}") #prints a JSON string