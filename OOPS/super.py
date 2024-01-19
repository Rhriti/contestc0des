class Parent:
    def show(self):
        print("Parent's show method")

class Child(Parent):
    def show(self):
        super().show()  # Call the show method of the superclass
        print("Child's show method")

#
child = Child()
child.show()
