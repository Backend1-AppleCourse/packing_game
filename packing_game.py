# ● we are simulating a packing game.
# ● in the game we have the following items and properties (see
# appendix A)
# ● you can pack a max total of 80 weight units, and max of 6
# items.
# ● support add/remove functionality. The user via the cli can add
# or remove one of the objects from the bag, if the weight limit or
# the item limit is not surpassed.
# ● use OOP to categories and create the items. use inheritance
# when possible.
# ● add print all items of the bag
# ● add print all items, separated by category.
# ● add print item only from category X

# items in Appendix A should be Object Oriented Programming

# Appendix A
# ○ Passport: Color: blue, weight: 1, cost: 50, boughtFrom: USA

# ○ sunglasses: haveCase: yes, color: black, origin: italy, weight: 10

# ○ sneakers: brand: New Balance, new: false, bought from: Spain, weight: 14

# ○ universal charger: Color: black, price: 50, Size: Medium, Brand: Lenovo, weight: 12
# ○ Smartphone: Brand: Apple Operating, System: iOS, Storage: 128 GB, Display: AMOLED, Camera: Dual Lens,  materials: lithium, plastic
# ○ Laptop: Brand: Dell, Processor: Intel i7, RAM: 16 GB, Storage: 512 GB SSD, Graphics: NVIDIA GeForce4, weight: 60
# ○ Smartwatch: Brand: Samsung, Display: Touchscreen, Battery Life: 3 days, Fitness Features: Heart Rate Monitor, Connectivity: Bluetooth, weight: 44
# ○ campus, Brand: Samsung, accuracy: high, price: 50, materials: iron, plastic, weight: 4


class Item:
    def __init__(self, weight):
        self.weight = weight

    def __str__(self):
        return f"Weight: {self.weight}"

class Brand(Item):
    def __init__(self, weight, brand):
        super().__init__(weight)
        self.brand = brand

    def __str__(self):
        return f"Weight: {self.weight}, Brand: {self.brand}"

class Electrical(Brand):
    def __init__(self, weight, brand, color, price, size):
        super().__init__(weight, brand)
        self.color = color
        self.price = price
        self.size = size

    def __str__(self):
        return f"Weight: {self.weight}, Brand: {self.brand}, Color: {self.color}, Price: {self.price}, Size: {self.size}"

class Device(Brand):
    def __init__(self, weight, brand, storage):
        super().__init__(weight, brand)
        self.storage = storage

    def __str__(self):
        return f"Weight: {self.weight}, Brand: {self.brand}, Storage: {self.storage}"

class Passport(Item):
    def __init__(self, weight, color, cost, boughtFrom):
        super().__init__(weight)
        self.color = color
        self.cost = cost
        self.boughtFrom = boughtFrom

    def __str__(self):
        return f"Weight: {self.weight}, Color: {self.color}, Cost: {self.cost}, Bought From: {self.boughtFrom}"

class Product(Brand):
    def __init__(self, weight, brand, color, origin, haveCase):
        super().__init__(weight, brand)
        self.color = color
        self.origin = origin
        self.haveCase = haveCase

    def __str__(self):
        return f"Weight: {self.weight}, Brand: {self.brand}, Color: {self.color}, Origin: {self.origin}, Have Case: {self.haveCase}"

class Shoes(Brand):
    def __init__(self, weight, brand, boughtFrom, new):
        super().__init__(weight, brand)
        self.boughtFrom = boughtFrom
        self.new = new

    def __str__(self):
        return f"Weight: {self.weight}, Brand: {self.brand}, Bought From: {self.boughtFrom}, New: {self.new}"

class Campus(Brand):
    def __init__(self, weight, brand, accuracy, price, materials):
        super().__init__(weight, brand)
        self.accuracy = accuracy
        self.price = price
        self.materials = materials

    def __str__(self):
        return f"Weight: {self.weight}, Brand: {self.brand}, Accuracy: {self.accuracy}, Price: {self.price}, Materials: {self.materials}"

class Smartphone(Device):
    def __init__(self, weight, brand, storage, operatingSystem, display, camera, materials):
        super().__init__(weight, brand, storage)
        self.operatingSystem = operatingSystem
        self.display = display
        self.camera = camera
        self.materials = materials

    def __str__(self):
        return f"Weight: {self.weight}, Brand: {self.brand}, Storage: {self.storage}, Operating System: {self.operatingSystem}, Display: {self.display}, Camera: {self.camera}, Materials: {self.materials}"

class Laptop(Device):
    def __init__(self, weight, brand, storage, processor, ram, graphics):
        super().__init__(weight, brand, storage)
        self.processor = processor
        self.ram = ram
        self.graphics = graphics

    def __str__(self):
        return f"Weight: {self.weight}, Brand: {self.brand}, Storage: {self.storage}, Processor: {self.processor}, RAM: {self.ram}, Graphics: {self.graphics}"

class Smartwatch(Brand):
    def __init__(self, weight, brand, batteryLife, fitnessFeatures, connectivity):
        super().__init__(weight, brand)
        self.batteryLife = batteryLife
        self.fitnessFeatures = fitnessFeatures
        self.connectivity = connectivity

    def __str__(self):
        return f"Weight: {self.weight}, Brand: {self.brand}, Battery Life: {self.batteryLife}, Fitness Features: {self.fitnessFeatures}, Connectivity: {self.connectivity}"
class CLI:
    def __init__(self):
        self.items = []
        self.weight = 0
        self.itemCount = 0

    def add_item(self, item):
        if self.weight + item.weight <= 80 and self.itemCount < 6:
            self.items.append(item)
            self.weight += item.weight
            self.itemCount += 1
        else:
            print("Item cannot be added")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.weight -= item.weight
            self.itemCount -= 1
        else:
            print("Item not found")

    def print_all_items(self):
        for item in self.items:
            print(item)

    def print_all_items_by_category(self, category):
        for item in self.items:
            if category in str(item):
                print(item)

    def print_item_by_category(self, category):
        for item in self.items:
            if category in str(item):
                print(item)

    def main(self):
        while True:
            print("1. Add Item")
            print("2. Remove Item")
            print("3. Print All Items")
            print("6. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                print("1. Passport")
                print("2. Sunglasses")
                print("3. Sneakers")
                print("4. Universal Charger")
                print("5. Smartphone")
                print("6. Laptop")
                print("7. Smartwatch")
                print("8. Campus")
                print("9. Exit")

                choice = int(input("Enter choice: "))

                if choice == 1:
                    weight = int(input("Enter weight: "))
                    color = input("Enter color: ")
                    cost = int(input("Enter cost: "))
                    boughtFrom = input("Enter bought from: ")
                    item = Passport(weight, color, cost, boughtFrom)
                    self.add_item(item)
                elif choice == 2:
                    weight = int(input("Enter weight: "))
                    brand = input("Enter brand: ")
                    color = input("Enter color: ")
                    origin = input("Enter origin: ")
                    haveCase = input("Enter have case: ")
                    item = Product(weight, brand, color, origin, haveCase)
                    self.add_item(item)
                elif choice == 3:
                    weight = int(input("Enter weight: "))
                    brand = input("Enter brand: ")
                    boughtFrom = input("Enter bought from: ")
                    new = input("Enter new: ")
                    item = Shoes(weight, brand, boughtFrom, new)
                    self.add_item(item)
                elif choice == 4:
                    weight = int(input("Enter weight: "))
                    brand = input("Enter brand: ")
                    color = input("Enter color: ")
                    price = int(input("Enter price: "))
                    size = input("Enter size: ")
                    item = Electrical(weight, brand, color, price, size)
                    self.add_item(item)
                elif choice == 5:
                    weight = int(input("Enter weight: "))
                    brand = input("Enter brand: ")
                    storage = input("Enter storage: ")
                    operatingSystem = input("Enter operating system: ")
                    display = input("Enter display: ")
                    camera = input("Enter camera: ")
                    materials = input("Enter materials: ")
                    item = Smartphone(weight, brand, storage, operatingSystem, display, camera, materials)
                    self.add_item(item)
                elif choice == 6:
                    weight = int(input("Enter weight: "))
                    brand = input("Enter brand: ")
                    storage = input("Enter storage: ")
                    processor = input("Enter processor: ")
                    ram = input("Enter ram: ")
                    graphics = input("Enter graphics: ")
                    item = Laptop(weight, brand, storage, processor, ram, graphics)
                    self.add_item(item)
                elif choice == 7:
                    weight = int(input("Enter weight: "))
                    brand = input("Enter brand: ")
                    batteryLife = input("Enter battery life: ")
                    fitnessFeatures = input("Enter fitness features: ")
                    connectivity = input("Enter connectivity: ")
                    item = Smartwatch(weight, brand, batteryLife, fitnessFeatures, connectivity)
                    self.add_item(item)
                elif choice == 8:
                    weight = int(input("Enter weight: "))
                    brand = input("Enter brand: ")
                    accuracy = input("Enter accuracy: ")
                    price = input("Enter price: ")
                    materials = input("Enter materials: ")
                    item = Campus(weight, brand, accuracy, price, materials)
                    self.add_item(item)
                elif choice == 9:
                    break
            elif choice == 2:
                weight = int(input("Enter weight: "))
                brand = input("Enter brand: ")
                color = input("Enter color: ")
                price = int(input("Enter price: "))
                size = input("Enter size: ")
                item = Electrical(weight, brand, color, price, size)
                self.remove_item(item)
            elif choice == 3:
                self.print_all_items()
            elif choice == 6:
                break
            else:
                print("Invalid choice")
    
cli = CLI()
cli.main()