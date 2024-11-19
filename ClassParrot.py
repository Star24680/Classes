class Parrot:
    Species="Bird"
    def __init__(self,Name,Age):
        self.Name=Name
        self.Age=Age
Macaw=Parrot("Macaw",10)
Toucan=Parrot("Touacn",5)
print("Macaw is a {}".format(Macaw.Species))
print("Toucan is a {}".format(Toucan.Species))
print("{} is {} years old".format(Macaw.Name,Macaw.Age))
print("{} is {} years old".format(Toucan.Name,Toucan.Age))
