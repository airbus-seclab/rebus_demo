from rebus.agent import Agent
from rebus_demo.tools import string_tools


@Agent.register
class Stringer(Agent):
    """
    This agent performs the following tasks:

    * Wait for descriptors whose selectors begin with "/binary"
    * Extract printable strings from the binary, using the external command
      "strings"
    * Output the resulting strings to the bus as an array in a new descriptor,
      whose precursor is the origin /binary selector.

    """
    _name_ = "stringer"
    _desc_ = "Extract all strings from a binary"

    def selector_filter(self, selector):
        # Indicate that this agent is only interested in descriptors whose
        # selector start with "/binary"
        return selector.startswith("/binary/")

    def process(self, desc, sender_id):

        outbuf = string_tools.extract_strings(desc.value)
        lines = [unicode(x) for x in outbuf.splitlines()]

        # Create a new child descriptor for each string
        new_desc = desc.spawn_descriptor("/strings", lines,
                                         self.name)
        # Push the new descriptor to the bus
        self.push(new_desc)
