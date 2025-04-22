import Levenshtein


class RecipeManager:
  def matchRecipe(self, userInputtedRecipeName: str, recipesList: list[str], englishWordsList: list[str]) -> str:
    """
    Returns the string most similar to `userInputtedRecipeName` in `recipesList`.

    Specifications
    --------------
    - `userInputtedRecipeName` will contain 1 randomly chosen missing word.
    - Not including the missing word, each word in `userInputtedRecipeName`
    will have an Levenshtein distance less than or equal to 3 edits.
    - All string data will be provided in lowercase only.
    - If the input is blank, return `"None"`.
    - If multiple strings are equally similar, return a string containing all
    answers separated by `, ` in alphabetical order.
    
    Example:
    .. code-block:: python
      >>> recipeManager.matchRecipe("corean fred chickee", recipesList)
      soy garlic korean fried chicken, spicy korean fried chicken

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
    userInputtedRecipeNameList = userInputtedRecipeName.split(" ")

    for recipeWord, recipeWordIndex in enumerate(userInputtedRecipeNameList):
      closestWord = "None"
      closestWordScore = len(recipeWord)

      for englishWord in englishWordsList:
        if recipeWord == englishWord:
          closestWord = recipeWord
          closestWordScore = 0
          break

        if Levenshtein.distance(recipeWord, englishWord) >= closestWordScore: continue
        closestWord = englishWord
        closestWordScore = Levenshtein.distance(recipeWord, englishWord)

      userInputtedRecipeNameList[recipeWordIndex] = closestWord
    matchedRecipeName = ' '.join(userInputtedRecipeNameList)



    # 2. Use Cosine Similarity to find most similar words combination.

    return matchedRecipeName