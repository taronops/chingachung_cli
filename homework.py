import random
import time
Yes = 'Այո'
No  = 'Ոչ'
Rock = 'Քար'
Paper = 'Թուղթ'
Scissors = 'Մկրատ'
name = input('Մուտքագրեք ձեր անունը: ')
print(f'Բարև {name}!Բարի գալուստ Չինգա Չունգի CLI հարթակ. Պատրաստ ես հաղթելու ?')
start = input('Այո թէ Ոչ: ').title()

if start == 'Այո':
    print('Առաջ')
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print('Չին Գա Չունգ!!!')

    options = [Rock , Paper , Scissors]
    computer_choice = random.choice(options)
    player_choice = input('Ընտրեք որևիցե մեկը (Քար/Թուղթ/Մկրատ): ').title()

    print(f'Դուք ընտրեցիք {player_choice}, CLI֊ը ընտրեց {computer_choice}.')
    if player_choice == computer_choice:
        print("Ոչ ոքի!")
    elif player_choice == Rock and computer_choice == Scissors:
        print('Դուք հաղթեցիք!')
    elif player_choice == Paper and computer_choice == Rock:
        print('Դուք հաղթեցիք!')
    elif player_choice == Scissors and computer_choice == Paper:
        print('Դուք հաղթեցիք!')
    else:
        print('Դուք պարտվեցիք!')
else:
    print('Կրկին փորցեք!') 
