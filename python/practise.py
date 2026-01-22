a ="1 2 3"
b = a.replace(" ", "-")
print(b)

a = lambda x,y: x*y

print(a(2,3))

class Dupa:
    def __init__(self,dupa, kupa):
        self.dupa=dupa
        self.kupa=kupa
        self.papa='papa'
    def pokaz_dupe(self):
        print("pokaz dupe  Dupa")

class Ryba(Dupa):
    def __init__(self,dupa,kupa,ryba):
        super().__init__(dupa, kupa)
        self.ryba=ryba
    def pokaz_dupe(self):
        super().pokaz_dupe()
        print("pokaz dupe Ryba")

    def pokaz_rybe(self):
        print("pokaz rybe Ryba")

a= Dupa("dupa1","kupa1")
b= Ryba("dupa2","kupa2","ryba2")
print(b.dupa)
print(b.kupa)
print(b.papa)
print(b.ryba)
b.pokaz_dupe()




