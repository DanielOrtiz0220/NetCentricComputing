import socket


class Assignment2:
    def __init__(self, year):
        self.year = year

    def tellAge(self, currentYear):
        age = self.year - currentYear
        print(f"Your age is {currentYear}")

    def listAnniversaries(self):
        currentYear = 2022
        difference = currentYear - self.year
        decades = int(difference / 10)

        list = []

        for y in range(1, decades+1):
            list.append(y*10)

        return list

    def modifyYear(self, n):
        stringYearFull = str(self.year)

        modifiedYear = self.year * n
        stringYearModified = str(modifiedYear)

        stringYearShort = stringYearFull[0:2]*n

        for i in range(len(stringYearFull)):
            if (i % 2 == 0):
                stringYearShort += str(modifiedYear)[i]

        return stringYearShort

    @staticmethod
    def checkGoodString(string):
        goodString = False

        if (len(string) >= 9 and string[0].islower):
            for i in range(len(string)):
                if (string[i].isdigit()):
                    if goodString == True:
                        return False
                    goodString = True

        return goodString

    @staticmethod
    def connectTcp(host, port):
        connectedBool = False

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client.connect((host, port))
            print("it works")
            connectedBool = True

        except socket.error as e:
            print(f"Connection failed: {e}")
        client.close()

        return connectedBool
