import random
import os

def getName():
    bank = ['en','po','fu','der','call','ick','duo','up','at','el','kar','tuk','da']
    name = ''
    for i in range(3):
        name += bank[random.randint(0,len(bank)-1)]
    return name

class Character:
    def __init__(self,name):
        self.name = name
        self.health = 100

    def show(self):
        print(f'''Name: {self.name}
Type: {self.typ}
Health: {self.health}
Power: {self.power}
Special Attack Power: {self.sap}
Speed: {self.speed}''')

class Barbarian(Character):
    def __init__(self,name):
        super().__init__(name)
        self.typ = 'B'
        self.power = 70
        self.sap = 20
        self.speed = 50

class Elf(Character):
    def __init__(self,name):
        super().__init__(name)
        self.typ = 'E'
        self.power = 30
        self.sap = 60
        self.speed = 10

class Wizard(Character):
    def __init__(self,name):
        super().__init__(name)
        self.typ = 'W'
        self.power = 50
        self.sap = 70
        self.speed = 30
    
class Dragon(Character):
    def __init__(self,name):
        super().__init__(name)
        self.typ = 'D'
        self.power = 90
        self.sap = 40
        self.speed = 50

class Knight(Character):
    def __init__(self,name):
        super().__init__(name)
        self.typ = 'K'
        self.power = 60
        self.sap = 10
        self.speed = 60

def newCharacter():
    choice = random.randint(0,4)
    if choice == 0:
        c = Barbarian(getName())
    elif choice == 1:
        c = Elf(getName())
    elif choice == 2:
        c = Wizard(getName())
    elif choice == 3:
        c = Dragon(getName())
    else:
        c = Knight(getName())
    return c

def buildCharacter(data):
    data = data.split(',')
    c = Character(data[0])
    c.typ = data[1]
    c.health = int(data[2])
    c.power = int(data[3])
    c.sap = int(data[4])
    c.speed = int(data[5])
    return c

def Menu():
    team = []
    cont = True
    while cont:
        print('''\n- - - - - - - - - - - - - - - -
WELCOME TO PLANET OF FIGHTCRAFT
- - - - - - - - - - - - - - - -
Select an option by entering the corresponding number:
(1) View Team
(2) Add Characters to Team
(3) Delete Characters from Team
(4) Edit Character Stats
(5) Save Team to File
(6) Load Team from File
(7) Quit\n''')
        validSelection = False
        while not validSelection:
            try:
                selection = int(input('>>> '))
                validSelection = True
            except TypeError or selection < 1 or selection > 7:
                print('Invalid input. Please try again.\n')
        if selection == 7:
            cont = False
        elif selection == 1:
            if len(team) == 0:
                print('Your team is currently empty! Add some characters to it!')
            else:
                for i,v in enumerate(team):
                    print('Character ' + str(i+1))
                    v.show()
                    print('\n')
        elif selection == 2:
            try:
                qty = int(input('How many characters do you want to add?\n>>> '))
            except:
                qty = 0
            for i in range(qty):
                team.append(newCharacter())
            print(f"{qty} new characters successfully added.")
        elif selection == 3:
            for i,v in enumerate(team):
                print('Character ' + str(i+1))
                v.show()
                print('\n')
            validDeletion= False
            while not validDeletion:
                try:
                    toDelete = ('Select the number of the character you want to delete:\n>>>')
                    validDeletion = True
                except TypeError or toDelete < 1 or toDelete > len(team):
                    print('Invalid input. Please try again.\n')
            print('\n' + team[toDelete-1].show())
            confirm = input('Are you sure you want to delete this character? (Y/N)')
            if confirm == 'Y' or confirm == 'y' or confirm == 'yes' or confirm == 'YES' or confirm == 'Yes':
                team.pop(toDelete-1)
                print('Successfully deleted character.')
            else:
                print('Aborting character deletion...')
        elif selection == 4:
            if len(team) == 0:
                print('Your team is currently empty! Add some characters to it!')
            else:
                for i,v in enumerate(team):
                    print('Character ' + str(i+1))
                    v.show()
                    print('\n')
                validEditing= False
                while not validEditing:
                    try:
                        toEdit = int(input('Select the number of the character you want to edit the stats of:\n>>> '))
                        if toEdit > 0 and toEdit <= len(team):
                            validEditing = True
                        else:
                            print('Invalid input. Please try again.\n')
                    except TypeError:
                        print('Invalid input. Please try again.\n')
                print(team[toEdit-1].show())
                stats = ['health','type','name','power','special attack power','sap','speed','hp','typ']
                validStat= False
                while not validStat:
                    try:
                        stat = input('Enter which stat you would like to change (name/type/health/power/special attack power/speed):\n>>> ')
                        if (stat.lower() in stats):
                            validStat = True
                        else:
                            print('Invalid input. Please try again.\n')
                    except TypeError:
                        print('Invalid input. Please try again.\n')
                if stat == 'name':
                    newName = input('Enter new name for character:\n>>> ')
                    team[toEdit-1].name = newName
                elif stat == 'type':
                    validType = False
                    types = ['B','E','W','D','K']
                    while not validType:
                        try:
                            typ = input('Select the new type for the character (B/E/W/D/K):\n>>> ')
                            if (typ.upper() in types):
                                validType = True
                            else:
                                print('Invalid input. Please try again.\n')
                        except TypeError:
                            print('Invalid input. Please try again.\n')
                    team[toEdit-1].typ = typ
                else:
                    validValue = False
                    while not validValue:
                        try:
                            value = int(input('Enter new value: \n>>> '))
                            validValue = True
                        except TypeError or value < 0 or value > 100:
                            print('Invalid input. Please try again.\n')
                    if stat == 'health' or stat == 'hp':
                        team[toEdit-1].health = value
                        print('done')
                    elif stat == 'power':
                        team[toEdit-1].power = value
                    elif stat == 'special attack power' or stat == 'sap':
                        team[toEdit-1].sap = value
                    elif stat == 'speed':
                        team[toEdit-1].speed = value
                print('Successfully edited character stats!')
        elif selection == 5:
            if len(team) == 0:
                print('Your team is currently empty! Add some characters to it!')
            else:
                teamName = input('Enter name of team:\n>>> ')
                file = teamName + '.txt'
                f = open(file,'w')
                for x in team:
                    line = x.name + ',' + x.typ + ',' + str(x.health) + ',' + str(x.power) + ',' + str(x.sap) + ',' + str(x.speed) + '\n'
                    f.write(line)
                f.close()
                print('Team successfully saved!')
        elif selection == 6:
            teamName = input('Enter name of team to load from file:\n>>> ')
            file = teamName + '.txt'
            if os.path.isfile('C:/Users/nesud/OneDrive/Documents/bridgingTasks/' + file):
                f = open(file,'r')
                data = f.read()
                f.close()
                team = []
                data = data.split('\n')
                if '' in data:
                    data.remove('')
                for d in data:
                    team.append(buildCharacter(d))
            else:
                print('Team not found. Aborting team load from save...')
    quit()

Menu()
