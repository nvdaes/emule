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