import webbrowser
from time import sleep

print(" F = M x A")
sleep(2)
webbrowser.open_new_tab("https://s-media-cache-ak0.pinimg.com/564x/86/df/48/86df483e67d61ea9c6dd627ffaef56d0.jpg")
sleep(4)

menu=input("What would you like to find: Force, Acceleration or Mass??")

menu = menu.lower() #string functions

if menu == "Force" or menu == "force":
    mass=(float(input("Please enter your given Mass.. (in kg)")))
    accel=(float(input("Please enter your given Acceleration... (in m/s^2)")))
    answer1 = mass*accel
    answer1 = (str(answer1))
    print(answer1)

elif menu == "Accelerstion" or menu == "acceleration":
    mass2=(float(input("Please enter your given Mass.. (in kg)")))
    force=(float(input("Please enter your given Force... (in Newtons)")))
    answer2 = mass2/force
    answer2 = (str(answer2))
    print(answer2)

elif menu == "Mass" or menu == "mass":
    force2=(float(input("Please enter your given Force.. (In Newtons) ")))
    accel2=(float(input("Please enter your given Acceleration... (In m/s^2)")))
    answer3 = force2/accel2
    answer3 = (str(answer3))
    print(answer3)



