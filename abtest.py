
"""@author: Andy Ramakrishna

Very simple AB Test.
The test harness will output a tuple of the random bucket
generated and the treatment name that client gets assigned to.
Useful for quantitatively measuring efficacy of multiple options (for
example in a sign up flow UI). Typically the input would be read from a 
text file so that these tests could be run without deploying code and just
updating the configuration.

"""

from random import randint

class ABTest(object):

  def __init__(self):
    self.trials = {}

  def add_trial(self, name, treatments):
    """Memory map of trials, treatments, etc
    @param name: trial name
    @param treatments: [('a', 10)('b', 90)]
    """
    self.trials[name] = treatments

  def use_treatment(self, trial):
    """given a trial, return which treatment to use
    """
    bucket = randint(1, 100)
    weightsum = 0
    assigned_treatment = None
    for name, weight in self.trials[trial]:
      weightsum += weight
      if bucket <= weightsum:
        assigned_treatment = name
        break
    return bucket, assigned_treatment

def main():
  trial = 'SignupButton'
  treatments = [('BigOrangeButton', 50), ('BigBlueButton', 50)]
  abtest = ABTest()
  abtest.add_trial(trial, treatments)
  print abtest.use_treatment(trial)


if __name__ == '__main__':
  main()

