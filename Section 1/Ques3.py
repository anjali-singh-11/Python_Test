class Father:
    def property(self):
        print("Father's Method: property()")

    def business(self):
        print("Father's Method: business()")

class Son(Father):
    def study(self):
        print("Son's Method: study()")

class Daughter(Father):
    def dance(self):
        print("Daughter's method: dance()")

class GrandChild(Son, Daughter):
    def gaming(self):
        print("GrandChild's method: gaming()")        

obj = GrandChild()

print("  Calling all methods")
obj.property()
obj.business()
obj.study()
obj.dance()
obj.gaming()