#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configuration as config
from google.appengine.ext import db
from google.appengine.api import memcache

class BasicModel(db.Model):
    is_deleted = db.BooleanProperty(default=False)
    is_active = db.BooleanProperty(default=True)
    when_created = db.DateTimeProperty(auto_now_add=True)
    when_modified = db.DateTimeProperty(auto_now=True)

class InheritedModel(BasicModel):
    # Has all the BasicModel properties defined.
    pass

