"""Original Matrix:
1	2	3	
5	6	7	
8	7	6	
4	3	2	
Resultant Matrix:
1	3	6	
6	14	24	
14	29	45	
18	36	54"""

def summation(m, res, r, c):
    total = 0
    if r==0 and c==0: return m[0][0]
    elif r == 0:
        for i in range(c+1):
            total += res[r][c]
        return total
    elif c == 0:
        for i in range(r+1):
            total += m[r][c]
        return total
    else:
        for i in range(r+1):
            total += m[r][c]
        return total + res[r][c-1]
    

def integralMatrix(m, r, c):
    res = []
    for i in range(r):
        temp = []
        for j in range(c):
            val = summation(m, res, i, j)
            temp.append(val)
        res.append(temp)

    return res
        

def display(m, r, c):
    for i in range(r):
        for j in range(c):
            print((i,j), end="\t")
        print()
        

def main():
    m = [[1,2,3],
         [5,6,7],
         [8,7,6],
         [4,3,2]]

    print("Original Matrix:")
    display(m, len(m), len(m[0]))
    summation(m, r=len(m), c=len(m[0]))
    #print("Resultant Matrix:")
    #display(res, len(res), len(res[0]))

main()
