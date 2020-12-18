## score=[[]]
def query(search_query):
    import math
    import pymongo
    from pymongo import MongoClient
    connection = MongoClient()
    connection.database_names()
    db = connection.token

    score=[[]]

    links={}


    for x in search_query.split():
        text=db.words.find_one({'word':x})
        length=len(text['docid'])
        for z in range(0,length):
            if(text['docid'][z][1] in links):
                score_pos=links.get(text['docid'][z][1])
                inv_doc_score=math.log(text['docid'][z][4])+math.log(1/length)
                word_pos_score=(text['docid'][z][3]+1)/length
                word_pos_score=0
                print('link there',inv_doc_score,word_pos_score)
                score[score_pos][0]=score[score_pos][0]+inv_doc_score+word_pos_score
                score[score_pos][2].append(text['word'])
            else:
                temp_list=[0,'',[]]
                inv_doc_score=(math.log(text['docid'][z][4])+math.log(1/length))
                word_pos_score=(text['docid'][z][3]+1)/length
                word_pos_score=0
                print('link not there',inv_doc_score,word_pos_score)

                temp_list[0]=math.log(text['docid'][0][2])+inv_doc_score+word_pos_score
                temp_list[1]=text['docid'][z][1]
                temp_list[2].append(text['word'])
                score=score+[temp_list]
                links[temp_list[1]]=len(score)
        score.pop(0)
        score1=sorted(score, key=lambda x: x[0], reverse=True)
        dic={k: v for k,v in enumerate(score1)}        
        return dic
