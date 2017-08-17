import nltk
from nltk.corpus import brown
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
import os

# abrir texto em .txt
os.getcwd()
os.chdir('/home/kassio/Dropbox/MestradoCin/Recuperacao_inteligente_de_informacao/codes/')

text = open('text1.txt')
text = text.read()

# remocao de pontuacao
tokenizer = RegexpTokenizer(r'\w+')
text = tokenizer.tokenize(text)

# tokenize: deteccao de sentencas, segmentacao de frases

#sent_tokenize(text)
#tokens = word_tokenize(text)

# remocao de stopwords:

def remove_stopwords(word_list):
    processed_word_list = []
    for word in word_list:
        word = word.lower()   # coloca em letras minusculas (lower case)
        if word not in stopwords.words("english"):
            processed_word_list.append(word)
    return processed_word_list


tokens = remove_stopwords(text)
tokens

# stemming (reducao de palavras ao seu radical)
# stemer em portugues (!!!!)
stemmer_port= nltk.stem.RSLPStemmer()
stemmer_port.stem("computacional")

# continuando o exemplo:
porter = nltk.PorterStemmer()
porter.stem("absolutely")

tokens = [porter.stem(words) for words in tokens]


#### criar seu proprio corpora de textos. 
os.getcwd()
os.chdir('/home/kassio/Dropbox/MestradoCin/Recuperacao_inteligente_de_informacao/codes/corpora1/')

from nltk.corpus.reader.plaintext import PlaintextCorpusReader

corpusdir = '/home/kassio/Dropbox/MestradoCin/Recuperacao_inteligente_de_informacao/codes/corpora1/'
newcorpus = PlaintextCorpusReader(corpusdir, '.*')

# listar todos os textos do corpus
newcorpus.fileids()

# acessar o texto 3: text3.txt
text3 = newcorpus.raw('text3.txt')  # texto bruto
text3

# remocao de pontuacao
tokenizer = RegexpTokenizer(r'\w+')
text3 = tokenizer.tokenize(text3)

# remover stopwords
tokens3 = remove_stopwords(text3)

# stemming (reducao de palavras ao seu radical)
porter = nltk.PorterStemmer()
tokens3 = [porter.stem(words) for words in tokens3]

# contar frequencia das palavras
FreqDist(tokens3)

