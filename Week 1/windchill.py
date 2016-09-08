T = float(input("What is the temperature: "));
B = float(input("What is the windforce: "));

G= 13 + ((0.62 * T) - (14 * (B**0.24))) + (0.47 * (T * (B**0.24)));

print(G);