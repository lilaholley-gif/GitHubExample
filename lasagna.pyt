# ~~~~~ HELPER FUNCTIONS ~~~~~

def loadList():
    try:
        with open("LasagnaList.txt", "r") as listIn:
            loadedList = listIn.readlines()
            for idx in range(len(loadedList)):
                loadedList[idx] = loadedList[idx].replace("\n", "")
        return loadedList
    except FileNotFoundError:
        return []


def saveList(listIn):
    with open("LasagnaList.txt", "w") as newSave:
        for idx in range(len(listIn)):
            if idx < len(listIn) - 1:
                newSave.write(f"{listIn[idx]}\n")
            else:
                newSave.write(f"{listIn[idx]}")


def addItems(listIn):
    addMore = True
    ingredients = listIn
    while addMore:
        printList(ingredients)
        print("Enter ingredient to add (or 'done' to exit)")
        nextItem = input(" --> ")
        if nextItem == "done":
            addMore = False
        else:
            ingredients.append(nextItem)

    saveList(ingredients)


def removeItems(listIn):
    removeMore = True
    ingredients = listIn
    while removeMore:
        printList(ingredients)
        print("Enter an item number to remove (or 'done' to exit)")
        nextRemove = input(" --> ")
        if nextRemove == "done":
            removeMore = False
        else:
            ingredients.pop(int(nextRemove) - 1)

    saveList(ingredients)


def editItems(listIn):
    editMore = True
    ingredients = listIn
    while editMore:
        printList(ingredients)
        print("Choose an item number to edit ('done' to exit)")
        nextEdit = input(" --> ")
        if nextEdit == "done":
            editMore = False
        else:
            print("Type the updated ingredient")
            newEntry = input(" --> ")
            editIdx = int(nextEdit) - 1
            ingredients[editIdx] = newEntry

    saveList(ingredients)


def moveItems(listIn):
    moveMore = True
    ingredients = listIn
    while moveMore:
        printList(ingredients)
        print("Enter an item number to move (or 'done' to exit)")
        nextMove = input(" --> ")
        if nextMove == "done":
            moveMore = False
        else:
            nextElement = ingredients[int(nextMove) - 1]
            print("Enter a new position for the ingredient:")
            newPos = int(input(" --> ")) - 1
            ingredients.remove(nextElement)
            ingredients.insert(newPos, nextElement)

    saveList(ingredients)


def printList(listIn):
    if len(listIn) > 0:
        print("\n~~~ LASAGNA INGREDIENT LIST ~~~")
        for idx in range(len(listIn)):
            print(f"{idx+1}. {listIn[idx]}")
        print("")
    else:
        print("The ingredient list is empty!")


# ~~~~~ MAIN FUNCTION ~~~~~

def main():
    appOn = True
    print("Welcome to the Lasagna Ingredient Manager!")

    while appOn:
        ingredients = loadList()

        print("\n ~~~ Choose an Option Below ~~~")
        print("1. View Ingredient List")
        print("2. Add Ingredient")
        print("3. Remove Ingredient")
        print("4. Edit Ingredient")
        print("5. Move Ingredient")
        print("6. Exit")

        toDo = input(" --> ")

        if toDo == "1":
            printList(ingredients)
        elif toDo == "2":
            addItems(ingredients)
        elif toDo == "3":
            removeItems(ingredients)
        elif toDo == "4":
            editItems(ingredients)
        elif toDo == "5":
            moveItems(ingredients)
        elif toDo == "6":
            appOn = False
        else:
            print("Invalid option - try again!")

    saveList(ingredients)


# ~~~~~ PROGRAM START ~~~~~

if __name__ == "__main__":
    main() 