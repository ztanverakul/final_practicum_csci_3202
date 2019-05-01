#Zachary Tanverakul, Julien Rumsey Final Practicum Golf Bayes Network
## For the sake of brevity...
T, F = True, False

## From class:
def P(var, value, evidence={}):
    '''The probability distribution for P(var | evidence),
    when all parent variables are known (in evidence)'''
    if len(var.parents)==1:
        # only one parent
        row = evidence[var.parents[0]]
    else:
        # multiple parents
        row = tuple(evidence[parent] for parent in var.parents)
    return var.cpt[row] if value else 1-var.cpt[row]

class BayesNode:

    def __init__(self, name, parents, values, cpt):
        if isinstance(parents, str):
            parents = parents.split()

        if len(parents)==0:
            # if no parents, empty dict key for cpt
            cpt = {(): cpt}
        elif isinstance(cpt, dict):
            # if there is only one parent, only one tuple argument
            if cpt and isinstance(list(cpt.keys())[0], bool):
                cpt = {(v): p for v, p in cpt.items()}

        self.variable = name
        self.parents = parents
        self.cpt = cpt
        self.values = values
        self.children = []

    def __repr__(self):
        return repr((self.variable, ' '.join(self.parents)))


class BayesNet:
    '''Bayesian network containing only boolean-variable nodes.'''

    def __init__(self, nodes):
        '''Initialize the Bayes net by adding each of the nodes,
        which should be a list BayesNode class objects ordered
        from parents to children (`top` to `bottom`, from causes
        to effects)'''
        self.nodes = nodes
        self.variables = [node.variable for node in nodes]
        self.parents = [node.parents for node in nodes]
        self.cpt = [node.cpt for node in nodes]
        self.values = [node.values for node in nodes]
        self.children = [node.children for node in nodes]
        #print(self.nodes)



    def add(self, node):
        '''Add a new BayesNode to the BayesNet. The parents should all
        already be in the net, and the variable itself should not be'''
        assert node.variable not in self.variables
        assert all((parent in self.variables) for parent in node.parents)

        self.nodes.append(node)
        self.variables.append(node.variable)



    def find_node(self, var):
        '''Find and return the BayesNode in the net with name `var`'''
        for i in self.nodes:
            if i.variables == var:
                return(i)



    def find_values(self, var):
        '''Return the set of possible values for variable `var`'''
        return (var.values)



    def __repr__(self):
        return 'BayesNet({})'.format(self.nodes)


gir = BayesNode('gir', '', [T,F], 0.6740)
bird5  = BayesNode('bird5', ['p5', 'gir'], [T,F], {(T,T):0.5, (T,F):0.3, (F,T):0.15, (F,F):0.05})
p3 = BayesNode('p3', '', [T,F], 0.1079)
p4 = BayesNode('p4', '', [T,F], 0.1877)
p5 = BayesNode('p5', '', [T,F], 0.4789)

bird3  = BayesNode('bird3', ['p3', 'gir'], [T,F], {(T,T):0.3, (T,F):0.2, (F,T):0.09, (F,F):0.02})
bird4  = BayesNode('bird4', ['p4', 'gir'], [T,F], {(T,T):0.4, (T,F):0.2, (F,T):0.1, (F,F):0.04})
nodes = [p5, gir, bird5]
nodes2 = [p4, gir, bird4]
nodes3 = [p3, gir, bird3]

bayesnet = BayesNet(nodes)

print("Welcome to the Tiger Woods Augusta hole predictor!")

hole = input("Hi, what hole do you want? [3, 4, 5]")
green = input("Does Tiger hit the green in regulation? [y, n]")
par = input("Do you want to find Tiger's chances above or below par? [above, below]")

if (par == 'above'):
    probability = F
if (par == 'below'):
    probability = T

if (hole == "3"):
    if (green == 'y'):
        evid = {'p3':T, 'gir':T}
        print("Tigers probability of finishing", par, "par on a par", hole, "is:", P(bird3, probability, evid))
    if (green == 'n'):
        evid = {'p3':T, 'gir':F}
        print("Tigers probability of finishing", par, "par on a par", hole, "is:", P(bird3, probability, evid))

if (hole == "4"):
    if (green == 'y'):
        evid2 = {'p4':T, 'gir':T}
        print("Tigers probability of finishing", par, "par on a par", hole, "is:",P(bird4, probability, evid2))
    if (green == 'n'):
        evid2 = {'p4':T, 'gir':F}
        print("Tigers probability of finishing", par, "par on a par", hole, "is:", P(bird4, probability, evid2))

if (hole == "5"):
    if (green == 'y'):
        evid3 = {'p5':T, 'gir':T}
        print("Tigers probability of finishing", par, "par on a par", hole, "is:",P(bird5, probability, evid3))
    if (green == 'n'):
        evid3 = {'p5':T, 'gir':F}
        print("Tigers probability of finishing", par, "par on a par", hole, "is:", P(bird5, probability, evid3))
