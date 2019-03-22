#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol

bot = InstaBot('User', 'senha')

y = [
    "@mrfiiix @milacriis @Camila",
"@queiroz_ofc",
"@milacriis",
"@Camila",
"@andersonrobertoo_",
"@camilly.gc",
"@travassoss.a",
"@_dedessa3",
"@sarahthainesouza",
"@leonardocorream1",
"@_mmarcanzoni",
]
for x in y:
    bot.comment("1992337216253488658_367386260", x)