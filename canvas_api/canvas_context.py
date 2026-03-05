import requests
from .http import canvas_request, paginated_request
from . import model
import logging

class CanvasContext:

    def __init__(self, *, token, base_url):
        self.token = token
        self.base_url = base_url
        self.session = None

    def connect(self):
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'Bearer {self.token}'})

    def close(self):
        self.session.close()
        self.session = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def _check_open(self):
        if self.session is None:
            raise RuntimeError('CanvasContext is not open')

    def _get_paginated(self, endpoint, params=None, data=None, timeout=None, element_ctor=None):
        self._check_open()
        results = paginated_request(
            'GET', f'{self.base_url}{endpoint}',
            session=self.session,
            params=params, data=data, timeout=timeout
        )

        if element_ctor:
            results = list(map(element_ctor, results))

        return results

    @staticmethod
    def _pack_params(param_names, kwargs):
        params = {}
        for name, value in kwargs.items():
            is_list_param = f'{name}[]' in param_names
            param_name = f'{name}[]' if is_list_param else name
            if not is_list_param and name not in param_names:
                raise ValueError(f'Unknown parameter: {name}')
            if is_list_param and not isinstance(value, list):
                value = [value]
            params[param_name] = value
        return params

    @staticmethod
    def _model_ctor(model):
        def ctor(fs):
            value = model(**fs)
            if len(value.extra_fields):
                logging.log(logging.INFO, f'Extra fields for model {model.__name__}: {repr(value.extra_fields)}')
            return value
        return ctor

    def course_list(self, **kwargs):
        params = self._pack_params({'enrollment_type', 'enrollment_state', 'include[]', 'state[]'}, kwargs)
        return self._get_paginated(
            '/courses',
            params=params,
            element_ctor=self._model_ctor(model.Course)
        )
