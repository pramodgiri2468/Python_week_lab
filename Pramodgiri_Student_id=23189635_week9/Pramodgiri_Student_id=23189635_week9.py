class Vehicle:
    def init(self, make, model):
        self.make = make
        self.model = model
        self.state = "stopped"
    
    def move(self):
        print("I am moving!")
        self.state = "moving"

    def stop(self):
        print("I now stopped.")
        self.state = "stopped"

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def str(self):
        return f"{self.get_make()} {self.get_model()} is {self.get_state()}."


class Bus(Vehicle):
    def __init__(self, make, model, decks):
        Vehicle.init(self, make, model)
        self.decks_no = decks
        self.set_state("Not in use")
        self.route = ["New Street", "Bullring", "Moor Street", "BCU"]
        self.stop_index = 0

    def set_decks_no(self, deck):
        self.decks_no = deck

    def get_decks_no(self):
        return self.decks_no

    def get_route(self):
        return " - ".join(self.route)

    def move(self):
        if self.stop_index < len(self.route)-1:
            print(f"The bus was at {self.route[self.stop_index]} and is moving to {self.route[self.stop_index+1]}.")
            self.stop_index += 1
        else:
            print("I am finished for today!.")

    def stop(self):
        print("I am a non-stop bus.")


class Car(Vehicle):
    def init(self, make, model, doors):
        Vehicle.init(self, make, model)
        self.doors_no = doors

    def set_doors_no(self, number):
        self.doors_no = number

    def get_doors_no(self):
        return self.doors_no

    def str__(self):
        return f"{self.get_make()} {self.get_model()} with {self.get_doors_no()} doors is {self.get_state()}."


my_bus = Bus("TATA","New Delhi",6)
print(my_bus.get_route())
print(my_bus.get_state()) 
my_bus.stop() 
my_bus.move()
my_bus.move()
my_bus.move()
my_bus.move()

# Output
# New Street - Bullring - Moor Street - BCU
# Not in use
# I am a non-stop bus.
# The bus was at New Street and is moving to Bullring.
# The bus was at Bullring and is moving to Moor Street.
# The bus was at Moor Street and is moving to BCU.
# I am finished for today!.
