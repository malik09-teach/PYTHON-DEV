import time # Assuming time.sleep might be used if you add delays

# --- Define Parent Classes ---
class Music:
    def __init__(self, name, duration, artist):
        self.name = name
        self.duration = duration
        self.artist = artist
        print(f"Music initialized: {self.name} by {self.artist}")

class Publish:
    def __init__(self, guest, location):
        self.guest = guest
        self.location = location
        print(f"Publishing details initialized: {self.guest} at {self.location}")

# --- Corrected Concert Class ---
class Concert(Music, Publish): # Class names typically start with a capital letter
    # Class-level private attributes (conventionally, single underscore for internal use,
    # or consider making them instance attributes if they can vary per concert)
    __tickettot = 150      # Total tickets available for all concerts of this type
    __pertekprice = 3500   # Price per ticket

    def __init__(self, guest, location, name, duration, artist, tickets):
        # 1. Correctly initialize parent classes
        # When using multiple inheritance with distinct __init__ arguments,
        # calling parent constructors directly is often clearer than multiple super() calls.
        Music.__init__(self, name, duration, artist)
        Publish.__init__(self, guest, location)

        self.tickets = tickets # Tickets sold for this specific concert instance
        print(f"Concert '{self.name}' initialized with {self.tickets} tickets sold.")


    def amount_from_tickets(self):
        # Access private class attributes using self.__
        return (self.__tickettot - self.tickets) * self.__pertekprice

    def song_info(self):
        print("\n--- Info of Song ---")
        print("Song Name:", self.name)
        print("Artist:", self.artist)
        print("Duration:", self.duration, "min")
        print("--------------------")

    def infosofpub(self):
        print("\n--- Info of Concert Publishing ---")
        print("Location:", self.location)
        # Assuming guest is an iterable (like a list) for slicing
        print("The private guest list (reversed):", self.guest[::-1])
        print("----------------------------------")

    def overalldetail(self):
        print("\n--- Overall Concert Details ---")
        # 2. Add 'self.' when calling other methods of the same object
        self.song_info()
        self.infosofpub()
        
        # Access the amount_from_tickets method using self.
        total_amount = self.amount_from_tickets()
        print("Total amount generated from remaining tickets:", total_amount)
        print("-----------------------------\n")

# --- Calling through object ---
# Example: A concert for "Rock Anthem" by "Band X", 100 tickets sold,
#          with guests "VIPs" at "Stadium Arena"
obj = Concert(
    guest=["Alice", "Bob", "Charlie"], # Changed guest to a list for slicing
    location="Grand Stadium",
    name="Rock Anthem",
    duration=120,
    artist="The Pythoneers",
    tickets=100
)

# Now call the overall details method
obj.overalldetail()

# You can also call individual methods
# obj.song_info()
# obj.infosofpub()
# print(obj.amount_from_tickets())