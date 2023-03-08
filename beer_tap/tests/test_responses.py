

def test_new_disp(mocker):
    mocker.patch(
        # api_call is from slow.py but imported to main.py
        'app.new_dispenser.make_request_mock_api(headers, payload)',
        return_value={
            "id": "e678cd48-76cc-474c-b611-94dd2df533cb",
            "flow_volume": 0.0653
        }
    )