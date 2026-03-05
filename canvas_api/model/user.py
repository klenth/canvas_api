from .model import Model

class User(Model):

    _fields = [
        'id',
        'name', 'sortable_name', 'last_name', 'first_name', 'short_name',
        'sis_user_id', 'sis_import_id', 'integration_id',
        'login_id',
        'avatar_url', 'avatar_state',
        'enrollments',
        'email',
        'locale',
        'last_login',
        'time_zone',
        'bio',
        'pronouns',
    ]

    #def __init__(self, **kwargs):
    #    super().__init__(**kwargs)


    def __str__(self):
        return f'User(id={self.id},name={self.name})'

