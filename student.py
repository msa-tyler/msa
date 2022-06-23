class Student:
    def __init__(self, fName, lName, major, year, gpa, id):
        self.fName = fName
        self.lName = lName
        self.major = major
        self.year = year
        self.gpa = gpa
        self.id = id 
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
    def getYear(self):
        return self.__year
    def getGpa(self):
        return self.__gpa      
    def getId(self):
        return self.__id
    
    #set functions

    def setfName(self, fName):
        self.__fName = fName
    def setlName(self, lName):
        self.__lName = lName
    def setMajor(self, major):
        self.__major = major
    def setYear(self, year):
        self.__year = year
    def setGpa(self, gpa):
        self.__gpa = gpa    
    def setId(self, id):
        self.__id = id