class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2', **kwargs):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)
        self.actions = []
        seconds = kwargs.get('time', 30)
        self.calculation_time = datetime.timedelta(seconds=seconds)
        self.max_moves = kwargs.get('max_moves', 100)
        self.wins = {}
        self.plays = {}
        self.C = kwargs.get('C', 1.4)


class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.
        """

        # legal = gameState.getLegalActions(0)
        # Returns a list of legal actions for an agent
        # agentIndex=0 means Pacman, ghosts are >= 1

        # next_gameState = gameState.generateSuccessor(0, action)
        # Returns the successor game state after an agent takes an action

        agents = gameState.getNumAgents()
        # Returns the total number of agents in the game
        "*** YOUR CODE HERE ***"
        min_max_game = self.minimax(gameState, self.depth * 2, 0, True)
        return min_max_game[1]

    def minimax(self, gameState, depth, agent=0, maximize=True):
        if gameState.isWin() or gameState.isLose() or depth == 0:
            return self.evaluationFunction(gameState), 'Stop'
        legal = gameState.getLegalActions(agent)
        if maximize:
            scores = []
            for action in legal:
                next_gameState = gameState.generateSuccessor(agent, action)
                scores.append(self.minimax(next_gameState, depth - 1, 1, False)[0])
            top_Score = max(scores)
            index_list = [i for i in range(len(scores)) if scores[i] == top_Score]
            return top_Score, legal[random.choice(index_list)]
        else:
            scores = []
            if agent == gameState.getNumAgents() - 1:  # last ghost
                for action in legal:
                    next_gameState = gameState.generateSuccessor(agent, action)
                    scores.append(self.minimax(next_gameState, depth - 1, 0, True)[0])
            else:
                for action in legal:
                    next_gameState = gameState.generateSuccessor(agent, action)
                    scores.append(self.minimax(next_gameState, depth, agent + 1, False)[0])
            top_Score = min(scores)
            index_list = [i for i in range(len(scores)) if scores[i] == top_Score]
            return top_Score, legal[random.choice(index_list)]