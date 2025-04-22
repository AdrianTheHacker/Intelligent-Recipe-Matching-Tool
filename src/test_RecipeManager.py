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

  def __getRecipesList(self) -> list[str]:
    with open("..\\sample-data\\recipes.json", "r") as recipesFile:
      recipes = json.load(recipesFile)
    recipesFile.close()

    recipeNamesList: list[str] = []
    for recipe in recipes:
      recipeNamesList.append(recipe["name"].lower())

    return recipeNamesList

  def test_matchRecipe(self):
    results0 = self.recipeManager.matchRecipe("Corean Fred Chickee", self.recipesList)
    self.assertEqual(results0, "spicy korean fried chicken")
    print("Test Passed!🥳")

    results1 = self.recipeManager.matchRecipe("Munerone Sop", self.recipesList)
    self.assertEqual(results1, "minestrone soup")
    print("Test Passed!🥳")

    results2 = self.recipeManager.matchRecipe("Soup", self.recipesList)
    self.assertEqual(results2, "minestrone soup, cauliflower soup")
    print("Test Passed!🥳")


if __name__ == "__main__":
  unittest.main()