# -*- coding: UTF-8 -*-

# eMuleNVDASupport: An app module for eMule
# Version: 1.1-dev
# Fixed bug in script_find: Now works just on readonly edit controls
# Date: 17/05/2013
# Added comments for translators
# Date: 13/05/2012
# Added support for managing columns
# Date: 12/05/2013
# Version: 2.2
# Now doc file is opened when pressing NVDA+h
# Date: 23/04/2013
# Version: 2.1
# Deleted commands for list navigation: we don't need them now
# Date: 17/09/2012

import appModuleHandler
import addonHandler
import languageHandler
import os
import api
import ui
import speech
import oleacc
import winUser
import wx
import gui
import textInfos
import controlTypes
import NVDAObjects.IAccessible
from NVDAObjects.IAccessible import IAccessible
from NVDAObjects.behaviors import RowWithFakeNavigation

_lastFindText = ""

addonHandler.initTranslation()

class EmuleRowWithFakeNavigation(RowWithFakeNavigation):

	def initOverlayClass(self):
		for n in xrange(10):
			self.bindGesture("kb:NVDA+control+%d" % (n), "readColumn")
			self.bindGesture("kb:NVDA+shift+%d" % (n), "readColumn")
		self.bindGesture("kb:NVDA+shift+c", "copyColumn")

	def script_readColumn(self, gesture):
		try:
			col = int(gesture.keyName[-1])
		except AttributeError:
			col = int(gesture.mainKeyName[-1])
		if col == 0:
			col += 10
		if "shift" in gesture.modifierNames:
			col += 10
		self._moveToColumnNumber(col)
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_readColumn.__doc__ = _("Reads the specified column for the current item.")

	def script_copyColumn(self, gesture):
		try:
			col = api.getNavigatorObject().columnNumber
		except NotImplementedError:
			pass
		try:
			header = self._getColumnHeader(col)
			subitem = self._getColumnContent(col)
			column = ": ".join([header, subitem])
		except:
			return
		if api.copyToClip(column):
			# Translators: Message presented when an item column of the current list is copied to clipboard.
			ui.message("copied to clipboard %s" % column)
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_copyColumn.__doc__ = _("Copies the last column selected on the current list item.")

class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.role == controlTypes.ROLE_LISTITEM:
			clsList.insert(0, EmuleRowWithFakeNavigation)

	def getToolBar(self):
		statusBar = api.getStatusBar()
		if statusBar is not None:
			return api.getStatusBar().simpleNext
		else:
			return None

	def getWhere(self):
		toolBar = self.getToolBar()
		if toolBar is None:
			return None
		children=toolBar.children
		for child in children:
			if child.IAccessibleStates==16:
				return child

	def getName(self):
		where = self.getWhere()
		if where is not None:
			return self.getWhere().name

	def getChildID(self):
		where = self.getWhere
		if where is not None:
			return self.getWhere().IAccessibleChildID

	def getToolBarWindow(self):
		if self.getToolBar() is None:
			return None
		obj=self.getToolBar().simpleNext
		children=obj.children
		obj=None
		for child in children:
			if child.IAccessibleRole==oleacc.ROLE_SYSTEM_TOOLBAR:
				obj=child
		return obj

	def getIRCToolBarWindow(self):
		if self.getToolBar() is None:
			return None
		obj=self.getToolBar().simpleNext
		while obj.IAccessibleRole!=oleacc.ROLE_SYSTEM_TOOLBAR:
			obj=obj.simpleNext
		return obj

	def getHeader(self):
		obj=api.getFocusObject()
		if not obj.windowClassName==u'SysListView32':
			return None
		if obj.IAccessibleRole==oleacc.ROLE_SYSTEM_LISTITEM:
			obj=obj.parent
		location=obj.location
		if location and (len(location)==4):
			(left,top,width,height)=location
		else:
			return None
		obj=NVDAObjects.IAccessible.getNVDAObjectFromPoint(left, top)
		# obj=obj.parent.simpleFirstChild
		return obj

	def statusBarObj(self, pos):
		statusBar = api.getStatusBar()
		if statusBar is None:
			return None
		obj=api.getStatusBar().simpleFirstChild
		for n in xrange(pos):
			obj=obj.simpleNext
		text=obj.name
		return text

	def script_toolBar(self, gesture):
		obj = self.getToolBar()
		if obj is None:
			return
		api.moveMouseToNVDAObject(obj)
		api.setMouseObject(obj)
		if not controlTypes.STATE_FOCUSED in obj.states:
			obj.setFocus()
		speech.speakObject(obj, reason=controlTypes.REASON_FOCUS)
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_toolBar.__doc__=_("Moves the system focus and mouse to the main Tool Bar.")

	def script_where(self, gesture):
		name = self.getName()
		if name is None:
			return
		ui.message("%s" % name)
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_where.__doc__=_("Reports the current window.")

	def script_name(self, gesture):
		where = self.getWhere()
		if not hasattr(where, "IAccessibleChildID") or where.IAccessibleChildID != 6:
			return
		obj = self.getToolBar().simpleNext.simpleNext.lastChild
		obj.setFocus()
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_name.__doc__=_("Moves the system focus to Name field into Search window.")

	def script_searchList(self, gesture):
		where = self.getWhere()
		if not hasattr(where, "IAccessibleChildID") or where.IAccessibleChildID != 6:
			return
		obj = self.getToolBar().simpleNext.simpleNext.lastChild
		children = obj.children
		for child in children:
			if child.IAccessibleRole==oleacc.ROLE_SYSTEM_LIST:
				obj=child
		obj.setFocus()
		api.moveMouseToNVDAObject(obj)
		api.setMouseObject(obj)
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_searchList.__doc__=_("Moves the system focus and mouse to the search parameters list or Edit field for each option, into Search window.")

	def script_results(self, gesture):
		where = self.getWhere()
		if not hasattr(where, "IAccessibleChildID") or where.IAccessibleChildID != 6:
			return
		obj = self.getToolBar().simpleNext.firstChild
		children=obj.children
		for child in children:
			if child.IAccessibleRole==oleacc.ROLE_SYSTEM_TOOLBAR:
				obj=child.firstChild
		api.moveMouseToNVDAObject(obj)
		api.setMouseObject(obj)
		winUser.mouse_event(winUser.MOUSEEVENTF_LEFTDOWN,0,0,None,None)
		winUser.mouse_event(winUser.MOUSEEVENTF_LEFTUP,0,0,None,None)
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_results.__doc__=_("Moves the system focus to the results list on Search window.")

	def script_mainWindow(self, gesture):
		where = self.getWhere()
		if not hasattr(where, "IAccessibleChildID"):
			return
		if where.IAccessibleChildID!=9:
			obj = self.getToolBarWindow()
		else:
			obj = self.getIRCToolBarWindow()
		if obj is None:
			return
		obj.setFocus()
		api.moveMouseToNVDAObject(obj)
		api.setMouseObject(obj)
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_mainWindow.__doc__=_("Moves the system focus and mouse to the Context Tool Bar, so you can move using Tab key.")

	def script_mainIRC(self, gesture):
		where = self.getWhere()
		if not hasattr(where, "IAccessibleChildID") or where.IAccessibleChildID != 9:
			return
		obj = self.getIRCToolBarWindow().simpleNext.simpleNext
		if obj is None or obj.IAccessibleStates != 1048640:
			return
		obj.setFocus()
		api.setFocusObject(obj)
		speech.speakObject(obj)
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_mainIRC.__doc__=_("Moves the system focus to IRC received messages.")

	def script_header(self, gesture):
		obj = self.getHeader()
		if obj is None:
			return
		api.setNavigatorObject(obj)
		api.moveMouseToNVDAObject(obj)
		api.setMouseObject(obj)
		speech.speakObject(obj)
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_header.__doc__=_("Moves the navigator object and mouse to the current list headers.")

	def script_statusBarFirstChild(self, gesture):
		if self.statusBarObj(0) is None:
			return
		ui.message(self.statusBarObj(0))
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_statusBarFirstChild.__doc__=_("Reports the first object of Status Bar.")

	def script_statusBarSecondChild(self, gesture):
		if self.statusBarObj(1) is None:
			return
		ui.message(self.statusBarObj(1))
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_statusBarSecondChild.__doc__=_("Reports the second object of Status Bar.")

	def script_statusBarThirdChild(self, gesture):
		if self.statusBarObj(2) is None:
			return
		ui.message(self.statusBarObj(2))
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_statusBarThirdChild.__doc__=_("Reports the third object of Status Bar.")

	def script_statusBarForthChild(self, gesture):
		if self.statusBarObj(3) is None:
			return
		ui.message(self.statusBarObj(3))
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_statusBarForthChild.__doc__=_("Reports the fourth object of Status Bar.")

	def getDocFolder(self):
		langs = [languageHandler.getLanguage(), "en"]
		for lang in langs:
			docFolder = os.path.join(os.path.dirname(__file__), "..", "doc", lang)
			if os.path.isdir(docFolder):
				return docFolder
			if "_" in lang:
				tryLang = lang.split("_")[0]
				docFolder = os.path.join(os.path.dirname(__file__), "..", "doc", tryLang)
				if os.path.isdir(docFolder):
					return docFolder
				if tryLang == "en":
					break
			if lang == "en":
				break
		return None

	def getDocPath(self, docFileName):
		docPath = self.getDocFolder()
		if docPath is not None:
			docFile = os.path.join(docPath, docFileName)
			if os.path.isfile(docFile):
				docPath = docFile
		return docPath

	def script_about(self, gesture):
		try:
			os.startfile(self.getDocPath("readme.html"))
		except WindowsError:
			pass
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_about.__doc__ = _("Opens documentation for current NVDA's language.")

	def doFindText(self,text,reverse=False):
		if not text:
			return
		obj=api.getFocusObject()
		try:
			info=obj.makeTextInfo(textInfos.POSITION_CARET)
		except (NotImplementedError, RuntimeError):
			info=obj.makeTextInfo(textInfos.POSITION_FIRST)
		res=info.find(text,reverse=reverse)
		if res:
			info.updateCaret()
			speech.cancelSpeech()
			info.move(textInfos.UNIT_LINE,1,endPoint="end")
			speech.speakTextInfo(info,reason=controlTypes.REASON_CARET)
		else:
			wx.CallAfter(gui.messageBox,
			# Translators: Label of a dialog presented when the specified string of text is not found.
			_('text "%s" not found')%text,
			# Translators: Title of a dialog presented when the specified string of text is not found.
			_("Find Error"),
			wx.OK|wx.ICON_ERROR)
		global _lastFindText
		_lastFindText = text

	def doFindTextDialog(self):
		d = wx.TextEntryDialog(gui.mainFrame,
		# Translators: Label of a dialog for searching a specified string of text.
		_("Type the text you wish to find"),
		# Translators: Title of a dialog for searching a specified string of text.
		_("eMule search"),
		defaultValue=_lastFindText)
		def callback(result):
			if result == wx.ID_OK:
				# Make sure this happens after focus returns to the document.
				wx.CallLater(100, self.doFindText, d.GetValue())
		gui.runScriptModalDialog(d, callback)

	def script_find(self,gesture):
		obj = api.getFocusObject()
		if obj is None:
			return
		if not (obj.role == controlTypes.ROLE_EDITABLETEXT and controlTypes.STATE_READONLY in obj.states):
			return
		self.doFindTextDialog()
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_find.__doc__ = _("find a text string from the current cursor position.")

	def script_findNext(self,gesture):
		obj = api.getFocusObject()
		if obj is None:
			return
		if not (obj.role == controlTypes.ROLE_EDITABLETEXT and controlTypes.STATE_READONLY in obj.states):
			return
		if not _lastFindText:
			self.doFindTextDialog()
			return
		self.doFindText(_lastFindText)
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_findNext.__doc__ = _("find the next occurrence of the previously entered text string from the current cursor's position.")

	def script_findPrevious(self,gesture):
		obj = api.getFocusObject()
		if obj is None:
			return
		if not (obj.role == controlTypes.ROLE_EDITABLETEXT and controlTypes.STATE_READONLY in obj.states):
			return
		if not _lastFindText:
			self.doFindTextDialog()
			return
		self.doFindText(_lastFindText,reverse=True)
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_findPrevious.__doc__ = _("find the previous occurrence of the previously entered text string from the current cursor's position.")

	__gestures = {
		"kb:control+shift+h": "toolBar",
		"kb:control+shift+t": "where",
		"kb:control+shift+n": "name",
		"kb:control+shift+p": "searchList",
		"kb:control+shift+b": "results",
		"kb:control+shift+z": "mainWindow",
		"kb:control+shift+o": "mainIRC",
		"kb:control+shift+l": "header",
		"kb:control+shift+q": "statusBarFirstChild",
		"kb:control+shift+w": "statusBarSecondChild",
		"kb:control+shift+e": "statusBarThirdChild",
		"kb:control+shift+r": "statusBarForthChild",
		"kb:control+NVDA+f": "find",
		"kb:control+f3": "findNext",
		"kb:control+shift+f3": "findPrevious",
		"kb:NVDA+control+shift+h": "about",
	}
