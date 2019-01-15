"""
modulegraph._dotbuilder
"""
from typing import Callable, Dict, TextIO, Optional
from ._objectgraph import ObjectGraph, NODE_TYPE, EDGE_TYPE

# - Generic builder for ObjectGraph
# - Using D3.js
# - Enable using custom attributes for nodes and edges
# - Also tabular output?
# - Should reduce the need for a graphviz output


def export_to_dot(
    file: TextIO,
    graph: ObjectGraph[NODE_TYPE, EDGE_TYPE],
    format_node: Optional[Callable[[NODE_TYPE], Dict]] = None,
    format_edge: Optional[Callable[[EDGE_TYPE], Dict]] = None
) -> None:
    """
    Write an dot (graphviz) version of the *graph* to *fp".

    The arguments "format_node" and "format_edge" specify
    callbacks to format nodes and edges that are generated.

    These return dict with following keys (all optional):
    - ...
    """
    print("digraph modulegraph {", file=file)

    for source in graph.iter_graph():
        for edge, target in graph.outgoing(source):
            print(f'    "{source.identifier}" [label="{source.identifier}"]', file=file)
            print(f'    "{source.identifier}" -> "{target.identifier}"', file=file)
    print("}", file=file)