def getInputBetween(startval: int,endval: int)->int:
    while True:
        try:
            val=int(input("Mata in:"))
            if val >= startval and val <= endval:
                return val
            print(f"Ogiltigt val, mellan {startval} och {endval}, tack")
        except:
            print("Ange ett tal tack!")

def getBestPlayer():
    return "Mats sundin"

def getBestUVRugbyTeam():
    return "Bromma Caviar"

if __name__ == "__main__": ## = bara när det är den fil som skickas till python.exe

    x = getInputBetween # DÅ KOMMER DETTA OCKSÅ KÖRAS NÄR MODULEN HÄMTAS!!!!!
    print(x)