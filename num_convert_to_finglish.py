#!/usr/bin/env python
# coding: utf-8

# In[66]:


dict_finglish = {"yek":1 , "do":2 , "se":3 , "chahaar" :4 , "panj":5 , "shesh":6 , "haft":7 , "hasht":8 , "noh":9 , "dah":10
                ,"yaazdah":11 , "davaazdah":12 , "sizdah":13 , "chahaardah":14 , "paanzdah":15 , "shaanzdah":16 , "hifdah":17
                , "hijdah": 18 , "noozdah":19 , "bist":20 , "si":30 , "chehel":40 , "panjaah":50 , "shast":60 , "haftaad":70
                , "hashtaad":80 , "navad":90 , "sad":100 , "devist":200 , "sisad":300 , "chahaarsad":400 , "paansad":500,
                "sheshsad":600 , "haftsad":700 , "hashtsad":800 , "nohsad":900  }
query = int(input())
if query<=500 and query>=1:
    sql=[]
    for i in range(query):
        x = int(input())
        if x<=999 and x>=1:
            if x<20 :
                for key , value in dict_finglish.items():
                    if x==value:
                        sql.append(key)
            elif x>19 and x<100 :
                sample =""
                yekan =x%10
                dahgan =(x//10)*10
                for key , value in dict_finglish.items():
                    if value == dahgan:
                        sample+=key
                for key , value in dict_finglish.items():
                    if value ==yekan:
                        if value==0:
                            break
                        else:
                            sample+="o "+key
        
                sql.append(sample)
            else:
                sample2=""
                yekan1 =x%10
                dahgan1=((x//10)%10)*10
                dahgan2=(x%100)
                sadgan=(x//100)*100
                for key , value in dict_finglish.items():
                    if value ==sadgan:
                        sample2+=key

                if dahgan2<20 and dahgan2>10:
                    for key , value in dict_finglish.items():
                        if value==dahgan2:
                            sample2+="o "+key
                else:
                    for key , value in dict_finglish.items():
                        if value == dahgan1:
                            if value==0:
                                break
                            else:
                                sample2+="o "+key
                            
                    for key , value in dict_finglish.items():
                        if value ==yekan1:
                            if value==0:
                                break
                            else:
                                sample2+="o "+key
                sql.append(sample2)

for i in sql:
    print(i)

