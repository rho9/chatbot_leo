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

import re
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
    sentences = (topic_file.split(";")[2])
    sentences_list = re.findall("{topic}.+", sentences)
    # . -> Any character (except newline character)
    # + -> One or more occurrences
    sentence = sentences_list[random.randint(0, len(sentences_list)-1)]
    sentence = sentence[7:len(sentence)]  # remove {topic}
    print("choose_sentence before:", sentence)
    sentence = choose_optional(sentence)
    print("choose_sentence after:", sentence)
    # USARE SISTEMI
    choose_slots(sentence)


# funziona, ma stampa degli spazi che non dovrebbero esserci
def choose_optional(sentence):
    print("sentence[0]: ", sentence[0]) #  perchè stampa due spazi invece che uno???
    while "[" in sentence:
        index_left_bracket = sentence.rfind("[") # rfind trova l'ultima occorrenza, find la prima
        print("index_left_bracket: ", index_left_bracket)
        index_right_bracket = sentence.rfind("]")
        print("index_right_bracket: ", index_right_bracket)
        before_bracket = sentence[0:index_left_bracket]
        print("before_bracket: ", before_bracket)
        after_bracket = sentence[index_right_bracket+1:len(sentence)]
        print("after_bracket: ", after_bracket)
        include = random.randint(0, 1)
        if 1:  # da sostituire con include
            between_bracket = sentence[index_left_bracket+1:index_right_bracket]
            print("between_bracket: ", between_bracket)
            sentence = before_bracket + " " + between_bracket + after_bracket
        else:
            sentence = before_bracket + after_bracket
    return sentence


def choose_slots(sentence):
    # dobbiamo aprire sistemi
    # per ogni { in sentence cerchiamo il suo contenuto in sistemi
    # usiamo replace di string per effettuare la "scelta"
    # non ci serve fare come sopra perchè ora sostituiamo
    # e se sopra sostituissimo con la stringa vuota? Sarebbe molto più leggibile
    system_file = open("data/sistemi.igrm", "r")
    system = system_file.read()
    system_file.close()
    while "{" in sentence:
        index_left_bracket = sentence.find("{")
        index_right_bracket = sentence.find("}")
        print(sentence[index_left_bracket])
        print(sentence[index_right_bracket])
        slot = sentence[index_left_bracket:index_right_bracket+1]  # la prima la include, la seconda no
        print("Slot: ", slot)
        # per interrompre il ciclo. poi da togliere
        #sentence = sentence.replace(sentence[index_left_bracket], "")
        #sentence = sentence.replace(sentence[index_right_bracket-1], "")
        synonyms = (system.split(slot+" =\n")[1]).split("\n;")[0]
        print("synonyms: ", synonyms)
        syn_list = (synonyms.split("\n"))
        print("synonyms list: ", syn_list)
        # bene così o meglio utilizzare readfile e chiudere il file dopo?
        sentence = sentence.replace(slot, syn_list[random.randint(0, len(syn_list)-1)])
    print(sentence)


if __name__ == "__main__":
    main()
