import subprocess
import sys
import urllib.parse
import os

def defaultsetting():
    # some field needs empty for zeros
    params = {
        "NumThread": "2",
        "LoopCount": "2",
        "Ramp_Time": "0", # in seconds
        "ActionWhenSamplerError": "continue",
        "Timeout_Response": "3000", # in milliseconds ## IMPORTANT, "" empty means 0
        "Timeout_Connet": "",
        "KeepAlive": "false",
    }

    return params

# add Clofly special setting
def CloflyTest():
    params = defaultsetting()

    params['Method'] = "GET"
    #params['domain'] = "clofly.com"
    params['platform'] = "Clofly"

    return params

# add OpenLambda special setting
def OpenLambdaTest():
    params = defaultsetting()

    params['Method'] = "POST"
    params['BodyData'] = "{&quot;name&quot;:&quot;Heron&quot;}"
    #params['domain'] = "104.198.2.90"
    params['platform'] = "OpenLambda"

    return params

def IronTest():
    params = defaultsetting()
    params['Method'] = "GET"
    params['platform'] = "Iron"

    return params

def headerTailerJmeter(params):

    headerString = '<?xml version="1.0" encoding="UTF-8"?>\n'
    headerString += '<jmeterTestPlan version="1.2" properties="3.1" jmeter="3.1 r1770033">\n'
    headerString += '  <hashTree>\n'

    #Test plan description
    headerString += '    <TestPlan guiclass="TestPlanGui" testclass="TestPlan" '
    headerString += 'testname="'
    headerString += params["platform"] + '" enabled="true">\n'
    headerString += '      <stringProp name="TestPlan.comments"></stringProp>\n'
    headerString += '      <boolProp name="TestPlan.functional_mode">false</boolProp>\n'
    headerString += '      <boolProp name="TestPlan.serialize_threadgroups">false</boolProp>\n'
    headerString += '      <elementProp name="TestPlan.user_defined_variables" elementType="Arguments"'
    headerString += ' guiclass="ArgumentsPanel" testclass="Arguments" testname="userdefined" enabled="true">\n'
    headerString += '        <collectionProp name="Arguments.arguments"/>\n'
    headerString += '      </elementProp>\n'
    headerString += '      <stringProp name="TestPlan.user_define_classpath"></stringProp>\n'
    headerString += '    </TestPlan>\n'
    headerString += '    <hashTree>\n'

    tailerString = '    </hashTree>\n'
    tailerString += '  </hashTree>\n'
    tailerString += '</jmeterTestPlan>'

    return headerString, tailerString

def Thread_Group_Jmeter(params, URLString):


    thread_group_content = '      <ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" '
    thread_group_content += 'testname="Thread Group" enabled="true">\n'
    thread_group_content += '        <stringProp name="ThreadGroup.on_sample_error">'+params['ActionWhenSamplerError']+'</stringProp>\n'
    thread_group_content += '        <elementProp name="ThreadGroup.main_controller" '
    thread_group_content += 'elementType="LoopController" guiclass="LoopControlPanel" '
    thread_group_content += 'testclass="LoopController" testname="Loop Controller" enabled="true">\n'
    thread_group_content += '          <boolProp name="LoopController.continue_forever">false</boolProp>\n'
    thread_group_content += '          <stringProp name="LoopController.loops">'+params["LoopCount"]+'</stringProp>\n'
    thread_group_content += '        </elementProp>\n'
    thread_group_content += '        <stringProp name="ThreadGroup.num_threads">'+params["NumThread"]+'</stringProp>\n'
    thread_group_content += '        <stringProp name="ThreadGroup.ramp_time">'+params["Ramp_Time"]+'</stringProp>\n'

    # fixed start_time and end_time for 4/13/2017 15:51:21
    thread_group_content += '        <longProp name="ThreadGroup.start_time">1492113081000</longProp>\n'
    thread_group_content += '        <longProp name="ThreadGroup.end_time">1492113081000</longProp>\n'
    thread_group_content += '        <boolProp name="ThreadGroup.scheduler">false</boolProp>\n'
    thread_group_content += '        <stringProp name="ThreadGroup.duration"></stringProp>\n'
    thread_group_content += '        <stringProp name="ThreadGroup.delay"></stringProp>\n'
    thread_group_content += '      </ThreadGroup>\n'

    return thread_group_content

def HTTPRequest_Jmeter(params, URLStringPath):

    HTTPrequest_content = '      <hashTree>\n'
    HTTPrequest_content += '        <HTTPSamplerProxy guiclass="HttpTestSampleGui" '
    HTTPrequest_content += 'testclass="HTTPSamplerProxy" testname="HTTP Request" enabled="true">\n'

    if params['Method'] == "POST":
        HTTPrequest_content += '          <boolProp name="HTTPSampler.postBodyRaw">true</boolProp>\n'
        HTTPrequest_content += '          <elementProp name="HTTPsampler.Arguments" elementType="Arguments">\n'
        HTTPrequest_content += '            <collectionProp name="Arguments.arguments">\n'
        HTTPrequest_content += '              <elementProp name="" elementType="HTTPArgument">\n'
        HTTPrequest_content += '                <boolProp name="HTTPArgument.always_encode">false</boolProp>\n'
        HTTPrequest_content += '                <stringProp name="Argument.value">'
        HTTPrequest_content += params['BodyData']
        HTTPrequest_content += '</stringProp>\n'
        HTTPrequest_content += '                <stringProp name="Argument.metadata">=</stringProp>\n'
        HTTPrequest_content += '              </elementProp>\n'
        HTTPrequest_content += '            </collectionProp>\n'
        HTTPrequest_content += '          </elementProp>\n'
        HTTPrequest_content += ''
    elif params['Method'] == "GET":
        HTTPrequest_content += '          <elementProp name="HTTPsampler.Arguments" elementType="Arguments" '
        HTTPrequest_content += 'guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User '
        HTTPrequest_content += 'Defined Variables" enabled="true">\n'
        HTTPrequest_content += '            <collectionProp name="Arguments.arguments"/>\n'
        HTTPrequest_content += '          </elementProp>\n'

    else:
        raise ValueError("Not implmenet methods except 'GET' and 'POST'")


    # contents related to HTTPSample


    HTTPrequest_content += '          <stringProp name="HTTPSampler.domain">'+params["domain"]+'</stringProp>\n'
    HTTPrequest_content += '          <stringProp name="HTTPSampler.port"></stringProp>\n'
    HTTPrequest_content += '          <stringProp name="HTTPSampler.connect_timeout">'+params["Timeout_Connet"]+'</stringProp>\n'
    HTTPrequest_content += '          <stringProp name="HTTPSampler.response_timeout">'+params["Timeout_Response"]+'</stringProp>\n'
    HTTPrequest_content += '          <stringProp name="HTTPSampler.protocol"></stringProp>\n'
    HTTPrequest_content += '          <stringProp name="HTTPSampler.contentEncoding"></stringProp>\n'
    HTTPrequest_content += '          <stringProp name="HTTPSampler.path">'+URLStringPath+'</stringProp>\n'
    HTTPrequest_content += '          <stringProp name="HTTPSampler.method">'+params['Method']+'</stringProp>\n'
    HTTPrequest_content += '          <boolProp name="HTTPSampler.follow_redirects">true</boolProp>\n'
    HTTPrequest_content += '          <boolProp name="HTTPSampler.auto_redirects">false</boolProp>\n'
    HTTPrequest_content += '          <boolProp name="HTTPSampler.use_keepalive">'+params["KeepAlive"]+'</boolProp>\n'
    HTTPrequest_content += '          <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>\n'
    HTTPrequest_content += '          <boolProp name="HTTPSampler.monitor">false</boolProp>\n'
    HTTPrequest_content += '          <stringProp name="HTTPSampler.embedded_url_re"></stringProp>\n'
    HTTPrequest_content += '        </HTTPSamplerProxy>\n'
    HTTPrequest_content += '        <hashTree/>\n'
    HTTPrequest_content += '      </hashTree>\n'

    return HTTPrequest_content

def executeJmeter(outputFileName, inputURL, numFile, params):

    temp_configure_folder = 'temp_configure'
    temp_output_data_folder = 'temp_output_data'

    headerString, tailerString  = headerTailerJmeter(params)

    #create temparay folder to store the data
    result = subprocess.run(['mkdir', temp_configure_folder], stdout=subprocess.PIPE)
    result.stdout

    # CAUTIOUS remove temp_output_data_folder
    result = subprocess.run(['rm', '-r', temp_output_data_folder], stdout=subprocess.PIPE)
    result.stdout

    result = subprocess.run(['mkdir', temp_output_data_folder], stdout=subprocess.PIPE)
    result.stdout




    for i in range(numFile):

        with open("./temp_configure/testconfigure.jmx", 'w') as outfile:
            outfile.write(headerString)

            # add URL
            for index_URL in range(i + 1):
                thread_group_content = Thread_Group_Jmeter(params, inputURL[index_URL])
                outfile.write(thread_group_content)

                HTTPrequest_content = HTTPRequest_Jmeter(params, inputURL[index_URL])
                outfile.write(HTTPrequest_content)

            outfile.write(tailerString)

        #excetue Jmeter
        output_result = outputFileName + "function_" + str(i) + ".csv"
        output_result = os.path.join(".",temp_output_data_folder, output_result)
        #print("output_result is {0}".format(output_result))
        print("{0}/{1}".format(i+1, numFile))

        result = subprocess.run(['jmeter', '-n', '-t', './temp_configure/testconfigure.jmx', '-l', output_result],stdout=subprocess.PIPE)
        result.stdout




def main(TestPlatForm, inputFileName, NumURL):
    #result = subprocess.run(['jmeter', '-n', '-t', 'Clofly_test.jmx', '-l', 'clofly.jtl'], stdout=subprocess.PIPE)
    #result.stdout

    outputFileName = TestPlatForm + "_"

    #Get params

    if(TestPlatForm == "Clofly"):
        params = CloflyTest()
    elif(TestPlatForm == "OpenLambda"):
        params = OpenLambdaTest()
    elif(TestPlatForm == "Iron"):
        params = IronTest()
    else:
        error_message = "Wrong platform: " + TestPlatForm
        raise ValueError(error_message)

    print("Progress")

    #Read input URL
    inputURL = []
    with open(inputFileName, 'r') as infile:
        for line in infile:
            # process get only path

            #parsing url to split path and domain name
            #input: http://www.godl.com/d or 127.1.1.1/d

            url_path = line
            if "http://" in line:
                url_path = line.split("http://")[1] #[0] is empty

            #split by "/"
            url_path = url_path.split("/",1) # [0] is domain name, [1] is path
            params["domain"] = url_path[0].strip()

            #url_path = urllib.parse.urlparse(line).path
            #print("url_path {0}".format(url_path[1].strip()))
            inputURL.append(url_path[1].strip())

    executeJmeter(outputFileName, inputURL, min(int(NumURL), len(inputURL)), params)

    print("End of Jmeter Processing")



def warnInputargument(inputArgument):
    print("JmeterAuto takes two arguments:\n First is 'OpenLambda' or 'Clofly' or 'Iron'\n Second is input file name"
          "\n Third is the number of lines you want to test in input file")

    print("Your input is {0}".format(inputArgument))

if __name__ == '__main__':

    # sys.argv[0] is JmeterAuto.py, sys.argv[1] is testplantform, sys.argv[2] is inputFile, sys.argv[3]
    #print ("input argumaent {0}".format(sys.argv))
    if (len(sys.argv) != 4) or (int(sys.argv[3]) <= 0):
        warnInputargument(sys.argv)


    print("TestPlatForm is {0}".format(sys.argv[1]))
    main(sys.argv[1], sys.argv[2], sys.argv[3])