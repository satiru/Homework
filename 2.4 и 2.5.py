def Sr(a=1,b=2,c=3):
    print ('Введите новое значение а = ')
    a=int(input())
    print ('Введите новое значение b = ')
    b=int(input())
    print ('Введите новое значение c = ')
    c=int(input())
    sr=(a+b+c)/3
    print (sr)
    return sr
###################################
def Ura(A1,B1,C1,A2,B2,C2):
    D=A1*B2-A2*B1
    x=(C1*B2-C2*B1)/D
    y=(A1*C2-A2*C1)/D
    return x,y
####################################
Sr()
#############################
print ('Введите все значения переменных от А1 до С2')
A1,B1,C1,A2,B2,C2=map(int,input().split())

x,y=Ura(A1,B1,C1,A2,B2,C2)
print ('x=',x)
print ('y=',y)


