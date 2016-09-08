L = [1, 2, 3, 4, 5, 6];
for i in range(1, 6):
 L[i] = L[i - 1];
 #print(L);

 L1 = list(range(1, 10, 2));
 L2 = L1;
 L1[0] = 111;
 #print(L1);
 #print(L2);

 a, b = 0, 1;
 while b < 10:
     print(b);
     a, b = b, a + b;
