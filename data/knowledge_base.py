dictionary = {
    "rating": ["How much will you be * if 10 is like * uncontrollably and 0 is not * at all?",
               "Okay and how much are you * out of 10 if 10 is incredibly *?",
               "How much would you say that you believe that out of 10 if 10 is where you believe it totally and 0 is where you don't believe it at all?"
               ],
    "wrong rating": ["Can you use a number from 0 to 10?",
                     "I'm having some trouble understanding you...Can you please give a number from zero to ten?"
                     ],
    "recap": ["Okay, so you said that you *",
              "So it sounds like you are *. I see...",
              "Therefore it's like you *"
              ],
    "none": ["Can you be more specific?",
             "Can you give an example?"
             ]
}


keywords = [("work", "conc"), ("family", "conc"), ("university", "conc"),  # concerns
            ("have to", "sit"),  # situations
            ("look at me", "thoughts1"), ("stare at me", "thoughts1"), ("stupid", "thoughts2"),
            ("an idiot", "thoughts2"), ("freak", "thoughts2"), ("a weirdo", "thoughts2"),
            ("I can’t do my job", "thoughts3"), ("I should just go home", "thoughts3"),
            ("I wish I weren’t there", "thoughts3"),   # thoughts
            ("hot", "phys1"), ("sweating", "phys2"), ("blushing", "phys2"), ("going red", "phys2"),
            ("flushing", "phys2"), ("trembling", "phys2"), ("shaking", "phys2"),
            ("can’t breathe", "phys3"),  # physical_symptoms
            ("avoid eye contact", "sft1"), ("look down", "sft1"), ("hold tight", "sft2"), ("grip", "sft2"),
            ("hide behind", "sft1"), ("wear black", "sft1"), ("want to go home", "sft1"),  # safety_behaviours
            ("stop being lucid", "focus"), ("lose concentration", "focus"), ("can't think", "focus")  # self_focus
            ]


rates = ["10", "9", "8","0", "7", "6", "5", "4", "3", "2", "1", "zero", "one", "two", "three", "four", "five", "six",
         "seven", "eight", "nine", "ten"]
