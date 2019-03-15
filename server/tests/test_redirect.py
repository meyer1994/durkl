from utils import TestFlask


class TestRedirect(TestFlask):
    ''' Tests redirections in the / (root) endpoint '''
    def test_url(self):
        ''' Gets the site with id 1 '''
        response = self.client.get('/1')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, TestFlask.TEST_URLS[0])

    def test_invalid_url(self):
        ''' Gets the site with invalid id '''
        response = self.client.get('/100')
        self.assertEqual(response.status_code, 404)
