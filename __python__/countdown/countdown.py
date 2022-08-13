import sys, time
import sevseg

secondsLeft = 30

try:
    while True:
        # Clear the screen by printing several newlines
        print("\n"*60);

        # get the hours/minutes/seconds from seconds left:
        hours = str(secondsLeft // 3600)
        minutes = str( (secondsLeft % 3600) // 60 )
        seconds = str( secondsLeft % 60 )

        # get the digit string from the sevseg module
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Display the digits
        print(hTopRow    + "   " + mTopRow    + "   " + sTopRow)
        print(hMiddleRow + " * " + mMiddleRow + " * " + sMiddleRow)
        print(hBottomRow + " * " + mBottomRow + " * " + sBottomRow)

        if secondsLeft == 0:
            print()
            print("    * * * * BOOM * * * *")
            break

        print()
        print("Press Ctrl-C to quit.")

        time.sleep(1)  # 1 seconds delay
        secondsLeft -= 1
except keyboardInterrupt:
    sys.exit()
