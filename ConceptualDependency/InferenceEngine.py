from ConceptualDependency.ConceptualNode import ConceptualNode
from ConceptualDependency.ACTS import *
from ConceptualDependency.PP import PP
from ConceptualDependency.State import State
from ConceptualDependency.ConceptualGraph import ConceptualDependencyGraph, ConceptualDependencyRelation

class KnowledgeBase:
    def __init__(self):
        self.states = {}
        self.defaults = {}
        self.rules = {}
    
    def add_state(self, state_type, state):
        """Add a default state for a given state type (e.g., 'location', 'ownership')."""
        self.states[state.label] = state
    
    def get_state(self, state_type):
        """Retrieve a default state based on the state type."""
        return self.states.get(state_type, State(label="Unknown", state_type=state_type))

    def add_default(self, slot_name, value):
        """Add a default value for a specific slot."""
        self.defaults[slot_name] = value
    
    def get_default(self, slot_name):
        """Retrieve a default value for a given slot."""
        return self.defaults.get(slot_name)

    def add_rule(self, action_type, slot_name, default_value):
        """Add a rule for default slot filling based on action type."""
        if action_type not in self.rules:
            self.rules[action_type] = {}
        self.rules[action_type][slot_name] = default_value
    
    def get_rule(self, action_type, slot_name):
        """Retrieve a rule-based default value for a specific slot in an action type."""
        return self.rules.get(action_type, {}).get(slot_name)

class InferenceEngine:
    def __init__(self, knowledge_base = None):
        self.actions = []
        self.context = {}
        self.knowledge_based =  knowledge_base

    def set_knowledge_base(self, knowledge_base):
        """Set or update the knowledge base."""
        self.knowledge_base = knowledge_base

    def add_action(self, action):
        self.actions.append(action)
    
    def set_context(self, context):
        self.context = context
    
    def fill_slots(self, action):
        for slot_name, value in action.slots.items():
            if value is None:
                # Attempt to fill slot using context
                inferred_value = self.context.get(slot_name)
                if inferred_value:
                    action.fill_slot(slot_name, inferred_value)
                elif self.knowledge_base:
                    # use knowledge base for default values or rules
                    default_value = self.knowledge_base.get_rule(action.label, slot_name)
                    if not default_value:
                        default_value = self.knowledge_base.get_default(slot_name)
                    if not default_value and slot_name in ["FROM", "TO"]:
                        state_type = "location" if action.label in ["PTRANS", "MOVE"] else "ownership"
                    if default_value:
                        action.fill_slot(slot_name, default_value)
                    else:
                        # Query the user if no inference is possible
                        action.fill_slot(slot_name, self.query_user(slot_name, action.label))
                else:
                    action.fill_slot(slot_name, self.query_user(slot_name, action.label))
    
    def query_user(self, slot_name, action_label):
        return input(f"Please provide a value for the '{slot_name}' in action '{action_label}': ")

    def process_actions(self):
        for action in self.actions:
            print(f"Processing Action: {action.label}")
            self.fill_slots(action)
            # Process nested actions if any
            if hasattr(action, "nested_actions") and action.nested_actions:
                # print("====HAS NESTED ACTIONS====")
                for nested_action in action.nested_actions:
                    print(f"Processing Nested Action: {nested_action.label}")
                    self.fill_slots(nested_action)
    
    def run(self):
        self.process_actions()
        print("\nFinal Actions:")
        for action in self.actions:
            print(action)

