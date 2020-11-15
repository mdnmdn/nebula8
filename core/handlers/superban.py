#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core.database.repository.superban import SuperbanRepository
from languages.getLang import languages
from core.utilities.message import message
from core.utilities.functions import ban_user
from core.utilities.functions import delete_message

def init(update, context):
    user = update.effective_user.id
    rows = SuperbanRepository().getById([user])
    if rows:
        msg = "I got super banned <code>{}</code>".format(user)
        message(update,context,msg)
        delete_message(update,context)
        ban_user(update,context)