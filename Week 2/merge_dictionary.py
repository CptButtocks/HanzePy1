d1 = {'a': 100, 'b': 200};
d2 = {'x': 300, 'y': 200};



def mergeDictionary(dict1, dict2):
    return {**dict1, **dict2};

print(mergeDictionary(d1, d2));