from ConceptualDependency.ConceptualNode import ConceptualNode
from ConceptualDependency.State import State
from ConceptualDependency.PP import PP

class ACT(ConceptualNode):
    def __init__(self, label, primitive, tense = "present", modality = None, **properties):
        super().__init__(label, **properties)
        self.properties["primitive"] = primitive
        self.properties["tense"] = tense
        self.properties["modality"] = modality
        self.slots = {}
        self.nested_actions = []
        self.state_changes = []  # A list of dictionaries representing state changes
        self.slots["instruments"] = []  # New slot for a list of instruments

    
    def add_nested_action(self, action):
        if isinstance(action, ACT):
            self.nested_actions.append(action)
        else:
            raise ValueError("Nested actions must be of instance ACT.")
    
    def add_state_change(self, state_type, from_state, to_state):
        """Add a state change to the list of state changes."""
        if isinstance(from_state, State) and isinstance(to_state, State):
            self.state_changes.append({
                "state_type": state_type,
                "from_state": from_state,
                "to_state": to_state
            })
        else:
            raise ValueError("Both from_state and to_state must be instances of State.")

    def set_instruments(self, instruments):
        """Set a list of instruments used in the action."""
        if all(isinstance(instrument, PP) for instrument in instruments):
            self.slots["instruments"] = instruments
        else:
            raise ValueError("All instruments must be instances of PP.")


    def process_state_changes(self):
        """Update the properties of the object PP based on the state changes."""
        object_pp = self.slots.get("object")
        instruments = self.slots.get("instruments", [])

        if object_pp:
            for change in self.state_changes:
                state_type = change["state_type"]
                from_state = change["from_state"]
                to_state = change["to_state"]
                object_pp.update_state(to_state)
                print(f"State change processed: {state_type} updated from '{from_state.label}' to '{to_state.label}' for '{object_pp.label}'")

        # Process state changes for each instrument
        for instrument_pp in instruments:
            for change in self.state_changes:
                state_type = change["state_type"]
                if state_type == "control":  # Example: Instrument might change control state
                    instrument_pp.update_state(change["to_state"])
                    print(f"Instrument state change processed: {state_type} updated to '{change['to_state'].label}' for '{instrument_pp.label}'")

    def __repr__(self, level=0):
        indent = "  " * level
        nested_str = "\n".join([nested_action.__repr__(level + 1) for nested_action in self.nested_actions])
        state_changes_str = ", ".join([f"{change['state_type']}: {change['from_state'].label} → {change['to_state'].label}" for change in self.state_changes])
        instruments = self.slots.get("instruments", [])  # Use .get() to safely access the instruments slot
        instruments_str = ", ".join([instrument.label for instrument in instruments])
        return (f"ACT({self.label}, primitive={self.properties['primitive']}, "
                f"tense={self.properties['tense']}, modality={self.properties['modality']}, "
                f"slots={self.slots}, state_changes=[{state_changes_str}], instruments=[{instruments_str}])"
                + (f"\n{indent}Nested Actions:\n{nested_str}" if self.nested_actions else ""))

    
class ATRANS(ACT):
    def __init__(self):
        super().__init__(label = "ATRANS", primitive = "transfer of ownership")
        self.slots = {
            "agent":None, # the giver
            "object":None, # the item being transferred
            "recipient":None, # the receiver
            }
    
    def add_ownership_change(self, from_state, to_state):
        self.add_state_change("ownership", from_state, to_state)

class PTRANS(ACT):
    def __init__(self):
        super().__init__(label = "PTRANS", primitive = "physical transfer")
        self.slots = {
            "agent":None, # the mover
            "object":None, # the item being moved
            }
    
    def add_location_change(self, from_state, to_state):
        self.add_state_change("location", from_state, to_state)
        
    

class PROPEL(ACT):
    def __init__(self):
        super().__init__(label = "PROPEL", primitive = "apply force")
        self.slots = {
            "agent":None, # the one applying the force
            "object":None, # the item which the force is applied to
            "force":None, # the amount of force applied (NOT in original schema)
            "direction":None, # the direction of the applied force
            }

    def add_physical_state_change(self, from_state, to_state):
        self.add_state_change("physical", from_state, to_state)


class MTRANS(ACT):
    def __init__(self):
        super().__init__(label = "MTRANS", primitive = "transfer of information")
        self.slots = {
            "sender":None, # the one sending the information
            "receiver":None, # the one receiving the information
            "content":None, # the information being transferred, can be conceptualizations
        }
    
    def add_mental_state_change(self, from_state, to_state):
        self.add_state_change("mental", from_state, to_state)
    
    
class MBUILD(ACT):
    def __init__(self):
        super().__init__(label = "MBUILD", primitive = "mental construction")
        self.slots = {
            "builder":None, # The one creating the mental concept.
            "content":None, # the information/mental concept being constructed
            "source":None, # The source of information or stimulus.
        }

    def add_mental_state_change(self, from_state, to_state):
        self.add_state_change("mental", from_state, to_state)
        

class INGEST(ACT):
    def __init__(self):
        super().__init__(label = "INGEST", primitive = "consume/taking into oneself")
        self.slots = {
            "agent":None, # the consumer
            "consumed":None, # the item being consumed
        }
    def add_internal_state_change(self, from_state, to_state):
        self.add_state_change("internal", from_state, to_state)

class EXPEL(ACT):
    def __init__(self):
        super().__init__(label = "EXPEL", primitive = "expel something out of oneself")
        self.slots = {
            "agent":None, # the one expelling
            "object":None, # the item being expelled
        }

    def add_location_change(self, from_state, to_state):
        self.add_state_change("location", from_state, to_state)

class SPEAK(ACT):
    def __init__(self):
        super().__init__(label = "SPEAK", primitive = "verbal output")
        self.slots = {
            "speaker":None, # the person speaking
            "utterance":None, # the words being spoken
        }
class ATTEND(ACT):
    def __init__(self):
        super().__init__(label = "ATTEND", primitive = "focus attention")
        self.slots = {
            "agent":None, # the one paying attention
            "focus":None, # the object of attention
        }

class GRASP(ACT):
    def __init__(self):
        super().__init__(label = "GRASP", primitive = "take hold of")
        self.slots = {
            "agent":None, # the entity taking hold
            "object":None, # the object being held
        }

    def add_control_state_change(self, from_state, to_state):
        self.add_state_change("control", from_state, to_state)

class MOVE(ACT):
    def __init__(self):
        super().__init__(label = "MOVE", primitive = "move body part")
        self.slots = {
            "agent":None, # the entity moving itself
            "body_part":None, # the body part being moved
        }
    
    def add_physical_position_change(self, from_state, to_state):
        self.add_state_change("physical", from_state, to_state)

class DO(ACT):
    def __init__(self):
        super().__init__(label = "DO", primitive = "generic action")
        self.slots = {
            "agent":None, # the entity performing the action,
            "object":None, # the object of the action, if known.
        }

class ACT_GENERIC(ACT):
    def __init__(self):
        super().__init__(label = "ACT", primitive = "abstract action")
        self.slots = {
            "agent":None, # the entity performing the action,
            "recipient":None, # the entity affected by the action.
            "instrument":None # the tool or means used to perform the action.
        }

class CAUSE(ACT):
    def __init__(self):
        super().__init__(label = "CAUSE", primitive = "causative action")
        self.slots = { 
            "agent":None, # the entity causing the effect
            "effect":None, # the effect being caused
        }