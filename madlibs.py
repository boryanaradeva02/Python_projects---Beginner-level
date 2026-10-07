# #Choose a Reader: One person takes a Mad Libs book or sheet and acts as the reader.
# Keep the Story Secret: The reader hides the text of the story from everyone else.
# Ask for Words: The reader goes down the list of blanks 
# and asks the other players for random words.
# Match the Parts of Speech: Players call out words that fit the requested category,
# such as a noun, adjective, verb, or exclamation.
# Write Them Down: The reader writes each suggested word into the 
# corresponding numbered blank in the story.
# Read the Story Aloud: Once all the blanks are filled, the reader recites the final story out
#  loud to the group for a funny and absurd result.

adj = input("Adjective: ")
verb = input("Verb: ")
adverb = input("Adverb: ")
adjective2 = input("Adjective: ")
noun1 = input("Noun: ")
noun2 = input("Noun: ")
adjective3 = input("Adjective: ")

madlib = f"Today I went to the zoo. I saw a(n) {adj} monkey jumping up and down in its tree.\
He {verb}{adverb} through the large tunnel that led to its {adjective2} {noun1}.\
I got some peanuts and passed them through the cage to a gigantic gray {noun2} towering above my head. \
Feeding that animal made me hungry. I went to get a {adjective3} scoop of ice cream.\
It filled my stomach.\
Afterwards I had to {verb} {adverb} to catch our bus. When I got home,\
I {verb} my mom for a {adjective3} day at the zoo. "

print(madlib)

#second version 
#This version is for intermediate 
country = input("Country: ")
person = input("Person: ")
plural_noun = input("Plural Noun: ")
food = input("Food: ")
object = input("Object: ")
place = input("Place: ")    
adjective = input("Adjective: ")
animal = input("Animal: ")
occupation = input("Occupation: ")
short_sentence = input("Short Sentence: ")
verb = input("Verb: ")
funny_sentence = input("Funny Sentence: ")
vehicle = input("Vehicle: ")
superlative_adjective = input("Superlative Adjective: ")    

madlip_2 = f"Last summer, I decided to travel to {country} with my {person}. We packed {plural_noun}, {food}, and one extremely suspicious {object}.\
When we arrived, we immediately went to a {place}, where we saw a {adjective} {animal} dancing with a {occupation}.\
Suddenly, the animal shouted, {short_sentence}!\
Everyone started {verb + "ing"}, but I calmly pulled out my {object} and said, {funny_sentence}.\
Then a giant {adjective} {animal} appeared from behind the building and started {verb + "ing"}.\
We were so scared that we decided to {verb} all the way back to the hotel.\
Unfortunately, when we arrived, our room had been stolen by {plural_noun}.\
So, naturally, we spent the rest of the night {verb + "ing"} in a {vehicle} while eating {food}.\
It was the {superlative_adjective} vacation of my life"