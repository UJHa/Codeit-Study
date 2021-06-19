from typing import List, Text


class NoAgentFoundException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Agent(object):
    def __init__(self, name, skills, load):
        self._name = name
        self._skills = skills
        self._load = load

    def __str__(self):
        return "<Agent: {}>".format(self._name)

    def agent_can_load(self, restrictions: List[str]):
        for restriction in restrictions:
            if restriction in self._skills and self._load <= 3:
                return True

        return False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def skills(self):
        return self._skills

    @skills.setter
    def skills(self, skills):
        self._skills = skills

    @property
    def load(self):
        return self._load

    @load.setter
    def load(self, load):
        self._load = load




class Ticket(object):
    def __init__(self, id: str, restrictions: List[str]):
        self._id = id
        self._restrictions = restrictions

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def restrictions(self):
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        self._restrictions = restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        # raise NoAgentFoundException('[ERROR] class FinderPolicy > func _filter_loaded_agents')
        pass

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        # raise NoAgentFoundException('[ERROR] class FinderPolicy > func find')
        pass


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        least_agent = None
        for agent in agents:
            if agent.agent_can_load(ticket._restrictions):
                if least_agent is None:
                    least_agent = agent

                if agent._load <= least_agent._load:
                    least_agent = agent

        if least_agent is not None:
            least_agent._load += 1
            print(least_agent)
            return least_agent
        else:
            raise NoAgentFoundException('[ERROR] class LeastLoadedAgent > func find')


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        least_flexible_agent = None
        for agent in agents:
            if agent.agent_can_load(ticket._restrictions):
                if least_flexible_agent is None:
                    least_flexible_agent = agent

                if len(agent._skills) <= len(least_flexible_agent._skills):
                    least_flexible_agent = agent

        if least_flexible_agent is not None:
            least_flexible_agent._load += 1
            print(least_flexible_agent)
            return least_flexible_agent
        else:
            raise NoAgentFoundException('[ERROR] class LeastFlexibleAgent > func find')


ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)

least_loaded_policy = LeastLoadedAgent()
# returns the Agent with name "B" because of their currently lower load.
least_loaded_policy.find(ticket, [agent1, agent2])

least_flexible_policy = LeastFlexibleAgent()
# returns the Agent with name "A" because of their lower flexibility.
least_flexible_policy.find(ticket, [agent1, agent2])