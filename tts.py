from gtts import gTTS
word = 'Bayesian statistics is a theory in the field of statistics based on the Bayesian interpretation of probability where probability expresses a degree of belief in an event. Bayesian statistical methods use Bayes to compute and update probabilities after obtaining new data.'
tts = gTTS(word)
tts.save('hello2.mp3')
