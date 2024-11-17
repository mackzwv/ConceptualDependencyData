class ConceptualNode:
    def __init__(self, label, **properties):
        self.label = label
        self.properties = properties
        self.slots = {}
    
    def add_property(self, key, value):
        self.properties[key] = value

    def fill_slot(self, slot_name, value):
        self.slots[slot_name] = value
    
    def is_slot_filled(self, slot_name):
        return slot_name in self.slots and self.slots[slot_name] is not None
    # def add_relation(self, relation):
    #     self.relations.append(relation)
    
    def __repr__(self):
        return f"ConceptualNode({self.label}, {self.properties}, slots={self.slots})"
