musica = ['PROXYCITY','P.Y.N.G.','DNSUEY!','SERVERS','HOST!','CRIPTONIZE','OFFLINE DAY', 'SALT','ANSWER!','RAR?','WIFI ANTENNAS']

N = int(input())

while(N > 0):
    N -= 1
    X, Y = input().split()
    print(musica[int(X) + int(Y)])