import json
from types import SimpleNamespace

def serialize(obj):
    return json.dumps(obj, default=vars)

def deserialize(data):
    return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))