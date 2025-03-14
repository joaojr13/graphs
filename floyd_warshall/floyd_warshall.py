def floyd_warshall(W, n):
    d = [row[:] for row in W] 
    
    for k in range(n):  
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d