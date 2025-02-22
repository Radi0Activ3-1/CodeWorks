'''
Homework17
Name:
github link:
'''


"""
nato_phonetic.py

Define the NATO Phonetic Alphabet Dictionary.
"""
nato_alphabet = {
    "A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo",
    "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett",
    "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar",
    "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
    "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee",
    "Z": "Zulu"
}

def frequency_counter(data):
    """
    Count frequencies of elements in a collection.

    Args:
        data (list): A list of elements.

    Returns:
        dict: A dictionary with elements as keys and their frequencies as values.

    Examples:
        >>> frequency_counter([1, 2, 2, 3, 3, 3])
        {1: 1, 2: 2, 3: 3}
        
        >>> frequency_counter(['a', 'b', 'a'])
        {'a': 2, 'b': 1}
    """
    frequency = {}
    for element in data:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency

def spell_word(word):
    """
    Translate a word into the NATO Phonetic Alphabet.

    Args:
        word (str): A word to be translated.

    Returns:
        list: A list of NATO phonetic codes corresponding to the letters in the word.

    Examples:
        >>> spell_word('dog')
        ['Delta', 'Oscar', 'Golf']
        
        >>> spell_word('cat')
        ['Charlie', 'Alpha', 'Tango']
    """
    word = word.upper()
    result = []
    for letter in word:
        if letter in nato_alphabet:
            result.append(nato_alphabet[letter])
        else:
            result.append(f"'{letter}' is not a valid letter in the NATO alphabet.")
    return result

def main():
    # Example for frequency counter
    data = [1, 2, 2, 3, 3, 3]
    print("Frequency Counter Example:")
    print(frequency_counter(data))

    # Example for NATO Phonetic Alphabet translator
    print("\nNATO Phonetic Alphabet Translator:")
    user_word = input("Enter a word: ")
    print(spell_word(user_word))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
