def recur_array(N, R, C):
    if N == 0 :
        return 0

    H = pow(2, N-1)
    X = pow(H, 2)
    result = 0

    if R >= H :
        R -= H
        result += 2 * X
    if C >= H :
        C -= H
        result += X
    #print(result)
    return result + recur_array(N-1, R, C)

N, R, C = input().split()
N = int(N)
R = int(R)
C = int(C)

print(recur_array(N, R, C))