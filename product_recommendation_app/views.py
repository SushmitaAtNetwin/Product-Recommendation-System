from django.http import HttpResponse
from django.shortcuts import render
import os
import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD
import urllib.request
os.chdir("D:/")

from django.http import HttpResponse
from django.template import loader
import webbrowser
import json
from django.contrib import messages #import messages




def homepage(request):
    global load_data


    import os
    import pandas as pd
    import numpy as np
    from sklearn.decomposition import TruncatedSVD

    from PIL import Image
    os.chdir("D:/")
    fileData = pd.read_csv("random_data.csv")
    fileData = fileData.dropna()
    # fileData = fileData1.sample(frac=1)

    top5_prod = fileData.loc[fileData['rating'] == 5.0] 
    top5_prod.drop(['Unnamed: 0'], axis = 1, inplace = True)
    top_rated_product = top5_prod.sort_values(['rating'], ascending=False)

   
    top_five = top_rated_product.head()
    json_records  = top_five.to_json(orient ='records')
    load_data = []
    load_data = json.loads(json_records)
    
    context = {'d': load_data}
    

    
    return render(request, 'home.html', context)



def new_page(request):
   
    user_data = request.GET['q']

    print(user_data,"user entered")

   

    # test_str = "user_input" + ":" + user_data
    # res = []
    # for sub in test_str.split(', '):
    #     if ':' in sub:
    #         res.append(map(str.strip, sub.split(':', 1)))
    #     res = dict(res)

######################################################################

    import pandas as pd
    import os
    os.chdir("D:/")
    data = pd.read_csv("random_data.csv")

    # shuffled = data1.sample(frac=1)
    # data = data1[0:5000]
    data["ids12"]=[i for i in range(0,data.shape[0])]

    # df12 = data[data['Product_Type'].str.contains(user_data, na=False)]
    # print(len(df12), "records for belt")
  

    selected_product = data[['Product_Type','IMAGE','Description', 'PRICE']] [data['Product_Type'] == user_data]
    selected_json_records = selected_product.to_json(orient ='records')

    dataselected = json.loads(selected_json_records)
    
  
    from sklearn.feature_extraction.text import TfidfVectorizer
    import numpy as np
    vec=TfidfVectorizer()
    vecs=vec.fit_transform(data["imp"].apply(lambda x: np.str_(x)))
    vecs.shape
    from sklearn.metrics.pairwise import cosine_similarity
    sim=cosine_similarity(vecs) 
    print("***")
    def recommend(title):

        product_presence = data[data['Product_Type'].str.contains(title, na=False)]
        len_product_presence = len(product_presence)
    

        if(len_product_presence > 1):

            df12 = data[data['Product_Type'].str.contains(user_data, na=False)]
            df12.drop(['Unnamed: 0'], axis = 1, inplace = True)
            df12_top_rated = df12.loc[df12['rating'] == 5.0] 
            df12_top_rated = df12_top_rated.sort_values(['rating'], ascending=False)
            product_list_df12 = df12_top_rated['Product_Type']
            products = list(product_list_df12)

            return products
       
        elif(len_product_presence == 1):
            product_id=data[data.Product_Type==title]["ids12"].values[0]
            scores=list(enumerate(sim[product_id]))
        
            sorted_scores=sorted(scores,key=lambda x:x[1],reverse=True)
        
            sorted_scores=sorted_scores[1:]
        
            products=[data[products[0]==data["ids12"]]["Product_Type"].values[0] for products in sorted_scores]
            return products
        else:
            print("product not found")
        
            

    def recommend_ten(product_list):
        first_ten=[]
        count=0
        for product in product_list:
            if count > 20:
                break
            count+=1
            first_ten.append(product)
           
        return first_ten

    # lst=recommend("BuckleUp Men Brown Leather Belt")
    lst = recommend(user_data)
    m=recommend_ten(lst)
    l = []
    for i in m:
        if i not in l:
            l.append(i) 
    top_five_reco =  l[0:5]
    data123 = []
    for i in top_five_reco:
        
        grp1 = data[['Product_Type','IMAGE','Description', 'PRICE']] [data['Product_Type'] == i]
        json_records1  = grp1.to_json(orient ='records')
        data12 = json.loads(json_records1)
        data123.append(data12[0])


######################################################################


    return render(request, 'newpage.html', {'user_data':user_data,'data123': data123,'dataselected':dataselected})


def request_access(request):
    print("DJANGO VIEW")
    a = request.POST.get('request_data')
    b = request.POST.get('data')
    print(a)
    print(b)
    return HttpResponse(json.dumps(a),content_type="application/json")

def loginform(request):
    return render(request, 'login.html')


def account(request):

    print("inside account")



    from sklearn.feature_extraction.text import TfidfVectorizer
    import numpy as np
    
    data1234 = []
    
    login_id = request.GET['username']
    import pandas as pd
    import os
    os.chdir("D:/")
    data = pd.read_csv("random_data.csv")
    data["ids123"]=[i for i in range(0,data.shape[0])]

    vec=TfidfVectorizer()
    vecs=vec.fit_transform(data["imp"].apply(lambda x: np.str_(x)))
    vecs.shape
    from sklearn.metrics.pairwise import cosine_similarity
    sim=cosine_similarity(vecs) 
   
    def cal():
        global user_history_load_data
        user_presence = data[data['user_id'].apply(str).str.contains(login_id, na=False)]
        user_presence.drop(['Unnamed: 0'], axis = 1, inplace = True)
        user_presence = user_presence.loc[user_presence['rating'] >= 3.0] 
        user_presence = user_presence.sort_values(['rating'], ascending=False)

        json_records  = user_presence.to_json(orient ='records')
     
        user_history_load_data = json.loads(json_records)
        print(user_history_load_data,"formatted data is")

        # print(user_presence,"user purchased this products")

        # user_json_records  = user_presence.to_json(orient ='records')

        list_of_purchased_products = list(user_presence['Product_Type'])

        user_recommend(list_of_purchased_products)
       

    def user_recommend(list_of_purchased_products):
     
    
        for x in list_of_purchased_products:
           

            product_id=data[data.Product_Type==x]["ids123"].values[0]
            scores=list(enumerate(sim[product_id]))
        
            sorted_scores=sorted(scores,key=lambda x:x[1],reverse=True)
        
            sorted_scores=sorted_scores[1:]
        
            products=[data[products[0]==data["ids123"]]["Product_Type"].values[0] for products in sorted_scores]
            m_u = recommend_ten_u(products)

            l_u = []
            for i in m_u:
                if i not in l_u:
                    l_u.append(i) 
            top_five_reco =  l_u[0:5]
            
            for i in top_five_reco:
                
                grp1 = data[['Product_Type','IMAGE','Description', 'PRICE']] [data['Product_Type'] == i]
          
                json_records1  = grp1.to_json(orient ='records')
                data12 = json.loads(json_records1)
                data1234.append(data12[0])  

              

    def recommend_ten_u(product_list):

        first_ten=[]
        count=0
        for product in product_list:
            if count > 20:
                break
            count+=1
            first_ten.append(product)
           
        return first_ten


    cal()
   
 
    print(user_history_load_data,"user purchased history",)

    return render(request, 'account.html', {"user_history":data1234,"login_id":login_id,"user_puchased_history": user_history_load_data,"first_page": load_data})
   


  