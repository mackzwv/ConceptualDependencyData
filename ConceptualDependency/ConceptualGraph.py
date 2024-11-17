from ConceptualDependency.ConceptualNode import ConceptualNode
from ConceptualDependency.ACTS import *
from ConceptualDependency.PP import PP
from ConceptualDependency.State import State

class ConceptualDependencyRelation:
    def __init__(self, from_node, to_node, relation_type, **properties):
        self.from_node = from_node
        self.to_node = to_node
        self.relational_type = relation_type # e.g., "agent", "recipient", "object","from_location", "to_location"
        self.properties = properties

        def __repr__(self):
            return f"ConceptualDependencyRelation({self.from_node.label} -> {self.to_node.label}, type={self.relational_type}, properties{self.properties})"

class ConceptualDependencyGraph:
    def __init__(self):
        self.nodes = []
        self.relations = []
    
    def add_node(self, node):
        self.nodes.append(node)
    
    def add_relation(self, relation):
        self.relations.append(relation)
        # relation.from_node.add_relation(relation)
    
    # def find_nodes(self, **criteria):
    #     return [node for node in self.nodes if all(node.properties.get(k)== v for k, v in criteria.items())]
    
    def find_relations(self, **criteria):
        return [rel for rel in self.relations if all(rel.properties.get(k) == v for k, v in criteria.items())]

    def __repr__(self):
        # return f"ConceptualDependencyGraph({(node.label for node in self.nodes)}, {(rel.relational_type for rel in self.relations)})"
        return f"ConceptualDependencyGraph(nodes={len(self.nodes)}, relations={len(self.relations)})"
