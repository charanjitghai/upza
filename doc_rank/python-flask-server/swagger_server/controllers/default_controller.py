import connexion
import six

from swagger_server.models.process_doc_request import ProcessDocRequest  # noqa: E501
from swagger_server.models.process_msg_request import ProcessMsgRequest  # noqa: E501
from swagger_server.models.rank_entities_request import RankEntitiesRequest  # noqa: E501
from swagger_server.models.rank_entities_response import RankEntitiesResponse  # noqa: E501
from swagger_server.models.entity import Entity
from swagger_server.models.set_cookie_request import SetCookieRequest
from swagger_server import util
from .pl import pl

pli = pl('./data/', debug=True)

def process_doc(body):  # noqa: E501
    """Process new doc

     # noqa: E501

    :param body: Doc object that needs to be processed
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ProcessDocRequest.from_dict(connexion.request.get_json())  # noqa: E501
        url = body.url
        pli.process_doc(url)
        return 'processed doc ' + url

    return "Can't process non json requests", 400


def process_msg(body):  # noqa: E501
    """Process new msg

     # noqa: E501

    :param body: Doc object that needs to be processed
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ProcessMsgRequest.from_dict(connexion.request.get_json())  # noqa: E501
        msg_id = body.msg_id
        msg_text = body.msg_text
        pli.process_msg(msg_id, msg_text)
        return 'processed doc ' + msg_id

    return "Can't process non json requests", 400


def rank_entities(body):  # noqa: E501
    """Rank Entities

     # noqa: E501

    :param body: Rank arguments
    :type body: dict | bytes

    :rtype: RankEntitiesResponse
    """
    if connexion.request.is_json:
        body = RankEntitiesRequest.from_dict(connexion.request.get_json())  # noqa: E501
        keywords = body.keywords
        limit = body.limit
        ranked = pli.rank(keywords, limit)
        resp = RankEntitiesResponse()
        entities = []
        for r in ranked:
            ei = Entity()
            ei.entity_id = r[0]
            ei.score = r[1]
            entities.append(ei)
        resp.entities = entities
        return resp
    

    return "Can't process non json requests", 400

def set_cookie(body):  # noqa: E501
    """Set new cookie

     # noqa: E501

    :param body: Cookie that needs to be set
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = SetCookieRequest.from_dict(connexion.request.get_json())  # noqa: E501
        cookie = body.cookie
        new_cookie = pli.set_cookie(cookie)
    return new_cookie