# Mancala-IA
This is an IA for the Mancala Game

# Folders
- Dataset 
  - Dataset containing more than 150 000 games with their evaluations with the MCTS function
- Model
  - The model trained with this Dataset
- Other
  - An evaluation function based on the Genetic Algorithm (in progress)

# Files
- MancalaBoard
  - A class representing the current state of the game
- MancalaButton
  - A class I used to represent my button on pygame
- MancalaNode
  - A class that represents a Node (built on top of the current state)
  - You can also find all the heuristics (1,2 or 3) plus my own constructed heuristics (MCTS/CNN)
- MancalaPlay
  - A class that allows us to play with the computer or manually.
- MancalaSearch
  - A class where we can find all search algorithms such as MinMax / Negamax.
- main
  - A class that builds a Pygame interface with the AI game (AI VS AI or AI vs Human).
