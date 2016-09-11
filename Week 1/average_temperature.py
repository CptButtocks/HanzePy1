with open("C:\\Users\\RonOS\\Documents\\hanze 2.1 literatuur\\Assignments\\Python\\station_VL.txt") as f:
    content = f.readlines();

del content[0];
temps = 0;
daysCollection = [];
tempCollection = [];
averageCollection = [];
seen = set();
for line in content:
    seen.add(line.split('\t')[0]);

daysCollection = [ x for x in seen if x.isdigit() ]
daysCollection.sort(key=int);
for day in daysCollection:
    tempCollection.append([]);

for line in content:
    index = int(line.split('\t')[0]) -1;
    tempCollection[index].append(float(line.split('\t')[2]) / 10);

for day in tempCollection:
    total = 0;
    for temp in day:
        total = total + temp;

    averageCollection.append(total / len(day));

print(averageCollection);

