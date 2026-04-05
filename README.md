# KB-logical-reasoning
Create a logical knowledge base and query it.
<br><br>
Instructions to run code:
<br><br>
Run python reasoning.py.
<br><br>
The knowledge base syntax is as follows:
<br><br>
Use ^ for the "AND" operation, v for the "OR" operation and => for implication.<br>
Any alphanumeric variable name will work.
<br><br>
Only one operator in premises and only one variable in conclusion are allowed:
<br><br>
a^bvc => d will not work.<br>
a^b => d^c will not work.<br>
a^b => c will work.<br>
<br><br>
Type "nil" to finish typing in the knowledge base.
<br><br>
Then type queries by typing the name of the variable in question, followed by a question mark.
<br><br>
E.g. knowledge base:
<br><br>
P^Q => F<br>
PvA => Q<br>
P<br>
A<br>
nil<br>
<br><br>
E.g. query:<br>
A?<br>
