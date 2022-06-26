from urllib import request
from datetime import datetime
import simplejson
from aws_config import settings


class GraphqlClient:

    def __init__(self):
        self.endpoint = settings.appsync_endpoint
        self.headers = {'x-api-key': settings.api_key_appsync}


    @staticmethod
    def serialization_helper(o):
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%dT%H:%M:%S.000Z')

    def execute(self, query, operation_name, variables={}):
        data = simplejson.dumps({
            "query": query
        },
            default=self.serialization_helper,
            ignore_nan=True
        )
        r = request.Request(
            headers=self.headers,
            url=self.endpoint,
            method='POST',
            data=data.encode('utf8')
        )

        response = request.urlopen(r).read()
        return response.decode('utf8')



gq_client = GraphqlClient()
