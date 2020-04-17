# weights in case in a sentence more keys are present?
dictionary = {
    "concerns": [# "Are there any situations that you completely avoid?",
                 # "What are the things that you just will not do because of your social anxiety?",
                 "Is there a context in which you feel inappropriate?",
                 "If you think about your life, what is it that makes you anxious?"
                 ],
    "situations": ["You said you have some problems with your *.",
                   "Let's talk about your * concerns."
                   # "Can you give an example of your * problems?",
                   # "What are the situations that worried you when you are*?"
                   ],
    #"sound": ["What would be so bad about if you did say something*?"
    #          ],
    #"afraid of looking": ["What do you think are the actions that make you look*?"
    #                      ],
    "avoided_situations": ["Are there any situations that you completely avoid?",
                           "What are the things that you just won’t do because of your social anxiety?"
                           ], # not used because not present in the case study
    "not_avoided_situations": ["Can you think of a situation in which you experienced social anxiety, but were able to stay in the situation?",
                               "Can you give an example of a typical situation that you managed to endure?"
                               ],
    "thoughts": ["When you *, what kinds of thoughts do you have?",
                 "What do you think about when you *?",
                 "What was going through your mind?",
                 "In your mind, which was the worst thing that could happen in that situation?"
                 ],
    "physical_symptoms": ["How did your body feel when you *?",
                          "Did you experience any physical symptoms of anxiety?",
                          "Did you notice anything like sweating, blushing, trembling?"
                          #"How about your heart?"
                          ],
    "safety_behaviours": ["Did you do anything in the situation to try to prevent your feared consequences from occurring?",
                          # (use specific feared consequences from patient’s information)
                          "Did you do anything to try to prevent people from noticing*?",
                          "Is there anything you do to try to ensure that you will come across well?",
                          "Do you do anything to try to control your symptoms?",
                          "Do you do anything to try to avoid drawing attention to yourself?"
                          ],
    "self_focus": ["When you were afraid that* would happen in this situation, what happened to your attention?",
                   "As you focused attention on yourself, what did you notice? Did you become more self-conscious?"
                   ],
    "self_image": ["As you focused attention on yourself, did you have an image in your mind of how you were coming across to others?",
                   "As you focused attention on yourself, what did it look like?",
                   # After
                   "If I closed my eyes and tried to picture the image you have, what would I see?",
                   "How does having this image affect you?",
                   "When you completely avoid situations, is your decision affected by an image like this?"
                   ],
    "none": ["Can you be more specific?",
             "Can you give an example?"
             ]
}

# have I to divide it in concerns, situations, ...?
keywords = [ "work", "family", "university",  # concerns
             "have to",  # situations
             "worried"]  # thoughts
