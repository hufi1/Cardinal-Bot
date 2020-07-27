# Cardinal-Bot
A Bot that automatically opens and plays Cardinal, a flash game located here: https://www.newgrounds.com/portal/view/634256

once this bot has opened Cardinal in the webbrowser, it mainly works with pyautogui to locate the game on the screen and interact with the game

Process:

1)  open the game in the standard browser, using the webbrowser module.
2)  locate the game on the screen, using a screenshot of the lower left corner (press 'm' to mute) since this corner always is the same.
3)  calculate the coordinates of the game
4)  start the game by clicking on it, pressing space and muting the sound by pressing m
5)  play the game by recognizing the colors of specific pixels within the red barriers. if the barrier is not red --> press the corresponding direction
6)  find out if the game is over. If so: ask if the user wants the bot to play again. Yes: Do so, No: close the bot.

Game Rules: 

You control a dot in the middle of the screen which is surrounded by red barriers, of which during each round, one disappears. 
To survive, the Player has to move the dot outwards through the gap left behind by the missing barrier. 
To move the dot, you press one of these keys: 'left', 'right', 'up', 'down'.
To start the game you press 'space', to mute it 'm'.

Have fun watching a computer-Let's Play ;) 

Hufi
