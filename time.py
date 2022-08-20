# encoding: utf-8
import sys

import time

from workflow import Workflow, ICON_WEB

API_KEY = 'your-pinboard-api-key'


def get_time(s):
    # 秒级时间戳
    s = s
    # 毫秒级时间戳
    ms = str(s * 1000)
    # 格式化成2016-03-20 11:45:39形式
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    wf.add_item(uid="time", title="时间: " + str(current_time), arg=current_time, valid=True, icon=ICON_WEB)
    wf.add_item(uid="s", title="秒: " + str(s), arg=s, valid=True, icon=ICON_WEB)
    wf.add_item(uid="ms", title="毫秒: " + str(ms), arg=ms, valid=True, icon=ICON_WEB)
    wf.send_feedback()


if __name__ == "__main__":
    wf = Workflow()
    query = sys.argv[1]
    if (query == 'now'):
        s = time.time()
        get_time(int(s))
    else:
        ts = int(query)
        if ts > 253402185600:
            ts = ts / 1000
        get_time(ts)
