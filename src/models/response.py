from json import dumps
from http import HTTPStatus


class Response:

    @staticmethod
    def of(http_status: HTTPStatus, message: str):
        return {
            'statusCode': http_status.value,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": dumps({
                'code': http_status.value,
                'message': message
            })
        }
