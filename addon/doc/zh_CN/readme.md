# eMule - 电骡支持插件 #

*	作者： Noelia, Chris, Alberto.

此插件有助于提高eMule与nVDA的可访问性。它还提供了用于在不同窗口中移动的其他键盘命令，并提供了有关eMule的有用信息。

当前插件基于同一作者开发的eMuleNVDASupport插件。您应该卸载该旧插件以使用此插件，因为两者都有共同的按键和功能。

Tested on [eMule][1] 0.50a and 70b.

## 快捷键: ##

*	control+shift+h： 移动鼠标和焦点到”主工具栏。
*	control+shift+t: 朗读当前窗口。
*	control+shift+n： 移动焦点到“查找”窗口的“名称”编辑区。
*	control+shift+p： 切换焦点和鼠标到“搜索”窗口的搜索参数列表和编辑区选项。
*	control + shift + b：将焦点移动到当前窗口的列表中。例如，可在“搜索”窗口中使用，在“传输”窗口中下载等。
*	control + shift + o：将焦点移动到当前窗口中的只读编辑框。例如，IRC收到消息，可用服务器等。
*	control + NVDA + f：如果插入符号位于只读编辑框中，则打开查找对话框以使用命令搜索NVDA中可用的文本。
*	control+shift+l： 移动鼠标和浏览对象到当前列表的表头。
*	control+shift+q： 朗读状态栏的第一个对象，提供最近一次活动的信息。
*	control+shift+w: 朗读状态栏的第二个对象，提供当前服务器的用户和文件的数目信息。
*	control+shift+e： 查看第三个状态栏的对象，常用来了解上传和下载速度。
*	control+shift+r: Reads The fourth object of the status bar; reports on connecting of eD2K and Kad network.
* Not assigned: Toggles the usage of an alternative approach to read sliders.

## 管理列。 ##

在一个列表内，您可以使用 CTRL加ALT家光标键 在列表的行列之间进行浏览。在此插件，下面的按键也是可用的：

*	nvda+control+1到0： 朗读前十列。
*	nvda+shift+1到0： 朗读第11到20列。
*	nvda+shift+C： 拷贝最后一次朗读的那一列的内容到剪贴板。


## Changes for 20.0.0
* Some edit boxes and sliders are labelled, thanks to the
  [labelAutofinderCore
  project](https://github.com/ABuffEr/labelAutofinderCore) developed by
  Alberto Buffolino, one of the authors of this add-on.
* A command (not assigned) has been added to toggle the usage of an
  alternative approach to read sliders (off by default).

## Changes for 7.0
* Compatible with NVDA 2023.1.

## 版本6.0
*	需要 NVDA 2022.1 或更高版本。

## 版本5.0
*	兼容 NVDA 2021.1。

## 版本4.0 ##
*	需要NVDA 2019.3或更高版本。

## 版本3.0 ##
*	 To search text in the readonly edit boxes,  the find dialog  can be used,
   such as nvda+control+f to activate the find dialog.

## 版本2.0 ##
*	 插件管理器现在已提供了插件的帮助。

## 版本1.2 ##
*	 当移动到 IRC 消息时，选择的文本内容已可正确的朗读。
*	 用于移动到搜索结果列表的快捷键已被推广，以便能够将焦点移动到当前窗口中的任何可用列表。
*	 用于聚焦IRC消息的快捷键已被推广到移动到任何只读编辑框，从而可以在“服务器”窗口中查看连接信息。
*	 当移动鼠标并将焦点移动到工具栏时，在某些情况下它会被朗读两次。这已得到修复。

## 版本1.1 ##
*	 修复在用户配置文件夹名称包含非拉丁字符时 NVDA 帮助菜单下的 eMule 项目，发生的错误。
*	 现在，可使用“创建手势”对快捷键进行更改。

## 版本1.0 ##
*	 初始版本。



[[!tag dev stable]]

[1]: https://www.emule-project.net
