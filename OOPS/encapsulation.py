class Person:
    def __init__(self, name, age):
        self.name = name              # Public attribute
        self._age = age               # Protected attribute
        self.__contact = None         # Private attribute

    def update_contact(self, new_contact):
        self.__contact = new_contact

    def get_contact(self):
        return self.__contact

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Contact: {self.__contact}")


person = Person("Alice", 30)

# Accessing public attributes
print(person.name)  # Output: Alice

# Accessing protected attribute (convention, not enforced)
print(person._age)  # Output: 30
person.update_contact("1234567890")
print(person._Person__contact)

# Displaying details using the method
person.display_details()
