d = {"red": 4, "blue": 1, "green": 14, "yellow": 2};


d['red'] = d['blue']
print(d);
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2};
d['blue'] += 10
print(d);
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2};
d['yellow'] = len(d)
print(d);
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2};
d['green'] = {'orange' : 6}
print(d);
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2};
d = dict(zip(d.keys(), d.values()))
print(d);
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2};
d = dict.fromkeys(d, 0)
print(d);
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2};
d.pop('black', None)
print(d);
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2};
d.get('black', None)
print(d);
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2};
d.setdefault('black', None)
print(d);
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2};
d = {k : 0 for k in d.keys()}
print(d);
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2};
d = {}
print(d);
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2};