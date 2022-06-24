class Student:
    def __init__(self, fName, lName, major, creditHours, gpa, id):
        self.__fName = fName
        self.__lName = lName
        self.__major = major
        self.__creditHours = creditHours
        self.__gpa = gpa
        self.__id = id 
        #first name
        #last name
        #major
        #year (freshman, soph, etc)
        #gpa

    # get functions

    def getfName(self):
        return self.__fName
    def getlName(self):
        return self.__lName
    def getMajor(self):
        return self.__major
    def getCreditHours(self):
        return self.__creditHours
    def getGpa(self):
        return self.__gpa      
    def getId(self):
        return self.__id
    
    #set functions

    def setfName(self, newFName):
        self.__fName = newFName
    def setlName(self, newLName):
        self.__lName = newLName
    def setMajor(self, newMajor):
        self.__major = newMajor
    def setCreditHours(self, newCredits):
        self.__creditHours = newCredits
    def setGpa(self, newGpa):
        self.__gpa = newGpa    
    def setId(self, newId):
        self.__id = newId

    #find the class level dependent on credit hours
    def getClassLevel(self):
        if 0<self.__creditHours<30:
            return "Freshman"
        elif 31<self.__creditHours<60:
            return "Sophomore"
        elif 61<self.__creditHours<90:
            return "Junior"
        elif self.__creditHours > 90:
            return "Senior"

    def updateCreditHours(self, newCredits):
        self.__creditHours += newCredits

         