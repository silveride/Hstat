# House model


class CHouse:
    # Initialisation
    def __init__(self):
        pass;

    # Setters
    def setName(self,name):
        self.name = name

    def setAddress(self,address):
        self.address = address

    def setNumBedrooms(self,nBedrooms):
        self.num_bedrooms = nBedrooms

    def setBedrooms(self,bedrooms):
        self.bedrooms = bedrooms;

    def setArea(self,area):
        self.area = area

    # Getters
    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getNumBedrooms(self):
        return self.nBedrooms

    def getBedrooms(self):
        return self.bedrooms;

    def getArea(self):
        return self.area

    # DB Initialisation

# Unit Test Area

class CTestHouse :
    def testName(self,house,iname):
        house.setName(iname)
        if house.getName() == iname:
            print("pass")


if  __name__ == "__main__":
    print("Test Starting: CHouse")
    thouse = CTestHouse()
    house = CHouse()
    thouse.testName(house,"Test")
