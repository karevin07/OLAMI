#-*- coding：utf-8 -*-
'''
	Copyright 2017, VIA Technologies, Inc. & OLAMI Team.

	http://olami.ai

	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.
'''

from Config import Config
from ControlCenter import ControlCenter

def checkConfig():
    ret = False
    if len(Config.NLI_SERVER) > 0 and len(Config.APP_KEY) > 0 and len(Config.APP_SECRET) > 0:
        ret = True
    else:
        print("Please set NLI_SERVER, APP_KEY, APP_SECRET in Config.py\n")
    return ret

if __name__ == '__main__':
    print("Olami python demo: 1.00\n")
    if checkConfig():
        controlCenter = ControlCenter()
        if controlCenter.init() == True:
            controlCenter.setDaemon(True);
            controlCenter.start()

        print("ctrl+c to exit")
        controlCenter.join()
        controlCenter.uninit()


