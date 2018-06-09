print('Hello, Django girls!')


if 3 > 2:
    print('To działa!')


if 5 > 2:
    print('5 jest jednak większe od 2')
else:
    print('5 nie jest większe od 2')


name = 'yuyuyu'
if name == 'Ola':
    print('Hej Ola!')
elif name == 'To Tomek':
    print('Hej Tomek!')
elif name == 'Ewa':
    print('Hej Ewa!')
elif name == 'Sonja':
    print('Hej Szymon!')
elif name == 'Sonja':
    print('Hej Beata!')
elif name == 'Sonja':
    print('Hej Sonja!')
else:
    print('Hej anonimie!')


volume = 5
# Change the volume if it's too loud or too quiet
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")


def hi():
    print('Hej!')
    print('Jak się masz?')

hi()



def hi(imie):
    if imie == 'Ola':
        print('Hej Ola!')
    elif imie == 'Sonja':
        print('Hej Sonja!')
    else:
        print('Hej nieznajoma!')
imie = "Ola"
hi("imie")




def hi(imie):
    print('Hej ' + imie + '!')

hi("Rachel")



def hi(imie):
    print('Witaj ' + imie + '!')

dziewczyny = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Ty']
for imie in dziewczyny:
    hi(imie)
    print('Kolejna dziewczyna')


for i in range(1, 6):
    print(i)
