from rebus.agent import Agent
from rebus_demo.tools import hash_tools


@Agent.register
class Hasher(Agent):
    """
    This agent performs the following tasks:

    * Wait for descriptors whose selectors begin with "/binary"
    * Compute the MD5 hash for every matching descriptor, and output it to the
      bus as a new descriptor, whose precursor is the origin /binary selector
    """
    _name_ = "hasher"
    _desc_ = "Return md5 of a binary"

    def selector_filter(self, selector):
        # Indicate that this agent is only interested in descriptors whose
        # selector start with "/binary"
        return selector.startswith("/binary")

    def process(self, desc, sender_id):

        # call the very complex tool on the received value
        md5_hash = hash_tools.md5hasher(desc.value)

        # Create a new child descriptor
        new_desc = desc.spawn_descriptor("/md5_hash", unicode(md5_hash), self.name)

        # Push the new descriptor to the bus
        self.push(new_desc)
