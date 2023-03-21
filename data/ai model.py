# Import required libraries
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('punkt stopwords wordnet')
# Load a text document to process
with open("ugugdul lab2.txt", "r", encoding='utf-8') as f:
    text = f.read()

# Tokenize the text into sentences and words
sentences = sent_tokenize(text)
words = word_tokenize(text)

# Remove stop words (common words like "the", "is", "in", etc.)
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Stem or lemmatize the remaining words (reduce to their base form)
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

# Define a list of question words to match against
question_words = ["what", "when", "where", "who", "why", "how"]

# Loop through the sentences and identify any questions
for sentence in sentences:
    words = word_tokenize(sentence)
    if words[0].lower() in question_words:
        # Extract information from the sentence based on the question type
        if words[0].lower() == "what":
            # Look for nouns and noun phrases in the sentence
            tagged_words = nltk.pos_tag(words)
            nouns = [word for word, pos in tagged_words if pos.startswith("N")]
            noun_phrases = nltk.ne_chunk(tagged_words).draw()
            print("The nouns in the sentence are:", nouns)
            print("The noun phrases in the sentence are:", noun_phrases)
        elif words[0].lower() == "when":
            # Look for date or time expressions in the sentence
            date_expressions = nltk.chunk.ne_chunk(nltk.pos_tag(words)).draw()
            print("The date or time expressions in the sentence are:", date_expressions)
        elif words[0].lower() == "where":
            # Look for location or place names in the sentence
            location_names = nltk.chunk.ne_chunk(nltk.pos_tag(words)).draw()
            print("The location or place names in the sentence are:", location_names)
        # ...and so on for other question types
