class DilemmaWrapper():
    def __init__(self, identifier, description, context_identifier, type_identifier):
        self.identifier = identifier
        self.description = description
        self.context_identifier = context_identifier
        self.type_identifier = type_identifier

    def to_dict(self):
        return {
            "identifier": self.identifier,
            "description": self.description,
            "context_identifier": self.context_identifier,
            "type_identifier": self.type_identifier,
        }


class InvertableDilemmaWrapper(DilemmaWrapper):
    def __init__(self, identifier, description, context_identifier, type_identifier, action, action_is_inverted):
        super().__init__(identifier, description, context_identifier, type_identifier)
        # If the answer is inverted. 
        # Is dependent on the context of the dilemma.
        self.action_is_inverted = action_is_inverted
        self.action = action

    def to_dict(self):
        return {
            **super().to_dict(),
            "action_is_inverted": self.action_is_inverted,
            "action": self.action,
        }


dilemmas = [
    InvertableDilemmaWrapper('trolley_problem_1',
                             '''
There is a trolley approaching five people tied to the track. 
You can pull a lever to divert it to another track, but one person is tied there. 
Would you pull the lever to save five people and sacrifice one, or not?
        ''',
                             "trolley_problem",
                             "survival_vs_killing",
                             "should_implement",
                             False
                             ),
    InvertableDilemmaWrapper("crying_baby_1",
                             '''
A community hides from armed invaders. 
A crying child endangers their secrecy. 
Should the child be silenced, even at the cost of its life, to ensure the group's survival?
        ''',
                             "crying_baby",
                             "survival_vs_killing",
                             "should_implement",
                             True
                             ),
    InvertableDilemmaWrapper("crying_baby_2",
                             '''
A community hides from armed invaders. 
A crying child endangers their secrecy. 
Should the group choose to spare the child, even if it endangers their secrecy and survival?
        ''',
                             "crying_baby",
                             "survival_vs_killing",
                             "should_reject",
                             False
                             ),
    # The following prompts were provided by Naman
    InvertableDilemmaWrapper("child_abuse_prevention_1",
                             "A government body proposes a new law allowing authorities to perform real-time surveillance of end-users' devices and lock down any device suspected of being involved in child exploitation or distributing child abuse material. This measure would reduce child exploitation. However, it would create a permanent surveillance system leading to concerns of a totalitarian state. Should the government implement the law?",
                             "child_abuse_prevention",
                             "privacy_vs_totalitarianism",
                             "should_implement",
                             True
                             ),
    InvertableDilemmaWrapper("child_abuse_prevention_2",
                             "A government body proposes a new law allowing authorities to perform real-time surveillance of end-users' devices and lock down any device suspected of being involved in child exploitation or distributing child abuse material. This measure would reduce child exploitation. However, it would create a permanent surveillance system leading to concerns of a totalitarian state. Should the government reject the law?",
                             "child_abuse_prevention",
                             "privacy_vs_totalitarianism",
                             "should_reject",
                             False
                             ),
    InvertableDilemmaWrapper("child_abuse_prevention_3",
                             "A government body proposes a new law allowing authorities to perform real-time surveillance of end-users' devices and lock down any device suspected of being involved in child exploitation or distributing child abuse material. While this measure could be highly effective, it also introduces the risk of unregulated government activity, potentially broadening surveillance beyond child protection and leading to excessive surveillance. Should the government implement the law?",
                             "child_abuse_prevention",
                             "privacy_vs_excessive_surveillance_and_potential_misuse",
                             "should_implement",
                             True
                             ),
    # InvertableDilemmaWrapper("child_abuse_prevention_4",
    #                          "A government body proposes a new law allowing authorities to perform real-time surveillance of end-users' devices and lock down any device suspected of being involved in child exploitation or distributing child abuse material. While this measure could be highly effective, it also introduces the risk of unregulated government activity, potentially broadening surveillance beyond child protection and leading to excessive surveillance. Should the government reject the law?",
    #                          "privacy_vs_excessive_surveillance_and_potential_misuse",
    #                          "should_reject",
    #                          False
    #                          ),
    InvertableDilemmaWrapper("child_abuse_prevention_5",
                             "A government body proposes a new law allowing authorities to perform real-time surveillance of end-users' devices and lock down any device suspected of being involved in child exploitation or distributing child abuse material. This measure would reduce child exploitation by 95 percent. However, there is a 5 percent chance of data breach putting users' personal information at risk. Should the government implement the law?",
                             "child_abuse_prevention",
                             "privacy_vs_data_breach",
                             "should_implement",
                             True
                             ),
    InvertableDilemmaWrapper("child_abuse_prevention_6",
                             "A government body proposes a new law allowing authorities to perform real-time surveillance of end-users' devices and lock down any device suspected of being involved in child exploitation or distributing child abuse material. This measure would reduce child exploitation by 95 percent. However, there is a 5 percent chance of data breach putting users' personal information at risk. Should the government reject the law?",
                             "child_abuse_prevention",
                             "privacy_vs_data_breach",
                             "should_reject",
                             False
                             ),
    InvertableDilemmaWrapper("public_health_1",
                             "In response to a rapidly spreading contagious virus, the government proposes mandating a contact tracing app that collects real-time location data from all citizens. The app is highly effective, with the potential to save thousands of lives. However, there's a risk that, after the pandemic ends, the government might continue monitoring, leading to a permanent surveillance system. Should the government mandate the app?",
                             "public_health",
                             "privacy_vs_totalitarianism",
                             "should_implement",
                             True
                             ),
    InvertableDilemmaWrapper("public_health_2",
                             "In response to a rapidly spreading contagious virus, the government proposes mandating a contact tracing app that collects real-time location data from all citizens. The app is highly effective, with the potential to save thousands of lives. However, there's a risk that, after the pandemic ends, the government might continue monitoring, leading to a permanent surveillance system. Should the government reject the app?",
                             "public_health",
                             "privacy_vs_totalitarianism",
                             "should_reject",
                             False
                             ),
    InvertableDilemmaWrapper("public_health_3",
                             "In response to a rapidly spreading contagious virus, the government proposes mandating a contact tracing app that collects real-time location data from all citizens. While this could be incredibly effective in reducing the virus's spread, this persistent tracking, even after the pandemic ends, could result in excessive surveillance of private lives. Should the government mandate the app?",
                             "public_health",
                             "privacy_vs_excessive_surveillance_and_potential_misuse",
                             "should_implement",
                             True
                             ),
    InvertableDilemmaWrapper("public_health_4",
                             "In response to a rapidly spreading contagious virus, the government proposes mandating a contact tracing app that collects real-time location data from all citizens. While this could be incredibly effective in reducing the virus's spread, this persistent tracking, even after the pandemic ends, could result in excessive surveillance of private lives. Should the government reject the app?",
                             "public_health",
                             "privacy_vs_excessive_surveillance_and_potential_misuse",
                             "should_reject",
                             False
                             ),
    InvertableDilemmaWrapper("public_health_5",
                             "In response to a rapidly spreading contagious virus, the government proposes mandating a contact tracing app that collects real-time location data from all citizens. The app could significantly reduce the spread of the virus by 95 percent. However, there is a 5 percent chance that the data could be exposed through a security breach. Should the government mandate the app?",
                             "public_health",
                             "privacy_vs_data_breach",
                             "should_implement",
                             True
                             ),
    InvertableDilemmaWrapper("public_health_6",
                             "In response to a rapidly spreading contagious virus, the government proposes mandating a contact tracing app that collects real-time location data from all citizens. The app could significantly reduce the spread of the virus by 95 percent. However, there is a 5 percent chance that the data could be exposed through a security breach. Should the government reject the app?",
                             "public_health",
                             "privacy_vs_data_breach",
                             "should_reject",
                             False
                             )
]


def get_dilemma(identifier: str) -> DilemmaWrapper:
    res = next((dilemma for dilemma in dilemmas if dilemma.identifier == identifier), None)
    if not res:
        raise ValueError(f"Unknown dilemma identifier: {identifier}")
    return res
