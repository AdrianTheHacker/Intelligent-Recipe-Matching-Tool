# Recipe Fuzzy Search Example
Author - Adrian Tarantino ([@AdrianTheHacker](https://github.com/AdrianTheHacker))

Here is where you can find all code relating to the real world problem in [What is Fuzzy Search and How We Use It - AdrianTheHacker](https://www.youtube.com/@AdrianTheHacker). I encourage you to watch that video before attempting this problem.

If you have any testcases you'd like to contribute, or any corrections, feel free to create a pull request or leave a comment on [the video](https://www.youtube.com/@AdrianTheHacker)!

### The Problem
Let’s just say a recipe app contains a search bar where users can type in the name of their favourite recipe, and the app will return the instructions for that recipe. 

One of our clients really wants to make a given recipe. However, in his eagerness to start cooking he makes many typos and forgets to write one of the words in the name. Write an algorithm that would recommend the most likely food our client is looking for (hint: use a combination of Levenshtein distance and Cosine Similarity).

## Setup Instructions
### Prerequisites
1. Python 3 must be install
    - All code must be written in Python3 and a Python3 interpreter must be used
2. Pip is installed

### General
1. Clone the repository.
2. Navigate to the cloned directory in your command terminal of choice.
3. (Optional) [Create a virtual environment](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) inside of the project directory.
4. Install project dependencies by typing in `pip install -r requirements.txt`
5. Navigate to `./src` directory in your command terminal of choice.
6. Run `Python test_RecipeManager.py` to test your code.

### Solving the Problem Yourself
1. In your code editor of choice, navigate to `./src/RecipeManager.py`.
2. Write your code inside `RecipeManager.matchRecipe(self, userInputtedRecipeName: str, recipesList: list[str])`.
    - Make sure to read through the specifications, parameters, and returns thoroughly before attempting.
3. Navigate to `./src` in the terminal of your choice.
4. Test your function using by typing `python test_RecipeManager.py` in your terminal of choice.

### Testing My Demo-Solution
1. In your code editor of choice, navigate to `./src/test_RecipeManager.py`.
2. Change `from RecipeManager import RecipeManager` to `from ExampleRecipeManager import RecipeManager`.
    - Note that in order to run your own code later, you must revert this change.
3. In your terminal of choice, navigate to `./src`.
4. Test my demo-solution my typing `python test_RecipeManager.py` in your terminal of choice.

