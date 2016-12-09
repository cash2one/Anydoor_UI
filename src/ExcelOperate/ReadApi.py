#coding=utf8
#######################################################
#filename:Interface_Test.py
#author:defias
#date:2015-7
#function:
#######################################################
import time
import unittest

from ReadElement import ReadElement
from conf.Run_conf import read_config
from src.Element import Element
from src.Public.Common import operate_api
from src.Public.Common import resultClass
from src.Public.Global import L
from src.appOperate import AppOperate

logger = L.logger
class ReadApi(unittest.TestCase):
	
	def __init__(self):
		# super(ReadApi,self).__init__()
		'''
		:param case_list: 此参数为公共案例库和sheet1 中用例所公用列表入参
		'''
		# self.case_list=case_list
		self.platformName = read_config('appium', 'platformName')
		self.appOperate = AppOperate()
		self.wd = Element()
		self.readElement = ReadElement()
		
	def readApiList(self,case_list=[]): #case_list是一维数组
		logger.debug('case_list :%s' % case_list)
		if case_list:
			try:
				self.callApi(case_list)
				return True
			except Exception as e:
				logger.error(e)
				return False

	@staticmethod
	def get_error_trace():
		return resultClass.trace
	
	@staticmethod
	def get_img_base64():
		return resultClass.img_base64
	
	def callApi(self,case_list):
		'''
		:description:通过字典api_dict管理api,并调用api,api定义则在operate_api类中
		:param case_list:
		:return:
		'''
		logger.debug('callApi执行中')
		
		api_dict = {
					operate_api.assertTrueCheckPlugin:lambda :self.assertTrue(self.appOperate.check_plugin(case_list[6],case_list[7]),case_list[2]),
					operate_api.assertTrue:lambda :self.assertTrue(self.appOperate.wait_for_text(int(case_list[7]),case_list[6]),case_list[2]),
					operate_api.assertFalse:lambda :self.assertFalse(self.appOperate.wait_for_text(int(case_list[7]),case_list[6]),case_list[2]),
		            operate_api.sendkeys:lambda :self.appOperate.sendKeys(self.readElement.find_element(self.readElement.read_element_text(case_list[5])),case_list[7]),
		            operate_api.click:lambda :self.appOperate.click(self.readElement.find_element(self.readElement.read_element_text(case_list[5])),case_list[2]),
		            operate_api.swipe2left:lambda :self.wd.swipe_left(),
		            operate_api.swipe2right:lambda :self.wd.swipe_right(),
		            operate_api.hidekeyboard:lambda :self.wd.hide_keyboard(case_list[7]),
		            operate_api.waitFortext:lambda :self.appOperate.wait_for_text(int(case_list[7]),case_list[6]),
		            operate_api.sleep:lambda :time.sleep(int(case_list[7])),
					operate_api.checkPlugin:lambda :self.appOperate.check_plugin(case_list[6],case_list[7]),
		            operate_api.closeH5:lambda :self.appOperate.closeH5(),
		            operate_api.closeH5ByPluginId:lambda :self.appOperate.closeH5_byPluginId(case_list[6]),
		            operate_api.getScreenShot:lambda :self.appOperate.get_screen_shot(),
		            operate_api.getPluginList:lambda :self.appOperate.getPluginList()
		    
		            }
		if api_dict.has_key(case_list[3]):
			logger.debug('Action_Keyword 操作:[ %s ]' % case_list[3])
			return api_dict[case_list[3]]()  #返回api对应的操作对象
		else:
			logger.warning('请检查Action_Keyword中的api是否输入正确!')
			# raise
			
	
	
if __name__ == '__main__':
	readapi = ReadApi()
	# readapi.callPublicCase('SwipeToClickPersonalCenter')
	# for publicCase in readapi.publicCaseList:
		