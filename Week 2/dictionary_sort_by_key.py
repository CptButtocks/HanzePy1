import collections

d = {'red': '#FF0000', 'green': '#008000', 'black': '#000000', 'white': '#FFFFFF'};



def sortByKey(dictionary):
    od = collections.OrderedDict(sorted(dictionary.items()));
    return dict(od);

print(sortByKey(d));