# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.process_doc_request import ProcessDocRequest  # noqa: E501
from swagger_server.models.process_msg_request import ProcessMsgRequest  # noqa: E501
from swagger_server.models.rank_entities_request import RankEntitiesRequest  # noqa: E501
from swagger_server.models.rank_entities_response import RankEntitiesResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_process_doc(self):
        """Test case for process_doc

        Process new doc
        """
        body = ProcessDocRequest()
        response = self.client.open(
            '//actions/process/doc',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_process_msg(self):
        """Test case for process_msg

        Process new msg
        """
        body = ProcessMsgRequest()
        response = self.client.open(
            '//actions/process/msg',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_rank_entities(self):
        """Test case for rank_entities

        Rank Entities
        """
        body = RankEntitiesRequest()
        response = self.client.open(
            '//actions/rank',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
