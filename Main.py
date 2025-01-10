#### Stone Paper Scissors game by Micky Guha...

import random      ### Here we import random module so that a random value between 1, 0, -1 can be assigned to the variable Computer...
Computer=random.choice([1,2,3])  ## a random value between 1,0,-1 will be assigned to Computer.. 
print(f"{1} --> Stone \n{2} --> Paper\n{3} --> Scissors ")
Your_input=int (input("Enter your choice: "))  ## Taking input from user in integer form..
Values={1: "Stone", 2: "Paper", 3: "Scissors"}   ## We using dictionay to store the corresponding values of input
print(f"You choose {Values[Your_input]}")      ## Printing the corresponding value of your input
print(f"Computer's value: {Computer}")         ## Random value assisgned in Computer
print(f"Computer choose {Values[Computer]}")   ## Printing the corresponding value of Computer
if (Computer==Your_input):
    print(f"It's Draw") 
    print(f"Let's try again")                  ## Printing some random messages
    print(f"Good Luck!")                       ## Printing some random mesages

else:
    if(Computer == 1 and Your_input==2):     ## Computer --> Stone  VS  User --> Paper == User Win!
        print(f"You Win!")
        print(f"Let's try again")                  
        print(f"Good Luck!") 

    elif(Computer == 1 and Your_input==3):  ## Computer --> Stone  VS  User --> Scissors == User Lose!
        print(f"You Lose!")
        print(f"Let's try again")                  
        print(f"Good Luck!") 

    elif(Computer == 2 and Your_input==1):  ## Computer --> Paper  VS  User --> Stone == User Lose!
        print(f"You Lose!")
        print(f"Let's try again")                  
        print(f"Good Luck!") 
    
    elif(Computer == 2 and Your_input==3):  ## Computer --> Paper  VS  User --> Scissors == User Win!
        print(f"You Win!")
        print(f"Let's try again")                  
        print(f"Good Luck!") 

    elif(Computer == 3 and Your_input==1):  ## Computer --> Scissors  VS  User --> Stone == User Win!
        print(f"You Win!")
        print(f"Let's try again")                  
        print(f"Good Luck!") 


    elif(Computer == 3 and Your_input==2):  ## Computer --> Scissors  VS  User --> Stone == User Lose!
        print(f"You Lose!")
        print(f"Let's try again")                  
        print(f"Good Luck!") 
    else:
        print("Try again")
       