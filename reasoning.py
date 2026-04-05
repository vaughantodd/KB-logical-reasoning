from collections import deque

def debug(string):
    if DEBUG:
        print(string)


print("Enter KB using ^, v and =>. Type nil when done\n" \
"Note: only one v or ^ allowed in premises and only one variable as conclusion, if ^ is present, v will be treated as a letter.\n")
DEBUG = False
facts = set()
rules = {}
_in = ""
while(_in != "nil"):
    _in = input("kb>> ")
    if _in == "nil":
        break
    elif _in == "debug":
        DEBUG = True
        continue
    if "=>" not in _in:
        #Is a fact
        debug(f"Added fact \"{_in}\"")
        facts.add(_in)
        continue
    else:
        premises = []
        ruletype = None
        #Is a rule
        parts = _in.split("=>")
        if len(parts) != 2:
            #Invalid, has too many implies
            print("kb>> Invalid input")
            continue
        body = parts[0].strip() #Before =>
        conclusion = parts[1].strip() #After =>
        debug(f"Body: {body}, Conclusion: {conclusion}")
        if body:
            if "^" in body:
                premises = [p.strip() for p in body.split("^")]
                ruletype = "AND"
            elif "v" in body:
                premises = [p.strip() for p in body.split("v")]
                ruletype = "OR"
            else:
                premises = [body]
                ruletype = "AND"
        else:
            print("kb>> Invalid input, must contain body")
        
        if ruletype is not None:
            if conclusion not in rules:
                rules[conclusion] = []
            rules[conclusion].append({"type":ruletype,"premises":premises})

print("Enter queries with ? after (or \"quit\"):")

def prove(goal, rules, facts, visited):
    proved = False
    debug(f"Attempting to prove {goal}")
    if goal in facts:
        debug(f"{goal} is a fact, returning true")
        return True
    if goal in visited:
        debug(f"{goal} already visited, returning false")
        return False
    visited.add(goal)
    for rule in rules.get(goal,[]):
        if rule["type"] == "AND":
            debug(f"Trying rule: {"^".join(rule["premises"])} => {goal}")
            proved = all([prove(p, rules, facts, visited) for p in rule["premises"]])
            debug(f"{"^".join(rule["premises"])} is {proved.__repr__().lower()}, therefore {goal} is {"true" if proved else "unproved"}")
        if rule["type"] == "OR":
            debug(f"Trying rule: {"v".join(rule["premises"])} => {goal}")
            proved = any([prove(p, rules, facts, visited) for p in rule["premises"]])
            debug(f"{"v".join(rule["premises"])} is {proved.__repr__().lower()}, therefore {goal} is {"true" if proved else "unproved"}")
        if proved:
            break
    visited.remove(goal)
    return proved


while True:
    query = input("query>> ").strip()
    if query == "quit":
        break
    if query == "debug":
        DEBUG = True
        continue
    if query.endswith("?"):
        goal = query[:-1].strip()
        ans = "yes" if prove(goal, rules, facts, set()) else "no"
        print("ans>> " + ans)
