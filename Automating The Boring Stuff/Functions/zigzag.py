import time,sys
indent = 0 # How many space to indent.
indentIncreasing = True # Wheather the indentation is increasing or not.

try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # pause for 1/10 of a second.

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
               # change direction
               indentIncreasing = False

        else:
            # Decrease the number of spaces:
            indent = indent - 1

        if indent == 0:
            # Change direction
            indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()
