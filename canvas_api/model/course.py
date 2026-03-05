from .model import Model
from .util import date_fields, model_field, model_list_field

from .enrollment import Enrollment

class Term(Model):
    _fields = (
        'id',
        'name',
        *date_fields('start_at', 'end_at'),
    )

class Course(Model):
    _fields = (
        'id',
        'sis_course_id',
        'uuid',
        'integration_id', 'sis_import_id',
        'name',
        'course_code',
        'original_name',
        'workflow_state',
        'account_id', 'root_account_id',
        'enrollment_term_id',
        'grading_periods', 'grading_standard_id', 'grade_passback_settings',
        *date_fields('created_at', 'start_at', 'end_at'),
        'locale',
        model_list_field('enrollments', Enrollment),
        'total_students',
        'calendar',
        'default_view',
        'syllabus_body',
        'needs_grading_count',
        model_field('term', Term),
        'course_progress',
        'apply_assignment_group_weights',
        'permissions',
        'is_public', 'is_public_to_auth_users',
        'public_syllabus', 'public_syllabus_to_auth',
        'public_description',
        'storage_quota_mb',
        'storage_quota_used_mb',
        'hide_final_grades',
        'license',
        'allow_student_assignment_edits', 'allow_wiki_comments', 'allow_student_forum_attachments',
        'open_enrollment', 'self_enrollment', 'restrict_enrollments_to_course_dates',
        'course_format',
        'access_restricted_by_date',
        'time_zone',
        'blueprint', 'blueprint_restrictions', 'blueprint_restrictions_by_object_type',
        'template',
    )
