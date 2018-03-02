# coding: utf-8

import os
import unittest

from tapioca_trustwave import Trustwave

os.environ["TRUSTWAVE_API_ROOT"] = "https://api.test.com/"


class TestTapiocaTrustwave(unittest.TestCase):
    uri_root = os.getenv('TRUSTWAVE_API_ROOT')

    def setUp(self):
        self.wrapper = Trustwave(uri_root=self.uri_root)

    def test_resource_access(self):
        fake_name = 'www.test.com'
        expected_URI = '{}application/www.test.com/id'.format(self.uri_root)

        resource = self.wrapper.get_application_id_by_name(application_name=fake_name)

        self.assertEqual(resource.data, expected_URI)


if __name__ == '__main__':
    unittest.main()
