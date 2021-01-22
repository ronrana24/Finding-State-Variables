# Function for appending items in the list
def appendItemsInTheList(sv):
    for j in range(0, len(sv)):
        if j % 12 == 0:
            temp.append(sv[j])
        elif j % 12 == 1:
            mpa.append(sv[j])
        elif j % 12 == 2:
            vf.append(sv[j])
        elif j % 12 == 3:
            vg.append(sv[j])
        elif j % 12 == 4:
            uf.append(sv[j])
        elif j % 12 == 5:
            ug.append(sv[j])
        elif j % 12 == 6:
            hf.append(sv[j])
        elif j % 12 == 7:
            hg.append(sv[j])
        elif j % 12 == 8:
            hfg.append(sv[j])
        elif j % 12 == 9:
            sf.append(sv[j])
        elif j % 12 == 10:
            sg.append(sv[j])
        else:
            sfg.append(sv[j])
    sv.clear()
    pass


# To find the value of state variable
def findSV(mpa, y, closeIndex, x, compare):
    for i in range(0, len(mpa)):
        if y >= float(mpa[i]) and y <= float(mpa[i + 1]):
            if y - float(mpa[i]) >= float(mpa[i + 1]) - y:
                closeIndex = i + 1
            else:
                closeIndex = i
            break
        else:
            continue
    if compare:
        if x == 1:
            return temp[closeIndex]
        else:
            return temp[closeIndex] 
    else:
        print()
    if x == 1:
        print("Temperature(C):")
        print('T:', temp[closeIndex])
    else:
        print("Pressure(MPa):")
        print('P:', mpa[closeIndex])
    # Common print Values
    print("Volume(m^3/s):")
    print('vf:', vf[closeIndex], 'vg:', vg[closeIndex])
    print("Energy(KJ/kg):")
    print("uf:", uf[closeIndex], "ug:", ug[closeIndex])
    print("Enthalpy(KJ/kg):")
    print("hf:", hf[closeIndex], 'hg:', hg[closeIndex], 'hfg:', hfg[closeIndex])
    print("Entropy(KJ/kg K):")
    print("sf:", sf[closeIndex], 'sg:', sg[closeIndex], 'sfg:', sfg[closeIndex])
    pass

# File Handler
handle = open("saturated.txt")

# list of TEMPERATURE
temp = list()
# list of SATURATED PRESSURE
mpa = list()
# list of VOLUME OF SATURATED LIQUID
vf = list()
# list of VOLUME OF SATURATED VAPOUR
vg = list()
# list of ENERGY OF SATURATED LIQUID
uf = list()
# list of ENERGY OF SATURATED VAPOUR
ug = list()
# list of ENTHALPY OF SATURATED LIQUID
hf = list()
# list of ENTHALPY OF SATURATED VAPOUR
hg = list()
# list of ENTHAPLY DIFFERENCE
hfg = list()
# list of ENTROPY OF SATURATED liquid
sf = list()
# list of ENTROPY OF SATURATED vapour
sg = list()
# list of ENTROPY DIFFERENCE
sfg = list()

# REFERENCE LIST
l = []
# REFERENCE LIST FOR SATURATION VARIABLE
sv = []
# list of all the SUPERHEATED VALUES--> i.e. mpa
superlist = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.18, 0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60 ,0.65, 0.70, 0.75, 0.80, 0.9, 1.00, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.8, 2.0, 2.2 ,2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 22.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]

for line in handle:
    l.append(line)
    pass
# l[1] = "SATURATION LINE BASE": TEMPERATURE"
# l[2] = "Saturation Line Base: PRESSURE"

# An Empty String
s = ""
# A reference variable
closeIndex = 0

# WHAT DO YOU WANT TO FIND
q = True
while q:
    x = int(input(
        "What do you want to find type only 1 or 2\n1) SATURATION LINE BASE: TEMPERATURE\n2) SATURATION LINE "
        "BASE: PRESSURE\n"))
    if x == 1 or x == 2:
        # Boolean variable to show that actual value is equal to value given in saturation
        compare = False
        if x == 1:
            for i in l[0]:
                if i == " " or i == "\n":
                    sv.append(s)
                    s = ""
                else:
                    s += i
            # Appending values to their LIST
            appendItemsInTheList(sv)
            MPa = float(input("Enter any value of SATURATED PRESSURE(MPa)--> "))
            # Asking for actual temperature value
            show = input("Do you want to input your actual Temperature Value\nType YES or NO--> ")
            if 'y' in show.lower():
                compare = True
                actualValue = float(input("Enter Actual value Here--> "))
                # to find your desired properties
                x = float(findSV(mpa, MPa, closeIndex, x, compare))
                print(x)
                if actualValue > x:
                    # We will look up in superheated table
                    print("Look up in superHeated table")
                    for i in range(len(superlist)-1):
                        if actualValue >= superlist[i] and actualValue <= superlist[i+1]:
                            if actualValue - superlist[i] >= superlist[i+1] - actualValue:
                                a = i+1
                            else:
                                a = i
                            break
                        else:
                            continue
                    print(a)
                elif x == actualValue:
                    compare = False
                    findSV(mpa, MPa, closeIndex, x, compare)
                else:
                    print("You have given low value of Actual Temperature")
            else:
                findSV(mpa, MPa, closeIndex, x, compare)
        else:
            for i in l[1]:
                if i == " " or i == "\n":
                    sv.append(s)
                    s = ""
                else:
                    s += i
            # Appending values to their LIST
            appendItemsInTheList(sv)
            Tsat = float(input("Enter any value of SATURATED TEMPERATURE(Tsat)--> "))  # mpa --> temp and temp --> mpa
            findSV(mpa, MPa, closeIndex, x)
        q = input("DO YOU WANT TO QUIT? TYPE t--> ")
        if q == 't':
            q = False
            pass
    else:
        print("Try putting 1 or 2")
print("Thank You")
