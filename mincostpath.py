def minPathCost(listOfLists):
    dp = [[0 for j in range(len(listOfLists))] for i in range(len(listOfLists))]
    r = len(listOfLists)
    c = len(listOfLists[0])
    # Top dowm
    # fill last cell
    dp[r-1][c-1] = listOfLists[r-1][c-1]
    #fill last row
    #print(dp)
    for i in range(c-2,-1,-1):
        dp[r-1][i] = dp[r-1][i+1] + listOfLists[r-1][i]
    #fill last col
    for i in range(r-2,-1,-1):
        dp[i][c-1] = dp[i+1][c-1] + listOfLists[i][c-1]

    for i in range(r-2, -1, -1):
        for j in range(c-2, -1,-1):
            dp[i][j] = listOfLists[i][j] + min([dp[i+1][j],dp[i][j+1]] )
    return dp[0][0]

if  __name__ == "__main__":
    t = int(input().strip())
    mat=[]
    for ti in range(t):
        rc = input().strip().split(' ')
        r = int(rc[0])  
        c = int(rc[1])  

        for _ in range(r):
            rowList = list(map(int, input().strip().split(' ')))
            mat.append(rowList)
        print(minPathCost(mat))