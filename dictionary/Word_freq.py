text = "There were many guest in the event although it rained"

word_freq = {word: text.split().count(word) for word in set(text.split())}
