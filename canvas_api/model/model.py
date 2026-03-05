class Model:

    def __init__(self, **kwargs):
        self.extra_fields = {}
        processed_fields = set()
        for field in self.__class__.__dict__['_fields']:
            if isinstance(field, str):
                setattr(self, field, kwargs.get(field))
                processed_fields.add(field)
            elif isinstance(field, dict):
                field_name = field['name']
                field_ctor = field['ctor']
                field_value = kwargs.get(field_name)

                if field_name in kwargs:
                    field_value = field_ctor(field_value)

                setattr(self, field_name, field_value)
                processed_fields.add(field_name)

        for name, value in kwargs.items():
            if name not in processed_fields:
                self.extra_fields[name] = value

    def update(self, **kwargs):
        for field in self.__class__.__dict__['_fields']:
            if isinstance(field, str):
                if field in kwargs:
                    setattr(self, field, kwargs.get(field))
            elif isinstance(field, dict):
                field_name = field['name']
                if field_name in kwargs:
                    field_ctor = field['ctor']
                    field_value = kwargs.get(field_name)
                    field_value = field_ctor(field_value)

                    setattr(self, field_name, field_value)
            else:
                raise ValueError('Invalid value in _fields')

        for name, value in kwargs.items():
            if name not in self.__class__.__dict__['_fields']:
                self.extra_fields[name] = value

    def as_dict(self, include_missing=False, include_extra_fields=False):
        def field_name(field):
            if isinstance(field, str):
                return field
            elif isinstance(field, dict):
                return field['name']
            else:
                raise ValueError('Invalid value in _fields')

        def field_value(value):
            from datetime import datetime
            if isinstance(value, Model):
                return value.as_dict(include_missing=include_missing, include_extra_fields=include_extra_fields)
            elif isinstance(value, datetime):
                return value.isoformat()
            elif isinstance(value, list):
                return [field_value(v) for v in value]
            else:
                return value

        d = {
            fn: field_value(fv)
            for field in self.__class__.__dict__['_fields']
            if (fv := getattr(self, fn := field_name(field))) is not None or include_missing
        }

        if include_extra_fields:
            d['extra_fields'] = self.extra_fields

        return d
