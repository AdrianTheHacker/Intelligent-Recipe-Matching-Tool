import Levenshtein


class RecipeManager:
  def matchRecipe(self, userInputtedRecipeName: str, recipesList: list[str]) -> str:
    """
    Returns the string most similar to `userInputtedRecipeName` in `recipesList`.

    Specifications
    --------------
    - `userInputtedRecipeName` will contain 1 randomly chosen missing word.
    - Not including the missing word, each word in `userInputtedRecipeName`
    will have an Levenshtein distance less than or equal to 3 edits.
    - All string data will be provided in lowercase only.
    - You may use the `Levenshtein.distance(s1, s2)` from https://rapidfuzz.github.io/Levenshtein/levenshtein.html#distance 
    for calculating Levenshtein Distance.
    - If the input is blank, return `"None"`.
    - If multiple strings are equally similar, return a string containing all
    answers separated by `, ` in alphabetical order.
    
    Example:
    .. code-block:: python
      >>> recipeManager.matchRecipe("corean fred chickee", recipesList)
      garlic korean fried chicken, spicy korean fried chicken

    Parameters
    ----------
    userInputtedRecipeName : str
      The recipe name that the user has entered.
    recipesList : list[str]
      A list of recipes.
    englishWordsList : list[str]
      A list of all words in the English Dictionary.

    Returns
    -------
    str
      The string most similar to `userInputtedRecipeName` in `recipesList`.
    """
 
    # 1. Use Levenshtein Distance to correct spelling mistakes.
    recipeWords = self.__getWordsList(recipesList)
    correctlySpelledUserInputtedRecipeNameMatrix = self.__getCorrectSpellingOfPhrase(userInputtedRecipeName, recipeWords)

    print(recipeWords)
    print(self.__getVectorizedPhrase(" ".join(recipeWords), recipeWords))
    print(self.__getVectorizedPhrase("spicy korean fried chicken", recipeWords))
    # 2. Use Cosine Similarity to find most similar words combination.
    # Use bag of words method

    return ""
  
  def __getVectorizedPhrase(self, phrase: str, referenceWords: list[str]) -> list:
    vectorizedPhrase = []
    for word in referenceWords:
      if phrase.split(" ").count(word) == 0: 
        vectorizedPhrase.append(0)
        continue

      vectorizedPhrase.append(1)

    return vectorizedPhrase
  
  def __getCorrectSpellingOfPhrase(self, string: str, referenceWords: list[str]) -> list[list[str]]:
    """
    Returns a matrix where each row is a word in `string` and each column represents
    an alternative for correctly spelling it with equal edit distance.

    Parameters
    ----------
    string: str
      A phrase likely containing spelling mistakes

    referenceWords: list[str]
      A list of words that are used to check spelling in string.
      Allowing a small sample of words to be referenced rather than
      the entire English dictionary can be used in order to prevent 
      words with no relevance to the search from showing up in the data.

    Returns
    -------
    list[list[str]]
      A matrix where each row is a word in `string` and each column represents
      an alternative for correctly spelling it with equal edit distance.
    """
    words = string.split(" ")
    closestWords: list[list[str]] = []

    for wordIndex, word in enumerate(words):
      lowestEditDistance = len(word)
      closestWords.append(["None"])

      for referenceWord in referenceWords:
        if word == referenceWord:
          closestWords[wordIndex] = [referenceWord]
          lowestEditDistance = 0
          break
        
        wordEditDistance = Levenshtein.distance(word, referenceWord)

        if wordEditDistance > lowestEditDistance: continue
        if wordEditDistance == lowestEditDistance:
          closestWords[wordIndex].append(referenceWord)
          continue

        closestWords[wordIndex] = [referenceWord]
        lowestEditDistance = wordEditDistance

    return closestWords

  def __getWordsList(self, phrases: list[str]) -> list[str]:
    """
    Returns a list of all unique words in a list of strings.

    Example:
    .. code-block:: python
    >>> samplePhrases = ["cow jumps over moon", "cow eats food", "cow flies to moon"]
    >>> recipeManager.__getWordsList(samplePhrases)
    ['cow', 'jumps', 'over', 'moon', 'eats', 'food', 'flies', 'to']

    Parameters
    ----------
    phrases: list[str] 
      A list of phrases that the function will find all 
      unique words in.

    Returns
    -------
    list[str]
      A list of all unique words found inside of `phrases`.
    """
    wordsList = []

    for phrase in phrases:
      for word in phrase.split(" "):
        if wordsList.count(word) == 1: continue
        wordsList.append(word)

    return wordsList