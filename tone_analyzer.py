import json
from ibm_watson import ToneAnalyzerV3
from ibm_watson import ApiException

text = 'hello :)'

def tone_analyzer(text):
    try:
        tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        iam_apikey='bFFMuJmMPVXbvDr2u31YtrjdGv69UKjUJ7s1WO73NmA-',
        url='https://gateway-lon.watsonplatform.net/tone-analyzer/api'
        )

        tone_analysis = tone_analyzer.tone(
        {'text': text}, content_type='application/json').get_result()
        parsed_string = json.loads(json.dumps(tone_analysis, indent=2))
        #print(json.dumps(tone_analysis, indent=2))     
        result = {'anger':None,'anxiety':None,'happiness':None,'sadness':None}

        for item in parsed_string["document_tone"]["tones"]:
            for key , value in item.items():
                if  result['anger'] == None : 
                    result['anger'] = round(item['score'],2) if 'anger' in item.values() else 0
                if  result['anxiety'] == None :
                    result['anxiety'] = round(item['score'],2) if 'fear' in item.values() else 0
                if  result['happiness'] == None :
                    result['happiness'] = round(item['score'],2) if 'joy' in item.values() else 0
                if  result['sadness'] == None :
                    result['sadness'] = round(item['score'],2) if 'sadness' in item.values() else 0
        for key, value in result.items():
            if value == None:
                result[key] = 0

        print(result)
        return(result)

    except ApiException as ex:
        print('Method failed with status code ' + str(ex.code) + ': ' + ex.message)

tone_analyzer(text)

