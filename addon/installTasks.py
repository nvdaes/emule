# -*- coding: UTF-8 -*-
#Copyright (C) 2013-2016 Noelia Ruiz Martínez, other contributors
# Released under GPL2

import globalVars
import os
import shutil
import glob

def onInstall():
	configPath = globalVars.appArgs.configPath
	modulePath = os.path.join(configPath, "appModules")
	modulePath = glob.glob(modulePath+"\\emule.*")
	for file in modulePath:
		try:
			os.remove(file)
		except WindowsError:
			pass
	modulePath = os.path.join(configPath, "appModules", "eMule")
	try:
		shutil.rmtree(modulePath)
	except WindowsError:
			pass