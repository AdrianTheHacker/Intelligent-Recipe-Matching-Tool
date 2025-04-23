import json
from ExampleRecipeManager import RecipeManager
# from RecipeManager import RecipeManager


def getRecipesList() -> list[str]:
  with open("..\\sample-data\\recipes.json", "r") as recipesFile:
    recipes = json.load(recipesFile)
  recipesFile.close()

  recipeNamesList: list[str] = []
  for recipe in recipes:
    recipeNamesList.append(recipe["name"].lower())

  return recipeNamesList


def main():
  """
  In the console, you can type in a recipe name.

  The only recipe names that the program knows are:
  Cheesy Pickle Chips, Minestrone Soup, Cauliflower Soup, Sesame Soba Noodles,
  Crispy Baked Falafel, Jerk Chicken, Spicy Korean Fried Chicken, Roasted Broccoli Salad, 
  Spicy Chicken Curry, Creamy Garlic Chicken, Soy Garlic Korean Fried Chicken

  You can type in any of these names with some misspellings and missing characters,
  and in theory the program will guess which one you were trying to search.
  """
  userInput = input("Search Recipe: ")
  recipesList = getRecipesList()

  recipeManager = RecipeManager()
  similarRecipeName = recipeManager.matchRecipe(userInput, recipesList)

  print(similarRecipeName)


if __name__ == "__main__":
  main()