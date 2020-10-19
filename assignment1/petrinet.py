from assignment1.transition import Transition


class PetriNet:
    def __init__(self):
        self.places = []  # Each of the states
        self.transitions = []  # connects two states
        self.transitions_dic = {}
        self.edges = []
        self.tokens = []

    def add_place(self, name):
        self.places.append(name)

    def add_transition(self, name, id):
        t = Transition()
        t.id = id
        t.value = name
        self.transitions.append(t)
        self.transitions_dic[name] = id

    def add_edge(self, source, target):
        if target < 0:
            for transition in self.transitions:
                if transition.id == target:
                    transition.pre.append(source)
                    return self
        if source < 0:
            for transition in self.transitions:
                if transition.id == source:
                    transition.post.append(target)
                    return self

    def get_tokens(self, place):
        count = 0
        for token in self.tokens:
            if place == token:
                count += 1
        return count

    def is_enabled(self, transition):
        counter = 0
        for tran in self.transitions:
            if tran.id == transition:
                for pre in tran.pre:
                        if pre in self.tokens:
                            counter += 1

                #print("Transition: " + str(tran.id) + ", Preconditions " + str(tran.pre))
                if counter == len(tran.pre):
                    return True
                else:
                    return False

    def add_marking(self, place):
        self.tokens.append(place)

    def fire_transition(self, transition):
        # check there is a token in place before transition
        # check what places are connected with that transition
        # token = 2, 3
        # if self.is_enabled(transition) == False:
        #     return False

        for tran in self.transitions:
            if tran.id == transition:
                for pre in tran.pre:
                    self.tokens.remove(pre)
                for post in tran.post:
                    self.tokens.append(post)

    def transition_name_to_id(self, transition_value):
        for tran in self.transitions:
            if tran.value == transition_value:
                return tran.id

        return False


