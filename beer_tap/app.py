import uuid
import datetime
import json
import requests
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError, validator


mock_url = "https://stoplight.io/mocks/rviewer/beer-tap-dispenser/90004725"
app = FastAPI()


class New_dispenser_schema(BaseModel):
    flow_volume: float
    id: uuid.UUID

class Usages_schema(BaseModel):
    opened_at: str
    closed_at: str

    @validator('opened_at', 'closed_at')
    def check_time_format(cls, v):
        datetime_object = datetime.datetime.strptime(v,"%Y-%m-%dT%H:%M:%SZ")
        assert datetime.datetime == type(datetime_object)
        return v


@app.post('/new_dispenser')
def new_dispenser(request: Request, flow_volume:float) -> Response:
    
    headers = { 'Content-Type': "application/json" }
    payload = {"flow_volume": flow_volume}
    def make_request_mock_api(headers, payload):
        results = requests.post(f"{mock_url}/dispenser", headers=headers, data=json.dumps(payload))
        return results
    results = make_request_mock_api(headers, payload)
    
    contents = json.loads(results.text)

    if results.status_code == 200:
        status_code = status.HTTP_200_OK
    
    try:
        New_dispenser_schema(
            flow_volume = contents['flow_volume'],
            id = contents['id']
        )
    except ValidationError as e:
        print(e)
        contents = {"Status": "Internal server error"}
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return JSONResponse(content=contents, status_code=status_code)


@app.put("/open/dispenser/{id}/status")
def open_tap(request: Request, id:str) -> Response:
    headers = { 'Content-Type': "application/json" }
    date_now = datetime.datetime.now()
    date_now = date_now.strftime("%Y-%m-%dT%H:%M:%SZ")
    payload = {
        "status": "open",
        "updated_at": date_now
    }

    results = requests.put(f"{mock_url}/dispenser/{id}/status", headers=headers, data=json.dumps(payload))

    if results.status_code == 202:
        contents = {"status": f"Tap with id {id} opened"}
        status_code = 202

    elif results.status_code == 409:
        contents = {"status":"The tap is already opened"}
        status_code = 409

    elif results.status_code == 422:
        contents ={"status":"Unprocessable Entity"}
        status_code = 422

    elif results.status_code == 500:
        contents = {"status":"Internal server error"}
        status_code = 500
    
    else:
        contents = {"status":"Undefined"}
        status_code = results.status_code

    return JSONResponse(content=contents, status_code=status_code)


@app.put("/close/dispenser/{id}/status")
def close_tap(request: Request, id:str) -> Response:
    headers = { 'Content-Type': "application/json" }
    date_now = datetime.datetime.now()
    date_now = date_now.strftime("%Y-%m-%dT%H:%M:%SZ")
    
    payload = {
        "status": "close",
        "updated_at": date_now
    }

    results = requests.put(f"{mock_url}/dispenser/{id}/status", headers=headers, data=json.dumps(payload))

    if results.status_code == 202:
        contents = {"status": f"Tap with id {id} closed"}
        status_code = 202

    elif results.status_code == 409:
        contents = {"status":"The tap is already closed"}
        status_code = 409

    elif results.status_code == 422:
        contents ={"status":"Unprocessable Entity"}
        status_code = 422

    elif results.status_code == 500:
        contents = {"status":"Internal server error"}
        status_code = 500
    
    else:
        contents = {"status":"Undefined"}
        status_code = results.status_code


    return JSONResponse(content=contents, status_code=status_code)


@app.get('/dispenser/{id}/spending')
def get_bill(request: Request, id:str) -> Response:
    headers = { 'Content-Type': "application/json" }
    results = requests.get(f"{mock_url}/dispenser/{id}/spending", headers=headers)
    contents = json.loads(results.text)

    usages = len(contents['usages'])
    total_time_in_operation_in_seconds = 0

    services = []
    for index, usage in enumerate(contents['usages']):
        try:
            Usages_schema(opened_at=usage["opened_at"], closed_at=usage["closed_at"])
        except ValidationError as e:
            print(e)

        if usage["closed_at"] == 'null':
            # Tap is out of order
            break
        opened_datetime = datetime.datetime.strptime(usage["opened_at"],"%Y-%m-%dT%H:%M:%SZ")
        closed_datetime = datetime.datetime.strptime(usage["closed_at"],"%Y-%m-%dT%H:%M:%SZ")
        service_in_seconds = (closed_datetime - opened_datetime).total_seconds()
        total_time_in_operation_in_seconds += service_in_seconds

        services.append({f"Service {index}": usage["total_spent"]})
    
    summary = {
        f"Summary for dispenser": id,
        f"Total operations": usages,
        f"Total seconds in operation": total_time_in_operation_in_seconds,
        f"Money yield in each operation": services
    }

    return JSONResponse(content=summary, status_code=status.HTTP_200_OK)
