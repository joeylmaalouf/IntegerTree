import sys


def validate(argv):
  """ Given the argument values, make sure that we have
      a tree depth, and that it's a valid integer.
  """
  # if no depth is provided, show the user how to do so
  if len(argv) < 2:
    print("Usage: {} <depth>".format(argv[0]))
    sys.exit(1)

  # if the depth isn't a valid int, error out
  try:
    return int(argv[1])
  except ValueError:
    print("Error: Tree depth must be a valid integer.")
    sys.exit(1)


def make_tree(depth):
  """ Given a tree depth, (recursively?) create an actual
      tree from it that follows the problem requirements.
  """
  return [None] * depth


def display_tree(tree):
  """ Given the tree structure, display it with proper
      formatting.
  """
  print(tree)


if __name__ == "__main__":
  depth = validate(sys.argv)
  tree = make_tree(depth)
  display_tree(tree)
