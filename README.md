# english-anagram-translator

This is a simple english anagram translator I created with Python. You can write an anagram and get
results from the english dictionary with words that use the exact same characters
as your input. You can also type a word and have the program create an anagram
for you. 

This program can only find word-matches that is from the English Dictionary. 
I'm planning on making an anagram-name function aswell where you'll get the option
to match the anagram/word with names.

The GUI is made with tkinter, and it's not finished. This GUI is just something
I put together quickly to test how the program could work together with a GUI.

Error: Check the README:
If you got this message it means that you most likely haven't installed everything 
you need. You can try the following to fix it:

Check if you've installed NLTK. 
This link shows you how to do it: https://www.nltk.org/install.html

If you've allready installed nltk, check if you have downloaded the english
dictionary through nltk.
1. run nltk.download() in your IDE. (This will show a GUI)
2. Click on the Corpora tab in the GUI.
3. Scroll down until you see "words".
4. Click on "words" and then click on "Download".
