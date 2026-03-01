# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
   the games purpose is to untilze binary search (lol). the games purpose it to guess a number within a certain range based on difficulty and as few guesses as posible 
- [ ] Detail which bugs you found.
   1. hard coded number range
   2. inverse hints 
   3. typecast to string every other geuss
   4. starting the game of with one guess
   5. the test cases did not split the result tuple
   6. the session was not takin the new difficulty into account when creating the new secreate
- [ ] Explain what fixes you applied.
   1. used high and low instead based on the diffculty set for each game mode
   2. swaped the hints to be correct
   3. got rid of the typecast
   4. initilized at zero instead
   5. spilt into reslut and message
   6. check if the difficulty is diffrent than the prevoise difficulty if so then we genrate a new secraet with the new difficulty ranges  


## 📸 Demo

- [x] ![screenshot](<https://github.com/rhy900/ai110-module1show-gameglitchinvestigator-starter/blob/main/Screenshot%202026-03-01%20at%204.42.50%E2%80%AFPM.png>)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
