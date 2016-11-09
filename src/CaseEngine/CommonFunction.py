#coding=gbk
#######################################################
#filename:Comm_Function.py
#author:defias
#date:2015-8
#function:����������ȫ�ֱ���
#######################################################
from src.Public import ExcelRW
from RunCaseEngine import RunCaseEngine
from RunCaseEngine import RunElementEngine
from src.Global import *
from conf.Run_conf import read_config

# �����ļ����ֶζ���
testcase_col = {u'CaseSuite(����)':1, u'CaseID(����id)':2, u'Description(��������)':3, u'Action_Keyword(����)':4,
                u'ios or android(ios��android���в���)':5, u'Element(Ԫ�ط�װ)':6, u'PageObject(ҳ��Ԫ��)':7,u'Parameter(�������)':8}

element_col = {u'Ԫ�ط�װ':1,u'��λ��ʽ(android)':2,u'Ԫ��ʵ��(android)':3,
               u'����(android)':4,u'��λ��ʽ(ios)':5,u'Ԫ��ʵ��(ios)':6,u'����(ios)':7}

platformName = read_config('appium','platformName')

def Get_Element_Excel(datafile, sheetn, element_row):
    element_rown = element_row +1
    # �ж���
    element_coln = element_col[u'Ԫ�ط�װ']
    operate_type_andr_coln = element_col[u'��λ��ʽ(android)']
    operate_type_ios_coln = element_col[u'��λ��ʽ(ios)']
    operate_value_andr_coln = element_col[u'Ԫ��ʵ��(android)']
    operate_value_ios_coln = element_col[u'Ԫ��ʵ��(ios)']
    operate_index_andr_coln = element_col[u'����(android)']
    operate_index_ios_coln = element_col[u'����(ios)']

    # ��ʼ�����������ļ�����
    xlseng = ExcelRW.XlsEngine(datafile)
    xlseng.open()

    # �洢��ȡ������
    element_name = xlseng.readcell(sheetn, element_rown, element_coln)
    operate_type_andr = xlseng.readcell(sheetn, element_rown, operate_type_andr_coln)
    operate_type_ios = xlseng.readcell(sheetn, element_rown, operate_type_ios_coln)
    operate_value_andr = xlseng.readcell(sheetn, element_rown, operate_value_andr_coln)
    operate_value_ios = xlseng.readcell(sheetn, element_rown, operate_value_ios_coln)
    operate_index_andr = xlseng.readcell(sheetn, element_rown, operate_index_andr_coln)
    operate_index_ios = xlseng.readcell(sheetn, element_rown, operate_index_ios_coln)

    element_result_list ={}
    if platformName.lower() == 'ios':
        run_element_engine_ios = RunElementEngine(element_name,operate_type_ios,operate_value_ios,operate_index_ios)
        return run_element_engine_ios
    elif platformName.lower() == 'android':
        run_element_engine_andr = RunElementEngine(element_name,operate_type_andr,operate_value_andr,operate_index_andr)
        return run_element_engine_andr
    else:
        logger.warning('�ݲ�֧�ֵ�ƽ̨����')
        return 0

# ��ʼ����ȡһ������������Ϣ
def Runner_TestCase(datafile, sheetn, testid):
    #����������
    testcase_rown = testid + 1

    #�ж���
    case_id_coln = testcase_col[u'CaseID(����id)']
    case_suit_coln = testcase_col[u'CaseSuite(����)']
    case_description_coln = testcase_col[u'Description(��������)']
    case_api_coln = testcase_col[u'Action_Keyword(����)']
    andr_or_ios_coln = testcase_col[u'ios or android(ios��android���в���)']
    case_element_coln = testcase_col[u'Element(Ԫ�ط�װ)']
    case_pageobject_coln = testcase_col[u'PageObject(ҳ��Ԫ��)']
    case_param_coln = testcase_col[u'Parameter(�������)']

    #��ʼ�����������ļ�����
    xlseng = ExcelRW.XlsEngine(datafile)
    xlseng.open()

    # �洢��ȡ������
    case_id = xlseng.readcell(sheetn, testcase_rown, case_id_coln)
    case_suit = xlseng.readcell(sheetn, testcase_rown, case_suit_coln)
    # case_description = xlseng.readcell(sheetn, testcase_rown, case_description_coln)
    case_api = xlseng.readcell(sheetn, testcase_rown, case_api_coln)
    andr_or_ios = xlseng.readcell(sheetn, testcase_rown, andr_or_ios_coln)
    case_element = xlseng.readcell(sheetn, testcase_rown, case_element_coln)
    case_pageobject = xlseng.readcell(sheetn, testcase_rown, case_pageobject_coln)
    case_param = xlseng.readcell(sheetn, testcase_rown, case_param_coln)

    result_list = [] # ��ź������ؽ��
    runcaseengine = RunCaseEngine(case_id,case_api,andr_or_ios,case_element,case_pageobject,case_param)
    runcase_operate = runcaseengine.operate()
    result_list.append(runcase_operate)
    #tresponse=result_list.append(response)
    #print "tresponse",tresponse
    result_list.append(case_suit)
    result_list.append(case_api)
    result_list.append(andr_or_ios)
    result_list.append(case_element)

    #print "result_list=",result_list
    return result_list

# ��ȡ�����ļ��е��������ƺͽӿ�����
def Get_Testcase_Name(datafile, sheetn, testid):
    #����������
    testcase_rown = testid + 1
    #�ж���
    casename_coln = testcase_col[u'��������']
    operate_type_coln = testcase_col[u'��λ��ʽ']
    operate_value_coln = testcase_col[u'��λԪ��']

    #��ʼ�����������ļ�����
    xlseng = ExcelRW.XlsEngine(datafile)
    xlseng.open()

    casename = xlseng.readcell(sheetn, testcase_rown, casename_coln)
    operate_type = xlseng.readcell(sheetn, testcase_rown, operate_type_coln)
    operate_value = xlseng.readcell(sheetn, testcase_rown, operate_value_coln)
    # ���ݱ��������������ֵ��˳��
    return casename,operate_type,operate_value

if __name__ == '__main__':
    datafile = '..\\..\\TestCase\\Excel\\TestCase.xlsx'
    result_list = Runner_TestCase(datafile, 'Sheet1', 1)
    print result_list
    # response = result_list[0]
    # # print response.status_code
    # print response.headers
    # print response.content

    #print Get_Testcase_Name(datafile,'Sheet1', 1)[2]
