import inspect
from fwk.page.AndroidCommonPage import AndroidCommonPage


'''contact HP on facebook messager page.'''
class Page_contactHPonFacebookMessager_model(AndroidCommonPage):
    page_name = 'page_contactHPonFacebookMessager'

    def __init__(self):
        self.__AndroidCommonPage = AndroidCommonPage.__init__(self)

    def dialog_do_not_show_again_checkbox(self):
        return self.get(inspect.stack()[0][3])

    def button_Cancel(self):
        return self.get(inspect.stack()[0][3])

    def button_Message(self):
        return self.get(inspect.stack()[0][3])
