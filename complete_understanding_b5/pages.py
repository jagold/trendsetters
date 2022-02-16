from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import random


from otreeutils.pages import AllGroupsWaitPage, ExtendedPage, UnderstandingQuestionsPage, APPS_DEBUG

class Introduction(Page):
    pass

class Q(UnderstandingQuestionsPage):
    page_title = 'Comprehension Question'
    set_correct_answers = False   # do not fill out the correct answers in advance (this is for fast skipping through pages)
    form_model = 'player'
    form_field_n_wrong_attempts = 'comprehension_wrong_attempts'
    questions = [
        {
            'question': 'For this block, what is the maximum payoff per round?',
            'options': ['$20', '$12', '$8', '$4'],
            'correct': '$4',
            'hint': 'Please review instructions below.'
        },
    ]

page_sequence = [Introduction, Q]