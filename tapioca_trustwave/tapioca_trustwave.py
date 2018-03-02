# coding: utf-8
import os

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)

from .resource_mapping import RESOURCE_MAPPING


PROTOCOL = os.getenv('TRUSTWAVE_PROTOCOL')
SERVER = os.getenv('TRUSTWAVE_SERVER')
CLIENT = os.getenv('TRUSTWAVE_CLIENT')
CUSTOMER = os.getenv('TRUSTWAVE_CUSTOMER')


class TrustwaveClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = '{protocol}://{server}/Hailstorm.WS/HailstormRESTService.svc/' \
               'client/{client}/customer/{customer}/'.format(
        protocol=PROTOCOL, server=SERVER, client=CLIENT, customer=CUSTOMER)
    resource_mapping = RESOURCE_MAPPING

    def get_api_root(self, api_params):
        return api_params.get('api_root')

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(TrustwaveClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)
        return params

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass


Trustwave = generate_wrapper_from_adapter(TrustwaveClientAdapter)
