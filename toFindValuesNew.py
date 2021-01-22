# !-- Function --!
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

# function to find values of state variables
def findSV(var, x, mpa):
    closeIndex = compare(mpa, var)
    if x == 1:
        print("Temperature(C):")
        print('T:', temp[closeIndex])
    else:
        print("Pressure(MPa):")
        print('P:', temp[closeIndex])
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

# function of adding superheated value in there respective list
def addvalues(sv):
    temp.clear()
    vf.clear()
    hf.clear()
    sf.clear()
    uf.clear()
    for i in range(len(sv)):
        if i % 5 == 0 :
            temp.append(sv[i])
        elif i % 5 == 1 :
            vf.append(sv[i])
        elif i % 5 == 2:
            uf.append(sv[i])
        elif i % 5 == 3:
            hf.append(sv[i])
        else:
            sf.append(sv[i]) 

#Function to compare two state variables
def compare(commonList, w):
    if w == 0:
        return 0
    else:
        for i in range(len(commonList)-1):
            if w >= float(commonList[i]) and w <= float(commonList[i + 1]):
                if w - float(commonList[i]) >= float(commonList[i + 1]) - w:
                    closeIndex = i + 1
                else:
                    closeIndex = i
                break
            else:
                continue
        return closeIndex
    pass 

# function to search index
def searchIndex(commonList, w):
    i = compare(commonList, w)
    print()
    if temp[i] == temp[i+1]:
        # LIQUID PHASE
        print("FOR LIQUID PHASE")
        print("Temperature T(C): ", temp[i])
        print("Specific VOlume v(m^3/kg): ", vf[i])
        print("Specific Energy u(kJ/kg): ", uf[i])
        print("Specific Enthaply h(kJ/kg): ", hf[i])
        print("Specific Entropy s(kJ/kg K): ", sf[i])
        print("--------------------------------")
        # VAPOUR PHASE
        print("FOR VAPOUR PHASE")
        print("Temperature T(C): ", temp[i+1])
        print("Specific VOlume v(m^3/kg): ", vf[i+1])
        print("Specific Energy u(kJ/kg): ", uf[i+1])
        print("Specific Enthaply h(kJ/kg): ", hf[i+1])
        print("Specific Entropy s(kJ/kg K): ", sf[i+1])
    else:
        print("Temperature T(C): ", temp[i])
        print("Specific VOlume v(m^3/kg): ", vf[i])
        print("Specific Energy u(kJ/kg): ", uf[i])
        print("Specific Enthaply h(kJ/kg): ", hf[i])
        print("Specific Entropy s(kJ/kg K): ", sf[i])
    temp.clear()
    vf.clear()
    hf.clear()
    sf.clear()
    uf.clear()
    pass

# function to show the supeheated value of state variables
def superheatedValue(superIndex, sl, v):
    # Empty string
    z = ""
    for i in sl[superIndex]:
        if i == "\n" or i == " ":
            sv.append(z)
            z = ""
        else:
            z += i
    addvalues(sv)
    if v == '1':
        w = float(input("Enter T(C) value --> "))
        searchIndex(temp, w)
    elif v == '2':
        w = float(input("Enter v(m^3/kg) value --> "))
        searchIndex(vf, w)
    elif v == '3':
        w = float(input("Enter u(kJ/kg) value --> "))
        searchIndex(uf, w)
    elif v == '4':
        w = float(input("Enter h(kJ/kg) value --> "))
        searchIndex(hf, w)
    else:
        w = float(input("Enter s(kJ/kg K) value --> "))
        searchIndex(sf, w)
    
    sv.clear()
    pass
# !---- FUNCTION ENDS ----!

# !-- LIST OF ALL VARIABLES --!
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
#!---- LIST ENDS ------!

# !-- MAIN CODE --!
# file handle for file saturated.txt
handle = open("saturated.txt")
# list of all the SUPERHEATED VALUES--> i.e. mpa
superlist = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.18, 0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.9, 1.00, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.8, 2.0, 2.2, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 22.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]

# appending files lines in a reference list
l = []
for line in handle:
    l.append(line)
    pass

# l[0] = "SATURATION LINE BASE": TEMPERATURE"
# l[1] = "Saturation Line Base: PRESSURE"

# file handle for file superheated.txt
fhandle = open("superheated.txt")

# appending files lines in a reference list for superHeated table
sl = [] # Reference list of superheated table
for line in fhandle:
    sl.append(line)
    pass
# Empty String GLobal Declare
s = ""

# sv --> state variable list i.e Reference List for variables
sv = []

q = True
try:
    while q:
        # input of options
        print()
        x = int(input("Which steam table would you like to access? TYPE 1 or 2 or 3\n1) SATURATION LINE BASE: TEMPERATURE\n2) SATURATION LINE BASE: PRESSURE\n3) WATER(SUBCOOLED) / STEAM(SUPERHEATED)\n--> "))
        # Checking if x == 1 or x == 2 or x == 3 
        if x == 1 or x == 2 or x == 3:
            # x == 1 means --> SATURATION LINE BASE: TEMPERATURE
            if x == 1:
                # appending SATURATION LINE BASE: TEMPERATURE in sv i.e. sv.append(l[0]) in the form of String
                for i in l[0]:
                    if i == " " or i == "\n":
                        sv.append(s)
                        s = ""
                    else:
                        s += i
                # Appending values to their LIST
                appendItemsInTheList(sv)
                # MPa variable
                MPa = float(input("Enter any value of SATURATION PRESSURE(MPa)--> "))
                findSV(MPa, x, mpa)
            elif x == 2:
                # temp list will store mpa values and mpa list will store temp value
                # x == 2 means --> SATURATION LINE BASE: PRESSURE
                # appending SATURATION LINE BASE: TEMPERATURE in sv i.e. sv.append(l[1]) in the form of String
                for i in l[1]:
                    if i == " " or i == "\n":
                        sv.append(s)
                        s = ""
                    else:
                        s += i
                # Appending values to their LIST
                appendItemsInTheList(sv)
                # MPa variable
                Tsat = float(input("Enter any value of SATURATION TEMPERATURE(Tsat)--> "))
                findSV(Tsat, x, mpa)
            else :
                Psat = float(input("Enter any value of SATURATION PRESSURE(MPa)--> "))
                v = input(
                    "Enter 1, 2, 3, 4 or 5 for their respective values\n1) T(C)\t 2) v(m^3/kg)\t 3) u(kJ/kg)\t 4) h(kJ/kg)\t 5) s(kJ/kg K)\n--> ")
                superIndex = compare(superlist, Psat)
                superheatedValue(superIndex, sl, v)
            q = input("Do you want to quit? Type YES/NO--> ")
            if 'yes' in q.lower():
                q = False
        else:
            print("You are only required to type :- 1, 2 or 3")
except:
    print("You must have entered a string, character or an out of bound input.")
print()
print("Thank You!")
#!--------- MAIN CODE ENDS ----------!
