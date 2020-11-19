# LEO - LEt's talk it Over
In the treatment manual for social phobia "Comprehensive Cognitive Behavior
Therapy for Social Phobia: A Treatment Manual" Ledley, Foa and
Huppert outline a treatment program designed for patients with social phobia.
In this work we follow the treatment manual to implement LEO, a chat-bot which purpose is to help people with socialization
problems or that suffer from social phobia using AI. The structure of LEO
is a rules-based model enriched by a machine readable corpus inferred from
real psychological sessions. At this stage the implemented psychological sessions are the first and the second one.


## Structure:
The chat-bot is divided in different classes according to their purpose. We describe them briefly:
* leo: the main class that must be run is leo which prints a small introduction and handles the
calls to activate session 1 and session 2;
* session_one: here the first session is managed. An introduction to
the first session is printed and then the user is aked about his/her
concerns and difficult situations. It then starts a loop to 
dialogue with the user;
* session_two: during the second session, the characteristics
of the situation with their evaluations collected during the 
first session are printed. Some pre-defined
sentences are then printed to explain the user what to do;
* string_manager: in this class there are the methods that process 
sentences;
* kb_manager: this class manages the accesses to the knowledge base
where grammars and keywords are located;
* classifier: this class is used to find the topic of the input.
According to the variable CHOOSE_TOPIC_MODEL, it uses a different
method.
* grammar: in this directory there are all the grammars. Each grammar
has a topic and some sentences related to the topic. In the grammar,
the tokens within curly brackets are replaced
by a synonym taken from the file systems.igrm; the tokens within
round brackets separated by pipes are alternative and are chosen 
randomly, and the tokens within square brackets are printed randomly
or not.
* system: this file contains different slots with synonyms that can
be inserted in the sentences in an equivalent way. 


## References
* Deborah Roth Ledley, Edna B. Foa, and Jonathan D. Huppert. Com-
prehensive Cognitive Behavior Therapy for Social Phobia: A Treatment
Manual. Tech. rep. 2009.
* TensorFlow. Universal Sentence Encoder. Available at hhttps://www.tensorflow.org/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder
* Pre-trained word vectors from Twitter data available
at this link: https://nlp.stanford.edu/projects/glove/ [Jeffrey Pennington, Richard Socher, and Christopher D. Manning. 2014].
