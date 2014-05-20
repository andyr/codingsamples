"""
@author: Andy Ramakrishna
python 2.7.3

@description: Take a sequence of evidence (input)
and construct one or more timelines of what happened.

Example:
  input = [
    ['fight', 'gunshot', 'fleeing'],
    ['gunshot', 'falling', 'fleeing']
  ]
  output = [
    ['fight', 'gunshot', 'falling', 'fleeing']
  ]

Run test module: 
  test_detective.py to run unit tests with more examples

Caveats:
  The code below is written in a functional style. Also was a
  timed exercise and written to be readable, so there are 
  optimizations that can be made (avoid recopying arrays).

"""


def sanitize_input_timelines(input_timelines):
  """Transform input; combine overlapping sequences to initial input
  """
  for i in xrange(len(input_timelines)):
    current = input_timelines[i]
    remaining = input_timelines[:i] + input_timelines[i+1:]
    for r in remaining:
      if current[-1] == r[0]:
        input_timelines[i] = current + r[1:]
  return input_timelines


def build_graph(input_timelines):
  """Transform input_timelines into a graph
  """
  graph = {}
  for timeline in input_timelines:
    for i in xrange(len(timeline)-1):
      node = timeline[i]
      neighbor = timeline[i+1]
      if not graph.has_key(node):
        graph[node] = []
      if neighbor not in graph[node]:
        graph[node].append(neighbor)
  return graph


def find_all_paths(graph, start, end, path=[]):
  """Find all paths from start to end
  """
  path = path + [start]
  if start == end:
    return [path]
  if not graph.has_key(start):
    return []
  paths = []
  for node in graph[start]:
    if node not in path:
      newpaths = find_all_paths(graph, node, end, path)
      for newpath in newpaths:
        paths.append(newpath)
  return paths


def reduce_timelines(timelines):
  """Eliminate redundancy by removing paths that are subsets
  """
  reduced = []
  for i in xrange(len(timelines)):
    current = timelines[i]
    remaining = timelines[:i] + timelines[i+1:]
    if not any([set(current).issubset(set(e)) for e in remaining]):
      reduced.append(current)
  return reduced


def construct_timelines(input_timelines):
  """Compile list of best result timelines from input timelines
  """
  input_timelines = sanitize_input_timelines(input_timelines)
  graph = build_graph(input_timelines)
  paths = []
  for timeline in input_timelines:
    paths.extend(find_all_paths(graph, timeline[0], timeline[-1]))
  return reduce_timelines(paths)


