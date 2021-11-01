import json


# 1. Write a Python program to convert JSON data to Python object.
def json_to_obj(json_data):
    return json.loads(json_data)
# for k,v in json_to_obj('{ "Name":"David", "Class":"I", "Age":6 }').items():
#     print(k, '=', v)


# 2. Write a Python program to convert Python object to JSON data
def dict_to_json(dict):
    return json.dumps(dict)
# print(dict_to_json({ "Name":"David", "Class":"I", "Age":6 }))


# 3. Write a program to convert Python objects into JSON strings. Print all the values.

# 4. Write a program to convert Python dictionary object (sort by key) to JSON data.
#       Print the object members with indent level 4.

# 5. Write a program to convert JSON encoded data into Python objects.

# 6. Write a program to create a new JSON file from an existing JSON file.

# 7. Write a program to check whether an instance is complex or not. Go to the editor

# 8. Write a program to check whether a JSON string contains complex object or not.

# 9. Write a program to access only unique key value of a Python object.
