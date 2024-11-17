## ConceptualDependencyData
Python OOP Implementation of Roger Schank's Conceptual Dependency Framework 

This project implements a Conceptual Dependency (CD) Parser in Python for natural language understanding. It uses a graph-based representation to break down sentences into conceptual actions (ACTs) and physical objects (PPs). The system supports common conceptual actions like PTRANS (movement), ATRANS (ownership transfer), MTRANS (information transfer), and more. Each action can have slots filled with agents, objects, locations, and instruments, as well as nested actions for complex scenarios.

## Features
Action Representation: Models physical, mental, and communicative actions using an extensible ACT class hierarchy.
Graph Structure: Represents conceptual dependencies using nodes and relations in a directed graph.
Slot-Filling: Automatically fills action slots using context and default values from a knowledge base.
Nested Actions: Supports complex actions composed of nested sub-actions.
Inference Engine: Provides a basic inference engine for filling missing information based on context and user input.

## Goal
This project provides a framework for building knowledge graphs and extracting conceptual dependencies, making it useful for natural language processing and AI research applications.

## References
- Schank, Roger C. “CONCEPTUAL DEPENDENCY THEORY.” In Conceptual Information Processing, 22–82. Elsevier, 1975. https://doi.org/10.1016/B978-1-4832-2973-7.50007-9.
- Schank, Roger C. “CONCEPTUAL DEPENDENCY AS A FRAMEWORK FOR LINGUISTIC ANALYSIS.” Linguistics 7, no. 49 (1969). https://doi.org/10.1515/ling.1969.7.49.28.
