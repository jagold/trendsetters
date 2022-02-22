from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

from otreeutils.pages import AllGroupsWaitPage, ExtendedPage, UnderstandingQuestionsPage, APPS_DEBUG

class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'
    body_text = "Waiting for other participants to decide."


class Results(Page):
    def app_after_this_page(self, upcoming_apps):
        if self.subsession.vars_for_admin_report() == {'decisionlist': ['Green','Green','Green','Green']}:
            return "end"


page_sequence = [Decision, ResultsWaitPage, Results]