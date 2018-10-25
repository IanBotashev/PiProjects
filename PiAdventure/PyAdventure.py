

import os
def clear():
    print('\n' *100)
    
def PrintStore():
    shopP = 'Game Files\\Shop\\itemshop.txt'
    store = open(shopP, 'r')
    print(store.read())
    store.close()

def openfile(file):
    g=open(file, "r")
    print(g.read())
def Gold():
    print("You have ", gold, " gold left")
def PrintHealth():
    print("You have ", health," health.")
Items = []
health=10
gold = 0
print("Hello yond travler, how are you?")
PText = input(">")
print("Ok.. Anyways, lets go on an adventure on a far away land.")
print("First lets earn some gold...")
apples =0
while True:
    print("what do you want to be?(Type 'help' if you don't know what to be)")
    PText = input(">")
    if PText == 'help':
        openfile("Game Files\\Roles\\Roles.txt")
    if PText == 'Bank Manager':
        
    
gold = apples
apples = 0
while True:
    Gold()
    print("Whay do you want to get?(Type 'help' if you don't know what do get)")
    PText = input('>')
    if PText =='help':
        PrintStore()
        
    if PText == 'Sword':
        if 'Sword' not in Items:
            if gold>=10:
                gold = gold-10
                Items.append("Sword")
            else:
                print("Sorry, but you don't have enough gold for that")
        if 'Sword' in Items:
            print("Sorry, you alderdy have that")
            
    if PText == 'Heavy Sowrd':
        if 'Heavy Sword' in Items:
            print("You alderdy have one of those")
        if 'Heavy Sword' not in Items:
            if gold>=30:
                gold = gold-30
                Items.append("Heavy Sword")
            else:
                print("Sorry, but you don't have enough gold for that")
            
    if PText == 'Shield':
        if 'Shield' not in Items:
            if gold>=10:
                gold = gold-10
                Items.append("Shield")
        
            else:
                print("Sorry, but you don't have enough gold for that")
        if 'Shield' in Items:
            print("You alderdy have that")

    if PText == 'Medkit':
        if gold>=15:
            gold = gold-15
            Items.append("Medkit")
        else:
            print("Sorry, but you don't have enough gold for that")

    if PText == 'Extra Health':
        if gold>=30:
            gold = gold-30
            health = health+10
        else:
            print("Sorry, but you don't have enough gold for that")

    if PText == 'Done':
        break

print("You start on a journy, with your,")
x = 0
clear()
length = len(Items)
while x<length:
    print(Items[x])
    x=x+1
Shield = False
Shield2 = False
print("You have to get a cart across a plain, there are monstors, but you are ready for the challenge")
print("An arrow comes out of nowhere, you doge it by a few centimeters")
print("what do you want to do?")
if 'Shield' in Items:
    print("You can take your shield out(Say 'Take shield out' if you want to do that)")
print("You can hide behind the cart(Say 'Hide behind the van' if you want to hide behind the van)")
PText = input(">")
if 'Shield' in Items:
    if PText == 'Take shield out':
        Shield = True
        print("You have taken your shield out")
elif PText == 'Hide behind the van':
    print("Ok")
    Shield2 = True

else:
    print("You get shot by an arow")
    health = health-3
       
print("You see what is hitting you, do you want to run up to it and kill it?(yes, no)")
PText = input(">")
if PText == 'yes':
    shield2 = False
if 'Shield' in Items:
    if Shield == False:
        print("You run up and hit the goblin, it as a huge cut in its body, he manages to hit you, you did noy have your shield out so you lose 2 health")
        health = health-2
        PrintHealth()
    if Shield == True:
        print("You run up and hit the goblin, it as a huge cut in its body, he tries to hit you but you had your shield out, and deflected it.")
if 'Shield' not in Items:
    print("You run up and hit the goblin, it as a huge cut in its body, he manages to hit you. You lose 2 health")
    health = health-2
    PrintHealth()
if 'Heavy Shield' in Items:
    print("You run up tp the goblin, you hit him and he dies...")
