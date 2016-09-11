students = { 0: "Nynke", 1: "Lolle", 2: "Jikke", 3: "Popke", 4: "Teake", 5: "Lieuwe", 6: "Tsjabbe", 7: "Klaske", 8: "Ypke", 9: "Lobke"};
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)];

friendshipMatrix = [range(len(students))[2]];
count = 0;
for student in students:
    friendshipMatrix[count] = student[count];
    count = count + 1;

print(friendshipMatrix);