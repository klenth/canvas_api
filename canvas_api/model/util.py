from datetime import datetime

def date_field(name):
    return {'name': name, 'ctor': parse_date}

def model_field(name, model):
    return {'name': name, 'ctor': lambda f: None if f is None else model(**f)}

def model_list_field(name, model):
    return {'name': name, 'ctor': lambda fs: None if fs is None else [model(**f) for f in fs]}

def date_fields(*names):
    return [date_field(name) for name in names]

def parse_date(s):
    if s is None:
        return None
    return datetime.fromisoformat(s)
