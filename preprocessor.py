import nltk
from nltk import FreqDist
import pymorphy2
import re
from pathlib import Path
import textstat
from nltk.tokenize import sent_tokenize

morph = pymorphy2.MorphAnalyzer()

data_folder = Path("C:/Users/amara/Desktop")
file1= data_folder / "text0nltk.txt"
with open(file1) as textstr:
        text0 = textstr.read()
text1 = re.findall( r'\w+' , text0 )

print(text1)

text3=[]
for word in text1:
	p = morph.parse(word)[0]
	wordx=p.normal_form
	text3.append(wordx)
print('')
print(text3)
	
#frequency of 50 most common vocab items in the text
fdist = FreqDist(text3)
print("|| frequency of 50 most common vocab items in the text ||")
print(fdist.most_common(50))

#length of the text, no duplicates
print("|| length of the text without duplicates ||")
print(len(set(word.lower() for word in text3)))

#length without articles
textnoart = text3.count(" a ") + text3.count(" an ") + text3.count(" the ") + text3.count( " A ") + text3.count(" An ") + text3.count(" The ")
textlennoart= len(text3)- textnoart
print("|| length of the text, no articles ||")
print(textlennoart)

#lexical richness
lexrich=((len(set(text1)))/(len(text1)))*100
print("|| lexical richness ||")
print(lexrich)

#syntactical complexity
sentok = sent_tokenize(text0)
lensentok=len(sentok)
lenwrds=len(set(text1))
syntcomp= 1-(lensentok/lenwrds)
print("|| syntactical complexity ||")
print(syntcomp)

#average word length
sredsum = sum(len(w) for w in text3)
print("|| average word length ||")
print(sredsum/len(text3))

#collocations
text4 = nltk.Text(text3)
print("|| collocations ||")
print(text4.collocations())

#fog-index
fog= (textstat.gunning_fog(text0))
print("|| fog index ||")
print(fog)

#flesch reading ease
flesch= (textstat.flesch_reading_ease(text0))
print("|| flesch reading ease ||")
print(flesch)

#concordance
print("|| concordance ||")
print(text4.concordance("we"))

print(fdist.plot(50))
