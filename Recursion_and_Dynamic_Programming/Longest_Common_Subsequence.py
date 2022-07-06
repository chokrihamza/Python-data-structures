def lcs_recursive(seq1,seq2,idx1=0,idx2=0):
    # base case
    if idx1==len(seq1) or idx2==len(seq2):
        return 0
    elif seq1[idx1]==seq2[idx2]:
        return 1+ lcs_recursive(seq1,seq2,idx1+1,idx2+1)
    else:
        option1=lcs_recursive(seq1,seq2,idx1+1,idx2)
        option2=lcs_recursive(seq1,seq2,idx1,idx2+1)
        return max(option1,option2)


#print(lcs_recursive("serendipitous","precipitation"))
#print(lcs_recursive("ser","pre"))


""" 
Time complexity: 2^(m+n) 
m: length of sequence 1
n:length of sequence 2
"""
#-------------------------------------------------------------------------
""" 
The next solution is by using memoization

"""

def lcs_memo(seq1,seq2):
    memo={}
    def recurse(idx1=0,idx2=0):
        # create the key for our hashtable
        key=(idx1,idx2)
        if key in memo:
            return memo[key]
        elif idx1==len(seq1) or idx2==len(seq2):
            memo[key]=0

        elif seq1[idx1]==seq2[idx2]:
            memo[key]=1+recurse(idx1+1,idx2+1)
        else:
            memo[key]=max(recurse(idx1+1,idx2),recurse(idx1,idx2+1))
        return memo[key]
    return recurse(0,0)   # the entire string we begin from 0,0
print(lcs_memo("serendipitous","precipitation"))
# Complexity O(m*n) the size of memo














"""
solution using dynamic programming 
"""
n1,n2=5,7
#print([[0 for x in range(n1)] for x in range(n2)])

def lcs_dynamic(seq1,seq2):
    n1,n2=len(seq1),len(seq2)
    table=[[0 for x in range(n2+1)] for x in range(n1+1)]
    for i in range(n1):
        for j in range(n2):
            if seq1[i]==seq2[j]:
                table[i+1][j+1]=1+table[i][j]
            else:
                table[i+1][j+1]=max(table[i][j+1],table[i+1][j])
    return table,"result: "+str(table[-1][-1])

#print(lcs_dynamic("serendipitous","precipitation"))