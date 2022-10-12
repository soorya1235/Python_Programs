from jsonschema import validate

jsondata = {
  "a" : 1,
  "b" : 1,
}

jsonschema = {
  "type": "object",
  "properties": {
    "a": {
      "type": "integer"
    },
    "b": {
      "type": "string"
    }
  },
  "required": [
    "a",
    "b"
  ]
}

def validate_schema(jsondata,jsonschema):
  try:
    validate(jsondata,jsonschema)
    return True
  except Exception as e:
    print(e)
    return False


status = validate_schema(jsondata,jsonschema)
print(status)