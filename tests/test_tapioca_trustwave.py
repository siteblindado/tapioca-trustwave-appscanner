# coding: utf-8

import unittest

from tapioca_trustwave import Trustwave


class TestTapiocaTrustwave(unittest.TestCase):
    def setUp(self):
        self.wrapper = Trustwave(server='appscan.com', client='client_name', customer='customer_name')

    def test_resource_access(self):
        fake_name = 'www.comicstorebrasil.com.br'
        expected_URI = 'https://appscan.com/Hailstorm.WS/HailstormRESTService.svc/client/client_name/customer/customer_name/application/www.comicstorebrasil.com.br/id'

        resource = self.wrapper.get_application_id_by_name(application_name=fake_name)
        self.assertEqual(resource.data, expected_URI)


if __name__ == '__main__':
    unittest.main()
