import unittest
import json
from RecipeManager import RecipeManager

class TestRecipeManager(unittest.TestCase):
  """
  Unit Tests for Recipe Manager Function(s).

  Credits
  -------
  1. Corey Schafer - Python Tutorial: Unit Testing Your Code with the unittest Module
  https://youtu.be/6tNS--WetLI?si=8J3gejHBml4sx_GB
  """
  def setUp(self):
    self.recipeManager = RecipeManager()
    self.recipesList = self.__getRecipesList()
    # self.englishWordsList = self.__getEnglishWordsList()

  def __getRecipesList(self) -> list[str]:
    with open("..\\sample-data\\recipes.json", "r") as recipesFile:
      recipes = json.load(recipesFile)
    recipesFile.close()

    recipeNamesList: list[str] = []
    for recipe in recipes:
      recipeNamesList.append(recipe["name"].lower())

    return recipeNamesList
  
  # def __getEnglishWordsList(self) -> list[str]:
  #   with open("..\\sample-data\\englishWords.json", "r") as englishWordsFile:
  #     englishWords = json.load(englishWordsFile)
  #   englishWordsFile.close()

  #   englishWordsList: list[str] = list(englishWords.keys())
  #   return englishWordsList

  def test_matchRecipe(self):
    results0 = self.recipeManager.matchRecipe("Corean Fred Chickee", self.recipesList)
    self.assertEqual(results0, "korean fried chicken")

    results1 = self.recipeManager.matchRecipe("Munerone Sop", self.recipesList)
    self.assertEqual(results1, "minestrone soup")

if __name__ == "__main__":
  unittest.main()