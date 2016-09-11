def function1(n, m):
    function2(3.4)
    function1(2, 3)

def function2(n):
    if n > 0:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        return -1

def main():
    print(min('Jan', 'jan'))
def min(n1, n2):
    smallest = n1
    if n2 < smallest:
     smallest = n2

main()
def intersect(seq1, seq2):
    res = set()
    for x in seq1:
        if x in seq2:
            res.add(x)
            return res
print(intersect('beer', 'burger'))
print(intersect((1,2,3,4),(1,4,2,5)))
print(intersect({1,2,3,4},{1,4,2,5}))

v = 42
def do():
    v = 0
    v += 1
    print (v)

def da():
    global v
    v += 1
    print (v)
do()
da()
print(v)

def make(N):
    return lambda x: x**N
square = make(2)
cube = make(3)
hyper = make(4)
print(square(3))
print(cube(3))
print(hyper(3))