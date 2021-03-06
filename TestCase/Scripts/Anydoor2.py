# -*- coding:utf-8 -*-
#######################################################
# filename:Anydoor.py
# author:Jeff
# date:2016-09-21
# function:对测试用例进行操作处理
#######################################################
import sys, time
import unittest, pytest
from conf.Run_conf import read_config
from src.Public.Global import L, D, S
from src.Public.appOperate import AppOperate
from src.lib.Element import Element
from src.Public import Public

reload(sys)
sys.setdefaultencoding('utf-8')

class Anydoor_UI(unittest.TestCase):

	def setup_class(cls):
		'''
		setup class
		:return:
		'''
		driver = D.driver
		cls.driver = Element(driver)
		cls.appOperate = AppOperate(driver)
		cls.username = read_config('login', 'login_username')
		cls.password = read_config('login', 'login_password')
		# global pluginList
		# pluginList = cls.appOperate.getPluginList()
		L.logger.debug('测试用例即将执行,初始化工作')

	def teardown_class(cls):
		'''
		teardown class
		:return:
		'''
		# cls.driver.close_app()
		# cls.driver.quit()
		L.logger.debug('测试用例执行完成,退出服务')



	def test_A1(self):
		'''用例名称:宿主一账通H5登录'''
		try:
			self.appOperate.loginByH5(self.username, self.password)
			time.sleep(3)
			loginResult = self.appOperate.wait_for_text(30, '我的订单')
			self.assertTrue(loginResult, '登陆成功')
		finally:
			self.appOperate.closeH5()
			time.sleep(3)
			self.driver.swipe_left()


	def test_A2(self):
		'''用例名称:获取插件列表'''
		getPluginList = self.appOperate.getPluginList()
		self.assertTrue(len(getPluginList),'获取所有插件列表')
		time.sleep(3)


	# def test_B1(self):
	# 	'''用例名称: 检查插件,插件名称: 买航意险,插件ID: PA01100000000_02_YYG,插件断言: 立即投保 '''
	# 	pluginId = 'PA01100000000_02_YYG'
	# 	L.logger.debug('遍历插件,插件ID: %s' % pluginId)
	# 	self.assertTrue(self.appOperate.check_plugin(pluginId, '1元GO'), '插件: %s 断言失败' % pluginId)

	# 判断如果插件平台如果不是ios,就跳过此用例
	# @pytest.mark.skipif(S.device['platformName'].lower() != 'ios','Android does not support plguin: PA01100000000_02_PAZB')
	# @unittest.skipIf(S.device['platformName'].lower() != 'ios','Android does not support plguin: PA01100000000_02_PAZB')

	@pytest.mark.parametrize('pluginId',['PA01100000000_02_PAZB'])
	@pytest.mark.skipif(Public.platform_pluginIn_isTrue('PA01100000000_02_PAZB'),
	                    'Android does not support plguin: PA01100000000_02_PAZB')
	def test_A3(self,pluginId):
		'''用例名称: 检查插件,插件名称: 平安地图,插件ID: PA01100000000_02_PAZB ,插件断言: 加油站 '''
		# pluginId = 'PA01100000000_02_PAZB'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '加油站'), '插件: %s 断言失败' % pluginId)  # 进行断言

	@pytest.mark.skipif(Public.platform_pluginIn_isTrue('PA01100000000_02_WLC'),
	                    'Android does not support plguin: PA01100000000_02_WLC')
	def test_A4(self):
		'''用例名称: 检查插件,插件名称: 模拟炒股,插件ID: PA01100000000_02_WLC ,插件断言: 值得买 '''
		pluginId = 'PA01100000000_02_WLC'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '值得买'), '插件: %s 断言失败' % pluginId)

	@pytest.mark.skipif(Public.platform_pluginIn_isTrue('PA02100000000_02_CJYX'),
	                    'Android does not support plguin: PA02100000000_02_CJYX')
	def test_A5(self):
		'''用例名称: 检查插件,插件名称: 辞旧赢薪,插件ID: PA02100000000_02_CJYX ,插件断言: 8、理财有风险，投资需谨慎。 '''
		pluginId = 'PA02100000000_02_CJYX'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '8、理财有风险，投资需谨慎。'), '插件: %s 断言失败' % pluginId)


	# @pytest.mark.skipif(True, reason='PA00300000000_02_MCX is offline!')
	@pytest.mark.skipif(Public.platform_pluginIn_isTrue('PA00300000000_02_MCX'),
	                    'Android does not support plguin: PA00300000000_02_MCX')
	def test_A51(self):
		'''用例名称: 检查插件,插件名称: 买车险,插件ID: PA00300000000_02_MCX,插件断言: 买车险' '''
		pluginId = 'PA00300000000_02_MCX'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '买车险'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_A6(self):
		'''用例名称: 检查插件,插件名称: 看直播,插件ID: PA00500000000_02_GSZB,插件断言: 热 门 '''
		pluginId = 'PA00500000000_02_GSZB'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '视频'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_A7(self):
		'''用例名称: 检查插件,插件名称: 活动集合,插件ID: PA01100000000_02_HDJHY,插件断言: 本活动的最终解释权归平安科技所有 '''
		pluginId = 'PA01100000000_02_HDJHY'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '本活动的最终解释权归平安科技所有'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	# 进入第二个页面
	def test_A8(self):
		'''用例名称: 检查插件,插件名称: 积分福利,插件ID: PA02100000001_02_JF,插件断言: 可用积分 '''
		pluginId = 'PA02100000001_02_JF'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		# self.driver.swipe_left()
		self.assertTrue(self.appOperate.check_plugin(pluginId, '可用积分'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	# 定位问题
	def test_A9(self):
		'''用例名称: 检查插件,插件名称: 找网点,插件ID: PA01100000001_02_WDCX,插件断言: ATM '''
		pluginId = 'PA01100000001_02_WDCX'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, 'ATM'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_B0(self):
		'''用例名称: 检查插件,插件名称: 卡面由你,插件ID: PA01100000001_02_XYK,插件断言: 我的信用卡 '''
		pluginId = 'PA01100000001_02_XYK'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '我的信用卡'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_B1(self):
		'''用例名称: 检查插件,插件名称: 买航意险,插件ID: PA01100000000_02_YYG,插件断言: 立即投保 '''
		pluginId = 'PA01100000000_02_YYG'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '1元GO'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_B2(self):
		'''用例名称: 检查插件,插件名称: 在线投资,插件ID: PA02500000000_02_TZLC,插件断言: XCUIElementTypeOther[3] '''
		pluginId = 'PA02500000000_02_TZLC'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '/0/0/1/0/1/0/0/0/0/0/2'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_B3(self):
		'''用例名称: 检查插件,插件名称: 房按揭,插件ID: PA03300000000_02_AJDK,插件断言: 试算一下 '''
		pluginId = 'PA03300000000_02_AJDK'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '试算一下'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_B4(self):
		'''用例名称: 检查插件,插件名称: 平安好贷,插件ID: PA01200000000_02_XYD,插件断言: 马上贷款 '''
		pluginId = 'PA01200000000_02_XYD'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '马上贷款'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_B5(self):
		'''用例名称: 检查插件,插件名称: 应急钱包,插件ID: PA02100000000_02_YJQB,插件断言: 获取动态码 '''
		pluginId = 'PA02100000000_02_YJQB'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '获取动态码'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_B6(self):
		'''用例名称: 检查插件,插件名称: 查号码,插件ID: PA00800000000_02_PACX,插件断言: 使馆信息 '''
		pluginId = 'PA00800000000_02_PACX'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '使馆信息'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	# @pytest.mark.xfail(run=False) #不运行此用例
	@pytest.mark.skipif(True, reason='PA01100000000_02_ZCCX is remaining!')
	def test_B7(self):
		'''用例名称: 检查插件,插件名称: 资产查询,插件ID: PA01100000000_02_ZCCX,插件断言: 资产提醒 '''
		pluginId = 'PA01100000000_02_ZCCX'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '资产提醒'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_B70(self):
		'''用例名称: 检查插件,插件名称: 活期盈,插件ID: PA02100000000_02_HQY,插件断言: 获取验证码 '''
		pluginId = 'PA02100000000_02_HQY'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '获取验证码'), '插件: %s 断言失败' % pluginId)

	def test_B71(self):
		'''用例名称: 检查插件,插件名称: 明星理财,插件ID: PA02100000000_02_KY,插件断言: 立即投资'''
		pluginId = 'PA02100000000_02_KY'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '收益5%-6%，明星产品，稳健首选！'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	# ------------ 下一页 ----------------
	def test_B8(self):
		'''用例名称: 检查插件,插件名称: 融e贷,插件ID: PA00500000000_02_RED,插件断言: 申请条件 '''
		pluginId = 'PA00500000000_02_RED'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		# self.driver.swipe_left()
		self.assertTrue(self.appOperate.check_plugin(pluginId, '申请条件'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	@pytest.mark.skipif(True, reason='PA01100000000_02_RYG is wrong with closeButton!')
	def test_C0(self):
		'''用例名称: 检查插件,插件名称: 精品特卖,插件ID: PA01100000000_02_RYG,插件断言: 个人中心 '''
		pluginId = 'PA01100000000_02_RYG'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '个人中心'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_C1(self):
		'''用例名称: 检查插件,插件名称: 意见反馈,插件ID: PA01100000000_02_YHFK,插件断言: 建议反馈 '''
		pluginId = 'PA01100000000_02_YHFK'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '建议反馈'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)


	def test_C3(self):
		'''用例名称: 检查插件,插件名称: 财富礼包,插件ID: PA02100000000_02_JNHPS,插件断言: 点击查看活动规则 '''
		pluginId = 'PA02100000000_02_JNHPS'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '点击查看活动规则'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_C4(self):
		'''用例名称: 检查插件,插件名称: 财富宝,插件ID: PA00400000000_02_CFBXZZC,插件断言: 温馨提示 '''
		pluginId = 'PA00400000000_02_CFBXZZC'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '温馨提示'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	@pytest.mark.skipif(True, reason='PA01100000001_02_WDCX is repeated!')
	def test_C5(self):
		'''用例名称: 检查插件,插件名称: 网点地图,插件ID: PA01100000001_02_WDCX,插件断言: ATM '''
		pluginId = 'PA01100000001_02_WDCX'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, 'ATM'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	# @pytest.mark.skipif(True, reason='PA02700000000_02_PAYX is wrong with closeButton!')
	def test_C50(self):
		'''用例名称: 检查插件,插件名称: 平安游戏,插件ID: PA02700000000_02_PAYX,插件断言: 欢乐游戏 '''
		pluginId = 'PA02700000000_02_PAYX'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '欢乐游戏'), '插件: %s 断言失败' % pluginId)

	# 电影票 - --PA02100000000_02_DYP - --H
	def test_C51(self):
		'''用例名称: 检查插件,插件名称: 电影票,插件ID: PA02100000000_02_DYP,插件断言: 电影 '''
		pluginId = 'PA02100000000_02_DYP'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '电影'), '插件: %s 断言失败' % pluginId)

	def test_C52(self):
		'''用例名称: 检查插件,插件名称: 薪易通,插件ID: SZDBK00000000_02_XYT,插件断言: 个人信息 '''
		pluginId = 'SZDBK00000000_02_XYT'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '个人信息'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	@pytest.mark.skipif(True, reason='PA02100000000_02_WDZC is remaining!')
	def test_C6(self):
		'''用例名称: 检查插件,插件名称: 我的资产,插件ID: PA02100000000_02_WDZC,插件断言: 个人中心 '''
		pluginId = 'PA02100000000_02_WDZC'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '个人中心'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_C7(self):
		'''用例名称: 检查插件,插件名称: 平安易贷,插件ID: PA02100000000_02_PAYD,插件断言: 小额消费贷款 '''
		pluginId = 'PA02100000000_02_PAYD'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '小额消费贷款'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	# ------ 下一页 ---------
	def test_C8(self):
		'''用例名称: 检查插件,插件名称: 买保尊宝 ,插件ID: PA02500000000_02_BZB,插件断言: 热销基金 '''
		pluginId = 'PA02500000000_02_BZB'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		# self.driver.swipe_left()
		self.assertTrue(self.appOperate.check_plugin(pluginId, '热销基金'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_C9(self):
		'''用例名称: 检查插件,插件名称: 车估值,插件ID: PA02100000000_02_CGZ,插件断言: 添加车 '''
		pluginId = 'PA02100000000_02_CGZ'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '添加车'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_D0(self):
		'''用例名称: 检查插件,插件名称: 房估值,插件ID: PA02100000000_02_FGZ,插件断言: 我的房产 '''
		pluginId = 'PA02100000000_02_FGZ'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '我的房产'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	# @pytest.mark.skipif(True, reason='PA02100000000_02_CJKX is wrong with closeButton!')
	def test_D1(self):
		'''用例名称: 检查插件,插件名称: 财经快讯,插件ID: PA02100000000_02_CJKX,插件断言: 财经快讯 '''
		pluginId = 'PA02100000000_02_CJKX'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '财经快讯'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	@pytest.mark.skipif(True, reason='PA02800000000_02_ESF is wrong with closeButton!')
	def test_D2(self):
		'''用例名称: 检查插件,插件名称: 二手房,插件ID: PA02800000000_02_ESF,插件断言: 售价 '''
		pluginId = 'PA02800000000_02_ESF'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '售价'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	@pytest.mark.skipif(True, reason='PA02800000000_02_XF is offline!')
	def test_D3(self):
		'''用例名称: 检查插件,插件名称: 新房,插件ID: PA02800000000_02_XF,插件断言: 总价 '''
		pluginId = 'PA02800000000_02_XF'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '总价'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_D4(self):
		'''用例名称: 检查插件,插件名称: 平安易贷,插件ID: PA02100000000_02_XEDK,插件断言: 小额消费贷款 '''
		pluginId = 'PA02100000000_02_XEDK'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '小额消费贷款'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_D5(self):
		'''用例名称: 检查插件,插件名称: 亲子礼包,插件ID: PA02100000000_02_JNHRS,插件断言: 点击查看活动规则 '''
		pluginId = 'PA02100000000_02_JNHRS'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '点击查看活动规则'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	@pytest.mark.skipif(True, reason='PA02100000000_02_JXHYYGW is offline!')
	def test_D51(self):
		'''用例名称: 检查插件,插件名称: 领购物卡,插件ID: PA02100000000_02_JXHYYGW,插件断言: 20元京东购物券充值至京东账户后，即可使用； '''
		pluginId = 'PA02100000000_02_JXHYYGW'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '20元京东购物券充值至京东账户后，即可使用；'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	# def test_D52(self):
	#     '''用例名称: 检查插件,插件名称: 领购物卡,插件ID: PA02100000000_02_JXHYYGW,插件断言: 20元京东购物券充值至京东账户后，即可使用； '''
	#     pluginId = 'PA02100000000_02_JXHYYGW'
	#     L.logger.debug('遍历插件,插件ID: %s' % pluginId)
	#     self.assertTrue(self.appOperate.check_plugin(pluginId, '20元京东购物券充值至京东账户后，即可使用；'), '插件: %s 断言失败' % pluginId)
	#     # self.appOperate.closeH5_byPluginId(pluginId)

	# -------- 下一页 ----------
	def test_D6(self):
		'''用例名称: 检查插件,插件名称: 领话费,插件ID: PA02100000000_02_JNHJK,插件断言: 点击查看活动规则 '''
		pluginId = 'PA02100000000_02_JNHJK'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '点击查看活动规则'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_D7(self):
		'''用例名称: 检查插件,插件名称: 保险超市,插件ID: PA01100000000_02_BXCS,插件断言: 旅行意外险 '''
		pluginId = 'PA01100000000_02_BXCS'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '旅行意外险'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_D8(self):
		'''用例名称: 检查插件,插件名称: 双11爆款,插件ID: PA01100000000_02_LHBLC,插件断言: 专享爆款 '''
		pluginId = 'PA01100000000_02_LHBLC'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '专享爆款'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	def test_D9(self):
		'''用例名称: 检查插件,插件名称: 股票组合,插件ID: PA00500000000_02_GPZH,插件断言: 股市有风险，投资需谨慎 '''
		pluginId = 'PA00500000000_02_GPZH'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '股市有风险，投资需谨慎'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)

	# 签到礼---PA02100000000_02_KXJ1---N
	@pytest.mark.skipif(True, reason='PA02100000000_02_KXJ1 is offline!')
	def test_D91(self):
		'''用例名称: 检查插件,插件名称: 签到礼,插件ID: PA02100000000_02_KXJ1,插件断言: 签到，立即兑换好礼（每日限量） '''
		pluginId = 'PA02100000000_02_KXJ1'
		L.logger.debug('遍历插件,插件ID: %s' % pluginId)
		self.assertTrue(self.appOperate.check_plugin(pluginId, '您已累计签到'), '插件: %s 断言失败' % pluginId)

	# self.appOperate.closeH5_byPluginId(pluginId)


	# """
# def test_E0(self):
#     '''用例名称: 检查插件,插件名称: 平安地图,插件ID: PA01100000000_02_PAZB ,插件断言: mapSelected '''
#     pluginId = 'PA01100000000_02_PAZB'
#     L.logger.debug('遍历插件,插件ID: %s' % pluginId)
#     self.assertTrue(self.appOperate.check_plugin(pluginId, 'mapSelected'),'插件: %s 断言失败' % pluginId)
#
# def test_E1(self):
#     '''用例名称: 不存在的插件ID,测试用例失败专用 '''
#     pluginId = 'PA00500000000_02_1GPZH'
#     L.logger.debug('遍历插件,插件ID: %s' % pluginId)
#     self.assertTrue(self.appOperate.check_plugin(pluginId, '专家观点'), '插件: %s 断言失败' % pluginId)
#
# def test_E2(self):
#     '''用例名称: 存在的插件ID,不存在的断言,测试用例失败专用 '''
#     pluginId = 'PA00500000000_02_GPZH'
#     L.logger.debug('遍历插件,插件ID: %s' % pluginId)
#     self.assertTrue(self.appOperate.check_plugin(pluginId, '专家2观点'), '插件: %s 断言失败' % pluginId)


if __name__ == '__main__':
	unittest.main()
# try:
#     print '*' * 40, " 开始测试 ", '*' * 40
#     suite = unittest.TestSuite()
#     # 跑指定某一个用例
#     # suite.addTest(Anydoor_UI("test_A1"))
#     # suite.addTest(Anydoor_UI("test_A3"))
#     # suite.addTest(Anydoor_UI("test_D3"))
#     # suite.addTest(Anydoor_UI("test_E0"))
#     #加载一个测试类下的所有测试用例
#     loader = unittest.TestLoader()
#     suite = loader.loadTestsFromTestCase(Anydoor_UI)
#
#     timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
#     report_path = os.path.abspath('../output/html/') + timestr + '_report.html'
#     ReportObject = open(report_path, "wb")
#     testRunner = HTMLTestRunner(stream=ReportObject,title='测试报告',description='IOS UI 自动化')
#     testRunner.run(suite)
#     ReportObject.close()
#     print '*' * 40, " 结束测试 ", '*' * 40
# except Exception as e:
#     L.logger.error(e)
# # finally:
#     appiumserver.stop_server()
# finally:
#     self.driver.quit()
