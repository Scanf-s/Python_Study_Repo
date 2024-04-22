def game_settings(settings):
    while True:
        print("Choose a setting\n1. Resolution\n2. Volume\n3. Difficulty\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Input Resolution Width")
            resolution_width = input()
            print("Input Resolution Height")
            resolution_height = input()
            settings.set_screen_dimensions(resolution_width, resolution_height)
        if choice == "2":
            print("Current Volume : " + str(settings.volume))
            print("Input Volume: ")
            volume = int(input())
            settings.set_volume(volume)
        if choice == "3":
            print("Current Difficulty : " + str(settings.difficulty))
            print("Input Difficulty number (1. Easy, 2. Medium, 3. Hard): ")
            difficulty = input()
            if difficulty == "1":
                settings.set_difficulty("easy")
            elif difficulty == "2":
                settings.set_difficulty("medium")
            elif difficulty == "3":
                settings.set_difficulty("hard")
        if choice == "4":
            return