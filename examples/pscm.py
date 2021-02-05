#***************** Problem Formulation *****************

'''
1. The state representation. These are the attributes and values that are used to describe the different
states of the problem.

2. The initial state creation. An operator will generate the state where the problem solving starts.

3. State elaboration rules. These rules elaborate the state with additional structures that aren’t
fundamental to the state (they aren’t created and deleted by operator application rules), but are
derived from the core aspect of the state. Thus, they are entailments that are useful abstractions,
often making it possible to create simpler rules for proposing and comparing operators.

4. The operator proposal rules. These are the rules that propose the legal state transformations that can
be made toward solving the problem. We can define this as classes of operators:

Eg: A -> A, A -> B, B -> A

5. The operator application rules. These are the rules that transform the state when an operator is
selected.

6. The operator and state monitoring rules. These are optional rules that print out the operator as it
applies and prints out the current state.

7. The desired state recognition rule. This is a rule that notices when one of the desired states is
achieved.

8. The search control rules. These are optional rules that prefer the selection of one operator over
another. Their purpose is to avoid useless operators and/or direct the search toward the desired
state. Theoretically you could encode enough rules so that the correct operator is always selected for
each state. However, you would have had to already solved the problem yourself to figure out those
rules. Our goal is to have the program solve the problem, using only knowledge available from the
problem statement and possibly some general knowledge about problem solving. Therefore, search
control will be restricted to general problem solving heuristics.
'''