import random
import datetime
# import math.log as log
from random import choice


class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"
        print(legalMoves[chosenIndex])
        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        if successorGameState.isWin():
            return 1000000
        score = successorGameState.getScore()
        now_food = currentGameState.getFood().asList()
        food_list = newFood.asList()
        if len(now_food) == len(food_list):
            score -= 50
            close_food = ['None', 100]
            for food in food_list:
                dist = manhattanDistance(newPos, food)
                if dist < close_food[1]:
                    close_food = [food, dist]
            score -= 1.5 * close_food[1] ** 2

        Ghost_now = currentGameState.getGhostState(1).getPosition()
        new_Ghost = successorGameState.getGhostState(1).getPosition()

        if newScaredTimes[0] < 2:
            if newPos == Ghost_now:
                score -= 100
            if newPos == new_Ghost:
                score -= 100
            else:
                if manhattanDistance(newPos, new_Ghost) <= 3:
                    score += 1.5 * manhattanDistance(newPos, new_Ghost)
                else:
                    score += 50
        capsule = currentGameState.data.capsules
        for c in capsule:
            if newPos == c:
                score += 1000
            score -= 1.5 * manhattanDistance(newPos, c)
        if action == 'Stop':
            score -= 100

        return score
