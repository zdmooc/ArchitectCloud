import json 

data = {
        'quiz' : {
            'Chapitre 1 : premier pas' : {
                'Question 1' : {
                    'question' : 'Un bloc de code python est composée ',
                    'options' : [
                                    "d'instructions regroupées en bloc de code",
                                    "de formule magique",
                                    "de bloc de ciment",
                                    "de bloc en plastique",
                                    'de mots phrase et paragraphe avec "The End" en fin de scripts'
                        ],
                    'reponse'  : '1'
                    },
                'Question 2' : {
                    'question' : 'un bloc de code se défini en fonction de ',
                    'options'  : [
                                    "Son niveau d'indentation",
                                    "son taux d'alcool",
                                    "sa densité",
                                    "son poids en kilogrammes",
                                    "du nombre de lignes"
                                ],
                    'reponse'  : '1'
                    }
                }
            }
        }


data_json = json.dumps(data)
#print( data_json )
data_py = json.loads( data_json )
for chapitres in data_py['quiz'].values():
    for question, detail in chapitres.items():
        print(" Question : ",detail['question'] )
        for n, option in enumerate(detail['options']):
            print("  %s : %s " % (n+1, option))
