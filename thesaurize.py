from nltk.corpus import wordnet
import random

# Create a function that takes a word as input. It should search the list of synonyms, and return a random one. If the word is either not in NLTK's dictionary, or has no synonyms; it should return the word itself. 
# First, we should check for special characters. If there are special characters: we should note the position of the special character, and which one it is. 
# List of special characters: . , ! ? : ; ' " ( ) [ ] { } / \ | @ # $ % ^ & * - _ + = ~ ` < >
# If there are special characters in the word, they should be ignored when thesaurizing, but should be included in the returned word.
# For example, if the word is "/roll", it should be interpreted as "roll". If the returned synonym is "throw", it should be returned as "/throw".
# We need to keep track where the special characters are, so we can put them back in the right place. We also need to make sure we're putting the right special character back in the right place.
# We also need to account for if there are no special characters in the word.
def thesaurize(word): 
    # We're going to check if the word is in all caps; or if the first letter is capitalized. If so, we'll set the corresponding variable to True, and then convert the word to lowercase. This will make it easier to find synonyms.
    if word.isupper():
        all_caps = True
        word = word.lower()
    else:
        all_caps = False

    if word[0].isupper():
        first_letter_capitalized = True
        word = word.lower()
    else:
        first_letter_capitalized = False

    special_characters = ['.', ',', '!', '?', ':', ';', "'", '"', '(', ')', '[', ']', '{', '}', '/', '\\', '|', '@', '#', '$', '%', '^', '&', '*', '-', '_', '+', '=', '~', '`', '<', '>', "'", '"']
    special_character_positions = [] # This array will hold the positions of the special characters in the word.
    special_character_indexes = [] # This array holds which special character is in each position.

    # First, we should check if the entire word is a special character. If it is, we can just return the word.
    if word in special_characters:
        return word

    # Check if the word has any special characters in it. If there are, we'll note the position of the special character in special_character_positions; and what special character it is in special_character_indexes. Finally, we'll remove the special character from the word.
    # Special rule: If the special character is at the end of the word, we'll note its position as -1 instead.
    for i in range(len(special_characters)):
        if special_characters[i] in word:
            if word.index(special_characters[i]) == len(word) - 1:
                special_character_positions.append(-1)
            else:
                special_character_positions.append(word.index(special_characters[i]))
            special_character_indexes.append(i)
            word = word.replace(special_characters[i], '')
    
    # Now, we can check if the word is in NLTK's dictionary. If it is, we can find synonyms for it. If possible, we'll exclude the original word from the list of synonyms.
    synonyms = wordnet.synsets(word)
    synonyms_list = [lemma.name() for synset in synonyms for lemma in synset.lemmas()]
    synonyms_list = list(set(synonyms_list))
    if word in synonyms_list:
        synonyms_list.remove(word)
    # Print the original word and the number of synonyms.
    print(f"{word}: {len(synonyms_list)} synonyms")
    if synonyms_list:
        word = random.choice(synonyms_list)

    # Now, we can check if the word is in all caps, or if the first letter is capitalized. If so, we'll convert the word back to all caps, or capitalize the first letter.
    if all_caps:
        word = word.upper()
    elif first_letter_capitalized:
        word = word.capitalize()

    # Now, we can add the special characters back into the word.
    # Note: If the index is -1, that means it was at the end of the word.
    for i in range(len(special_character_positions)):
        if special_character_positions[i] == -1:
            word = word + special_characters[special_character_indexes[i]]
        else:
            word = word[:special_character_positions[i]] + special_characters[special_character_indexes[i]] + word[special_character_positions[i]:]
    
    # Finally, we should check if the word has any underscores in them. If so, we should replace them with spaces.
    # if '_' in word:
    #     word = word.replace('_', ' ')

    return word

# Create a function that takes a sentence as input. It should split the sentence into words, and then call the thesaurize function on each word. It should then join the words back together into a sentence, and return it.
def thesaurize_sentence(sentence):
    # First, we should check if this is empty. If it is, we can just return an empty string.
    if not sentence:
        return ''
    
    words = sentence.split()
    thesaurized_words = []
    for word in words:
        thesaurized_words.append(thesaurize(word))
    return ' '.join(thesaurized_words)

sentence = "Own a musket for home defense, since that's what the founding fathers intended. Four ruffians break into my house. \"What the devil?\" As I grab my powdered wig and Kentucky rifle. Blow a golf ball sized hole through the first man, he's dead on the spot. Draw my pistol on the second man, miss him entirely because it's smoothbore and nails the neighbors dog. I have to resort to the cannon mounted at the top of the stairs loaded with grape shot, \"Tally ho lads\" the grape shot shreds two men in the blast, the sound and extra shrapnel set off car alarms. Fix bayonet and charge the last terrified rapscallion. He Bleeds out waiting on the police to arrive since triangular bayonet wounds are impossible to stitch up. Just as the founding fathers intended."
print(thesaurize_sentence(sentence))