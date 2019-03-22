#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol

bot = InstaBot(
    login=os.environ['login'],
    password=os.environ['password']
    )

y = os.environ['comentario']

for x in y:
    bot.comment(os.environ['media_id'], x)