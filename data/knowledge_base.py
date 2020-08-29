# weights in case in a sentence more keys are present?
dictionary = {
    #"concerns": [# "Are there any situations that you completely avoid?",
                 # "What are the things that you just will not do because of your social anxiety?",
    #             "Is there a particular context in which you feel inappropriate?",
    #             "If you think about your life, what is it that makes you anxious?"
    #             ],
    "situations": ["You said you have some problems with your *. ",
                   "Let's then talk about your * concerns. "
                   # "Can you give an example of your * problems?",
                   # "What are the situations that worried you when you are*?"
                   ],
    "avoided_situations": ["Are there any situations that you completely avoid?",
                           "What are the things that you just won’t do because of your social anxiety?"
                           ], # not used because not present in the case study
    "not_avoided_situations": ["Can you think of a situation in which you experienced social anxiety, but were able to stay in the situation?",
                               "Can you give an example of a typical situation that you managed to endure?"
                               ],
    "thoughts": ["When you *, what kinds of thoughts do you have?",
                 "What do you think about when you *?",
                 #"What was going through your mind?",
                 "In your mind, which was the worst thing that could happen in that situation?"
                 ],
    "physical_symptoms": ["How does your body feel when you *?",
                          "Do you usually experience any physical symptoms of anxiety?",
                          "Do you notice anything like sweating, blushing, trembling?",
                          "Can you describe yourself? How do you think you look when you're in these situations?"
                          # "How about your heart?"
                          ],
    "safety_behaviours": ["Do you usually do anything in the situation to try to prevent your feared consequences from occurring?",
                          "Did you do anything to try to prevent people from noticing you *?",
                          "Is there anything you do to try to ensure that you will come across well?",
                          "Do you do anything to try to control your symptoms?",
                          "Do you do anything to try to avoid drawing attention to yourself?"
                          ],
    "self_focus": ["When you are afraid to start *, what happens to your attention?",
                   "If you focus attention on yourself, what do you notice? Do you become more self-conscious?",
                   "I feel like I am totally zoned out like I'm not even putting attention to what that person saying"
                   ],
    # "self_image": ["As you focused attention on yourself, do you have an image in your mind of how you are coming across to others?",
                   # "As you focused attention on yourself, what did it look like?",
                   # After
                   # "If I closed my eyes and tried to picture the image you have, what would I see?",
                   # "How does having this image affect you?",
                   # "When you completely avoid situations, is your decision affected by an image like this?"
                   # ],
    "rating": ["How much will you be * if 10 is like * uncontrollably and 0 is not * at all?",
               "Okay and how much are you * out of 10 if 10 is incredibly *?",
               "How much would you say that you believe that out of 10 if 10 is where you believe it totally and 0 is where you don't believe it at all?"
               ],  # not good for every case!!
    "wrong rating": ["Can you use a number from 0 to 10?",
                     "I'm having some trouble understanding you...Can you please give a number from zero to ten?"
                     ],
    "more": ["Are there any other things that happens?",
             "Is there anything else that you do to manage these situations?",
             "Do you do anything else?",
             "Do you do something else besides *?"
             ],
    "recap": ["Okay, so you said that you *",
              "So it sounds like you are *. I see...",
              "Therefore it's like you *"
              ],
    "confirmation": ["Is it correct?",
                     "Did I understand correctly?",
                     "Did I get it right?",
                     "Did I correctly interpret what you told me?",
                     "Is that what you meant?"],
    "correction": ["Oh okay...How is it then?",
                   "I'm sorry. Can you tell me it again, then?"],
    "none": ["Can you be more specific?",
             "Can you give an example?"
             ]
}

# Have I to divide it in concerns, situations, ...?
# Is it better to analyze what is after verbs or something like that?
# In this way you don't have to write a huge dictionary
keywords = ["work", "family", "university",  # concerns
            "have to",  # situations
            "worried" "(look|stare) at me", "they think I'm (stupid|an idiot|freak|a weirdo)",
            "they think I look like (a stupid|an idiot|a freak|a weirdo)", "they think I can’t do my job",
            "I should just go home", "wishing I weren’t there",  # thoughts
            "hot", "sweating", "blushing", "going red",  "flushing", "trembling", "shaking", "can’t breathe",  # physical_symptoms
            "avoid eye contact", "look down", "hold tight", "grip", "firm",# safety_behaviours
            "stop being lucid", "lose concentration", "can't think", "hide behind", "wear black", "go/went home",    # self_focus
            "self_image123",  # self_image
            ]


pos_emos = ["agreeable", "amazed", "amused", "animated", "appreciative", "attractive", "awe-filled", "beautiful",
            "blissful", "bold", "brave", "bright", "calm", "cheerful", "clever", "comfortable", "confident", "content",
            "contented", "cool", "delighted", "delightful", "ecstatic", "elated", "encouraged", "encouraging",
            "enthralled", "euphoric", "excited", "exhilarated", "festive", "free", "fresh", "friendly", "gentle",
            "giddy", "glad", "gleeful", "gratified", "happy", "hopeful", "inspired", "jolly", "jovial", "joyful",
            "jubilant", "kind", "lively", "loving", "manic", "merry", "open", "optimistic", "overjoyed", "peaceful",
            "playful", "pleased", "proud", "radiant", "rapturous", "respectful", "satisfied", "serene", "smiling",
            "supportive", "sweet", "sympathetic", "tranquil", "upbeat", "vivacious", "warm", "wonderful"]

neg_emos = ["affronted", "afraid", "aggravated", "aggressive", "alarmed", "alert", "angry", "annoyed", "antagonized",
            "anxious", "apathetic", "apprehensive", "arrogant", "aversive", "awful", "belligerent", "bitter", "bored",
            "bristling", "cautious", "chilly", "cold", "concerned", "confused", "contemptuous", "crabby", "cranky",
            "critical", "cross", "curious", "depressed", "detached", "dirty", "disconcerted", "disenchanted",
            "disgruntled", "disgusted", "disoriented", "displeased", "disquieted", "distressed", "distrustful",
            "doubtful", "dreadful", "edgy", "evil", "exasperated", "fearful", "fidgety", "filled with dread",
            "frustrated", "furious", "gloomy", "glum", "grouchy", "grumpy", "guilty", "hateful", "heavy", "hesitant",
            "horrified", "hostile", "hurtful", "impatient", "incensed", "indecisive", "indifferent", "indignant",
            "inflamed", "insecure", "irritated", "jumpy", "leery", "livid", "mad", "menacing", "miserable", "moody",
            "nasty", "nervous", "obnoxious", "offended", "oppressive", "outraged", "overbearing", "panicked",
            "paralyzed", "peeved", "pensive", "perturbed", "pessimistic", "petrified", "phobic", "rankled", "rattled",
            "raving", "resentful", "riled up", "sad", "sadistic", "sarcastic", "sardonic", "seething", "selfish",
            "shaky", "shocked", "shy", "sour", "spiteful", "startled", "stressed", "suspicious", "tearful", "tense",
            "terrible", "terrorized", "timid", "tired", "ugly", "uneasy", "unnerved", "unsettled", "vengeful",
            "vindictive", "violent", "wary", "watchful", "weak", "worried"]

rates = ["10", "9", "8","0", "7", "6", "5", "4", "3", "2", "1", "zero", "one", "two", "three", "four", "five", "six",
         "seven", "eight", "nine", "ten"]  # pos from nltk?
