import scipy
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# from embedding import universal_sentence_encoder_tf as use


def main():
    s1 = "The president greets the press in Chicago"
    s2 = "Obama speaks to the media in Illinois"
    s3 = "user rt the , "
    s4 = "you user number ? "
    model = load_glove_model()
    cosine_distance_wordembedding_method(s1, s4, model)
    # heat_map_matrix_between_two_sentences(s1, s2)


def run_glove(user_sentence, model, messages):
    #messages = []
    db_sentences = messages  # use.update_messages(messages)
    similarity = -1
    final_sentence = ""
    # model = load_glove_model()
    for sentence in db_sentences:
        cos_sim = cosine_distance_wordembedding_method(sentence, user_sentence, model)
        if cos_sim > similarity:
            similarity = cos_sim
            final_sentence = sentence
    print("Similarity =", similarity)
    if similarity >= 65:
        return final_sentence
    else:
        #print("Ehi, la soglia è bassa, guarda:", similarity)
        return "Threshold issue"


def cosine_distance_wordembedding_method(s1, s2, model):
    v1 = []
    word1 = preprocess(s1)
    word2 = preprocess(s2)
    # print("word1:", word1)
    # print("word2:", word2)
    for elem in model:
        for word in word1:
            if elem[0] == word:
                v1.append(elem[1:])
    vector_1 = np.mean(v1, axis=0)
    # print("vector 1:", vector_1)
    # vector_1 = np.mean([model.index(word) for word in preprocess(s1)],axis=0)
    v2 = []
    for elem in model:
        for word in word2:
            if elem[0] == word:
                v2.append(elem[1:])
    vector_2 = np.mean(v2,axis=0)
    # attenzione: se la parola non è presente si rompe DA VERIFICARE
    # vector_n saranno vettori con la stessa dimensione di prima,
    # ma con un nuovo valore: la media dei vettori di tutte le parole della frase
    # preprocess immagino che debba mettere le parole in minuscolo, togliere le stop words e la pnteggiatura
    cosine = scipy.spatial.distance.cosine(vector_1, vector_2)
    # print('Word Embedding method with a cosine distance asses that our two sentences are similar to',round((1-cosine)*100,2),'%')
    return round((1-cosine)*100,2)


def load_glove_model():
   # file = open('glove.twitter.27B/glove.twitter.27B.25d.txt', "r", encoding="utf8")
   # file_content = file.read()
   # file.close()
    #return file_content
   # così non si può fare perché il file è troppo grande (scrivere l'eccezione ottenuta nella tesi?)
    model = []
    with open("embedding/glove.twitter.27B/glove.twitter.27B.25d.txt", "r", encoding="utf8") as myfile:
        for line in myfile:
            line2 = bytes(line, 'utf-8').decode('utf-8', 'ignore')
            model.append(line2.strip("\n").split(" ")) # attenzione: l'ultimo valore ha anche l'a capo
    # print("Model:", model)
    # from string to float
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
    # print("Filtered sentence:", filtered_sentence)
    return filtered_sentence


if __name__ == "__main__":
    main()
