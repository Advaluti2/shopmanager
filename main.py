#Shop Manager
import time
from random import randint

class GameInit():
    #handles inital startup
    @staticmethod
    def variables():
        #general
        global day, cash, level, exp, req_exp, total_customers, total_profit
        
        day = 1
        cash = 50
        level = 1
        exp = 0
        req_exp = 10
        total_customers = 0
        total_profit = 0
        
        #stock
        global fish, potato, cooked_fish, cooked_potato
        
        fish = 20
        cooked_fish = 0
        potato = 20
        cooked_potato = 0

        #prices
        global fish_cost, cooked_fish_cost, potato_cost, cooked_potato_cost
        
        fish_cost = 1
        cooked_fish_cost = 2
        potato_cost = 2
        cooked_potato_cost = 2

        #exp values
        global fish_exp, potato_exp

        fish_exp = 1
        potato_exp = 2

    @staticmethod
    def tutorial():
        #tutorial func. teachering the user
        print("Uncle Bob: Welcome to the tutorial!")
    
    @staticmethod
    def manager_name():
        #handles the username
        global username
        username = input("Uncle Bob: What is your name, I always forget... ")
        username_ch = input("Uncle Bob: Just to check, your name is "+username+", right? ")
        username_ch = username_ch.lower()
        if username_ch in ["yes", "y"]:
            return
        if username_ch in ["no", "n"]:
            GameInit.manager_name()
            return
        else:
            print("Game: Please enter a valid response!")
            GameInit.manager_name()

    @staticmethod  
    def startup():
        #runs all the startup stuff
        pre_init = input("Game: Would you like to start a new game? ")
        pre_init = pre_init.lower()
        
        if pre_init in ["yes", "y"]:
            GameInit.variables()
            GameInit.manager_name()
            GameMain.main()
            return
        if pre_init in ["no", "n"]:
            SaveLoad.load()
            return
        else:
            print("Game: Please enter a valid response!")
            GameInit.startup()

    @staticmethod
    def end():
        print("Fred: Congratulations Boss, you finished the day!")
        print("Fred: You sold "+str(total_customers)+" stock and made $"+str(total_profit)+". You now have made $"+str(cash)+" overall")
        print("Fred: You are level "+str(level)+" and have "+str(exp)+"/"+str(req_exp)+" EXP for the next level.")
        print("Fred: Sadly, all unsold food had to be thrown away.")
        daytime = 0
        global day
        day = day + 1
        ask_sav = input("Game: Would you like to save your game? ")
        ask_sav = ask_sav.lower()
        if ask_sav in ["yes", "y"]:
            SaveLoad.save()
            return
        elif ask_sav in ["no", "n"]:
            return
        else:
            print("Game: Please enter a valid response!")

    @staticmethod
    def buy_stock():
        global fish, fish_cost, potato, potato_cost, cash

        ask_stock = input("Fred: Hey boss, would you like to buy some stock this morning (You have $"+ str(cash)+")? ")
        if ask_stock.lower() in ["yes", "y"]:
            ask_buy = input("Fred: Okay boss, would you like to buy some fish (Stock: "+str(fish)+") or potatoes (Stock: "+str(potato)+")? ")
            #fish
            if ask_buy.lower() in ["fish", "f"]:
                ask_amount = int(input("Fred: How many Fish would you like to order? ($" + str(fish_cost) + " a fish) "))
                if ask_amount > cash:
                    print("Fred: Sorry, we don't have the money to order that much!")
                    buy_stock()
                    return
                else:
                    cash = cash - (ask_amount * fish_cost)                
                    fish = fish + ask_amount
                    print("Fred: The order has arrived thanks to Congo Prime and it's instant delivery!")
                    return
            #potato
            if ask_buy.lower() in ["potato", "potatoes", "p"]:
                if not level < 3:
                    print("Sorry! You need to be level 3 to unlock this!")
                    buy_stock()
                else:
                    ask_amount = int(input("Fred: How many Potatoes would you like to order? ($" + str(potato_cost) + " a potato) "))
                    if ask_amount > cash:
                        print("Fred: Sorry, we don't have the money to order that much!")
                        buy_stock()
                        return
                    else:
                        cash = cash - (ask_amount * potato_cost)                
                        potato = potato + ask_amount
                        print("Fred: The order has arrived thanks to Congo Prime and it's instant delivery!")
                        return
        if ask_stock.lower() in ["no", "n"]:
            print("Fred: We can always order more tomorrow if we need.")
            return
            
    @staticmethod
    def cook_stock():
        #variables
        global fish, cooked_fish, potato, cooked_potato

        #fish
        print("Fred: Sounds good! How many fish do you want to cook this morning? ")
        ask_fish = int(input("Fred: Oh, you currently have "+str(fish)+": "))
        if ask_fish > fish:
            print("Fred: Boss, you can't cook more than you have!")
            cook_stock()
            return
        else:
            print("Fred: I'll cook the fish now Boss!")    
            time.sleep(1.5)
            fish = fish - ask_fish
            cooked_fish = ask_fish
            print("Fred: Al'ight Boss, "+str(cooked_fish)+" fish were cooked!")

        #potato
        if level >= 3:
            ask_pots = input("Would you like to cook chips today? ")
            if ask_pots.lower() in ["yes", "y"]:
                print("Fred: Sounds great! How many fish do you want to cook this morning? ")
                ask_potato = int(input("Fred: Oh, you currently have "+str(potato)+": "))
                if ask_potato > potato:
                    print("Fred: Boss, you can't cook more than you have!")
                    cook_stock()
                    return
                else:
                    print("Fred: I'll cook the fish now Boss!")
                    time.sleep(1.5)
                    potato = potato - ask_potato
                    cooked_potato = ask_potato
                    print("Fred: Al'ight Boss, "+str(cooked_potato)+" portions of chips were cooked!")
            if ask_buy.lower() in ["no", "n"]:
                print("Fred: Okay boss.")
        else:
            return

    @staticmethod
    def special_days():
        #special days
        global cash, day
        if day == 1:
            print("-= Day 1: The Beginning =-")
            print("Uncle Bob: Welcome to ShopManager! You must run the shop inherited from me, your Uncle Bob!")
            time.sleep(1.5)
        
        if day == 7:
            print("-= Day 7: The First Week =-")
            print("Uncle Bob: Congratulations "+username+", you made it through the week. Here's an extra $50 to get you on your way!")
            cash = cash + 50
            print("Game: You now have $"+str(cash)+"!")
            time.sleep(1.5)

        if day == 14:
            print("-= Day 14: The Second Week =-")
            print("Uncle Bob: Congratulations "+username+", you made it through a second week. Impressive! Here's an extra $100 to get you on your way!")
            cash = cash + 100
            print("Game: You now have $"+str(cash)+"!")
            time.sleep(1.5)

        
        elif not (day == 1) or (day == 7) or (day == 14):
            print("-= Day "+str(day)+" =-")
            time.sleep(1.5)

class GameMain():
    #handles the main game
    @staticmethod
    def main():
        while True:
            print("")
            GameMain.generic_day()

    @staticmethod
    def generic_day():
        #global imports
        global level, cooked_fish, cooked_potato, cooked_fish_cost, cooked_potato_cost, total_customers, total_profit, cash, exp, req_exp
        
        #start of day
        GameInit.special_days()
        GameInit.buy_stock()
        GameInit.cook_stock()
        
        #middle section of day
        print("Fred: Well boss, we'd better open up for the day.")
        daytime = 0

        while True:
            #time prints
            print("Game: "+str((daytime + 3))+":00pm")
            time.sleep(2)

            #customers entering
            fish_rand_no = level * randint(1, 3)
            fish_customers = randint(0, fish_rand_no)
            fish_hour_exp = fish_customers * fish_exp

            if level >= 3:
                potato_rand_no = level * randint(1, 3)
                potato_customers = randint(0, potato_rand_no)
                potato_hour_exp = potato_customers * fish_exp
                

            #stock check
            fish_sellable = True
            potato_sellable = True
            
            if fish_customers > cooked_fish:
                print("Fred: Welp, we're out of fish!")
                fish_sellable = False
                if not level >= 3:
                    GameInit.end()
                    return
                
            if (level >= 3) and (potato_customers > cooked_potato):
                print("Fred: Welp, we're out of chips!")
                potato_sellable = False
                
            if (fish_sellable == False) and (potato_sellable == False):
                GameInit.end()
            
            cooked_fish = cooked_fish - fish_customers
            profit = 0
            profit = (fish_customers * cooked_fish_cost)

            if level >= 3:
                cooked_potato = cooked_potato - potato_customers
                profit = profit + (potato_customers * cooked_potato_cost)
                if potato_customers == 0:
                    print("Fred: "+str(potato_customers)+" customers bought any fish.")
                    
            if fish_customers == 0:
                print("Fred: "+str(fish_customers)+" customers bought any fish.")
                customers = fish_customers
                hour_exp = fish_hour_exp
            else:
                if level >= 3:
                    customers = fish_customers + potato_customers
                    hour_exp = fish_hour_exp + potato_hour_exp
                else:
                    customers = fish_customers
                    hour_exp = fish_hour_exp
                print("Fred: "+str(customers)+" customers have come in. They ordered "+str(fish_customers)+" cooked fish and we now have "+str(cooked_fish)+" left!")
                if potato_sellable == False:
                    print("Fred: From this, you've made $"+str(profit)+" and gained "+str(hour_exp)+" EXP.")
                if (potato_sellable == True) and (level <= 3):
                    print("Fred: From this, you've made $"+str(profit)+" and gained "+str(hour_exp)+" EXP.")
                elif level >= 3:
                    print("Fred: They also also bought "+str(potato_customers)+" portions of chips and we now have "+str(cooked_potato)+" portions left!")
                    print("Fred: From this, you've made $"+str(profit)+" and gained "+str(hour_exp)+" EXP.")

            #managing totals
            total_customers = total_customers + customers
            total_profit = total_profit + profit

            cash = cash + profit
            exp = exp + hour_exp

            #run level check
            if exp >= req_exp:
                level = level + 1
                exp = exp - req_exp
                req_exp = req_exp * 2
                print("Uncle Bob: Congratulations! You levelled up to "+str(level)+"!")
                print("Uncle Bob: With this, your reputation has increased.")
            
            if daytime >= 7:
                if (fish_sellable == False) and (potato_sellable == False):
                    return
                else:
                    #end of day
                    GameInit.end()
                    return
            
            daytime = daytime + 1
            
class SaveLoad():
    #handles the save/load functions
    @staticmethod
    def save():
        #handles game saving
        save_name = input("Game: What would you like the save file to be called? ")
        print("Game: Saving Game...")
        file = open(save_name+".shs", "w")
        file.write(username)
        file.write("\n")
        file.write(str(day))
        file.write("\n")
        file.write(str(level))
        file.write("\n")
        file.write(str(cash))
        file.write("\n")
        file.write(str(fish))
        file.write("\n")
        file.write(str(potato))
        file.write("\n")
        file.write(str(exp))
        file.write("\n")
        file.write(str(req_exp))
        file.write("\n")
        print("Game: Game Saved!")

    @staticmethod
    def load():
        #handles game loading
        save_name = input("Game: What is the name of the save file? ")
        print("Game: Loading Game...")
        GameInit.variables()

        global username, day, level, cash, fish, potato, exp, req_exp
        
        file = open(save_name+".shs", "r")
        #username
        username = file.readline().replace("\n", "")

        #day
        day = int(file.readline().replace("\n", ""))

        #level
        level = int(file.readline().replace("\n", ""))

        #cash
        cash = int(file.readline().replace("\n", ""))

        #fish
        fish = int(file.readline().replace("\n", ""))
        
        #potato
        potato = int(file.readline().replace("\n", ""))

        #exp
        exp = int(file.readline().replace("\n", ""))

        #req_exp
        req_exp = int(file.readline().replace("\n", ""))
        print("Game: Game Loaded!")
        GameMain.main()
        
GameInit.startup()
