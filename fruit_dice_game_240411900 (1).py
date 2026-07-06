import random as rnd
#simdi challence icin fonksiyon olusturacagim
def challenge (ad1,ad2):
    print("Welcome to the Multiplayer Fruit Dice challenge !")
    oyuncu1=0
    oyuncu2=0
    #3 tur donmesi icin for'da range kullaniyorum
    for i in range(0,3):
        print(f"___ Round {i+1} ___")
        kullanici1=0
        kullanici2=0
        #zardan rastgele sayi secilmesi icin rnd.randint kullaniyorum
        zar=rnd.randint(1,6)
        #rastgele meyve secilmesi icin rnd.choice kullaniyorum
        meyve =rnd.choice(['kiraz','muz','elma'])
        #bonus ve puanlarin sartlari icin if kullaniyorum
        if (zar==6 and meyve=='kiraz'):
            bonus1=10
            kullanici1+=bonus1+zar
            print(f"{ad1} rolled a {zar} and got a cherry!")
            print("Bonus combo! +10 points")
        elif (meyve=='muz'):
            bonus2=6
            kullanici1+=bonus2+zar
            print(f"{ad1} rolled a {zar} and got a banana!")
            print('Banana bonus! +6 points')
        else:
            kullanici1=zar
            print(f"{ad1} rolled a {zar} and got a {meyve}")
            print(f"your point {kullanici1}")
        zar2=rnd.randint(1,6)
        meyve2=rnd.choice(['kiraz','muz','elma'])
        if (zar2==6 and meyve2=='kiraz'):
            bonus1=10
            kullanici2+=bonus1+zar
            print(f"{ad2} rolled a {zar2} and got a cherry!")
            print("Bonus combo! +10 points")
        elif (meyve2=='muz'):
            bonus2=6
            kullanici2+=bonus2+zar
            print(f"{ad2} rolled a {zar2} and got a banana!")
            print('Banana bonus! +6 points')
        else:
            kullanici2=zar2
            print(f"{ad2} rolled a {zar2} and got a {meyve2}")
            print(f"your point {kullanici2}")
        print('...')
        oyuncu1+=kullanici1
        oyuncu2+=kullanici2
    print("Final Scores:")
    print(f'{ad1}: {oyuncu1} points \n{ad2}: {oyuncu2} points')
    return "Bob wins !"
kisi1=input("Enter name for player 1: ")
kisi2=input("Enter name for player 2: ")
#fonksiyonu cagiriyorum
print(challenge(kisi1,kisi2))