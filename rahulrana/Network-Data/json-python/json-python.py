import json
data = '''{
    "name" : "Rana",
    "phone" : {
        "type" : "intl",
        "number" : "+91 844 791 7137"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data) # loads the json format of data into python data structure for use (Data is a dictionary with name, phone, email out of which phone, email are dictionaries too)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])