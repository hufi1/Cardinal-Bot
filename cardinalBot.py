#! python3
# -- cardinalBot.py -- little bot to autonomously play the game Cardinal under the following URL:
# https://www.newgrounds.com/portal/view/634256

### Hufi
### 25/07/2020 - 27/07/2020

import pyautogui, sys, os, time, logging, webbrowser

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.disable(logging.DEBUG) # uncomment ot block debug log messages


def imgPath(image):
    # makes it easier to generate the path used to locate the image Files.
    return os.path.join('FILEPATH IMAGES' + image)

# VARIABLES USED:

GAME_REGION = ()    # region, where the game is located on screen.


score = 0           # well, the score.


def main():
    # main function calling every other function in the game. Called at the very end.
    logging.debug('Program Started. Press Ctrl-C to abort at any time.')
    logging.debug('To interrupt mouse movement, move mouse to upper left corner.')
    openGame()
    locateGameRegion()
    startGame()
    playGame()
    checkLost()

def openGame():
    game = webbrowser.open('https://www.newgrounds.com/portal/view/634256')     # open the webpage in browser.
    time.sleep(15)   # timer to let the webpage load



def locateGameRegion():
    # function to recognize and locate the game on the screen.
    global GAME_REGION
    region = pyautogui.locateOnScreen(imgPath('press_m_to_mute.png')) # lower left corner used as starting point for calculation.
    if region is None:                                                # because it is always looking the same (press m to mute)
        raise Exception('Could not find the game on the screen.')     # Exception to let us know that the game isn't visible.

    topLeftX = region[0]
    topLeftY = region[1] + region[3] - 550                            # image(upper border) + [abs.height of img] minus game height.
    GAME_REGION = (topLeftX, topLeftY, 550, 550)                      # game regioncoordinates, height and width
    logging.debug('Game region found: %s' % (GAME_REGION,))



def startGame():
    # clicks the center of the game and then starts the game.
    dot = pyautogui.locateCenterOnScreen(imgPath('center.png'), region=GAME_REGION)
    pyautogui.click(dot)                # click center
    time.sleep(0.75)
    pyautogui.press('space')            # start game by pressing space
    pyautogui.press('m')                # mute the game (the sound is annoying when playing it for the 17596th time.


def playGame():
    global score
    while True:
        time.sleep(0.4)                                         # gives us a little extra time in between each patterns
        screenshot = pyautogui.screenshot()                     # creates new screenshot to use within each loop
        if screenshot.getpixel((GAME_REGION[0] + 504, GAME_REGION[1] + 537)) == (170, 16, 48):
            # color code of the red color used in the game. if this specific pixel (within the "T" in press Space To play) is red, then the game is stopped/lost.
            logging.debug('You lost. Your Score: %s' % (score-6)) # Score: subtract 6 to get to the actual points( beginning and end have multiple entries.
            logging.debug('Do you want to play again? (Y/N)')     # usually: 6 multiple entries per game --> therefore substract that amount.
            antwort = input()
            if antwort.lower() == 'y':
                pyautogui.click((GAME_REGION[0] + 200, GAME_REGION[1] + 200))
                pyautogui.press('space')            # restart game
                score = 0                           # reset score

            else:
                logging.debug('Ok ciao!')           # display goodbye msg
                time.sleep(3)
                sys.exit()                          # exit bot


        elif screenshot.getpixel((GAME_REGION[0] + 504, GAME_REGION[1] + 537)) != (170, 16, 48):    # pixel not red here, therefore game is still going.

            if screenshot.getpixel((GAME_REGION[0] + 100, GAME_REGION[1] + 155)) != (176, 1, 26):   # pixel within left red block is not red: left block missing.
                pyautogui.press("left")                                                             # therefore: press 'left' key.
                logging.debug('left')
                score +=1

            elif screenshot.getpixel((GAME_REGION[0] + 483, GAME_REGION[1] + 155)) != (176, 1, 26):
                pyautogui.press("right")                                                            # for the other 3 options: same with corresponding direction
                logging.debug('right')
                score +=1

            elif screenshot.getpixel((GAME_REGION[0] + 273, GAME_REGION[1] + 75)) != (176, 1, 26):
                pyautogui.press("up")
                logging.debug('up')
                score +=1

            elif screenshot.getpixel((GAME_REGION[0] + 273, GAME_REGION[1] + 420)) != (176, 1, 26):
                pyautogui.press("down")
                logging.debug('down')
                score +=1


# actually running the program:
if __name__ == '__main__':
    main()



