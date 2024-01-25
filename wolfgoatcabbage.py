#! /usr/bin/env python3

from search import *

eight_puzzle = EightPuzzle((2, 3, 1, 4, 5, 7, 8, 6, 0))

class WolfGoatCabbage(Problem):
    """ The problem of Wolf Goat Cabbage is defined by solving how to deliver all objects 
    across a river in a boat that can only carry 2 objects at a time. But, the Wolf and Goat
    may never be left alone as well as the Goat and Cabbage. The Farmer must always accompany
    the boat in crossing. """

    def __init__(self, initial = {'F','W','G','C'}, goal={}):
        """ Define goal state and initialize a problem """
        super().__init__(frozenset(initial), goal)


    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """
        possible_actions = [{'F','G'}, {'F','C'}, {'F','W'}, {'F'}]
        valid_actions = []
        for action in possible_actions:
            right_check = {'F','W','G','C'} - state
            if ((not(action.issubset(state)))and (not(action.issubset(right_check)))):
                continue
            next_state = self.result(state, action)
            left = next_state
            right = {'F','W','G','C'} - left

            if('W' in left and 'G' in left and 'C' in left and 'F' in right):
                continue

            # Eliminates objects being eating
            if((('F' in right and 'C' in right) and ('W' in left and 'G' in left)) or (('F' in left and 'C' in left) and ('W' in right and 'G' in right))):
                continue
            if((('F' in right and 'W' in right) and ('C' in left and 'G' in left)) or (('F' in left and 'W' in left) and ('C' in right and 'G' in right))):
                continue


            valid_actions.append(action)

        return valid_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        state_list = list(state)
        action_list = list(action)

        if 'F' in state:
            state = state - action
            state_list = list(state)
        else:
            state_list = state_list + action_list

        return frozenset(state_list)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        cold_goal = frozenset(self.goal)
        return state == cold_goal

if __name__ == '__main__':
    #print(astar_search(eight_puzzle, h=None, display=True).solution())
    #print(breadth_first_graph_search(eight_puzzle, display=True).solution())
    #print(depth_first_graph_search(eight_puzzle, display=True).solution())

    wgc = WolfGoatCabbage()

    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    
    exit()