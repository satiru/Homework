def Time(N):
    h=N//60//60
    N=N-h*60*60
    m=N//60
    return m
#############################
def Day(k):
    a=k//7
    d=(k-a*7)+1
    return d
#############################
print ('Введите количество секунд ')
N=int(input())
m=Time(N)
print ('С конца прошлого часа прошло',m,'минут')
################################
print ('Введите количество прошедших дней ')
k=int(input())
d=Day(k)
if d==1:
 print (k,'день это понедельник')
if d==2:
 print (k,'день это вторник')
if d==3:
 print (k,'день это среда')
if d==4:
 print (k,'день это четверг')
if d==5:
 print (k,'день это пятница')
if d==6:
 print (k,'день это суббота')
if d==7:
 print (k,'день это воскресенье')


