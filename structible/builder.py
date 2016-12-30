"""The builder submodule exposes the Builder class."""

import logging


class Builder(object):
    """Makes a filesystem structure corresponding to a tree of nodes."""

    def make_node(self, node):
        """Create the file or directory corresponding to a node."""
        if node.is_file:
            operation = 'touch'
        else:
            operation = 'mkdir'
        logging.debug('%s %s', operation, node.path)
