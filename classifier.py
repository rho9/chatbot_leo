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

import random
from nltk.stem import PorterStemmer
from data import keywords as kw


# def classifier():
def main():
    stems = find_stems("I've just recently moved out from living with my parents")
    topic = find_topic(stems)
    choose_sentence(topic)


def find_stems(sentence):
    ps = PorterStemmer()
    # were e was non li rende is, ma chissene..non sono keywords..magari fai un check sulle keywords
    sentence = sentence.lower()
    words = sentence.split()
    sentence_stems = ""
    for word in words:
        sentence_stems = sentence_stems + " " + ps.stem(word)
    print("find_stems: ", sentence_stems)
    return sentence_stems


def find_topic(stems):
    matches = 0
    topic = ""
    for keyword in kw.keywords:
        values = kw.keywords[keyword]
        count = 0
        for value in values:
            if value in stems:
                count += 1
        if count > matches:
            matches = count
            topic = keyword
    print("Final matches: ", matches)
    print("Final topic: ", topic)
    return topic
    # possiamo mettere gli slot nelle keyword?


def choose_sentence(topic):
    grm = open("data/grammar/" + topic + ".grm", "r")
    topic_file = grm.read()
    grm.close()
    sentence = (topic_file.split(";")[2]).split("{topic}")[1]
    print("choose_sentence before:", sentence)
    # USARE SISTEMI + CONSIDERARE LE [] + NON PRENDERE SOLO LA PRIMA RISPOSTA
    # []
    while "[" in sentence:
        index_left_bracket = sentence.rfind("[")
        index_right_bracket = sentence.rfind("]")
        before_bracket = sentence[0:index_left_bracket-1]
        after_bracket = sentence[index_right_bracket+1:len(sentence)]
        include = random.randint(0, 1)
        if 1:
            between_bracket = sentence[index_left_bracket+1:index_right_bracket]
            sentence = before_bracket + between_bracket + after_bracket
        else:
            sentence = before_bracket + after_bracket
    print("choose_sentence after:", sentence)



if __name__ == "__main__":
    main()

