#!/usr/bin/env python

"""@author: Andy Ramakrishna
"""

import sys
import unittest
from detective import construct_timelines

class DetectiveTest(unittest.TestCase):

  def test_merge_simple(self):
    input_timeline = [
      ['fight', 'gunshot', 'fleeing'],
      ['gunshot', 'falling', 'fleeing']
    ]
    expected = [
      ['fight', 'gunshot', 'falling', 'fleeing']
    ]

    result = construct_timelines(input_timeline)
    self.assertEqual(expected, result)

  def test_partial_merge(self):
    input_timeline = [
      ['shadowy figure', 'demands', 'scream', 'siren'],
      ['shadowy figure', 'pointed gun', 'scream']
    ]
    expected = [
      ['shadowy figure', 'demands', 'scream', 'siren'],
      ['shadowy figure', 'pointed gun', 'scream', 'siren']
    ]

    result = construct_timelines(input_timeline)
    self.assertEqual(expected, result)

  def test_no_merge(self):
    input_timeline = [
      ['argument', 'coverup', 'pointing'],
      ['press brief', 'scandal', 'pointing'],
      ['argument', 'bribe']
    ]
    expected = input_timeline

    result = construct_timelines(input_timeline)
    self.assertEqual(expected, result)

  def test_merge_another(self):
    input_timeline = [
      ['shouting', 'fight', 'fleeing'],
      ['fight', 'gunshot', 'panic', 'fleeing'],
      ['anger', 'shouting']
    ]
    expected = [
      ['anger', 'shouting', 'fight', 'gunshot', 'panic', 'fleeing']
    ]

    result = construct_timelines(input_timeline)
    self.assertEqual(expected, result)


  def test_merge_partial_prefix(self):
    """This test mainly exercises sanitize_input_timelines
    to produce the correct result
    """
    input_timeline = [
      ['a','c'], ['b','c'], ['c','d']
    ]
    expected = [['a','c','d'], ['b','c','d']]
    result = construct_timelines(input_timeline)
    self.assertEqual(expected, result)


  def test_merge_partial_multiple(self):
    input_timeline = [
      ['pouring gas', 'laughing', 'lighting match', 'fire'],
      ['buying gas', 'pouring gas', 'crying', 'fire', 'smoke']
    ]
    expected = [
      ['buying gas', 'pouring gas', 'laughing', 'lighting match', 'fire', 'smoke'],
      ['buying gas', 'pouring gas', 'crying', 'fire', 'smoke']
    ]
    result = construct_timelines(input_timeline)
    self.assertEqual(expected, result)



if __name__ == '__main__':
  unittest.main()



