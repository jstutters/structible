"""The node submodule exposes the Node class."""


class Node(object):
    """Represents files and folders in a tree structure."""

    def __init__(self, name, parent=None, is_file=False):
        """Create a new Node.

        Args:
            name (str): The name of this node

        Keyword args:
            parent (Node): The parent of this node
            is_file (boolean): ``True`` if the node is a file
        """
        self.name = name
        self.is_file = is_file
        self.parent = parent
        self.children = []
        if parent is not None:
            parent.children.append(self)

    @property
    def path(self):
        """Calculate this node's path by walking parents."""
        path_stack = []
        p = self
        while p is not None:
            path_stack.append(p.name)
            p = p.parent
        path_stack.append('.')
        path = '/'.join(path_stack[::-1])
        return path
