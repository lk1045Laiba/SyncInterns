'Chatbot using Python'

import numpy as np
import nltk
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

f = open('data.txt','r',errors='ignore')
dataset = f.read()

dataset = dataset.lower()
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

sentence_tokens = nltk.sent_tokenize(dataset)
word_tokens = nltk.word_tokenize(dataset)

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
  return [lemmer.lemmatize(token) for token in tokens]

remove_punc_dict = dict((ord(punct),None) for punct in string.punctuation)

def LemNormalize(text):
  return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punc_dict)))

greet_inputs = ('hello','hi','whassup')
greet_responses = ('hi','Hey', 'Hey There!', 'There there!!')

def greet(sentence):
  for word in sentence.split():
    if word.lower() in greet_inputs:
      return random.choice(greet_responses)

def response(user_response):
  robo1_response = ''
  TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
  tfidf = TfidfVec.fit_transform(sentence_tokens[:])
  vals = cosine_similarity(tfidf[-1].toarray(), tfidf.toarray())
  idx = vals.argsort()[0][-2]
  flat = vals.flatten()
  flat.sort()
  req_tfidf = flat[-2]
  if req_tfidf == 0:
    robo1_response = robo1_response + "I am sorry. I am unable to understand you."
    return robo1_response
  else:
    robo1_response = robo1_response + sentence_tokens[idx]
    return robo1_response

flag = True
print('\nWelcome to the AI knowledge hub! This chatbot is designed to answer your questions about artificial intelligence (AI). As a language model trained on the latest research and developments in the field, I can provide insights on a wide range of AI topics, including machine learning, deep learning, AI ethics, and more. Whether you\'re a student, researcher, or curious learner, I\' here to help you explore the exciting world of AI. So feel free to ask me anything!\n')
while flag:
  user_response = input("You: ").lower()
  if user_response != 'bye':
    if user_response in ['thank you', 'thanks']:
      flag = False
      print('Bot: You are welcome.')
    else:
      if greet(user_response):
        print('Bot:', greet(user_response))
        print('\n')
      else:
        sentence_tokens.append(user_response)
        word_tokens = word_tokens + nltk.word_tokenize(user_response)
        final_words = list(set(word_tokens))
        print(f'Bot: {response(user_response.split())}\n')
        sentence_tokens.remove(user_response)
  else:
    flag = False
    print("Bot: Goodbye!")

