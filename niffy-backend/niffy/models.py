# coding=utf-8
import logging
from google.appengine.ext import ndb

import humanize

from dripcil import currency
from dripcil.gae_ndb import BaseModel, File


class InvoiceLine(ndb.Model):

    code = ndb.StringProperty()
    description = ndb.StringProperty()
    unit_of_measure = ndb.StringProperty()

    quantity = ndb.FloatProperty()
    net_total = ndb.FloatProperty()
    tax_payable = ndb.FloatProperty()
    settlement_total = ndb.FloatProperty()


class Company(ndb.Model):

    name = ndb.StringProperty()
    business_name = ndb.StringProperty()
    address_detail = ndb.StringProperty()
    tax_id = ndb.StringProperty()
    postal_code = ndb.StringProperty()
    country = ndb.StringProperty()
    phone = ndb.StringProperty()


class Invoice(BaseModel):

    date = ndb.DateProperty()
    doc_type = ndb.StringProperty()
    company = ndb.StructuredProperty(Company, repeated=False)
    lines = ndb.StructuredProperty(InvoiceLine, repeated=True)
    net_total = ndb.FloatProperty()
    gross_total = ndb.FloatProperty()
    description = ndb.StringProperty()
    tags = ndb.StringProperty(repeated=True)

    file_key = ndb.KeyProperty(kind=File)

    @property
    def company_name(self):
        return self.company.business_name or self.company.name

    @property
    def total_formatted(self):
        return currency.format(self.gross_total)

    @property
    def date_formatted(self):
        return self.date.strftime('%Y-%m-%d')

    @property
    def date_formatted(self):
        return humanize.naturaldate(self.date)
        # return self.date.strftime('%Y-%m-%d')
