import pytest
# import requests_mock
# from .._module_interface import *
from app import app
from beer_tap._module_interface import *



# def test_a(mocker):
#     flow_volume = 0.0
#     mocker.patch
#     with requests_mock.Mocker() as rm:
#         rm.put(mock_address, json=mock_response, status_code=200)
#         response = admin_elasticsearch.create_index("test_index")
#         assert response == mock_response


# def test_new_dispenser(requests_mock):
#     flow_volume = 0.1
#     requests_mock.get(f'{__BASE_URL}/employee/{test_id}', json= {'name': 'awesome-mock'})
#     resp = get_employee('random-id')
#     assert resp == {'name': 'awesome-mock'}

def test_new_disp(mocker):
    mocker.patch(
        # api_call is from slow.py but imported to main.py
        'app.new_dispenser.make_request_mock_api(headers, payload)',
        return_value={
            "id": "e678cd48-76cc-474c-b611-94dd2df533cb",
            "flow_volume": 0.0653
        }
    )