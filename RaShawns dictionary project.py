import time

import random

lst1 = [1,2,3,4,5,6]

lst2 = [1,2,3,4,5,6]

s_l = 5

def current_lives(s_l):
    
    current_life = s_l - 1

    return current_life

def restart(s_l):
    
    s_l = 4

    return s_l
    

loadout = {
    'primary_weapon' : "Assult Rifles",
    'seconday_weapon' : "Pistols", 
    'perks' : "Quick revive, Scavenger",
    'lives' : 4,
    }

exp_information = {
    'current_exp' : 0,
    'exp_needed' : 200000,
    'current_level' : 1,
    }

rules = {
    'roll' : " press R",
    'stop' : " press N",
    'Lives' : "You have four chances to roll a 10 or over and if you dont you lose",
    }

control = {
    'r' : "roll a dice",
    't' : "Stop the game",
    }

background_info = print("You have been transported to a magical world with monsters and demons. The only way to get back home is to climb and tower and fight monsters to get to the top. You only have 4 lives so good luck")

time.sleep(5)

while True:
    
    info = input("press (f) to get loadout informatioin: " 
             "press (e) to get exp information: " 
             "press (r) for rules: " 
             "press (c) for controls: "  
             "press (g) to play the game: ")
    
    if info == "f":
        print("loading...")
        time.sleep(.5)
        print(loadout)
        time.sleep(1)
        
    elif info == "e":
        print("loading...")
        time.sleep(.5)
        print(exp_information)
        time.sleep(1)
        
    elif info == "r":
        print("loading...")
        time.sleep(.5)
        print(rules)
        time.sleep(1)
        
    elif info == "c":
        print("loading...")
        time.sleep(.5)
        print(control)
        time.sleep(1)
        
    elif info == "g":
        print("loading...")
        time.sleep(.5)
        print("Here they come, get ready!")
        time.sleep(1)
        s_l = 5
        while True:
            s_l = s_l -1
            
            new_lives = current_lives(s_l)
            
            first_roll  = random.choice(lst1)
            
            second_roll = random.choice(lst2)
            
            damage = first_roll + second_roll
    
            roll = input("Roll(r): ")
            
            if roll == "r":
                
             
             if damage >= 10:
                 time.sleep(.5)
                 print("You win ")
                 time.sleep(1)
                 win = input("Press (n) to go back to the main menu ")
                 time.sleep(.5)
                 
                 if win == "n":
                        time.sleep(.5)
                        print("Loading...")
                        time.sleep(.5)
                        break

             elif damage < 10:
                     
                     print("You didn't do enough damage you did " + str(damage))
                     
                     time.sleep(.5)
                     
                     print("You have " + str(new_lives) + " live(s) left!!!")
                     
                     time.sleep(.25)
                     
                     if new_lives == 0:
                      time.sleep(.5)
                      print("G")
                      time.sleep(.5)
                      print("A")
                      time.sleep(.5)
                      print("M")
                      time.sleep(.5)
                      print("E")
                      time.sleep(.5)
                      print("")
                      time.sleep(.5)
                      print("O")
                      time.sleep(.5)
                      print("V")
                      time.sleep(.5)
                      print("E")
                      time.sleep(.5)
                      print("R")
                      time.sleep(.5)
                      
                      win = input("Press (n) to go back to the main menu ")

                      if win == "n":
                       time.sleep(.25)
                       print("Loading...")
                       time.sleep(.5)
                       break
                

                        
                
               
                         
                 

       
            
     
        
        
        

        
    

    
    
    




    
    
    
        
    
