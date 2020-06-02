import json

try:
    data = {'name': 'achilles', 'age': 18}

    print(data)
    print(json.dumps(data))
    str = "11"

except Exception as err:
    print(err)
