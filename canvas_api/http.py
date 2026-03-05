import requests

def canvas_request(method, url, *, params=None, data=None, headers=None, timeout=None, session=None):
    if session is None:
        session = requests.Session()

    req = requests.Request(method, url, params=params, data=data, headers=headers)
    res = session.send(
        session.prepare_request(req),
        timeout=15 if timeout is None else timeout
    )

    res.raise_for_status()

    return res.json()

def paginated_request(method, url, *, params=None, data=None, headers=None, timeout=None, per_page=1000, session=None):
    print(f'paginated_request: params = {repr(params)}')
    if session is None:
        session = requests.Session()

    if 'per_page' not in params and url.find('per_page=') < 0:
        params['per_page'] = per_page

    req = requests.Request(method, url, params=params, data=data, headers=headers)
    res = session.send(
        session.prepare_request(req),
        timeout=15 if timeout is None else timeout
    )

    res.raise_for_status()
    results = res.json()
    if not isinstance(results, list):
        raise ValueError('Response is not a list')
    print(f'paginated_request: got {len(results)} results')

    if res.links and 'next' in res.links:
        print(f'paginated_request: next url: {res.links['next']['url']}')
        results += paginated_request(
            method, res.links['next']['url'],
            params=params, data=data, headers=headers, timeout=timeout, session=session, per_page=None,
        )

    return results
