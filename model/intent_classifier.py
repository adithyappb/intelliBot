import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Initialize NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Training data (example intents and messages)
training_data = [
    ("Hello", "greeting"),
    ("How are you?", "greeting"),
    ("What's the weather like today?", "weather"),
    ("Show me some restaurants nearby", "restaurant_search"),
    # Add more examples as needed
]

# Preprocessing function
def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token not in stopwords.words('english') and token not in string.punctuation]
    return ' '.join(tokens)

# Preprocess training data
X_train = [preprocess(text) for text, intent in training_data]
y_train = [intent for text, intent in training_data]

# Vectorize text using TF-IDF
vectorizer = TfidfVectorizer(preprocessor=preprocess)
X_train_vectorized = vectorizer.fit_transform(X_train)

# Train SVM classifier
clf = SVC(kernel='linear')
clf.fit(X_train_vectorized, y_train)

# Function to predict intent
def predict_intent(message):
    message_vectorized = vectorizer.transform([preprocess(message)])
    predicted_intent = clf.predict(message_vectorized)[0]
    return predicted_intent

