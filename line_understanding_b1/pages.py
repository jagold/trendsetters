from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import random


from otreeutils.pages import AllGroupsWaitPage, ExtendedPage, UnderstandingQuestionsPage, APPS_DEBUG

colors = ['Purple','Green','Yellow','Unknown']
players = ['Q', 'R', 'T', 'S', 'Unknown']

class MyWaitPage(WaitPage):
    group_by_arrival_time = True
    body_text = "Sorting you into a group."

class Introduction(Page):
    pass

class Q(UnderstandingQuestionsPage):
    def is_displayed(self):
        return self.player.id_in_group == 1
    template_name = None
    page_title = 'Comprehension Questions'
    set_correct_answers = False   # do not fill out the correct answers in advance (this is for fast skipping through pages)
    form_model = 'player'
    form_field_n_wrong_attempts = 'comprehension_wrong_attempts'
    questions = [
        {
            'question': 'What is your maximum payoff in each round?',
            'options': random.sample(['28 points', '20 points', '12 points', '4 points', 'Unknown'], 5),
            'correct': '12 points',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which player are you?',
            'options': random.sample(players, 5),
            'correct': players[0],
            'hint': 'Please see diagram above and instructions below.'
        },
        {
            'question': 'Whose payoffs are shown to you at the end of each round?',
            'options': random.sample({'Only your own', "Nobody's", "Everyone's", "Your own and those of players adjacent to you"}, 4),
            'correct': 'Only your own',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Can the way payoffs are calculated change within each block of ten rounds?',
            'options': random.sample(['Yes', 'No'], 2),
            'correct': 'No',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Can the way payoffs are calculated change from block to block?',
            'options': random.sample(['Yes (and you will be told if they changed)', 'No'], 2),
            'correct': 'Yes (and you will be told if they changed)',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player Q choose?',
            'options': random.sample(colors, 4),
            'correct': 'Purple',
            'hint': 'Please see diagram above and instructions below.'
        },
        {
            'question': 'Which color did Player R choose?',
            'options': random.sample(colors, 4),
            'correct': 'Green',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player S choose?',
            'options': random.sample(colors, 4),
            'correct': 'Unknown',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player T choose?',
            'options': random.sample(colors, 4),
            'correct': 'Unknown',
            'hint': 'Please review instructions below.'
        },
    ]

class R(UnderstandingQuestionsPage):
    def is_displayed(self):
        return self.player.id_in_group == 2
    template_name = None
    page_title = 'Comprehension Questions'
    set_correct_answers = False   # do not fill out the correct answers in advance (this is for fast skipping through pages)
    form_model = 'player'
    form_field_n_wrong_attempts = 'comprehension_wrong_attempts'
    questions = [
        {
            'question': 'What is your maximum payoff in each round?',
            'options': random.sample(['28 points', '20 points', '12 points', '4 points', 'Unknown'], 5),
            'correct': '12 points',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which player are you?',
            'options': random.sample(players, 5),
            'correct': players[1],
            'hint': 'Please see diagram above and instructions below.'
        },
        {
            'question': 'Whose payoffs are shown to you at the end of each round?',
            'options': random.sample({'Only your own', "Nobody's", "Everyone's", "Your own and those of players adjacent to you"}, 4),
            'correct': 'Only your own',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Can the way payoffs are calculated change within each block of ten rounds?',
            'options': random.sample(['Yes', 'No'], 2),
            'correct': 'No',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Can the way payoffs are calculated change from block to block?',
            'options': random.sample(['Yes (and you will be told if they changed)', 'No'], 2),
            'correct': 'Yes (and you will be told if they changed)',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player Q choose?',
            'options': random.sample(colors, 4),
            'correct': 'Green',
            'hint': 'Please see diagram above and instructions below.'
        },
        {
            'question': 'Which color did Player R choose?',
            'options': random.sample(colors, 4),
            'correct': 'Purple',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player S choose?',
            'options': random.sample(colors, 4),
            'correct': 'Purple',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player T choose?',
            'options': random.sample(colors, 4),
            'correct': 'Unknown',
            'hint': 'Please review instructions below.'
        },
    ]


class T(UnderstandingQuestionsPage):
    def is_displayed(self):
        return self.player.id_in_group == 3
    template_name = None
    page_title = 'Comprehension Questions'
    set_correct_answers = False   # do not fill out the correct answers in advance (this is for fast skipping through pages)
    form_model = 'player'
    form_field_n_wrong_attempts = 'comprehension_wrong_attempts'
    questions = [
        {
            'question': 'What is your maximum payoff in each round?',
            'options': random.sample(['28 points', '20 points', '12 points', '4 points', 'Unknown'], 5),
            'correct': '12 points',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which player are you?',
            'options': random.sample(players, 5),
            'correct': players[2],
            'hint': 'Please see diagram above and instructions below.'
        },
        {
            'question': 'Whose payoffs are shown to you at the end of each round?',
            'options': random.sample({'Only your own', "Nobody's", "Everyone's", "Your own and those of players adjacent to you"}, 4),
            'correct': 'Only your own',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Can the way payoffs are calculated change within each block of ten rounds?',
            'options': random.sample(['Yes', 'No'], 2),
            'correct': 'No',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Can the way payoffs are calculated change from block to block?',
            'options': random.sample(['Yes (and you will be told if they changed)', 'No'], 2),
            'correct': 'Yes (and you will be told if they changed)',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player Q choose?',
            'options': random.sample(colors, 4),
            'correct': 'Unknown',
            'hint': 'Please see diagram above and instructions below.'
        },
        {
            'question': 'Which color did Player R choose?',
            'options': random.sample(colors, 4),
            'correct': 'Green',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player S choose?',
            'options': random.sample(colors, 4),
            'correct': 'Yellow',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player T choose?',
            'options': random.sample(colors, 4),
            'correct': 'Purple',
            'hint': 'Please review instructions below.'
        },
    ]


class S(UnderstandingQuestionsPage):
    def is_displayed(self):
        return self.player.id_in_group == 4
    template_name = None
    page_title = 'Comprehension Questions'
    set_correct_answers = False   # do not fill out the correct answers in advance (this is for fast skipping through pages)
    form_model = 'player'
    form_field_n_wrong_attempts = 'comprehension_wrong_attempts'
    questions = [
        {
            'question': 'What is your maximum payoff in each round?',
            'options': random.sample(['28 points', '20 points', '12 points', '4 points', 'Unknown'], 5),
            'correct': '12 points',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which player are you?',
            'options': random.sample(players, 5),
            'correct': players[3],
            'hint': 'Please see diagram above and instructions below.'
        },
        {
            'question': 'Whose payoffs are shown to you at the end of each round?',
            'options': random.sample({'Only your own', "Nobody's", "Everyone's", "Your own and those of players adjacent to you"}, 4),
            'correct': 'Only your own',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Can the way payoffs are calculated change within each block of ten rounds?',
            'options': random.sample(['Yes', 'No'], 2),
            'correct': 'No',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Can the way payoffs are calculated change from block to block?',
            'options': random.sample(['Yes (and you will be told if they changed)', 'No'], 2),
            'correct': 'Yes (and you will be told if they changed)',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player Q choose?',
            'options': random.sample(colors, 4),
            'correct': 'Unknown',
            'hint': 'Please see diagram above and instructions below.'
        },
        {
            'question': 'Which color did Player R choose?',
            'options': random.sample(colors, 4),
            'correct': 'Unknown',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player S choose?',
            'options': random.sample(colors, 4),
            'correct': 'Purple',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player T choose?',
            'options': random.sample(colors, 4),
            'correct': 'Green',
            'hint': 'Please review instructions below.'
        },
    ]

page_sequence = [MyWaitPage, Introduction, Q, R, S, T]