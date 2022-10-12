import json

from jsonschema import validate

jsondata = {
 "a":1,
 "b":"2",
}

jsonschema = {
  "type": "object",
  "properties": {
    "a": {
      "type": "integer"
    },
    "b": {
      "type": "integer"
    }
  },
  "required": [
    "a",
    "b"
  ]
}

def validate_json_schema(schema,data):
  try:
    validate(data,schema)
    return True
  except Exception as e:
    print(e)
    return False


a = validate_json_schema(jsonschema,jsondata)
print(a)