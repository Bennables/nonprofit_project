def displayIntro():
    #put an Introduction message to the user
    print ("Welcome to Project 1")
    
    return

def displayNonProfits():
    a = 0
    b = 0
    c = 0
    loop = True
    array = ["1. World Central Kitchen", "2. Crisis Text Line", "3. Heart to Heart International", "4. Finish"]
    
    while loop == True:
        x = ( input (f'Which would you like to donate to? \n {array[0]}, \n {array[1]}, \n {array[2]}, \n {array[3]}\n '))

        
        if x == "1":
            y = int( input ("How much money would you like to donate?"))
            if y > 0:
                a = a + y
                print(f'World Central Kitchen: ${a}')
                print(f'Crisis Text Line ${b}')
                print(f'Heart to Heart International ${c}')
            else:
                print ("Please don't try stealing from our organizations")
        elif x == "2":
            y = int( input ("How much money would you like to donate?"))
            if y > 0:
                b = b + y
                print(f'World Central Kitchen: ${a}')
                print(f'Crisis Text Line ${b}')
                print(f'Heart to Heart International ${c}')
            else:
                print ("Please don't try stealing from our organizations")
        elif x == "3":
            y = int( input ("How much money would you like to donate?"))
            if y > 0:
                c = c + y
                print(f'World Central Kitchen: ${a}')
                print(f'Crisis Text Line ${b}')
                print(f'Heart to Heart International ${c}')
            else:
                print ("Please don't try stealing from our organizations")
        elif x == "4":
            print ("Thank You for your donations! (If you made any.)")
            loop = False
        else:
            print("Please pick a number.")

    
    
    
    #print all the non-profits to the screen numerically. For Example:
    # 1. World Central Kitchen  
    # 2. Crisis Text Line
    # 3. Heart to Heart Internationalreturn


def main():
    displayIntro()
    displayNonProfits()

	#steps: 
	#1. welcome the user using a unique Intro Message (use a function for this)
	#2. create a variable for each nonprofit/charity that keeps track of how much total money has been donated
	#3. display all the non-profits to the user and ask which one they would like to donate to 
	#4. then ask the user how much money they would like to donate to that specific charity chosen in step 3
	#5. update the variable created in step 2 with whatever amount the user wanted to donated
			#for example: missionbit = 0 -> user wants to donate 100 so you would add 100 to missionbit. missionbit is now 100
	#6. now display all the nonprofits with their new total amounts donated
	#7. repeat this pro 
main()