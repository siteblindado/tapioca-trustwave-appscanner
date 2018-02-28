# coding: utf-8

import os
import unittest
from unittest.mock import patch

from tapioca.exceptions import ClientError

from tapioca_trustwave import Trustwave
from tapioca_trustwave.services import get_application_id_by_name, get_assessment_id_by_name, get_assessment_status

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
        fake_name = 'test.more60.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.com'
        self.assertRaises(ClientError, get_application_id_by_name, fake_name)

    @patch('tapioca_trustwave.services.request_assessment_id_by_name')
    def test_get_assessment_id_by_name(self, response_assessment_id):
        response_assessment_id.return_value = {
            "status-code": 0,
            "assessment-id": "eebc4bf6-927e-48a6-8139-e344e8d3e142"
        }

        fake_application_id = 'f64b7621-c470-4dcd-a6f6-0df19bdd1edf'
        fake_assessment_name = 'www.test.com'

        assessment_id = get_assessment_id_by_name(fake_application_id, fake_assessment_name)

        self.assertEqual(assessment_id, 'eebc4bf6-927e-48a6-8139-e344e8d3e142')

    @patch('tapioca_trustwave.services.request_assessment_status')
    def test_get_assessment_status(self, response_assessment_status):
        response_assessment_status.return_value = {
            "status-code": 0,
            "assessment-status": "Running"
        }

        fake_application_id = 'f64b7621-c470-4dcd-a6f6-0df19bdd1edf'
        fake_assessment_id = 'f0de09db-fdeb-4d83-99ba-25e2e8fddfde'

        assessment_status = get_assessment_status(fake_application_id, fake_assessment_id)

        self.assertEqual(assessment_status, 'Running')


if __name__ == '__main__':
    unittest.main()
