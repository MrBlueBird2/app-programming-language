import main

while True:
    try:
        command = input("(｡･ω･｡)ﾉ♡ > ")
        main.run(command)
    except KeyboardInterrupt:
        print("Program Ended")
        exit()