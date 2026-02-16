import time

class CoffeeMachine:
    """
    A class that represents a coffee machine, demonstrating abstraction.
    The user only interacts with high-level methods like 'make_espresso'.
    """

    def __init__(self):
        """Initializes the coffee machine."""
        print("Coffee machine is ready to brew.")
        # Any necessary setup or state variables would go here.

    # --- Encapsulated Low-Level Implementation Details ---
    # The underscore prefix is a convention for internal-use methods.
    def _heat_water(self):
        """Heats water to a specific temperature."""
        print("Heating water to 92°C...")
        time.sleep(2)

    def _grind_beans(self):
        """Grinds coffee beans based on a setting."""
        print("Grinding coffee beans...")
        time.sleep(2)

    def _brew_coffee(self):
        """Pushes water through the ground coffee."""
        print("Brewing coffee...")
        time.sleep(2)

    # --- Abstraction: The Clean, Public Interface ---
    # This is the main method the user should interact with.
    def make_espresso(self):
        """
        A single, clean function that abstracts the entire espresso-making process.
        """
        print("\n--- Making Espresso ---")
        self._heat_water()
        self._grind_beans()
        self._brew_coffee()
        print("Espresso is ready! Enjoy your coffee.")
        print("-----------------------\n")


# --- Main execution block to demonstrate the class ---
if __name__ == "__main__":
    # Create an instance of the coffee machine
    my_coffee_machine = CoffeeMachine()
    
    # Use the simple, abstract interface
    my_coffee_machine.make_espresso()

    # The user doesn't need to and shouldn't call the internal methods directly
    # my_coffee_machine._heat_water() # This would technically work but is not the intended use