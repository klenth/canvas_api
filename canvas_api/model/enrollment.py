from .model import Model
from .util import date_fields, model_field
from .grade import Grade
from .user import User

class Enrollment(Model):
    _fields = (
        'id',
        'course_id',
        'sis_course_id', 'course_integration_id',
        'course_section_id',
        'section_integration_id',
        'sis_account_id', 'sis_section_id', 'sis_user_id',
        'enrollment_state',
        'limit_privileges_to_course_section',
        'sis_import_id',
        'root_account_id',
        'type',
        'user_id',
        'associated_user_id',
        'role', 'role_id',
        *date_fields(
            'created_at', 'updated_at', 'started_at', 'end_at',
            'last_activity_at', 'last_attended_at',
        ),
        'total_activity_time',
        'html_url',
        model_field('grades', Grade),
        model_field('user', User),
        'override_grade', 'override_score',
        'unposted_current_grade', 'unposted_final_grade',
        'unposted_current_score', 'unposted_final_score',
        'has_grading_periods',
        'totals_for_all_grading_periods_option',
        'current_grading_period_title',
        'current_grading_period_id',
        'current_period_override_grade',
        'current_period_override_score',
        'current_period_unposted_current_score',
        'current_period_unposted_final_score',
        'current_period_unposted_current_grade',
        'current_period_unposted_final_grade',
    )
