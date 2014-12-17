import sys
from rebus.agent import Agent
import re


@Agent.register
class Grep(Agent):
    """
    This agent performs the following tasks:

    * Request descriptors whose selectors match the "/string" regexp
    * Run the external command "grep" to search a user-supplied pattern
    * Output the results to stdout
    """
    _name_ = "grep"
    _desc_ = "Search for occurrences of a string in existing /strings/ \
              selectors, display output to stdout"

    @classmethod
    def add_arguments(cls, subparser):
        subparser.add_argument("pattern", help="Regex to search for")

    def run(self, options):
        pattern = re.compile(options.pattern)
        sels = self.find(self.domain, "/strings/", 0)
        for s in sels:
            desc = self.get(self.domain, s)
            if pattern.search(desc.value):
                sys.stdout.write("%s = %s\n" % (desc.label, desc.value))
