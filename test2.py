# -*- coding:utf-8 -*-
from conf.Run_conf import read_config

project_path = read_config('testcase', 'project_path')
print project_path
project_path = read_config('testcase','project_path')
udid = 'udid'
casename = 'casename'
log_filter_path = project_path + '/output/{}/html/filter/{}.log'.format(udid,casename)
print log_filter_path
# import sys
# print sys.platform
# str1 = '(10.2)'
# str2 = '[ae679a86542a57c31e57a1d66351c87570c9bac7]'
# dict1 ={}
# print eval(str1,{})
# print str2[1:-1]
# list1 = [['List', 'of', 'devices', 'attached'] ,['7N2SSE154M000509', 'unauthorized'],[]]
# for li in list1[1:]:
# 	if len(li)==0:
# 		continue
# 	if str(li[0]).startswith('List'):
# 		continue
# 	print li
# 	# print str(li).startswith('List')
# import os
# cmd = "netstat -an | grep %s" % '4723'
# print cmd
# print os.popen(cmd).readlines()
