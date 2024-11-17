from ConceptualDependency.ConceptualNode import ConceptualNode

class State(ConceptualNode):
    def __init__(self, label, state_type, **properties):
        super().__init__(label, **properties)
        self.properties["state_type"] = state_type # e.g., "ownership", "mental", "location", "progress",  etc

    def __repr__(self):
        return f"State({self.label}, state_type={self.properties['state_type']}, properties={self.properties})"