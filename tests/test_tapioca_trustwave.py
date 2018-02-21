# coding: utf-8

import os
import unittest
from unittest.mock import patch

from tapioca.exceptions import ClientError

from tapioca_trustwave import Trustwave
from tapioca_trustwave.services import get_application_id_by_name

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

    @patch('tapioca_trustwave.services.request_application_id_by_name')
    def test_get_application_id_by_name_ok(self, response_application_id):
        response_application_id.return_value = {
            "status-code": 0,
            "application-id": "99bdd477-340e-461b-aa55-617d9b4b410d"
        }

        fake_name = 'www.test.com'
        application_id = get_application_id_by_name(fake_name)

        self.assertEqual(application_id, '99bdd477-340e-461b-aa55-617d9b4b410d')

    def test_get_application_id_by_name_whit_long_name(self):
        fake_name = 'test.more60.commmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm'
        self.assertRaises(ClientError, get_application_id_by_name, fake_name)

    def test_get_application_id_by_name_whit_special_character(self):
        fake_name = 'test.commmmmmmmm mmmm'
        self.assertRaises(ClientError, get_application_id_by_name, fake_name)


if __name__ == '__main__':
    unittest.main()
