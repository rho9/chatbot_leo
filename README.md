# Red Lion Chatbot
In this project you can find the realization of a chatbot whose aim is to help people with social anxiety problem

## Input:
* Read words (space, no punctuation); tokenize (nltk); look for token in keys (intents)
* What about compound words and proper names? [later]

## Structure:
* Base: Eliza script with tag inspired by real psychological sessions
* Not always the same answer:
  * Random between synonyms [better]
  * Change weight (reduce when used)
* Keys weights: keys are the most important words in utterances. Weights are used to decide which answer to give. How to assign the weights?
  * Assign the weights according to my personal judgment on which are the most important words in the dialogues that I use as an example
  * Or?
* Eliza answers considering only the last thing the user writes. We need to keep track of all the dialogue in order to use what we already learned. Therefore, we need context  
Context:
  * All past intents with their weights
  * All past intents with their weights updated based on when they appeared during the dialogue (past intents are less important)
  * Every utterance already said (from both user and bot)
  * Every utterance already said (from both user and bot ) which intents weights are >= threshold
  
  Which one is better? I would discard the last two techniques because what are used to choose what to answer are intents and not whole sentences. Therefore, I would test the first two techniques
* Recognize more than one intent in one utterance (if present)? [later]
* Manage more intents simultaneously? [later]
* Be sure to implement what is needed to let an example working (e.g. the one that gave you Professor Voegele)

## Notes
* Typo? [later]
* With few sentences, the answer is not immediately. Check what happens with more sentences
* Other way to find synonyms?
* Implement a part for the evaluation of the mood (suggested by Schommer)
* Add Socratic sentences
* Learn and use proper names
* Give space to question and implement how to answer

## Session two
during this session the chatbot should make a recap about what has been said underlying
the perception (the number given) that the user has and ask the user if it well understood:
if it's correct, then go on
if it's not, find out what is wrong and correct it
Then the chatbot should suggest to record a video in which the person act like he/she were
in one of the situation he/she talk about with the chatabot.
Then the chatbot suggest the user to watch at it focusing on the thing that has ben rated
Then the chatbot ask the user to rate again the symptoms
Then the chatbot should compare them with the old one:
if are rated with a minor number, it points out it to the user and ask him/she what he/she
thinks about that
if are similar or more? Search in the document, on the internet...?