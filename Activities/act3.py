class Plant:
    def __init__(self, name, water_need):
        self.name = name
        self.water_need = water_need
        self.health = 100
        print(f"Plant created: {self.name} (water need: {self.water_need})")

tomato = Plant("Tomato", 15)

updateResources(water=200, seeds=90, energy=110, hope=80, coins=999)

addPlantsToDropdown([
    ("Malunggay", "🌿", 10),
    ("Palay", "🌾", 15),
    ("Luya", "🫚", 8),
    ("Bawang", "🧄", 5)
])

print("Resource Storage and Plant dropdown unlocked!")