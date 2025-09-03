import time
import random
import os

a=''
daramad_zaman= 0
total_money = 100
list_daraii = []
khone = 0
mashin = 0
zamin = 0 
motor = 0

answer1 = input('do you want to play 100second (y/n) ')
if answer1 == 'y':
    start_time = time.time()
    
    while True:
        second = int(time.time() - start_time)
        if second >100:
            break
        
        dashbord = (f'''DASHBOD
zaman : {second}
daramd kasb shode az zaman : {daramad_zaman}
kole pool : {total_money}
list daraii : {list_daraii}
''')
        print(dashbord)
        
        while True:
            a = input('''\nhar moghe khasti dasshbord update she enter bezan : ()
kharid va frosh :(1)
qomar : (2)
:  ''')
            if a == '1':
                a2 = input('\n1.kharid , 2.frosh : ')
                if a2 == '1':
                    print(''' 
    1.khone : 6000 
    2.mashin : 1000
    3.zamin : 250
    4.motor : 100
    ''')
                    b1 = input('\nkodomo mikhay adadesh (1,2,3,4) : ')
                    if b1 == '1':
                        if total_money >= 6000:
                            total_money -=6000
                            list_daraii.append('khone')            
                            print('tabrik tonesti khone begiri')
                        else:
                            print('\npool nadri')

                    if b1 == '2':
                        if total_money >= 1000:
                            total_money -= 1000
                            list_daraii.append('mashin')
                            print('mashin kharidi')
                        else:
                            print('\npool nadri')


                    if b1 == '3':
                        if total_money >= 250 :
                            total_money -= 250
                            list_daraii.append('zamin')
                            print('zamin kharidi')
                        else:
                            print('\npool nadri')
                    
                    if b1 == '4':
                        if total_money >= 100:
                            total_money -= 100
                            list_daraii.append('motor')
                            print('motor kharidi')
                        else:
                            print('\npool nadri')
                
                if a2 == '2':
                    
                    print(f'''ghymat haye frosh :
1.khone : {khone}
2.mashin : {mashin}
3.zamin : {zamin}
4.motor : {motor}''')
                    b3 = input('chi mifroshi (1,2,3,4) : ')
                    if b3 == '1' :
                        if 'khone' in list_daraii:
                            list_daraii.remove('khone')
                            total_money += khone
                            print('khone frokhti')
                        else:
                            print('khone nadari')
                    elif b3 == '2':
                        if 'mashin' in list_daraii:
                            list_daraii.remove('mashin')
                            total_money += mashin
                            print('mashin frokhti')
                        else:
                            print('mashin  nadari')
                    elif b3 == '3':
                        if 'zamin' in list_daraii:
                            list_daraii.remove('zamin')
                            total_money += zamin
                            print('zamin frokhti')
                        else:
                            print('zamin nadari')
                    elif b3 == '4':
                        if 'motor' in list_daraii:
                            list_daraii.remove('motor')
                            total_money += motor
                            print('motor frokhti')
                        else:
                            print('motor nadari')

            if a == '2':
                print('''QOMAR HARAME
4 ta item darim ke be sorat random har kodam tabdil be jaieze mishan
list jaieze ha : pooch , -500 , -500 , 3000
1.shans1
2.shans2
3.shans3
4.shans4
''')
                b2 = input('shans mored nazar (1,2,3,4) : ')
                if total_money >= 500 :
                    shans = random.choice([0,-500,-500,3000])
                    total_money += shans
                    print(f'shoma barande {shans} shodid')
                else:
                    print('balaye 500 pool mikhay')
            if a == '' :
                break
        
        khone += second*100 
        mashin += second*10
        zamin += second*25
        motor += second*5

        daramad_zaman += second
        total_money += second
        time.sleep(1)
        os.system('cls')
        
print(f'{dashbord}\n BAZI TAMAM')

input('aya dobare mikhay bazi koni ?')

