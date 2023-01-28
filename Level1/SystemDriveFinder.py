import os
#locate
class SystemDriverFinder:
    def __init__(self):
        pass
    def find_drives(self):
        print("This is the method of system drive finder class")
        drives=[]
        for x in range(65,91):
            if os.path.exists(chr(x)+":"):
                drives.append(chr(x))
        return drives

if __name__=='__main__':
    obj=SystemDriverFinder()
    print(obj.find_drives())

