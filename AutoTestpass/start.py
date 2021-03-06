# coding: utf-8
from fwk.base.InitFwk import InitFwk
from projects.PrinterControl.cases.HomeMoreAbout import HomeMoreAbout
from projects.PrinterControl.cases.HomeMoreAppSettings import HomeMoreAppSettings
from projects.PrinterControl.cases.Files import Files
from projects.WebExample.cases.TestBrowser import TestBrowser
from projects.IosExample.cases.IosExample import IosExample

import unittest
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    initFwk = InitFwk()
    if initFwk.name_project == "PrinterControl":
        # suite.addTest(HomeMoreAbout("test_flow"))
        # suite.addTest(HomeMoreAbout("test_aioVersion"))
        # suite.addTest(HomeMoreAbout("test_copyRight"))
        # suite.addTest(HomeMoreAbout("test_legalInformaion"))
        # suite.addTest(HomeMoreAbout("test_endUserLicenseAgreement"))
        # suite.addTest(HomeMoreAbout("test_endUserLicenseAgreement_back"))
        # suite.addTest(HomeMoreAbout("test_hpOnlinePrivacyStatement"))
        # suite.addTest(HomeMoreAbout("test_hpOnlinePrivacyStatement_back"))
        # suite.addTest(HomeMoreAbout("test_shareThisApp"))
        # suite.addTest(HomeMoreAbout("test_shareThisApp_back"))
        # suite.addTest(HomeMoreAbout("test_headerDisplay"))

        # suite.addTest(HomeMoreAppSettings("test_flow"))
        # suite.addTest(HomeMoreAppSettings("test_verifyCheckbox"))

        suite.addTest(Files("test_flow"))
        suite.addTest(Files("test_File_Basicfunctionactionbaroption_step1"))
        suite.addTest(Files("test_File_Basicfunctionactionbaroption_step2_3_4_5_6"))
        suite.addTest(Files("test_File_Basicfunctionactionbaroption_step7"))
        suite.addTest(Files("test_File_Basicfunctionactionbaroption_step8"))
        suite.addTest(Files("test_File_Basicfunctionactionbaroption_step9"))
        suite.addTest(Files("test_File_Basicfunctionactionbaroption_step10"))
        suite.addTest(Files("test_File_Basicfunctionactionbaroption_step11"))

        suite.addTest(Files("test_FilesMoreOption_step1"))
        suite.addTest(Files("test_FilesMoreOption_step2"))
        suite.addTest(Files("test_FilesMoreOption_step3"))
        suite.addTest(Files("test_01_docs_pdf_pull_down"))
        suite.addTest(Files("test_02_select_a_file"))
        suite.addTest(Files("test_03_select_multiple_jpegs"))
        suite.addTest(Files("test_04_select_mixed_file_types"))
        suite.addTest(Files("test_05_only_jpegs"))
        suite.addTest(Files("test_06_select_multiple_jpegs"))
        suite.addTest(Files("test_07_only_pdf"))
        suite.addTest(Files("test_08_select_multiple_pdfs"))

    elif initFwk.name_project == "WebExample":
        suite.addTest(TestBrowser("test_flow"))
    elif initFwk.name_project == "IosExample":
        suite.addTest(IosExample("test_flow"))
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)

