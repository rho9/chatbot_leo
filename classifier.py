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
from data import keywords as kw

ps = PorterStemmer()
print(ps.stem("family")) # CONTROLLA DI STAR USANDO QUELLO PER L'INGLESE
# were e was non li rende is, ma chissene..non sono keywords..magari fai un check sulle keywords

# parto da move: scrivo una frase e conto quante keywords matchano. Risultato buono??
sentence = "it's the first time I move out from my family"
# USA UN METODO PER TRASFROMARE IN STEM E RICREARE LA FRASE
##########################################
sentence = sentence.lower()
words = sentence.split()
# find stems
stems = ""
for word in words:
    stems = stems + " " + ps.stem(word)
print("stems: ", stems)
##########################################
count = 0
topic = ""
values = []
for keyword in kw.keywords:
    values = kw.keywords[keyword]
    aux_count = 0
    for elem in values:
        if elem in stems:
            aux_count += 1
    if aux_count > count:
        count = aux_count
        topic = keyword
print("Final count: ", count)
print("Final topic: ", topic)
# possiamo mettere gli slot nelle keyword?
grms = os.listdir("data/grammar")
for file in grms:
    grm = open("data/grammar/"+file, "r")
    contents = grm.read()
    grm.close()
