while True:
    print("Please choose a character:")
    print("1. Wizard")
    print("2. Elf")
    print("3. Human")

    user_input = input("Choose your character: ")
    
    wizard = "Wizard"
    elf = "Elf"
    human = "Human"

    wizard_hp = 70
    elf_hp = 100
    human_hp = 150

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20

    dragon_hp = 300
    dragon_damage = 50

    if user_input == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        print(f"You chosen the character: {character}\nHealth: {my_hp}\nDamage: {my_damage}")
        break
    elif user_input == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        print(f"You chosen the {character}\nHealth: {my_hp}\nDamage: {my_damage}")
        break
    elif user_input == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        print(f"You chose the {character}\nHealth: {my_hp}\nDamage: {my_damage}")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

while True: 
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's health is now:", dragon_hp)

    if dragon_hp <= 0:
        print("The Dragon has lost the battle.")
        break

    my_hp = my_hp - dragon_damage
    print("The Dragon strikes back at the", character, "!")
    print("The", character, "hitpoints are now:", my_hp)

    if my_hp <= 0:
        print("The", character, "has lost the battle.")
        break