class Parameter:
    dlParam = []
    icount = 0
    def __init__(self):
        pass
    
    def AddParam(self, strMenuID, strMenuName, strID=100):
        rec = {'MenuID':strMenuID, 'MenuName':strMenuName, 'ID':strID}
        print(rec, type(rec))
        self.dlParam.append(rec)
        
    def printRec(self):
        print(self.dlParam) 

    
d = {'a':1, 'b':2, 'c':3}
d1 = {1:1, 2:2, 3:3}
d2 = {4:4, 5:5, 6:6}
dl = [d, d1]
dl.append(d2)
de = {}
print (d)
print (d1)
print (d2)
print (dl)
print (de)

p1 = Parameter
p1.AddParam(p1, 'P1.1', 'Menu1', '101')
p1.AddParam(p1, 'P1.2', 'Menu2', 102)

p1.printRec(p1)

