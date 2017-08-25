import nltk
from nltk.probability import ELEProbDist, FreqDist, DictionaryProbDist
from nltk import NaiveBayesClassifier
from nltk import FreqDist, ConditionalFreqDist
from nltk import BigramAssocMeasures
from collections import defaultdict



pos_tweets = [('Attention all Nature Lovers - Cattle Cruelty in India & Rescues', 'positive'),
              ('Are you having debate on Poojari Lynching for try to save cow slaughter?', 'positive'),
              ('Hope People start loving all animals like this & not show', 'positive'),
              ('if slaughter houses had glass walls everyone would be a vegetarian', 'positive'),
              ('BanBeef SayNOtoMEATexport PlunderOfIndia SaveGauVansh Cow Vegetarian JagoBharathJag', 'positive'),
              ('I will eat beef and pork for religious reasons, occasionally. I will be vegetarian for ethical reasons, frequently. #meatban #vegetarian','positive')
]
              
neg_tweets = [('Let try to ban hunger before we ban meat?', 'negative'),
              ('meatban causing price of pulses at 200+/kg', 'negative'),
              ('Where is Indian Politics heading to? Chicken, mutton or beef now parliament will approve the dinner', 'negative'),
              ('There is something truly secretly delicious about having your mouth enjoy a perfect BLT in a country with meat ban', 'negative'),
              ('We will let loose 100 pigs in Jama Masjid if the meatban was not enforced on 9 days of Navratri', 'negative')]     


test_tweet = [('A Question: Can someone please tell me how jhatka came into being in answer to halal in India? Please enlighten','negative')]             
             
tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split()
if len(e) >= 3]
    tweets.append((words_filtered, sentiment))             
#print(tweets)

test_tweets = []
for (words, sentiment) in test_tweet:
    words_filtered = [e.lower() for e in words.split()
if len(e) >= 3]
    test_tweets.append((words_filtered, sentiment))    
#print(test_tweets)       

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words     

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features         
    

word_features = get_word_features(get_words_in_tweets(tweets))   
#print(word_features)    

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features
    
a = extract_features(test_tweet)  
print(a) 
    
training_set = nltk.classify.apply_features(extract_features, tweets)
print(training_set)
classifier = nltk.NaiveBayesClassifier.train(training_set)

def train(labeled_featuresets, estimator= ELEProbDist):
    ...
    # Create the P(label) distribution
    label_freqdist = ConditionalFreqDist()
    label_probdist = estimator(label_freqdist)
    ...
    # Create the P(fval|label, fname) distribution
    feature_probdist = {}
    ...
    return NaiveBayesClassifier(label_probdist, feature_probdist)
    #!print(label_probdist.prob('positive'))    
    #!print(feature_probdist)   
    
print(classifier.show_most_informative_features(32))    

#tweet = 'Meat Ban reminds me of TV Ban. If one of your siblings was taking the board exams, you cannot watch too'
        #'And I support Cow,Buffalo #meatban if #India returns to #Swadeshi #agriculture Invest in Agriculture to #SaveIndia'
#print(classifier.classify(extract_features(tweet.split())))   
