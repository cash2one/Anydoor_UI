# -*- coding:utf-8 -*-
import os
import time
import unittest

from conf.Run_conf import read_config
from src.ExcelOperate.ReadApi import ReadApi
from src.Public.Common import operate_api
from src.Public.Common import public
from src.Public.Common import resultClass
from src.Public.Common import resultStutas
from src.Public.Global import L
from src.Public.HtmlReport import HtmlReport
from src.Public.Retry import Retry
from src.lib import ExcelRW
from src.lib.Element import Element

logger = L.logger
xls_file_path = read_config('testcase', 'xls_case_path')
retry_num = int(read_config('retry', 'retry_num'))
retry_isTrue = bool(read_config('retry', 'retry_isTrue'))
xlsEngine = ExcelRW.XlsEngine(xls_file_path)
xlsEngine.open()  # 打开excel
readApi = ReadApi()
case_sheet1 = xlsEngine.readsheet(public.case_sheet)
# 记录测试开始时间
start_time = time.time()
result = resultClass.result
# driver = Element()

class RunExcelCase(unittest.TestCase):
	def __init__(self,mouldeName,caselist):
		super(RunExcelCase,self).__init__(mouldeName)
		self.readApi = ReadApi()
		self.xls_file_path = read_config('testcase', 'xls_case_path')
		self.platform = read_config('appium','platformName')
		# self.screen_shot_isTrue = bool(read_config('testcase','screen_shot_isTrue'))
		self.xlsEngine = ExcelRW.XlsEngine(self.xls_file_path)
		self.xlsEngine.open()  # 打开excel
		self.publicCaseList = self.xlsEngine.readsheet(public.public_case_sheet)
		self.sheetCaseList = self.xlsEngine.readsheet(public.case_sheet)
		self.caselist = caselist
	
	@classmethod
	def setup_class(cls):
		cls.driver = Element()
		
	@classmethod
	def teardown_class(cls):
		cls.driver.quit()
	
	def callPublicCase(self, casename):
		'''
		:description:判断casename是否在公共案例库中,如有则执行公共案例库
		:param casename:
		:return:   还缺少对ios或者Android独有的判断
		'''
		public_case_type = 0 #公共案例库名称不为空
		result_public = [] #存放公共案例库执行结果
		logger.debug('callPublicCase 执行中')
		# 遍历公共案例库
		for publicCase in self.publicCaseList[1:] :
			# 执行公共案例库,案例名称为空的部分
			if public_case_type == 1:
				if (publicCase[0] == '') and (publicCase[1] !=''):
					if ((self.platform).lower() == str(publicCase[4]).lower()) or (len(publicCase[4]) == 0):
						if readApi.readApiList(publicCase):
							# 公共案例每步执行结果记录
							result_public.append(resultStutas.success)
						else:
							# 公共案例每步执行结果记录
							result_public.append(resultStutas.fail)
							# 跳出循环
							break
					else:
						# 跳出循环继续执行
						continue
				else:
					# 跳出循环
					break
			else:
				# 先定位到指定案例
				if casename == publicCase[0]:
					result_public.append(publicCase[0])
					# publicCaseID = publicCase[1]
					logger.debug('公共案例库中存在此方法: %s' % casename)
					if ((self.platform).lower() == str(publicCase[4]).lower()) or (len(publicCase[4]) == 0):
						if readApi.readApiList(publicCase):
							# 公共案例每步执行结果记录
							result_public.append(resultStutas.success)
						else:
							# 公共案例每步执行结果记录
							result_public.append(resultStutas.fail)
							#跳出循环继续执行
							break
					else:
						continue
					public_case_type = 1
				
		return result_public
	
	# def screen_shot_turn(self):
	# 	try:
	# 		screen_shot_path = os.path.abspath('./output/screenshot/{}.png'.format(self.caselist[0]))
	# 		if self.screen_shot_isTrue:
	# 			logger.debug('截图开关已打开,截图保存路径: %s' % screen_shot_path)
	# 			driver.screenshot_as_file(screen_shot_path)
	# 		else:
	# 			pass
	# 	except Exception as e:
	# 		logger.error(e)
		
	#function:运行一条测试用例,Retry 失败重跑,1重跑次数,isRetry重跑开关
	# @pytest.hookimpl()
	@Retry(retry_num,isRetry=retry_isTrue)
	def function(self):
		logger.debug('测试用例:%s ,执行开始' % self.caselist[0])
		
		case_start_time = time.time()
		case_list = []
		case_list.append(self.caselist[0])
		# 判断是否为公共库api
		if operate_api.publicCase == self.caselist[3]:
			# 执行公共案例库
			result_public = self.callPublicCase(self.caselist[7])
			logger.debug('公共案例库执行记录: %s' % result_public)
			if resultStutas.fail in result_public:
				# result[self.caselist[0]] = resultStutas.fail
				case_list.append(resultStutas.fail)
			else:
				# result[self.caselist[0]] = resultStutas.success
				case_list.append(resultStutas.success)
			if case_list:
				logger.debug('===' * 40)
				logger.debug('当前用例:%s ,执行结果: %s' % (case_list[0],case_list[1]))
				logger.debug('===' * 40)
			else:
				logger.warning('case_list 为空')
		
		else:
			# 执行测试用例
			if self.readApi.readApiList(self.caselist):
				case_list.append(resultStutas.success)
			else:
				case_list.append(resultStutas.fail)
				# 失败截图
				# self.screen_shot_turn()
			if case_list:
				logger.debug('===' * 40)
				# logger.debug('执行结果记录: %s' % case_list)
				logger.debug('当前用例:%s ,执行结果: %s' % (case_list[0],case_list[1]))
				logger.debug('===' * 40)
			else:
				logger.warning('case_list 为空')
		case_cost_time = time.time() - case_start_time
		case_cost_time =round(case_cost_time,3)
		case_list.append(case_cost_time)
		# 判断result列表最后一个元素是否是当前的测试用例,如果是当前用例则更新原用例的结果,如果不是,则添加新结果
		if result:
			if result[-1][0] == case_list[0]:
				result[-1][1]=case_list[1] # 更新结果
				result[-1][2] = case_list[2] # 更新时间
			else:
				result.append(case_list)
		else:
			result.append(case_list)
		
		logger.debug('测试用例:%s ,执行结束' % self.caselist[0])
		logger.debug('用例执行总结果: %s' % result)
		return case_list
	

def get_html_report():
	html_result_path = os.getcwd()+'/output/html/'+'report.html'
	htmlreport_path = os.path.abspath(html_result_path)
	# 测试结束时间
	end_time = time.time()
	tcHtmlReport = HtmlReport()
	# 生成测试报告
	tcHtmlReport.set_result_filename(htmlreport_path)
	tcHtmlReport.set_testcase_result(result)
	tcHtmlReport.set_run_time(end_time - start_time)
	tcHtmlReport.generate_html(u'测试报告')
	
def get_test_suite(case_list):
	test_suite = unittest.TestSuite()
	test_suite.addTest(RunExcelCase("function",case_list))
	return test_suite

def Run_Case(runner):
	# 类初始化
	RunExcelCase.setup_class()
	# 循环遍历测试用例列表
	for case_list in case_sheet1[1:]:
		test_suite = get_test_suite(case_list)
		runner.run(test_suite)
	# driver退出
	# RunExcelCase.teardown_class()
	logger.debug('所有用例的结果: %s' % result)
	get_html_report()

if __name__ == '__main__':
	
	# current_path = os.getcwd()
	# timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
	# report_path = current_path + '/output/html/'+ timestr + '_report.html'
	# ReportObject = open(report_path, "wb")
	# testRunner = HTMLTestRunner.HTMLTestRunner(stream=ReportObject, title='Report', description='IOS')
	#
	# # runner = unittest.TextTestRunner()
	# Run_Case(testRunner)
	# ReportObject.close()
	#
	
	runner = unittest.TextTestRunner()
	Run_Case(runner)
	