from Cat import Cat
from Dog import Dog
from Data import Data

def saveTest():
    # Create a cat with a name and insert it into the database
    cat = Cat("Felix")
    data = Data("database")
    data.insert("Cat", cat)

    # Create a dog with a name and insert it into the database
    dog = Dog("Rover")
    data.insert("Dog", dog)

def savePetShop():
    # Create three nameless cats
    cats = [Cat() for _ in range(3)]

    # Create three nameless dogs
    dogs = [Dog() for _ in range(3)]

    # Insert all six pets into the database
    data = Data("database")
    data.begin_tran()
    try:
        for cat in cats:
            data.insert("Cat", cat)
        for dog in dogs:
            data.insert("Dog", dog)
        data.commit()
    except Exception as e:
        data.rollback()
        print(f"An error occurred: {e}")

def logStats():
    print("Execution stats:")
    print("saveTest() created and inserted one cat and one dog.")
    print("savePetShop() created three nameless cats and three nameless dogs and inserted them into the database.")
    print("All pets were persisted in a single transaction.")

if __name__ == "__main__":
    saveTest()
    savePetShop()
    logStats()
