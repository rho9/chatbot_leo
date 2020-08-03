# Come facciamo la classificazione?
# Cerchiamo parole chiave nella risposta dell’utente e ci diamo un peso?
# Prendiamo il topic che ha più parole in comune con la frase scritta dall’utente?
# Potrebbe essere utile avere il topic per spiegare a cosa fa riferimento la risposta, ma avere anche
# un attributo {keywords} che fa attivare la risposta andando a contare quante delle keywords di quella
# risposta trova in ciò che ha scritto l’utente

# parto da un file della grammatica specifico
# usiamo moved il cui topic è "the patient just moved from living with parents"
# frasi da cui nasce:
# - I've just recently moved out from living with my parents
# - just recently moved out of home for the first time
# proviamo a vedere se funziona usando le keywords: un tot per ogni topic, vince il topic che match più
# keywords
# in futuro valutare se assegnare anche dei pesi alle parole e valutare quindi il peso finale al posto
# del conteggio delle parole
# e usare i sinonimi che sono in sistemi? Se nelle keywords trovi uno slot, cerchi la parola nello slot
# però negli slot non hai i lemmi..magari hai un verbo al passato e la persona lo scrive al presente
# e ciò vale anche per le keywords -> creare un db di lemmi? non esiste già?
# nltk.corpus.reader.wordnet.WordNetCorpusReader.lemma (https://www.nltk.org/api/nltk.corpus.reader.html?highlight=lemma#nltk.corpus.reader.wordnet.WordNetCorpusReader.lemma)

# proviamo ad usare il metodo per i lemmi

import os
from nltk.stem import PorterStemmer

ps = PorterStemmer()
print(ps.stem("shaking"))
# were e was non li rende is, ma chissene..non sono keywords..magari fai un check sulle keywords

# parto da move: scrivo una frase e conto quante keywords matchano. Risultato buono??
sentence = "I've just recently moved out from living with my parents"
sentence = sentence.lower()
words = sentence.split()
# find stems
stems = []
for word in words:
    stems.append(ps.stem(word))
print("stems: ", stems)
count = 0
topic = ""
grms = os.listdir("data/grammar")
for file in grms:
    grm = open("data/grammar/"+file, "r")
    contents = grm.read()
    grm.close()
    # count the keywords
    keys = (contents.split(";")[1]).split("=")[1]
    print("Keys: ", keys)
    aux_count = 0
    for stem in stems:
        if stem in keys:
            aux_count += 1
    if aux_count > count:
        count = aux_count
        topic = (contents.split(";")[0]).split("=")[1]
print("Topic: ", topic)
print("Count: ", count)
# now we need to read from every file and find the one with bigger count: