#! /usr/bin/env python

#Create DFA Class
class DFA:

    #Set Current State To Nothing
    currState = None;

    #Initialize DFA Object With (State, Alphabet, Transition Function, Start State, and Accept State) Values Passed In, Then Return
    def __init__(self, states, alphabet, transFunction, startState, accStates):
        self.states = states;
        self.alphabet = alphabet;
        self.transFunction = transFunction;
        self.startState = startState;
        self.accStates = accStates;
        self.currState = startState;
        return;

    #Given An Input List, Start Execution In Initial State, Transition On Each Line Given In File, Then Accept If Ends In Accept State
    def processInput(self, inList):
        self.initialState();
        for inp in inList:
            self.stateTrans(inp);
            continue;
        return self.acceptState();
    pass;

    #Intitialization State So Execution Begins At Start State
    def initialState(self):
        self.currState = self.startState;
        return;

    #Transition Function To Transition From One One State To Next With Given Input
    def stateTrans(self, inValue):
        if ((self.currState, inValue) not in self.transFunction.keys()):
            self.currState = None;
            return;
        self.currState = self.transFunction[(self.currState, inValue)];
        return;

    #Accept State Method Which Returns True If DFA Ends In Accept State
    def acceptState(self):
        return self.currState in accStates;


#Declare States, Alphabet, And Other Necessary Variables: Dictionary Key/Value To Hold States And Transitions, Temportary Dictionary To Count Number Of Similar Transtiions, Accept States Array, Machine Type Initialization
states = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255}
alphabet = {'\s', '`','!','\"','#','$','%','&','\'','(',')','{','|','}','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[','\\',']','^','_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}

#Dictionary Key/Value Pairs To Hold States and Transitions, Temporary Dictionary To Count Number Of Similar Transitions
#State List To Get And Count Unique Number Of States, Accept States List To Hold Accept States, Alphabet List To Hold Alphabet
#Declare Machine Type As Nothing Until Set, Set Start State and Counter To 0
tf = dict()
tempDictOne = {}
stateList = []
accStates = []
alpha = []
machType = None
startState = 0
count = 0


#Open Machine File, Read In Line By LIne
with open("m30.fa", 'r')as f: 
    lines = f.readlines()
    #Strip Lines Of Commas, Extra Characters
    for line in lines:
        line = line.strip()
        newline = line.split(",")
        if not line:
            continue
        elif line.startswith("{"):
            stripline = line.strip("{}")
            #Check If There Are Accept States, If So, Split Them By Comma Delimeter, If Not Set Accept To Trap State Set
            if stripline != '':
                stripline = map(int, stripline.split(','))
                accStates = set(stripline)
            else:
                stripline = map(int, {255, 255, 255})
                accStates = set(stripline)
        else:
            #Check If Transition Rules Are Within Range, Check If Any Epsilon Transitions
            if int(newline[0]) in states and int(newline[2]) in states:
                #Check For Empty Transition
                if newline[1] == '`':
                    epschar = 1
                else:
                    epschar = 0
                #Put Valid Transitions Into Dictionary To Check if Any Rules Are Duplicated, Put Alphabet Into Array
                alpha.append(newline[1])
                tf[(int(newline[0]), newline[1])] = int(newline[2])
                tempDictOne.setdefault(((int(newline[0]), newline[1])), []).append(int(newline[2]))
                stateList.append(str(newline[0]))
                stateList.append(str(newline[2]))

                


#Find Length Of Value Lists Of Key Value Pairs, If Any Key Has Value List Of More Than 1 Then Machine Is NFA
lengths = [len(v) for v in tempDictOne.values()]

#Convert State/Alphabet List To Set, Which Keeps Only Unique Values Of The List
stateList2 = set(stateList)
alphabet2 = set(alpha)

#Convert Alphabet Back To List To Be Sorted Later
alphabet2 = sorted(alphabet2, key=str.swapcase)
alphabet2 = list(alphabet2)

if '`' in alphabet2:
    alphabet2.remove('`')

#Classify The Machine Based On Number Of Similar Transitions and Epsilon Transitions
for i in lengths:
    if i > 1 or epschar == 1:
        machType = "NFA"
        break
    else: 
        machType = "DFA"

#Set DFA With Initial Values, Open Input File For Reading, Open Outut Files For Writing
dfa = DFA(states, alphabet, tf, startState, accStates)
input_file = open('input.txt', 'r')
output2 = open('results/m30.log', 'w')

if machType == "DFA":
    #Only Open 'basename.txt' If Machine is a DFA
    output = open('results/m30.txt', 'w')

    #Loop Over Input File, Print Accepted Strings To 'basename.txt' File
    for line in input_file:
        line = line.strip()
        inLine = list(line)
        if dfa.processInput(inLine) == True:
            output.write(line + "\n")
            count = count + 1
    output.close()

    #Output Necessary Information To 'basename.log' File
    output2.write("Valid: " + machType + "\n")
    output2.write("States: " + str(len(stateList2)) + "\n")
    output2.write("Alphabet: " + ''.join(map(str, alphabet2)))
    output2.write("\n")
    output2.write("Accepted Strings: " + str(count) +"/10297" + "\n")
    output2.close()

elif machType == "NFA":
    output2.write("Valid: " + machType + "\n")
    output2.write("States: " + str(len(stateList2)) + "\n")
    output2.write("Alphabet: " + ''.join(map(str, alphabet2)))
    output2.write("\n");
    output2.write("Accepted Strings: " + "0/0" + "\n")
    output2.close()
