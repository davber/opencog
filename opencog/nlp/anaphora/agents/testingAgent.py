"""
PLN Deduction Example

Demonstrates how to run the example in deduction_agent.py when
when interacting with PLN from a standalone Python environment
for development or testing purposes. The normal use case is to
run the example from the CogServer, for which you should use
deduction_agent.py instead.
"""

from __future__ import print_function
from pprint import pprint
from pln.examples.deduction import deduction_agent
from opencog.atomspace import types, AtomSpace, TruthValue
from hobbs import HobbsAgent
from dumpAgent import dumpAgent
from opencog.scheme_wrapper import load_scm,scheme_eval_h, __init__

__author__ = 'Hujie Wang'

# Create an AtomSpace with some sample information, equivalent to the
# information in atomspace_contents.scm
atomspace = AtomSpace()
__init__(atomspace)


data=["opencog/scm/config.scm",
      "opencog/atomspace/core_types.scm",
      "spacetime/spacetime_types.scm",
      "opencog/nlp/types/nlp_types.scm",
      "opencog/dynamics/attention/attention_types.scm",
      "opencog/embodiment/AtomSpaceExtensions/embodiment_types.scm",
      "opencog/learning/pln/pln_types.scm",
      "opencog/scm/apply.scm",
      "opencog/scm/file-utils.scm",
      "opencog/scm/persistence.scm",
      #"opencog/scm/repl-shell.scm",
      "opencog/scm/utilities.scm",
      "opencog/scm/av-tv.scm",
      "opencog/nlp/scm/type-definitions.scm",
      "opencog/nlp/scm/config.scm",
      "opencog/nlp/scm/file-utils.scm",
      "opencog/nlp/scm/nlp-utils.scm",
      "opencog/nlp/scm/disjunct-list.scm",
      "opencog/nlp/scm/processing-utils.scm",
      "opencog/nlp/scm/relex-to-logic.scm",

      "opencog/nlp/anaphora/tests/atomspace#1.scm"
    ]
#status2 = load_scm(atomspace, "opencog/nlp/anaphora/tests/atomspace.scm")

for item in data:
    load_scm(atomspace, item)

#init=initAgent()
#init.run(atomspace)
#dump=dumpAgent()
#dump.run(atomspace)
hobbsAgent = HobbsAgent()
hobbsAgent.run(atomspace)

