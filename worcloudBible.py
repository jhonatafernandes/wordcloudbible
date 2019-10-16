# instale o wordcloud caso você não tenha
!pip install wordcloud -q

# no terminal, retire o ! ou digite o comando
#apt-get install wordcloud -q


# hora de importar os pacotes necessários
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#importar os pacotes para tratar o json
import io
import json
from pandas.io.json import json_normalize


bible = json.load(io.open('nvi.json', 'r', encoding='utf-8-sig'))

bible_file = json_normalize(bible)

#Excluindo colunas e linhas com valores nulos
books = bible_file.dropna(subset=['chapters'], axis=0)['chapters']

all_words_bible = ''
for book in books:
    for chapter in book:
        for verse in chapter:
            
            all_words_bible += verse
    
print("Quantidade de Palavras: {}".format(len(all_words_bible)))

all_words_bible = all_words_bible.lower()

# lista de stopword
stopwords = set(STOPWORDS)
stopwords.update(["da", "meu", "em", "você", "de", "ao", "os", "e", "a","o","do","seu","dele","dela","para", "que", "com", "pelo", "no", "na", "das","dos","se","mas","como","não","pois", "ele", "ela", "quem", "vocês", "também", "lhe", "deu", "será", "por isso", "deles", "uma", "um", "porque", "entre", "até", "nos", "nas", "depois","quando", "sua", "por", "foi", "eles", "todo", "então", "nem", "pela", "por isso", "assim", "toda", "ou", "aquele", "minha", "meu", "lhes", "são", "todos", "este", "está", "isso", " isso", "São"])
 
# gerar uma wordcloud
wordcloud = WordCloud(stopwords=stopwords,
                      background_color="black",
                      width=1600, height=800).generate(all_words_bible)
 
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
 
plt.imshow(wordcloud);
wordcloud.to_file("bible_wordcloud.png")

# endereço LOCAL da SUA imagem
cruz_mask = np.array(Image.open("cruz-quadrada.png"))
   
# gerar uma wordcloud
wordcloud = WordCloud(stopwords=stopwords,
                      background_color="black",
                      width=1000, height=1000, max_words=1000,
                      mask=cruz_mask, max_font_size=200,
                      min_font_size=5).generate(all_words_bible.lower())

# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,10))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()

plt.imshow(wordcloud)
wordcloud.to_file("cruz_wordcloud_bible.png")