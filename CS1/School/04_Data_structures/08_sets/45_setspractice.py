def symdiff(A,B):
    return A-B|B-A
def symdiff2(A,B):
    return A-(A&B)|B-(A&B)
(A|B)-(A-B)
A={1,2,3,4}
B={3,4,5,6}
print(symdiff(A,B))
print(symdiff2(A,B))
