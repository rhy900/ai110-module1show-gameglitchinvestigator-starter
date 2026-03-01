# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

--- It was pretty bad. The very first number was negative, even though it's supposed to be between 1 and 100. The game also showed me the answer before my last guess and told me I didn't have any more guesses. Also, the secret number was 29 and when I input 70 it said go higher.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

--- I used AI to help me understand the `update_score` function because it was just a lot of text in one function, which made it difficult to parse without some type of assistance alongside inline comments. I also used AI to help me identify bugs I was not able to find in my initial observations.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

--- I decided a bug was fixed after testing it and running the game to make sure it worked. I ran tests on all the parts of the code that were in the logic to make sure they give the right output. the tests were pretty simple. I think understanding the problem made understanding the testing much easier.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

--- In the original app, the secret number kept changing because Streamlit reruns the entire script each time a button is pressed or the page reloads. This would cause a new secret to be generated on every rerun, so an `if` statement checking whether the secret already exists is useful for keeping it stable across button presses and guesses. We also need to be careful about the secret not changing when the difficulty is changed, but we can just add a check to see if the difficulty was changed and generate a new secret accordingly.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

--- I'd like to keep the habit of identifying and understanding bugs first before jumping into fixing and testing, because understanding what is causing the bug helps so much in writing the fix and the tests.
