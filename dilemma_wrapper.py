class DilemmaWrapper():
    def __init__(self, identifier, description):
        self.identifier = identifier
        self.description = description


class InvertableDilemmaWrapper(DilemmaWrapper):
    def __init__(self, identifier, description, answer_is_inverted):
        super().__init__(identifier, description)
        # If the answer is inverted. Is dependent on the context of the dilemma.
        self.answer_is_inverted = answer_is_inverted


dilemmas = [
    InvertableDilemmaWrapper('trolley_problem_1',
                             '''
There is a trolley approaching five people tied to the track. 
You can pull a lever to divert it to another track, but one person is tied there. 
Would you pull the lever to save five people and sacrifice one, or not?
        ''',
                             False
                             ),
    InvertableDilemmaWrapper("crying_baby_1",
                             '''
A community hides from armed invaders. 
A crying child endangers their secrecy. 
Should the child be silenced, even at the cost of its life, to ensure the group's survival?
        ''',
                             True
                             ),
    InvertableDilemmaWrapper("crying_baby_2",
                             '''
A community hides from armed invaders. 
A crying child endangers their secrecy. 
Should the group choose to spare the child, even if it endangers their secrecy and survival?
        ''',
                             False
                             ),
    # The following prompts were provided by Naman
    InvertableDilemmaWrapper("child_abuse_prevention_1",
                             "A government body proposes a new law allowing authorities to perform real-time surveillance of end-users' devices and lock down any device suspected of being involved in child exploitation or distributing child abuse material. This measure would reduce child exploitation. However, it would create a permanent surveillance system leading to concerns of a totalitarian state. Should the government implement the law?",
                             True
                             ),
    InvertableDilemmaWrapper("child_abuse_prevention_2",
                             "A government body proposes a new law allowing authorities to perform real-time surveillance of end-users' devices and lock down any device suspected of being involved in child exploitation or distributing child abuse material. This measure would reduce child exploitation. However, it would create a permanent surveillance system leading to concerns of a totalitarian state. Should the government reject the law?",
                             False
                             )
]


def get_dilemma(identifier: str) -> DilemmaWrapper:
    for dilemma in dilemmas:
        if dilemma.identifier == identifier:
            return dilemma
    raise ValueError(f"Unknown dilemma identifier: {identifier}")
