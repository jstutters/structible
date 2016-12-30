from structible.node import Node

def test_instantiation():
    n = Node('foo')
    assert n.parent is None
    assert n.name == 'foo'
    assert n.is_file == False
    assert n.children == []

def test_instantiate_file_with_parent():
    n = Node('foo')
    o = Node('bar', parent=n, is_file=True)
    assert o.parent == n
    assert o.is_file == True
    assert n.parent is None
    assert n.children == [o]

def test_single_path():
    n = Node('foo')
    assert n.path == './foo'

def test_parented_path():
    p = Node('foo')
    c = Node('bar', parent=p)
    assert p.path == './foo'
    assert c.path == './foo/bar'
