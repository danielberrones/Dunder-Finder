import bs4, random

class DunderFinder:
    '''Find Dunders in BS4 module'''
    def __init__(self):
        self.dir = dir(bs4)

    def setData(self):
        myarr = []
        self.dunderMethodsInBS4 = [i for i in self.dir if i.startswith('__') or i.startswith('_')]
        for i in self.dunderMethodsInBS4:
            if i.startswith('__'):
                myarr.append(i)
            else:
                return i
                # print(i)

        print(myarr)
                
        # return self.dunderMethodsInBS4
        # return len(self.dunderMethodsInBS4)
        # return len(self.dir)

        
    
dun = DunderFinder()
print(dun.setData())
