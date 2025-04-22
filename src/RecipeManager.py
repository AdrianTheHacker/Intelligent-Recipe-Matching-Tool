import Levenshtein
import itertools
import math

class RecipeManager:
  def matchRecipe(self, userInputtedRecipeName: str, recipesList: list[str]) -> str:
    """
    Returns the string most similar to `userInputtedRecipeName` in `recipesList`.

    Specifications
    --------------
    - `userInputtedRecipeName` will contain 1 randomly chosen missing word.
    - Not including the missing word, each word in `userInputtedRecipeName`
    will have an Levenshtein distance less than or equal to 3 edits.
    - All strings in `userInputtedRecipeName` and `recipesList` will be lowercase.
    - You may assume `userInputtedRecipeName` is not empty.
    - You may assume all elements of `recipesList` are not empty.
    - If multiple strings are equally similar, return a string containing all
    answers separated by `, ` (order does not matter).
    
    Example:
    --------
    .. code-block:: python
      >>> recipeManager.matchRecipe("corean fred chickee", recipesList)
      garlic korean fried chicken, spicy korean fried chicken

    Allowed Libraries
    -----------------
    - You may use the `Levenshtein.distance(s1, s2)` from https://rapidfuzz.github.io/Levenshtein/levenshtein.html#distance 
    for calculating Levenshtein Distance (already included in requirements.txt).
    - You may use any builtin Python modules (ie Random, Math, Itertools, ect.).

    Pre-made Helper Functions
    -------------------------
    - When computing the dot product, you may use `self.__getVectorDotProduct(vector1: list[int])`.
    - When computing a vector magnitude, you may use `self.__getVectorLength(vector: list[int])`.

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

    # Write your code here!
    # Good luck!

    return ""
  
  def __getVectorDotProduct(self, vector1: list[int], vector2: list[int]) -> int:
    """
    Computes the vector dot product between two vectors.

    Parameters
    ----------
    vector1: list[int]
      The first vector used in computing the dot product.

    vector2: list[int]
      The second vector used in computing the dot product.

    Returns
    -------
    int
      The vector dot product of the two vectors provided.
    """

    if len(vector1) != len(vector2):
      raise ValueError("Vector1 must have same dimensions as Vector2")
    
    dotProduct = 0
    for i in range(len(vector1)):
      dotProduct += vector1[i] * vector2[i]

    return dotProduct
  
  def __getVectorLength(self, vector: list[int]) -> float:
    """
    Calculates the length of `vector`.

    Parameters
    ----------
    vector: list[int]
      The vector you would like to calculate the length for.

    Returns
    -------
    float
      The magnitude of `vector` as a float
    """
    lengthSquared = 0

    for value in vector:
      lengthSquared += math.pow(value, 2)

    return math.sqrt(lengthSquared)
