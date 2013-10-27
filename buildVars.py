# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# add-on Name
	"addon-name" : "eMule",
	# Add-on description
	# TRANSLATORS: Summary for this add-on to be shown on installation and add-on information.
	"addon-summary" : _("eMule"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on installation and add-on information
	"addon-description" : _("""Improves eMule's accessibility with NVDA.
	eMule is a P2P program to search and share files.
	You can get more information about eMule at
	http://www.emule-project.net
	"""),
	# version
	"addon-version" : "1.0",
	# Author(s)
	"addon-author" : "Noelia <nrm1977@gmail.com>, Chris <llajta2012@hotmail.com>, Alberto <a.buffolino@gmail.com>",
	# URL for the add-on documentation support
	"addon-url" : "http://addons.nvda-project.org"
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "appModules", "*.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py", "docHandler.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
