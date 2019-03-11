# Simple Logic Car Game.
 

command = input("")
started = False
while True:
    command = input(">").lower()
    if command == 'start':
        if started:
            print(' Car already started...')
        else:
            started = True
            print('Car started ready to go !')
    elif command == ('stop'):
        if not started:
            print('Car already stoped ... ')
        else:
            started = False
            print('Car stopped')
    elif command == 'help' :
        print("""
Input start - to start the car
Input stop - to stop the car
Input qiut - to exit
        """)
    elif command == "quit":
        break
    else:
        ('Something went wrong')


