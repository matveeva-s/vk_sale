export async function fetchAPI(context, DATA_URL) {
    const url = process.env.DJANGO_HOST + DATA_URL;
    const reqHeaders = context.req.headers;
    let headers;
    if (reqHeaders.cookie) {
        headers = { cookie: reqHeaders.cookie }
    }
    const res = await fetch(
        url, { headers }
    );

    const csrfToken = res.headers.get('csrftoken');
    if (csrfToken) {
        context.res.setHeader('X-CSRFToken', csrfToken);
        context.res.setHeader('Set-Cookie', `csrftoken=${csrfToken}`);
    }
    return await res.json();
}

const API_DJANGO_HOST = '/api'

export async function reactFetchAPI(DATA_URL, method='GET', data=undefined, formadata=null) {
    const url = API_DJANGO_HOST + DATA_URL;
    const token = document.cookie.split(';')[0].split('=')[1];
    const headers = {
        'X-CSRFToken': token,
    };
    if (!formadata) {
        headers['Content-Type'] = 'application/json';
    }
    const res = await fetch(
        url, {
            method,
            credentials: 'include',
            body: data,
            headers,
        }
    );
    return await res.json();
}
