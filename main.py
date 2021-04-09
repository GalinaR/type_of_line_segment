"""
Functions that determine the type of line segment on a 2D plane. The segment is encoded as a pair of pairs and looks like: ((x1, y1), (x2, y2)) (nested pairs are the ends of the segment).
"""
def is_vertical(line):
  """
  If the line is a vertical line.
  """
  (x1, y1), (x2, y2) = line
  if x1 == x2 and y1 != y2:
    return True
  return False


def is_horizontal(line):
  """
  If the line is a horizontal line.
  """
  (x1, y1), (x2, y2) = line
  if x1 != x2 and y1 == y2:
    return True
  return False


def is_degenerated(line):
  """
  If the line is a point.
  """
  p1, p2 = line
  if p1 == p2:
    return True
  return False


def is_inclined(line):
  """
  If the line is oblique.
  """
  (x1, y1), (x2, y2) = line
  if x1 != x2 and y1 != y2:
    return True
  return False

# example of tuple: line = (0, 10), (100, 130)

