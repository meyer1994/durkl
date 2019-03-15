from utils import TestFlask


class TestApiUrl(TestFlask):
    def test_get_urls(self):
        ''' Get all URLs in server '''
        response = self.client.get('/api/urls').json
        urls = [u['url'] for u in response]
        self.assertListEqual(urls, TestFlask.TEST_URLS)
        self.assertEqual(len(response), 3)

    def test_get_url(self):
        ''' Get single URL from server '''
        for i, url in enumerate(TestFlask.TEST_URLS, start=1):
            response = self.client.get('/api/urls/%d' % i).json
            self.assertEqual(response['url'], url)

    def test_invalid_get_url(self):
        ''' Gets an URL that does not exist '''
        url_id = 100
        response = self.client.get('/api/urls/%d' % url_id).json
        message = response['message']
        status_code = response['status_code']
        self.assertEqual(status_code, 404)
        self.assertEqual(message, 'Id %d not found' % url_id)

    def test_post_url(self):
        ''' Post URL in server '''
        data = {'url': 'http://devdocs.io'}
        response = self.client.post('/api/urls', json=data).json
        self.assertEqual(response['url'], data['url'])
        self.assertEqual(response['id'], 4)

    def test_post_existing_url(self):
        ''' Returns the already existing URL '''
        data = {'url': TestFlask.TEST_URLS[0]}
        response = self.client.post('/api/urls', json=data).json
        self.assertEqual(response['url'], data['url'])
        self.assertEqual(response['id'], 1)

    def test_invalid_post_url(self):
        ''' Returns 400 when invalid URL is passed '''
        data = {'url': 'devdocs.io'}
        response = self.client.post('/api/urls', json=data).json
        message = response['message']
        status_code = response['status_code']
        self.assertEqual(status_code, 400)
        self.assertEqual(message, 'Invalid URL "%s"' % data['url'])

    def test_invalid_post_json(self):
        ''' Returns 400 when posting withou JSON '''
        response = self.client.post('/api/urls').json
        message = response['message']
        status_code = response['status_code']
        self.assertEqual(status_code, 400)
        self.assertEqual(message, 'Request must be of json type')

    def test_invalid_post_no_url(self):
        ''' Returns 400 when posting withou JSON '''
        data = {'not-url': 'http://devdocs.io'}
        response = self.client.post('/api/urls', json=data).json
        message = response['message']
        status_code = response['status_code']
        self.assertEqual(status_code, 400)
        self.assertEqual(message, 'Json object must have "url" key')
