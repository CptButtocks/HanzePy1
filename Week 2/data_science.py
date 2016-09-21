interests = [(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),(0, "Spark"), (0,"Storm"), (0, "Cassandra"),(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),(1, "Postgres"),(2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodels"),(2, "pandas"),(3, "R"), (3, "Python"),(3, "statistics"), (3, "regression"), (3, "probability"),(4, "machine learning"), (4, "regression"), (4, "decision trees"),(4, "libsvm"),(5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),(5, "Haskell"), (5, "programminglanguages"),(6, "statistics"),(6, "probability"), (6, "mathematics"), (6, "theory"),(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),(7, "neural networks"),(8, "neural networks"), (8, "deep learning"),(8, "Big Data"), (8, "artificialintelligence"),(9, "Hadoop"),(9, "Java"), (9, "MapReduce"), (9, "Big Data")]
students = { 0: "Nynke", 1: "Lolle", 2: "Jikke", 3: "Popke", 4: "Teake", 5: "Lieuwe", 6: "Tsjabbe", 7: "Klaske", 8: "Ypke", 9: "Lobke"};
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)];

friendshipMatrix = [];
studentInterests = {};

counter = 0;

for student in students:
    studentInterests[counter] = [];
    for interest in interests:
        if interest[0] == counter:
            studentInterests[counter].append(interest[1]);
    friendshipMatrix.append([]);
    counter += 1;

for friendship in friendships:
    friendshipMatrix[friendship[0]].append(friendship[1]);
    friendshipMatrix[friendship[1]].append(friendship[0]);

friendshipMatrix.sort(key=len);
print(friendshipMatrix);
print(studentInterests);


