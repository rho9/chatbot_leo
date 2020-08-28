# Code from TensorFlow notebook:
# https://www.tensorflow.org/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder?hl=en

from absl import logging

import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from data import keywords as kw

module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
model = hub.load(module_url)
print("module %s loaded" % module_url)


# returns a trackable object with a signatures
# attribute mapping from signature keys to functions
def embed(input):
    return model(input)


word = "Elephant"
sentence = "I am a sentence for which I would like to get its embedding."
paragraph = (
    "Universal Sentence Encoder embeddings also support short paragraphs. "
    "There is no hard limit on how long the paragraph is. Roughly, the longer "
    "the more 'diluted' the embedding will be.")
messages = [word, sentence, paragraph]

# Reduce logging output (log)
logging.set_verbosity(logging.ERROR)

message_embeddings = embed(messages)

# print the message, the embedding length of the message and the first three values
for i, message_embedding in enumerate(np.array(message_embeddings).tolist()):
    print("Message: {}".format(messages[i]))
    print("Embedding size: {}".format(len(message_embedding)))
    message_embedding_snippet = ", ".join(
      (str(x) for x in message_embedding[:3]))
    print("Embedding: [{}, ...]\n".format(message_embedding_snippet))


# The embeddings produced by the Universal Sentence Encoder are approximately normalized.
# The semantic similarity of two sentences can be trivially computed as the inner product
# of the encodings.
def plot_similarity(labels, features, rotation):
    corr = np.inner(features, features)
    sns.set(font_scale=1.2)
    g = sns.heatmap(
      corr,
      xticklabels=labels,
      yticklabels=labels,
      vmin=0,
      vmax=1,
      cmap="YlOrRd")
    g.set_xticklabels(labels, rotation=rotation)
    g.set_title("Semantic Textual Similarity")
    # plt.show()
    print("Best match with the last one")
    value = -1
    index = -1
    print("Frase con cui matchare:", labels[len(corr) - 1])
    for pos, last_feature in enumerate(corr[len(corr) - 1]):
        if last_feature > value and pos < len(features) - 1:
            value = last_feature
            index = pos
    print("value:", value)
    print("index:", index)
    print("labels[index]:", labels[index])


def run_and_plot(messages_, match_sentence):
    messages.append(match_sentence)
    message_embeddings_ = embed(messages_)
    plot_similarity(messages_, message_embeddings_, 90)


def update_messages():
    # quando viene chiamato vado a leggere tutti i valori presenti in keywords
    # e li salvo dentro a messages
    messages.clear()
    messages_list = list(kw.keywords.values())
    # message_list is a list of list of values from the dictionary
    for mes_list in messages_list:
        for elem in mes_list:
            messages.append(elem)
    print("### MESSAGES ###\n", messages)
    return messages


# messages = [
#   # Smartphones
#   "I like my phone",
#   "My phone is not good.",
#   "Your cellphone looks great.",
#
#   # Weather
#   "Will it snow tomorrow?",
#   "Recently a lot of hurricanes have hit the US",
#   "Global warming is real",
#
#   # Food and health
#   "An apple a day, keeps the doctors away",
#   "Eating strawberries is healthy",
#   "Is paleo better than keto?",
#
#   # Asking about age
#   "How old are you?",
#   "what is your age?",
# ]

messages = update_messages()
run_and_plot(messages, "I'm afraid of sound stupid")
