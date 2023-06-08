#!/usr/bin/env python3
from bots.bot_v2_spanish_end import main
import time

maxtries = 8    # 8 * 15 minutes = about 2 hours total of waiting,

for i in range(maxtries):
    try:
        main()
        break
    except:
        time.sleep(900)
        print("fail", i)
