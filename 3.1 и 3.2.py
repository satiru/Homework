print ('Как тебя зовут?')
a=str(input())
print ('Привет,',a,'!')
###########
def Sum(a,b,c):
    su=a+b+c
    pr=a*b*c
    return su,pr
#####################
a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))
c=int(input('Введите третье число: '))
su,pr=Sum(a,b,c)
print ('Сумма введенных чисел: ',su)
print ('Произведение введенных чисел: ',pr)
