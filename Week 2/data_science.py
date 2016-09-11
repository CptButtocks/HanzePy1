students = { 0: "Nynke", 1: "Lolle", 2: "Jikke", 3: "Popke", 4: "Teake", 5: "Lieuwe", 6: "Tsjabbe", 7: "Klaske", 8: "Ypke", 9: "Lobke"};
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)];

friendshipMatrix = [range(len(students))[0 for x in range(10)]];
studentCount = 0;
friendsAdded = 0;
friendCount = 0;
for student in students:
    friendshipMatrix[studentCount] = students[studentCount];
    for friendship in friendships:
        if friendship[friendCount[0]] == studentCount:
            friendshipMatrix[friendsAdded][studentCount] = friendships[friendCount];
            friendsAdded = friendsAdded + 1;

    studentCount = studentCount + 1;


    print(students[count]);
    print(count);
    count = count + 1;

print(friendshipMatrix);