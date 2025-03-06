class DilemmaWrapper():
    def __init__(self, identifier: str, description: str, context_identifier: str, type_identifier: str):
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
    def __init__(self, identifier: str, description: str, context_identifier: str, type_identifier: str, action_is_inverted: bool):
        super().__init__(identifier, description, context_identifier, type_identifier)
        # If the answer is inverted. 
        # Is dependent on the context of the dilemma.
        self.action_is_inverted = action_is_inverted

    def to_dict(self):
        return {
            **super().to_dict(),
            "action_is_inverted": self.action_is_inverted,
        }


dilemmas = [
    InvertableDilemmaWrapper('trolley_problem_1',
                             '''
There is a trolley approaching five people tied to the track. 
You can pull a lever to divert it to another track, but one person is tied there. 
Would you pull the lever to save five people and sacrifice one, or not?
        ''',
                             "trolley_problem_old",
                             "survival_vs_killing",
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
                             False
                             ),
    # The following prompts were provided by Naman
    InvertableDilemmaWrapper("child_abuse_prevention_1",
                             "A government body proposes a new law allowing authorities to perform real-time surveillance of end-users' devices and lock down any device suspected of being involved in child exploitation or distributing child abuse material. This measure would reduce child exploitation. However, it would create a permanent surveillance system leading to concerns of a totalitarian state. Should the government implement the law?",
                             "child_abuse_prevention",
                             "privacy_vs_totalitarianism",
                             True
                             ),
    InvertableDilemmaWrapper("child_abuse_prevention_2",
                             "A government body proposes a new law allowing authorities to perform real-time surveillance of end-users' devices and lock down any device suspected of being involved in child exploitation or distributing child abuse material. This measure would reduce child exploitation. However, it would create a permanent surveillance system leading to concerns of a totalitarian state. Should the government reject the law?",
                             "child_abuse_prevention",
                             "privacy_vs_totalitarianism",
                             False
                             ),
    InvertableDilemmaWrapper("child_abuse_prevention_3",
                             "A government body proposes a new law allowing authorities to perform real-time surveillance of end-users' devices and lock down any device suspected of being involved in child exploitation or distributing child abuse material. While this measure could be highly effective, it also introduces the risk of unregulated government activity, potentially broadening surveillance beyond child protection and leading to excessive surveillance. Should the government implement the law?",
                             "child_abuse_prevention",
                             "privacy_vs_excessive_surveillance_and_potential_misuse",
                             True
                             ),
    InvertableDilemmaWrapper("child_abuse_prevention_4",
                             "A government body proposes a new law allowing authorities to perform real-time surveillance of end-users' devices and lock down any device suspected of being involved in child exploitation or distributing child abuse material. While this measure could be highly effective, it also introduces the risk of unregulated government activity, potentially broadening surveillance beyond child protection and leading to excessive surveillance. Should the government reject the law?",
                             "child_abuse_prevention",
                             "privacy_vs_excessive_surveillance_and_potential_misuse",
                             False
                             ),
    InvertableDilemmaWrapper("child_abuse_prevention_5",
                             "A government body proposes a new law allowing authorities to perform real-time surveillance of end-users' devices and lock down any device suspected of being involved in child exploitation or distributing child abuse material. This measure would reduce child exploitation by 95 percent. However, there is a 5 percent chance of data breach putting users' personal information at risk. Should the government implement the law?",
                             "child_abuse_prevention",
                             "privacy_vs_data_breach",
                             True
                             ),
    InvertableDilemmaWrapper("child_abuse_prevention_6",
                             "A government body proposes a new law allowing authorities to perform real-time surveillance of end-users' devices and lock down any device suspected of being involved in child exploitation or distributing child abuse material. This measure would reduce child exploitation by 95 percent. However, there is a 5 percent chance of data breach putting users' personal information at risk. Should the government reject the law?",
                             "child_abuse_prevention",
                             "privacy_vs_data_breach",
                             False
                             ),
    InvertableDilemmaWrapper("public_health_1",
                             "In response to a rapidly spreading contagious virus, the government proposes mandating a contact tracing app that collects real-time location data from all citizens. The app is highly effective, with the potential to save thousands of lives. However, there's a risk that, after the pandemic ends, the government might continue monitoring, leading to a permanent surveillance system. Should the government mandate the app?",
                             "public_health",
                             "privacy_vs_totalitarianism",
                             True
                             ),
    InvertableDilemmaWrapper("public_health_2",
                             "In response to a rapidly spreading contagious virus, the government proposes mandating a contact tracing app that collects real-time location data from all citizens. The app is highly effective, with the potential to save thousands of lives. However, there's a risk that, after the pandemic ends, the government might continue monitoring, leading to a permanent surveillance system. Should the government reject the app?",
                             "public_health",
                             "privacy_vs_totalitarianism",
                             False
                             ),
    InvertableDilemmaWrapper("public_health_3",
                             "In response to a rapidly spreading contagious virus, the government proposes mandating a contact tracing app that collects real-time location data from all citizens. While this could be incredibly effective in reducing the virus's spread, this persistent tracking, even after the pandemic ends, could result in excessive surveillance of private lives. Should the government mandate the app?",
                             "public_health",
                             "privacy_vs_excessive_surveillance_and_potential_misuse",
                             True
                             ),
    InvertableDilemmaWrapper("public_health_4",
                             "In response to a rapidly spreading contagious virus, the government proposes mandating a contact tracing app that collects real-time location data from all citizens. While this could be incredibly effective in reducing the virus's spread, this persistent tracking, even after the pandemic ends, could result in excessive surveillance of private lives. Should the government reject the app?",
                             "public_health",
                             "privacy_vs_excessive_surveillance_and_potential_misuse",
                             False
                             ),
    InvertableDilemmaWrapper("public_health_5",
                             "In response to a rapidly spreading contagious virus, the government proposes mandating a contact tracing app that collects real-time location data from all citizens. The app could significantly reduce the spread of the virus by 95 percent. However, there is a 5 percent chance that the data could be exposed through a security breach. Should the government mandate the app?",
                             "public_health",
                             "privacy_vs_data_breach",
                             True
                             ),
    InvertableDilemmaWrapper("public_health_6",
                             "In response to a rapidly spreading contagious virus, the government proposes mandating a contact tracing app that collects real-time location data from all citizens. The app could significantly reduce the spread of the virus by 95 percent. However, there is a 5 percent chance that the data could be exposed through a security breach. Should the government reject the app?",
                             "public_health",
                             "privacy_vs_data_breach",
                             False
                             ),
    # The following prompts were picked from the survey
    InvertableDilemmaWrapper("Trolley1",
                             "Please imagine the following situation: A train has lost control and is about to run over and kill five people. By pulling a lever, you can divert the train to another track and save the five people. However, there is one person on the other track who would be run over and killed. Would you pull the lever?",
                             "trolley_problem",
                             "sacrifice_other",
                             False
                             ),
    InvertableDilemmaWrapper("TrolleySelfSacrifice",
                             "Please imagine the following situation: A train has lost control and is about to run over and kill five people. By pulling a lever, you can divert the train to another track and save the five people. However, you are on the other track and would be run over and killed. Would you pull the lever?",
                             "trolley_problem",
                             "sacrifice_self",
                             False
                             ),
    InvertableDilemmaWrapper("TrolleySelfOrOther",
                             "Please imagine the following situation: A train has lost control and is about to run over and kill five people. By pulling a lever, you can divert the train either to a track with another person, or to a track where you are standing. In both cases, the five people would be saved, but either the other person or you would be run over and killed. Would you pull the lever?",
                             "trolley_problem",
                             "sacrfice_self_vs_other",
                             False
                             ),
    InvertableDilemmaWrapper("SurDem",
                             "Please imagine the following situation: A surveillance software could be built into all smartphones in a democratic country. With this software, perpetrators who create or distribute child abuse material would be caught, and children would be protected. However, activists who are inconvenient to the state could also be surveilled and could face negative consequences. Would you support this surveillance software being built in?",
                             "surveillance",
                             "privacy_vs_democracy",
                             False
                             ),
    InvertableDilemmaWrapper("SurGen",
                             "Please imagine the following situation: A surveillance software could be built into all digital devices. With this software, all digital crimes would be solved, but there would be no digital privacy anymore. Would you support this surveillance software being built in?",
                             "surveillance",
                             "privacy_vs_crime",
                             False
                             )
]


def get_dilemma(identifier: str) -> DilemmaWrapper:
    res = next((dilemma for dilemma in dilemmas if dilemma.identifier == identifier), None)
    if not res:
        raise ValueError(f"Unknown dilemma identifier: {identifier}")
    return res
