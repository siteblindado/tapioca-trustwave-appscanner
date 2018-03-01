from tapioca_trustwave import Trustwave

from tapioca_trustwave.requests import request_application_id_by_name, request_assessment_id_by_name, \
    request_assessment_status
from tapioca_trustwave.validators import is_valide_uuid4, is_valid_application_name

api = Trustwave()


def application_exists(application_id):
    is_valide_uuid4(application_id)

    request = api.get_application_id_by_name(application_name=application_id).get()
    application_data = request().data

    application_status = application_data.get('application-status')

    return application_status


def get_application_id_by_name(application_name):
    is_valid_application_name(application_name)

    application_data = request_application_id_by_name(application_name)
    application_id = application_data.get('application-id')

    return application_id


def assessment_exists(application_id, assessment_id):
    is_valide_uuid4(application_id)
    is_valide_uuid4(assessment_id)

    request = api.check_if_assessment_exists(application_name=application_id,
                                             assessment_id=assessment_id).get()
    assessment_data = request().data

    assessment_exists = assessment_data.get('assessment-status')

    return assessment_exists


def get_assessment_id_by_name(application_id, assessment_name):
    is_valide_uuid4(application_id)

    assessment_data = request_assessment_id_by_name(application_id, assessment_name)
    assessment_id = assessment_data.get('assessment-id')

    return assessment_id


def get_assessment_status(application_id, assessment_id):
    is_valide_uuid4(application_id)
    is_valide_uuid4(assessment_id)

    assessment_data = request_assessment_status(application_id, assessment_id)
    status = assessment_data.get('assessment-status')

    return status


def get_current_assessment_run_id(application_id, assessment_id):
    is_valide_uuid4(application_id)
    is_valide_uuid4(assessment_id)

    request = api.get_assessment_runs(application_name=application_id,
                                      assessment_id=assessment_id).get()
    assessment_data = request().data
    status = assessment_data.get('assessment-status')

    return status


def get_assessment_run_status(application_id, assessment_run_id):
    is_valide_uuid4(application_id)
    is_valide_uuid4(assessment_run_id)

    request = api.get_assessment_runs(application_id=application_id,
                                      assessment_run_id=assessment_run_id).get()
    assessment_data = request().data
    status = assessment_data.get('assessment-status')

    return status


def get_assessment_run_results(application_id, assessment_run_id):
    is_valide_uuid4(application_id)
    is_valide_uuid4(assessment_run_id)

    request = api.get_assessment_runs(application_id=application_id,
                                      assessment_run_id=assessment_run_id).get()
    assessment_data = request().data
    status = assessment_data.get('assessment-status')
