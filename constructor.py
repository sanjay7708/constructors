class Sanjay:
    def __init__(self,array):
        self.array=array
    def sort(self):
        counter=0
        for i in range(len(self.array)):
            if self.array[i]=='a':
                counter+=1
        print(counter)
obj=Sanjay("sanjay")
obj.sort()