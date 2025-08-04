# Assignment 1 & 2: Designing a Class and Polymorphism Challenge

# -----------------------------------------------------------------------------
# Part 1: Design a Base Class and Inherit from It
# -----------------------------------------------------------------------------

# This is the base class for all characters. It's the "parent" class.
# It uses a constructor (__init__) to set initial values for each object created.
class Character:
    """
    This is the base class for all characters in our program.
    It demonstrates constructors and a common method to be overridden.
    """
    def __init__(self, name, alter_ego):
        """
        The constructor for the Character class. It is called when a new object
        is created and is responsible for initializing its attributes.
        It initializes the name and alter_ego attributes.
        """
        self.name = name
        self.alter_ego = alter_ego

    def display_info(self):
        """A method to display the character's core information."""
        return f"Name: {self.name}, Alter Ego: {self.alter_ego}"

    def perform_action(self):
        """
        A generic method that will be overridden by child classes.
        This is the core of our polymorphism demonstration. All child
        classes will have this method, but they will implement it differently.
        """
        return f"{self.name} is performing a generic action."

# The Superhero class inherits from the Character class.
# This means it automatically gets all the attributes and methods of Character.
class Superhero(Character):
    """
    This class inherits from Character and represents a superhero.
    It demonstrates inheritance and polymorphism.
    """
    def __init__(self, name, alter_ego, superpower):
        """
        The constructor for the Superhero class.
        The `super().__init__()` call is crucial here: it calls the parent class's
        constructor to initialize the 'name' and 'alter_ego' attributes,
        so we don't have to write that code again.
        """
        super().__init__(name, alter_ego)
        self.superpower = superpower

    def perform_action(self):
        """
        This method overrides the parent's `perform_action` method.
        This is how we show polymorphism. The same method name,
        but different behavior for the Superhero class.
        """
        return f"Aaaand... {self.name} is flying through the sky, using their {self.superpower} power!"

# The Supervillain class also inherits from the Character class.
# It further demonstrates inheritance by reusing the Character's base features.
class Supervillain(Character):
    """
    This class also inherits from Character and represents a supervillain.
    It further demonstrates polymorphism with its own version of the method.
    """
    def __init__(self, name, alter_ego, evil_plan):
        """
        The constructor for the Supervillain class.
        It also calls the parent class's constructor with `super()`.
        """
        super().__init__(name, alter_ego)
        self.evil_plan = evil_plan

    def perform_action(self):
        """
        This is another unique implementation of `perform_action`,
        demonstrating how polymorphism allows for varied behavior
        for a Supervillain object.
        """
        return f"Mwahaha! {self.name} is executing their evil plan: '{self.evil_plan}'"

# -----------------------------------------------------------------------------
# Part 2: Polymorphism in Action!
# -----------------------------------------------------------------------------

# Create a list of different objects (a Superhero and a Supervillain)
# that all share the same parent class.
characters = [
    Superhero("Captain Justice", "John Smith", "Invulnerability"),
    Supervillain("Dr. Chaos", "Dr. Emily Reed", "To turn the moon into cheese")
]

# Loop through the list and call the `perform_action` method on each object.
# The program automatically calls the correct, unique version of the method
# for each object, even though the call is identical. This is polymorphism.
print("--- Showtime! Watch our characters in action! ---")
for character in characters:
    print(character.perform_action())
    print("-" * 20)
