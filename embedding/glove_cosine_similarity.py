import scipy
import numpy as np
import strings_manager as sm


def main():
    s1 = "The president greets the press in Chicago"
    s2 = "Obama speaks to the media in Illinois"
    s3 = "user rt the , "
    s4 = "you user number ? "
    model = load_glove_model()
    cosine_distance_wordembedding_method(s1, s4, model)
    # heat_map_matrix_between_two_sentences(s1, s2)


def run_glove(user_sentence, model, messages):
    db_sentences = messages
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
        return "Threshold issue"


def cosine_distance_wordembedding_method(s1, s2, model):
    v1 = []
    words1 = sm.tokenize(s1)
    words2 = sm.tokenize(s2)
    for elem in model:
        for word in words1:
            if elem[0] == word:
                v1.append(elem[1:])
    vector_1 = np.mean(v1, axis=0)
    v2 = []
    for elem in model:
        for word in words2:
            if elem[0] == word:
                v2.append(elem[1:])
    vector_2 = np.mean(v2,axis=0)
    # attenzione: se la parola non è presente si rompe DA VERIFICARE
    # vector_n saranno vettori con la stessa dimensione di prima,
    # ma con un nuovo valore: la media dei vettori di tutte le parole della frase
    cosine = scipy.spatial.distance.cosine(vector_1, vector_2)
    return round((1-cosine)*100,2)


def load_glove_model():
    model = []
    with open("embedding/glove.twitter.27B/glove.twitter.27B.25d.txt", "r", encoding="utf8") as myfile:
        for line in myfile:
            line2 = bytes(line, 'utf-8').decode('utf-8', 'ignore')
            model.append(line2.strip("\n").split(" ")) # attenzione: l'ultimo valore ha anche l'a capo
    for elem in model:
        i = 1
        while i < len(elem):
            elem[i] = float(elem[i])
            i += 1
    return model


if __name__ == "__main__":
    main()
