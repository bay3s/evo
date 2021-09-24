"""
Usage: EVO --help
       EVO --train --env=CartPole-v0 --iter=10000 --display=True
       EVO --test --env=CartPole-v0 --iter=10 --display=True

Trains or tests a neural network in the specified environment based on the parameters provided.

Arguments:
  FILE File defining the CNF in DIMACS format
Options:
  --env Open AI environment to train your neural net
  --mode Whether the mode is train or test
  --iter Number of training iterations
  --display Whether to display the environment
"""
from docopt import docopt
from termcolor import colored, cprint
import sys

ARG_KEY_ENVIRONMENT = '--env'
ARG_KEY_MODE = '--mode'
ARG_KEY_EPOCHS = '--epochs'
ARG_KEY_DISPLAY = '--display'
ARG_KEY_NEW = '--new'
ARG_KEY_MODEL = '--model'

def error(message: str) -> None:
  """
  Prints out an error message in the terminal
  Parameters
  ----------
  message : str
      message to display the user
  Returns
  -------
  None
  See Also
  --------
  interpret : function interpreting the command line input and providing heuristic directive to the SAT solver
  """
  cprint(message, 'green', attrs = ['bold'], file = sys.stderr)

def success(message: str) -> None:
  """
  Prints out a success message in the terminal
  Parameters
  ----------
  message : str
      message to display the user
  Returns
  -------
  None
  See Also
  --------
  interpret : function interpreting the command line input and providing heuristic directives to the neural net
      training / testing framework
  """
  cprint(message, 'green', attrs = ['bold'], file = sys.stderr)

def interpret():
  """
  Interprets command line input and provides appropriate input for the neural net training / testing framework

  Returns
  -------
  None
  See Also
  --------
  success : function printing success messages to terminal
  error : function printing error messages to terminal
  """
  args = docopt(__doc__)
  has_error = False

  if args[ARG_KEY_ENVIRONMENT] is None:
    error('Invalid input for environment.')
    has_error = True
  
  if args[ARG_KEY_EPOCHS] is None:
    error('Invalid input for number of training iterations.')
    has_error = True

  if args[ARG_KEY_NEW] is True and args[ARG_KEY_MODEL] is not None:
    error(f'Cannot set --new=True and --model={args[ARG_KEY_MODEL]}. Set --new=False or unset the --model directive.')
    has_error = True

  print('Interpreted')

if __name__ == "__main__":
  interpret()
