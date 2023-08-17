from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class graph_01(Page):
    form_model = 'player'
    form_fields = ['has_cultivo_1', 'has_cultivo_2', 'time_cultivos', 'cnt_mistakes', 'question_1_cultivos', 'question_2_cultivos', 'question_3_cultivos', 'question_4_cultivos']
    def vars_for_template(self):
        return {
                'labels': Constants.anhos,
                'data_a': Constants.cultivo_1,
                'data_b': Constants.cultivo_2,
                'max_y': max(Constants.cultivo_1 + Constants.cultivo_2),
                'min_y': min(Constants.cultivo_1 + Constants.cultivo_2),
                'time_steps': Constants.time_steps,
                'investment_max': Constants.investment_max,
                'graphType': self.player.participant.vars['graphType']
                }

class instructions(Page):
    pass

page_sequence = [instructions, graph_01]
