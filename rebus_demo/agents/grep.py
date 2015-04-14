import sys
from rebus.agent import Agent
import re


@Agent.register
class Grep(Agent):
    """
    This agent performs the following tasks:

    * Request descriptors whose selectors match the "/string" regexp
    * Match user supplied pattern to lines
    * Output the results to stdout
    """
    _name_ = "grep"
    _desc_ = "Search for occurrences of a string in existing /strings/ \
              selectors, display output to stdout"

    @classmethod
    def add_arguments(cls, subparser):
        subparser.add_argument("pattern", help="Regex to search for")

    def run(self):
        pattern = re.compile(self.config['pattern'])
        sels = self.find(self.domain, "/strings/", 0)
        for s in sels:
            desc = self.get(self.domain, s)
            for s in desc.value:
                if pattern.search(s):
                    sys.stdout.write("%s = %s\n" % (desc.label, s))
