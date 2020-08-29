import scipy
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def main():
    s1 = "The president greets the press in Chicago"
    s2 = "Obama speaks to the media in Illinois"
    s3 = "user rt the , "
    s4 = "you user number ? "
    cosine_distance_wordembedding_method(s3, s4)
    # heat_map_matrix_between_two_sentences(s1, s2)


def cosine_distance_wordembedding_method(s1, s2):
    model = load_glove_model()
    v1 = []
    for elem in model:
        for word in preprocess(s1):
            if elem[0] == word:
                v1.append(elem[1:])
    vector_1 = np.mean(v1, axis=0)
    # vector_1 = np.mean([model.index(word) for word in preprocess(s1)],axis=0)
    v2 = []
    for elem in model:
        for word in preprocess(s2):
            if elem[0] == word:
                v2.append(elem[1:])
    vector_2 = np.mean(v2,axis=0)
    # attenzione: se la parola non è presente si rompe
    # vector_n saranno vettori lunghi il numero di parole della frase presenti nel file glove
    # preprocess immagino che debba mettere le parole in minuscolo, togliere le stop words e la pnteggiatura
    cosine = scipy.spatial.distance.cosine(vector_1, vector_2)
    print('Word Embedding method with a cosine distance asses that our two sentences are similar to',round((1-cosine)*100,2),'%')


def load_glove_model():
   # file = open('glove.twitter.27B/glove.twitter.27B.25d.txt', "r", encoding="utf8")
   # file_content = file.read()
   # file.close()
    #return file_content
    model = []
    with open("data.txt") as myfile:
        for line in myfile:
            model.append(line.strip("\n").split(" ")) # attenzione: l'ultimo valore ha anche l'a capo
    print("Model:", model)
    for elem in model:
        i = 1
        while i < len(elem):
            elem[i] = float(elem[i])
            i += 1
    return model


def preprocess(sentence):
    sentence = sentence.lower()
    word_tokens = word_tokenize(sentence)
    filtered_sentence = [w for w in word_tokens if w not in stopwords.words('english')]
    print("Filtered sentence:", filtered_sentence)
    return filtered_sentence


if __name__ == "__main__":
    main()