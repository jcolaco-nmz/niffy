# coding=utf-8
import datetime

from google.appengine.ext import ndb


class BaseModel(ndb.Model):
    created_by = ndb.StringProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_by = ndb.StringProperty()
    updated_at = ndb.DateTimeProperty(auto_now=True)
    account = ndb.KeyProperty()

    def to_json(self):
        return to_json(self)


class File(BaseModel):
    name = ndb.StringProperty()
    tags = ndb.StringProperty(repeated=True)
    data = ndb.BlobProperty(required=True)
    mimetype = ndb.StringProperty()


SIMPLE_TYPES = (int, long, float, bool, dict, basestring, str, unicode)  # list


def to_json(value, depth=0, **params):
    """Prepares a GAE model (ndb, not db) for JSON encoding. This is not really
    a JSON encoder, but more a 'to dictionary' prepared for encoding JSON encoding."""

    # TODO: support cycle/circular references (include a list of processed keys)

    if value is None or isinstance(value, SIMPLE_TYPES):

        return value

    elif isinstance(value, list):

        return [to_json(invalue, depth=depth, **params) for invalue in value]

    elif isinstance(value, (datetime.date, datetime.datetime)):

        return value.isoformat()

    elif isinstance(value, ndb.GeoPt):

        return {'lat': value.lat, 'lon': value.lon}

    elif isinstance(value, ndb.Model):

        try:
            exclude = value.JSON_EXCLUDE
        except:
            exclude = []

        output = dict([[a, to_json(v, depth-1, **params)] for a, v in value.to_dict(exclude=exclude).items()])

        if value.key:
            output['id'] = value.key.id()

        # Process explicitly included attributes (usualy non attributes)
        try:
            include = value.JSON_INCLUDE
        except:
            include = []
        for attr in include:
            ivalue = getattr(value, attr)
            output[attr] = to_json(ivalue, depth, **params)

        return output

    elif isinstance(value, ndb.Key):

        if depth <= 0:
            return value.id()
        else:
            return to_json(ndb.get(value), depth-1, **params)

    else:

        raise ValueError('Cannot encode ' + repr(value))
