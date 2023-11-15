#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Jeong Hin Chin
# Created Date: Nov 15, 2023
# version     : '1.0'
# ---------------------------------------------------------------------------

# TODO: Create children class for Voter
# NOTE: Assume the voters can be split into three political category: Left, Central, and Right
# NOTE: Assume the Race and Ethnicity of the voters are either Malay, Chinese, Indian, or Others


class Voter:
    """
    Represents an individual voter in the election model.

    Attributes:
        preference (str): The voter's current political preference.
    """

    def __init__(self, preference):
        """
        Initializes a Voter instance with a given preference.

        Parameters:
            preference (str): The initial political preference of the voter.
        """
        self.preference = preference

    def possibly_change_preference(self, influencers, change_probability):
        """
        Determines if the voter changes their preference based on influencers.

        The method randomly decides, based on the change_probability, whether to change
        the voter's preference to match that of a randomly selected influencer.

        Parameters:
            influencers (list of Voter): A list of Voter instances representing influencers.
            change_probability (float): Probability of the voter changing preference.
        """
        if random.random() < change_probability:
            influencer = random.choice(influencers)
            self.preference = influencer.preference


class ElectionModel:
    """
    Simulates an election with voters and influencers affecting voting preferences.

    Attributes:
        voters (list of Voter): A list of Voter instances representing the electorate.
        influencers (list of Voter): A list of Voter instances representing influential agents.
        change_probability (float): Probability of a voter changing their preference.
    """

    def __init__(self, num_voters, num_influencers, change_probability):
        """
        Initializes the ElectionModel with specified number of voters, influencers, and change probability.

        Parameters:
            num_voters (int): The number of voters in the simulation.
            num_influencers (int): The number of influencers in the simulation.
            change_probability (float): The probability of a voter changing their preference.
        """
        self.voters = [
            Voter(random.choice(["Party A", "Party B"])) for _ in range(num_voters)
        ]
        self.influencers = [
            Voter(random.choice(["Party A", "Party B"])) for _ in range(num_influencers)
        ]
        self.change_probability = change_probability

    def run_election_cycle(self):
        """
        Runs a single election cycle.

        During each cycle, each voter may change their preference based on the influence of the influencers.
        """
        for voter in self.voters:
            voter.possibly_change_preference(self.influencers, self.change_probability)

    def count_votes(self):
        """
        Counts the current votes for each party among all voters.

        Returns:
            tuple: A tuple containing the count of votes for each party (Party A, Party B).
        """
        return sum(voter.preference == "Party A" for voter in self.voters), sum(
            voter.preference == "Party B" for voter in self.voters
        )

    def simulate_election(self, cycles):
        """
        Simulates a specified number of election cycles and returns the voting results.

        Parameters:
            cycles (int): The number of election cycles to simulate.

        Returns:
            tuple of lists: Two lists containing the number of votes for each party after each cycle.
        """
        results_a, results_b = [], []
        for _ in range(cycles):
            self.run_election_cycle()
            votes_a, votes_b = self.count_votes()
            results_a.append(votes_a)
            results_b.append(votes_b)
        return results_a, results_b
