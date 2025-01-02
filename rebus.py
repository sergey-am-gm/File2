
def password (n):
    passw_ = ''
    for a in range(1,int(n/2) + 1):       # вычисляем правую границу,
        for b in range(1, n - a + 1):     # что-бы убрать лишние итерации
            if n % (a + b) == 0 and a < b:
                passw_ = passw_ + str(a) + str(b)
    return passw_

num = 0
while num < 3 or num > 20:
    num = int(input('Введите число от 3 до 20 '))
print(num)
print('пароль = ', password(num))

# Ниже это проверка, печать True если всё совпадает.
check_ = False
check_1 = False
if password(3) == '12':
    if password(4) == '13':
        if password(5) == '1423':
            if password(6) == '121524':
                if password(7) == '162534':
                    if password(8) == '13172635':
                        if password(9) == '1218273645':
                            if password(10) == '141923283746':
                                if password(11) == '11029384756':
                                    if password(12)  == '12131511124210394857':
                                        check_ = True
if password(13) == '112211310495867':
    if password(14) == '1611325212343114105968':
        if password(15) == '1214114232133124115106978':
            if password(16) == '1317115262143531341251161079':
                if password(17) == '11621531441351261171089':
                    if password(18) == '12151811724272163631545414513612711810':
                        if password(19) == '118217316415514613712811910':
                            if password(20) == '13141911923282183731746416515614713812911':
                                check_1 = True


print(check_ and check_1)