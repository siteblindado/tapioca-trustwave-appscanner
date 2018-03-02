# coding: utf-8

import os
import unittest

from tapioca_trustwave import Trustwave

PROTOCOL = os.getenv('TRUSTWAVE_PROTOCOL')
if not PROTOCOL:
    raise RuntimeError('TRUSTWAVE_PROTOCOL environment variable must be set')

SERVER = os.getenv('TRUSTWAVE_SERVER')
if not PROTOCOL:
    raise RuntimeError('TRUSTWAVE_SERVER environment variable must be set')

CLIENT = os.getenv('TRUSTWAVE_CLIENT')
if not PROTOCOL:
    raise RuntimeError('TRUSTWAVE_CLIENT environment variable must be set')

CUSTOMER = os.getenv('TRUSTWAVE_CUSTOMER')
if not PROTOCOL:
    raise RuntimeError('TRUSTWAVE_CUSTOMER environment variable must be set')


class TestTapiocaTrustwave(unittest.TestCase):
    api_root = '{protocol}://{server}/Hailstorm.WS/HailstormRESTService.svc' \
               '/client/{client}/customer/{customer}/'.format(
        protocol=PROTOCOL, server=SERVER, client=CLIENT, customer=CUSTOMER
    )

    def setUp(self):
        self.wrapper = Trustwave(api_root=self.api_root)

    def test_resource_access(self):
        fake_name = 'www.comicstorebrasil.com.br'
        expected_URI = '{}application/www.test.com/id'.format(self.api_root)

        resource = self.wrapper.get_application_id_by_name(application_name=fake_name)

        self.assertEqual(resource.data, expected_URI)


if __name__ == '__main__':
    unittest.main()
