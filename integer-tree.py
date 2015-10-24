import sys


def validate(argv):
  """ Given the argument values, make sure that we have
      a tree depth, and that it's a valid integer.
  """
  pass


def make_tree(depth):
  """ Given a tree depth, (recursively?) create an actual
      tree from it that follows the problem requirements.
  """
  pass


def display_tree(tree):
  """ Given the tree structure, display it with proper
      formatting.
  """
  pass


if __name__ == "__main__":
  depth = validate(sys.argv)
  tree = make_tree(depth)
  display_tree(tree)
