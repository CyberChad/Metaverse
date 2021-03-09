import json
import yaml


class ComplexEncoder(json.JSONEncoder):
     def default(self, obj):
         if isinstance(obj, complex):
            return [obj.real, obj.imag]
         # Let the base class default method raise the TypeError
         return json.JSONEncoder.default(self, obj)


class YamlDecoder():
    __init__():
        pass


if __name__ == '__main__':

    stream = open("foo.yaml", 'r')
    dictionary = yaml.load_all(stream)

    for doc in dictionary:
        print("New document:")
        for key, value in doc.items():
            print(key + " : " + str(value))
            if type(value) is list:
                print(str(len(value)))

