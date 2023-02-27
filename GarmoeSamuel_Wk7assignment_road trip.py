#Program to output the gas and food costs per person on a group road trip

#Samuel Garmoe
#February 27th, 2023
#CMIS102 Week 7 assignment

def give_welcome():
    print("Please use this program to calculate the costs of your recent road trip with friends")
    print("Follow the prompts and everything will be done for you!")


#info statements


def food_avg(people, days):             #fn to get food costs
    dailyfood = list()                  #initialize array 
    tripday = 1                         #counter for while loop
    triplength = days
    while tripday <= triplength:
        while True:
            try:            #data type validation
                print("How much did food cost on day",tripday,"? Please input a positive number.")
                value = int(input()) 
                tripday+= 1
                dailyfood.append(value)         #add value to food array
                break
            except:
                print("Please input a positive integer.")
        
    dailyfoodavg = sum(dailyfood) / len(dailyfood)  #food cost per day
    foodperperson = sum(dailyfood) / people         #total food cost per person
    return dailyfood


def gas_avg(people, days):              #fn to get gas costs
    dailygas = list()                   #daily gas cost array
    tripday = 1                         #loop counter 
    triplength = days
    while tripday <= triplength:
        while True:
            try:                #data type validation
                print("How much did gas cost in total dollars on day",tripday,"?")
                value = int(input())        #check for int
                dailygas.append(value)      #add value to gas array
                tripday+= 1
                break
            except:
                print("Please input a positive integer.")
    dailygasavg = sum(dailygas) / len(dailygas)         #daily gas total
    gasperperson = sum(dailygas) / people               #gas cost per person
    return dailygas

def main():
    #intro statements fn 
    give_welcome()              

    #basic input from user
    people = eval(input("How many people went on the road trip?"))
    days = eval(input("How many days long was your trip?"))

    #calculate total food cost
    dailyfood = food_avg(people, days)
    foodsum = sum(dailyfood)

    #calc total gas cost
    dailygas = gas_avg(people, days)
    gasSum = sum(dailygas)



    #print total food cost
    print("Overall, the cost of food for your trip is: ", foodsum)

    #print total gas cost
    print("Your gas total for the trip comes to: ", gasSum)
    

    #total trip cost
    total = foodsum + gasSum
    print("Altogether, the trip total comes to: ", total)

    #print cost per person
    foodpp = foodsum / people
    gaspp = gasSum / people
    costpp = foodpp + gaspp
    print("Therefore, the cost per person for the trip is: ", costpp)

#Execute program
main()    
    



#TEST CASES#
# Case #        People      Days        Food total          Gas total       Trip total          Cost per person    
#1              5           5           1500                475             1975                395
#2              10          3           2500                1000            3500                350
#3              3           10          5500                9642            15142               5047.33
