
import requests
url='https://lf8q0kx152.execute-api.us-east-2.amazonaws.com/default/computeFitnessScore'
x=requests.post(url,json={"qconfig":"5 1 6 0 3 7 4 2","userID":714061,"githubLink":"https://github.com/imsitu/8Queens_Genetic_Algo"})
print(x.text)

'''
/Users/situ/PycharmProjects/8Queens_Genetic_Algo/venv/bin/python /Users/situ/PycharmProjects/8Queens_Genetic_Algo/Week1.py
{"No Of Attempts lapsed out of 3": 2, "submittedConfiguration": [5, 1, 6, 0, 3, 7, 4, 2], "configurationStatus": "Valid", "configurationScore": 100.0}

Process finished with exit code 0
'''