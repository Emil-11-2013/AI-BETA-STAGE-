from textblob import TextBlob
from colorama import Fore, Style, init
init(autoreset=True)
text = input("Enter Your Text")
print("\n" + "-"*50)
print("Input Text:\n", text)
print("-"*50)

blob =TextBlob(text)
sentences = blob.sentences

print("\nSentence-wise Sentient Analysis:")
for i, sentence in enumerate(sentences, 1):
    polarity = sentence.sentiment.polarity
    subjectivity = sentence.sentiment.subjectivity
    
if polarity > 0:
    sentiment_label = Fore.GREEN + "Positive😊"
elif polarity < 0:
    sentiment_label = Fore.RED+ "Negative☹️"
else:
    sentiment_label = Fore.YELLOW  + "Neutral😑😶😑😶"

if subjectivity >= 0.5:
    subj_label = Fore.MAGENTA + "Subjective (opinion)"
else:
    subj_label = Fore.CYAN + "Subjective (fact-like)"

print(f"{i}. {sentence}")
print(f"   Polarity: {polarity:.2f}, Subjectivity: {subjectivity:.2f} {sentiment_label} | {subj_label} {Style.RESET_ALL}")