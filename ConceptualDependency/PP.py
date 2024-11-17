from ConceptualDependency.ConceptualNode import ConceptualNode

class PP(ConceptualNode):
    def __init__(self, name, category, **properties):
        super().__init__(label=name, **properties)
        self.properties["category"] = category
        self.current_states = {}  # Tracks the current state for each state type

    def update_state(self, state):
        """Update the current state based on the state type."""
        state_type = state.properties["state_type"]
        self.current_states[state_type] = state.label

    def get_state(self, state_type):
        """Retrieve the current state for a given state type."""
        return self.current_states.get(state_type, f"Unknown {state_type}")

    def __repr__(self):
        return f"PP({self.label}, category={self.properties['category']}, current_states={self.current_states})"
