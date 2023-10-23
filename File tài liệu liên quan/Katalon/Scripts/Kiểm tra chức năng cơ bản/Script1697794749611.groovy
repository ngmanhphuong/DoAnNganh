import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('')

WebUI.navigateToUrl('https://2051052105phuong.wordpress.com/')

WebUI.click(findTestObject('Object Repository/Testchucnang/Page_Daily News  Cp nht thng tin uy tn/a_Tin tc'))

WebUI.click(findTestObject('Object Repository/Testchucnang/Page_Tin tc  Daily News/a_L do  Nng tr thnh thnh ph ng n trong lng du khch'))

WebUI.click(findTestObject('Object Repository/Testchucnang/Page_L do  Nng tr thnh thnh ph ng n trong l_4eafd5/a_Thi s'))

WebUI.setText(findTestObject('Object Repository/Testchucnang/Page_Thi s  Daily News/input_Tm kim_s'), 'bão')

WebUI.sendKeys(findTestObject('Object Repository/Testchucnang/Page_Thi s  Daily News/input_Tm kim_s'), Keys.chord(Keys.ENTER))

WebUI.closeBrowser()

WebUI.click(findTestObject('Object Repository/Testchucnang/Page_Search Results for bo  Daily News/a_Bo cp 16 vo Bin ng'))

