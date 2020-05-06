# weights in case in a sentence more keys are present?
dictionary = {
    "concerns": [# "Are there any situations that you completely avoid?",
                 # "What are the things that you just will not do because of your social anxiety?",
                 "Is there a context in which you feel inappropriate?\n",
                 "If you think about your life, what is it that makes you anxious?\n"
                 ],
    "situations": ["You said you have some problems with your *. ",
                   "Let's then talk about your * concerns. "
                   # "Can you give an example of your * problems?",
                   # "What are the situations that worried you when you are*?"
                   ],
    "avoided_situations": ["Are there any situations that you completely avoid?\n",
                           "What are the things that you just won’t do because of your social anxiety?\n"
                           ], # not used because not present in the case study
    "not_avoided_situations": ["Can you think of a situation in which you experienced social anxiety, but were able to stay in the situation?\n",
                               "Can you give an example of a typical situation that you managed to endure?\n"
                               ],
    "thoughts": ["When you *, what kinds of thoughts do you have?\n",
                 "What do you think about when you *?\n",
                 #"What was going through your mind?\n",
                 "In your mind, which was the worst thing that could happen in that situation?\n"
                 ],
    "physical_symptoms": ["How does your body feel when you *?\n",
                          "Do you usually experience any physical symptoms of anxiety?\n",
                          "Do you notice anything like sweating, blushing, trembling?\n"
                          #"How about your heart?"
                          ],
    "safety_behaviours": ["Do you usually do anything in the situation to try to prevent your feared consequences from occurring?\n",
                          "Did you do anything to try to prevent people from noticing you *?\n",
                          "Is there anything you do to try to ensure that you will come across well?\n",
                          "Do you do anything to try to control your symptoms?\n",
                          "Do you do anything to try to avoid drawing attention to yourself?\n"
                          ],
    "self_focus": ["When you are afraid to start *, what happens to your attention?\n",
                   "If you focus attention on yourself, what do you notice? Do you become more self-conscious?\n"
                   ],
    # "self_image": ["As you focused attention on yourself, do you have an image in your mind of how you are coming across to others?",
                   # "As you focused attention on yourself, what did it look like?",
                   # After
                   # "If I closed my eyes and tried to picture the image you have, what would I see?",
                   # "How does having this image affect you?",
                   # "When you completely avoid situations, is your decision affected by an image like this?"
                   # ],
    "rating": ["How much will you be * if 10 is like * uncontrollably and 0 is not * at all?\n",
               "Okay and how * out of 10 if 10 is incredibly *?\n",
               "How much would you say that you believe that out of 10 if 10 is where you believe it totally and 0 is where you don't believe it at all?\n"
               ],
    "wrong rating": ["Can you use a number from 0 to 10?\n",
                     "I'm having some trouble understanding you...Can you please give a number from zero to ten?\n"],
    "none": ["Can you be more specific?\n",
             "Can you give an example?\n"
             ]
}

# have I to divide it in concerns, situations, ...?
keywords = ["work", "family", "university",  # concerns
            "have to",  # situations
            "worried",  # thoughts
            "sweating", "blushing", "going red", "trembling", "shaking",  # physical_symptoms
            "eye contact", "hold tightly",  # safety_behaviours
            "stop being lucid",  # self_focus
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

rates = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "zero", "one", "two", "three", "four", "five", "six",
         "seven", "eight", "nine", "ten"]
# REMEMBER: YOU MUST DOWN SIZE WHAT THE USER WRIGHT BEFORE INTERROGATE THE KB
