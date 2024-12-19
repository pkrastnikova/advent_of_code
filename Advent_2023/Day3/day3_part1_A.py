f = open('day3_part1.txt', "r")
lines = f.readlines()
matrix = []
result = 0


for line in lines:
    line.strip()
    row_list = []
    for i in range(len(line)):
        row_list.append(line[i].strip())
    matrix.append(row_list)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()   
    

M = len(matrix)  # number of rows (lines)
N = len(matrix[M-1]) # number of columns

def get_adj(i, j_first, j_last): #call with first and last j index of the number found

    adj_pairs = list()
    
    #current line
    if j_first == 0:
        adj_pairs.append([i, j_last+1])        
    if j_last == N-1:
        adj_pairs.append([i, j_first-1])
    if j_first > 0 and j_last < N-1:
        adj_pairs.append([i, j_first-1])
        adj_pairs.append([i, j_last+1])    
    
    #neighbouring up and down lines
    for j in range(max(0, j_first-1), min(N-1, j_last+2)):
        
        if (i > 0):
            adj_pairs.append([i-1, j])
        if (i < M-1):
            adj_pairs.append([i+1, j])
    
    return adj_pairs   


def check_adj(adj_list):    
    for adj in adj_list:
        i = adj[0]
        j = adj[1]
        if matrix[i][j] != "." and not matrix[i][j].isnumeric():
            print("matrix[i][j]: ", matrix[i][j])
            return True
    return False


def engine_schematic(m):
    result = 0
    for i in range(len(m)):
        number = ''
        indeces = list()
        j = 0
        while j < len(m[i]):
            while j < len(m[i]) and m[i][j].isnumeric():
                number += m[i][j]
                indeces.append(j)
                j+=1
                #print("current number: ", number)

            #found a number or reached end of line
            if len(indeces) > 0:               
               adj = get_adj(i, indeces[0], indeces[-1])
               print("number: ", number)
               print("indeces: ", indeces)
               print(adj)

               if check_adj(adj):                        
                    result += int(number, base=10)
                    print("Add number: ", number)

               j-=1
               number = ''
               indeces = list()                   
            
            j+=1
    
    print(result)



engine_schematic(matrix)

print("M: ", M)
print("N: ", N)




 
