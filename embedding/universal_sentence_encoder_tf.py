from absl import logging
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from data import keywords as kw

module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
model = hub.load(module_url)


# it returns a trackable object with a signatures
# attribute mapping from signature keys to functions
def embed(input):
    return model(input)

# Reduce logging output (log)
logging.set_verbosity(logging.ERROR)


# The embeddings produced by the Universal Sentence Encoder are approximately normalized.
# The semantic similarity of two sentences can be trivially computed as the inner product
# of the encodings.
def plot_similarity(labels, corr, rotation):
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
    plt.show()


def run_use(messages_, match_sentence):
    messages_.append(match_sentence)
    message_embeddings = embed(messages_)
    corr = np.inner(message_embeddings, message_embeddings)
    value = -1
    index = -1
    for pos, last_feature in enumerate(corr[len(corr) - 1]):
        if last_feature > value and pos < len(message_embeddings) - 1:
            value = last_feature
            index = pos
    # print("Similarity =", value)
    if value >= 0.65:
        return messages_[index]
    else:
        return "Threshold issue"
