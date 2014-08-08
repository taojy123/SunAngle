#coding=utf8
#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1CHOICE1, wxID_FRAME1CHOICE2, 
 wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, 
 wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT7, wxID_FRAME1TEXTCTRL1, 
 wxID_FRAME1TEXTCTRL2, wxID_FRAME1TEXTCTRL3, wxID_FRAME1TEXTCTRL4, 
] = [wx.NewId() for _init_ctrls in range(16)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(512, 209), size=wx.Size(746, 338),
              style=wx.DEFAULT_FRAME_STYLE, title=u'\u592a\u9633\u52a9\u624b')
        self.SetClientSize(wx.Size(730, 300))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(730, 300),
              style=wx.TAB_TRAVERSAL)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label=u'\u5f00\u59cb\u8ba1\u7b97', name='button1',
              parent=self.panel1, pos=wx.Point(288, 232), size=wx.Size(136, 32),
              style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'\u89c2\u6d4b\u70b9\u7ecf\u5ea6\uff1a', name='staticText1',
              parent=self.panel1, pos=wx.Point(41, 115), size=wx.Size(72, 13),
              style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'\u89c2\u6d4b\u70b9\u7eac\u5ea6\uff1a', name='staticText2',
              parent=self.panel1, pos=wx.Point(41, 163), size=wx.Size(72, 13),
              style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(113, 111), size=wx.Size(100, 21),
              style=0, value=u'')

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self.panel1, pos=wx.Point(113, 159), size=wx.Size(100, 21),
              style=0, value=u'')

        self.choice1 = wx.Choice(choices=["E", "W"], id=wxID_FRAME1CHOICE1,
              name='choice1', parent=self.panel1, pos=wx.Point(223, 111),
              size=wx.Size(58, 21), style=0)
        self.choice1.SetHelpText(u'')
        self.choice1.SetLabel(u'\u8fbe\u5230')
        self.choice1.SetStringSelection(u'E')
        self.choice1.SetToolTipString(u'choice1')

        self.choice2 = wx.Choice(choices=["N", "S"], id=wxID_FRAME1CHOICE2,
              name='choice2', parent=self.panel1, pos=wx.Point(223, 159),
              size=wx.Size(56, 21), style=0)
        self.choice2.SetStringSelection(u'N')

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'-------------------------------->', name='staticText3',
              parent=self.panel1, pos=wx.Point(312, 143), size=wx.Size(136, 13),
              style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'\u592a\u9633\u4ef0\u89d2\uff1a', name='staticText4',
              parent=self.panel1, pos=wx.Point(504, 119), size=wx.Size(60, 13),
              style=0)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'\u592a\u9633\u65b9\u4f4d\uff1a', name='staticText5',
              parent=self.panel1, pos=wx.Point(504, 164), size=wx.Size(60, 13),
              style=0)

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3, name='textCtrl3',
              parent=self.panel1, pos=wx.Point(566, 114), size=wx.Size(100, 21),
              style=0, value=u'')

        self.textCtrl4 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL4, name='textCtrl4',
              parent=self.panel1, pos=wx.Point(566, 162), size=wx.Size(100, 21),
              style=0, value=u'')

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'\u5185\u8499\u5927\u63a2\u9ad8\u7a7a\u4fdd\u969c',
              name='staticText6', parent=self.panel1, pos=wx.Point(624, 280),
              size=wx.Size(96, 13), style=0)
        self.staticText6.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              True, u'Tahoma'))

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'\u592a\u9633\u4ef0\u89d2\u53ca\u65b9\u4f4d\u89d2 \u81ea\u52a8\u5316\u8ba1\u7b97\u52a9\u624b',
              name='staticText7', parent=self.panel1, pos=wx.Point(144, 24),
              size=wx.Size(428, 33), style=0)
        self.staticText7.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))

    def __init__(self, parent):
        self._init_ctrls(parent)
