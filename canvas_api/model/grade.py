from .model import Model

class Grade(Model):

    _fields = (
        'html_url',
        'current_grade', 'final_grade',
        'current_score', 'final_score',
        'current_points',
        'unposted_current_grade', 'unposted_final_grade',
        'unposted_current_score', 'unposted_final_score',
        'unposted_current_points',
    )
