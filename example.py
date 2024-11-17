from ConceptualDependency.ConceptualNode import ConceptualNode
from ConceptualDependency.ACTS import *
from ConceptualDependency.PP import PP
from ConceptualDependency.State import State
from ConceptualDependency.ConceptualGraph import ConceptualDependencyGraph, ConceptualDependencyRelation

# Function to print all ACT instances and their nested actions recursively
def print_all_acts_recursive(action, level=0):
    indent = "  " * level
    print(f"{indent}{action}")
    # Check if the action has nested actions and print them recursively
    if hasattr(action, "nested_actions") and action.nested_actions:
        for nested_action in action.nested_actions:
            print_all_acts_recursive(nested_action, level + 1)

def print_all_acts_in_graph(graph):
    actions = [node for node in graph.nodes if isinstance(node, ACT)]
    print("\nAll Actions in the Conceptual Dependency Graph (including nested actions):")
    for action in actions:
        print_all_acts_recursive(action)

# Function to print all nodes in the graph
def print_all_nodes(graph):
    print("\nAll Nodes in the Conceptual Dependency Graph:")
    for node in graph.nodes:
        print(node)

# Function to print all relations in the graph
def print_all_relations(graph):
    print("\nAll Relations in the Conceptual Dependency Graph:")
    for relation in graph.relations:
        print(f"{relation.from_node.label} -> {relation.to_node.label} (Type: {relation.relational_type})")

# Function to print both nodes and relations
def print_graph_details(graph):
    print_all_nodes(graph)
    print_all_relations(graph)


# Example sentence
sentence = """John went to the park with Mary on a bicycle."""
print(f"Converting Sentence to Conceptual Dependency Graph: {sentence}")


# Creating nodes for John, Mary, park, and bicycle
john = PP(name="John", category="person")
mary = PP(name="Mary", category="person")
park = PP(name="Park", category="location")
bicycle = PP(name="Bicycle", category="vehicle")

# Creating the PTRANS action
went_action = PTRANS()
went_action.fill_slot("agent", john)
went_action.fill_slot("object", None)  # No specific object being transferred
went_action.fill_slot("to_location", park)

# Creating a nested action (e.g., John taking the bicycle as part of the trip)
grasp_action = GRASP()
grasp_action.fill_slot("agent", john)
grasp_action.fill_slot("object", bicycle)

# Adding the nested action to the main action
went_action.add_nested_action(grasp_action)

# Adding Co-Agent (companion) and Instrument
co_agent_relation = ConceptualDependencyRelation(from_node=john, to_node=mary, relation_type="co-agent")
instrument_relation = ConceptualDependencyRelation(from_node=went_action, to_node=bicycle, relation_type="instrument")

# Constructing the conceptual dependency graph
cd_graph = ConceptualDependencyGraph()
cd_graph.add_node(john)
cd_graph.add_node(mary)
cd_graph.add_node(park)
cd_graph.add_node(bicycle)
cd_graph.add_node(went_action)
cd_graph.add_node(grasp_action)

cd_graph.add_relation(co_agent_relation)
cd_graph.add_relation(instrument_relation)

# Output the details of the conceptual dependency graph
print(cd_graph)
print_graph_details(cd_graph)
