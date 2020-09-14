from flask import Flask,request,jsonify   
import re
app = Flask(__name__)

#@app.route("/ask", methods = ["POST", "GET"])
#def hello_bot():
#    return "Hello  Khadija how are you"
qa={
    "ukimwi ni nn?":"upungufu wa kinga mwwilini",
    "vvu ni nini": "ni virusi vinavyosambaza ugonjwa",
    "dalili ni zipi?":"homa kali,kuharisha,kutapika,mwili kukosa nguvu,vidonda mdomoni",
    "utapataje ukimwi?":"kwa njia ya kubadilishana majimaji yanayotoka kwa mgonjwa mfano damu,na kwa njia ya kujamiana pamoja na kuchangia vitu vya ncha kali",
    "ugonjwa huu unaweza kuenezwa kwa njia ya hewa?":"hapana",
    "utafahamu vp umeathirika":"kwa kupima",
    "kwa nn ukimwi unaathiri sana wanawake":"elimu ndog0 na kipato kidogo kinachopelekea kujiingiza katika vitendo viovu",
    "namna ya kujikinga na ukimwi":"kupunguza vitendo viovu na kuchangia vitu vya ncha kali",             
    "ni watu wote wenye vvu wana ukimwi":"hapana",
    "eleza":"Mtu mwenye virusi si laziam awe na ugonjwa wa ukimwi. Watu wenye virusiwanaweza ishi maisha marefu sana kabla viruis vya ukimwi kuwamaliza mwili nguvu"
}  
@app.route("/",methods=["POST","GET"])
def ask(question):
    question=request.get_json()["question"].lower().replace("?","").strip()
    if(re.search("hi|hello|howdy",question)):
        return ("Hello how are you!")
    elif(re.search("ukimwi",question)and ("nn",question)):
        return qa["ukimwi ni nn"]
    elif(re.search("vvu",question)and ("nini",question)):
        return qa["vvu ni nini"]
    elif(re.search("dalili",question)):
        return qa["dalili ni zipi"]
    elif(re.search("utapataje",question)):
        return qa["utapataje ukimwi"]
    elif(re.search("hewa",question)):
        return qa["hapana"]
    elif(re.search("vp",question)and ("umeathirika",question)):
        return qa["utafahamu vp umeathirika"]
    else:
          print("sijaelewa swali")