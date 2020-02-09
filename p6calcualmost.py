#setup libraries
import time
import math

#declaring formula parameters

#for: ohm's law
VOhm = float
IOhm = float
ROhm = float

#for: kinematics law
aveV = float #V-Bar
s = float #distance
t = float #time
Vi = float #initial V
Vf = float #final V
a = float #acceleration

#for pythagoras
A = float
B = float
C = float
#function declarations

def evaluate(x):
    try:
        return eval(x)
    except:
        return "" 

#!!OHM'S LAW!!
def ohmsVoltage():
    VOhm = IOhm * ROhm
    print("You have a Voltage of: ", VOhm, "Volts\n")
    return;

def ohmsCurrent():
    IOhm = VOhm / ROhm
    print("You have a Current of: ", IOhm, "Amperes\n")
    return;

def ohmsResistance():
    ROhm = VOhm / IOhm
    print("You have a Resistance of: ", ROhm, "Ohms\n")
    return;

#!!KINEMATICS!!

#For Vi & Vf finding average velocity
def vAverage():
    aveV = (Vi + Vf)/2
    print("You have a Velocity of: ", aveV, "units\n")
    return;

def constVinitialV():
    Vi = (aveV * 2) - Vf
    print("You have a Initial Velocity of: ", Vi, "units\n")
    return;

def constVfinalV():
    Vf = (aveV * 2) - Vi
    print("You have a Final Velocity of: ", Vf, "units\n")
    return;

#for constant acc basic
def accBasic():
    a = (Vf - Vi)/t
    print("You have an acceleration of: ", a, "units\n")
    return;

def vFBasicAcc():
    Vf = (a*t) + Vi
    print("You have a final velocity of: ", Vf, "units\n")
    return;

def vIBasicAcc():
    Vi = ((a*t) - Vf) * -1
    print("You have an initial velocity of: ", Vi, "units\n")
    return;

def timeBasicAcc():
    t = (Vf - Vi)/a
    print("You have an time of: ", t, "units\n")
    return;

#for universal distance formula
def universalFormulaDistance():
    s = (Vi * t) + (0.5 *(a*(t*t)))
    print("You have a distance of: ", s, "units\n")
    return;

def universalFormulaVi():
    Vi = (s - (0.5 *(a*(t*t))))/t
    print("You have an initial velocity of: ", Vi, "units\n")
    return;

def universalFormulaA():
    a = (2 * (s - (Vi * t))) / (t*t)
    print("You have an acceleration of: ", a, "units\n")
    return;

#for distance w/ acceleration but no time
def DistanceSpecial():
    s = ((Vf * Vf) - (Vi * Vi))/(2*a)
    print("You have a distance of: ", s, "units\n")
    return;

def VfSpecial():
    Vf = math.sqrt((2 * a * s) + (Vi * Vi))
    print("You have a Final Velocity of: ", Vf, "units\n")
    return;

def ViSpecial():
    Vi = (math.sqrt((2 * a * s) + (Vf * Vf))) * -1
    print("You have an Initial Velocity of: ", Vi, "units\n")
    return;

def AccSpecial():
    a = ((Vf * Vf) - (Vi * Vi))/(2*s)
    print("You have an acceleration of: ", a, "units\n")
    return;

#!!!PYTHAGOREAN!!
def sideC():
    C = math.sqrt((A * A) + (B * B))
    print("Your triangle has a hypotenuse of: ", C)
    return;

def sideA():
    A = math.sqrt((C * C) - (B * B))
    print("Your triangle has a side A of: ", A)
    return;

def sideB():
    B = math.sqrt((C * C) - (A * A))
    print("Your triangle has a side B of: ", B)
    return;

username = "username"
password = "password"
calcChoice = ""

print("\n|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("|               LOGIN              |")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")

loginUser = input("Username: ")
loginPass = input("Password: ")

if(loginUser == username and loginPass == password):

    calcPrompt = 0
    while(calcPrompt >= 0):
    
        print("\n|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("| Welcome to my Physics Calculator |")
        print("|    Coded By: Lorenzo Ballada     |")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")

        time.sleep(0.5)

        print("Greetings ", username)
        print("What do you want to do? (type in letter of choice)")
        print("A. Ohm's Law\nB. Kinematics Equations\nC. Pythagorean Theorem")
        calcChoice = input("")

        #Actual Calculations

        #Note: "" existing (==) is the value to be solved for/unknown values
        #"" not existing (!=) are the inputted values
        
        #ohm's law
        if (calcChoice == "A"): 
            print("Leave input blank for the value you are looking for")
    
            time.sleep(0.5)
            
            VOhm = evaluate(input("Enter your Voltage: "))
            IOhm = evaluate(input("Enter your Current: "))
            ROhm = evaluate(input("Enter your Resistance: "))

            #Voltage
            if (VOhm == "") and (IOhm != "") and (ROhm != ""):
                print("\nSolving for V..")
                time.sleep(0.3)
                ohmsVoltage()

            #Current
            elif (VOhm != "") and (IOhm == "") and (ROhm != ""):
                print("\nSolving for I..")
                time.sleep(0.3)
                ohmsCurrent()

            #Resistance
            elif (VOhm != "") and (IOhm != "") and (ROhm == ""):
                print("\nSolving for R..")
                time.sleep(0.3)
                ohmsResistance()

            #Error Checkers
            elif (VOhm != "") and (IOhm != "") and (ROhm != ""):
                print("Error! Too much parameters")
            else:
                print("Invalid Input! Not enough parameters")
        #ohm's law end

        #kinematics equations
        if (calcChoice == "B"):
            print("Leave input blank for the value/s you are looking for or do not know")
            print("The program will automatically find out what value you're looking for\nbased on what values are and aren't given\n")
            aveV = evaluate(input("Enter your Average Velocity: "))
            s = evaluate(input("Enter your Distance: "))
            t = evaluate(input("Enter your Time: "))
            Vi = evaluate(input("Enter your Inital Velocity: "))
            Vf = evaluate(input("Enter your Final Velocity: "))
            a = evaluate(input("Enter your Acceleration: "))

            #For Vi & Vf finding average velocity
            if (aveV == "") and (Vi != "") and (Vf != ""):
                print("\nSolving for Average Velocity..")
                time.sleep(0.3)
                vAverage()

            elif (aveV != "") and (Vi == "") and (Vf != ""):
                print("\nSolving for Initial Velocity..")
                time.sleep(0.3)
                constVinitialV()

            elif (aveV != "") and (Vi != "") and (Vf == ""):
                print("\nSolving for Final Velocity..")
                time.sleep(0.3)
                constVfinalV()

            elif (aveV != "") and (Vi != "") and (Vf != ""):
                print("Error! Too much parameters")
                
            else:
                print("Invalid Input! Not enough parameters")

            #For solving constant acceleration
            if (a == "") and (Vi != "") and (Vf != "") and (t != ""):
                print("\nSolving for Acceleration..")
                time.sleep(0.3)
                accBasic()

            elif (a != "") and (Vi == "") and (Vf != "") and (t != ""):
                print("\nSolving for Intial velocity..")
                time.sleep(0.3)
                vIBasicAcc()

            elif (a != "") and (Vi != "") and (Vf == "") and (t != ""):
                print("\nSolving for Final velocity..")
                time.sleep(0.3)
                vFBasicAcc()

            elif (a != "") and (Vi != "") and (Vf != "") and (t == ""):
                print("\nSolving for Time..")
                time.sleep(0.3)
                timeBasicAcc()

            elif (a != "") and (Vi != "") and (Vf != "") and (t != ""):
                print("Error! Too much parameters")

            else:
                print("Invalid Input! Not enough parameters")

            #Universal distance formula
            if (s == "") and (Vi != "") and (t != "") and (a != ""):
                print("\nSolving for Distance..")
                time.sleep(0.3)
                universalFormulaDistance()

            elif (s != "") and (Vi == "") and (t != "") and (a != ""):
                print("\nSolving for Initial Velocity..")
                time.sleep(0.3)
                universalFormulaVi()

            elif (s != "") and (Vi != "") and (t != "") and (a == ""):
                print("\nSolving for Acceleration..")
                time.sleep(0.3)
                universalFormulaA()

            elif (s != "") and (Vi != "") and (t != "") and (a != ""):
                print("Error! Too much parameters")

            else:
                print("Invalid Input! Not enough parameters")

            #UniversalDistance with acceleration and no time
            if (s == "") and (Vf != "") and (Vi != "") and (a != ""):
                print("\nSolving for distance")
                time.sleep(0.3)
                DistanceSpecial()

            elif (s != "") and (Vf == "") and (Vi != "") and (a != ""):
                print("\nSolving for final velocity")
                time.sleep(0.3)
                VfSpecial()

            elif (s != "") and (Vf != "") and (Vi == "") and (a != ""):
                print("\nSolving for initial velocity")
                time.sleep(0.3)
                ViSpecial()

            elif (s != "") and (Vf != "") and (Vi != "") and (a == ""):
                print("\nSolving for acceleration")
                time.sleep(0.3)
                AccSpecial()

            elif (s != "") and (Vf != "") and (Vi != "") and (a != ""):
                print("Error! Too much parameters")

            else:
                print("Invalid Input! Not enough parameters")

            #!!END OF KINEMATICS!!

                
            time.sleep(0.5)

        #pythagoras
        if (calcChoice == "C"):
            print("Leave input blank for the value you are looking for")

            time.sleep(0.5)

            A = evaluate(input("Enter your Side A: "))
            B = evaluate(input("Enter your Side B: "))
            C = evaluate(input("Enter your Side C/Hypotenuse: "))

            if (A == "") and (B != "") and (C != ""):
                print("\nSolving for side A..")
                time.sleep(0.3)
                sideA()

            elif (A != "") and (B == "") and (C != ""):
                print("\nSolving for side B..")
                time.sleep(0.3)
                sideB()

            elif (A != "") and (B != "") and (C == ""):
                print("\nSolving for the hypotenuse..")
                time.sleep(0.3)
                sideC()

            elif (A != "") and (B != "") and (C != ""):
                print("Error! Too much parameters")
            
            else:
                print("Invalid Input! Not enough parameters")

        calcAgain = ""
        calcAgain = input("Calculate again? y/n\n")
        if calcAgain == "y":
            calcPrompt += 1
        elif calcAgain == "n":

            print("\n|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|  Thank You for using my Calculator  |")
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")
    
            break

else:

    print("\n|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("|            !!!ERROR!!!           |")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")
