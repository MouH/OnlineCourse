# -*- coding: utf-8 -*-  
#!/usr/bin/env python  
import glob  
import mincemeat  
import operator  
  
text_files=glob.glob('hw3data/*')  
  
def file_contents(file_name):  
    f=open(file_name)  
    try:  
        return f.read()  
    finally:  
        f.close()  
  
source=dict((file_name,file_contents(file_name))  
            for file_name in text_files)  
  
# setup map and reduce functions  
  
def mapfn(key, value):  
    stop_words=['all', 'herself', 'should', 'to', 'only', 'under', 'do', 'weve',  
            'very', 'cannot', 'werent', 'yourselves', 'him', 'did', 'these',  
            'she', 'havent', 'where', 'whens', 'up', 'are', 'further', 'what',  
            'heres', 'above', 'between', 'youll', 'we', 'here', 'hers', 'both',  
            'my', 'ill', 'against', 'arent', 'thats', 'from', 'would', 'been',  
            'whos', 'whom', 'themselves', 'until', 'more', 'an', 'those', 'me',  
            'myself', 'theyve', 'this', 'while', 'theirs', 'didnt', 'theres',  
            'ive', 'is', 'it', 'cant', 'itself', 'im', 'in', 'id', 'if', 'same',  
            'how', 'shouldnt', 'after', 'such', 'wheres', 'hows', 'off', 'i',  
            'youre', 'well', 'so', 'the', 'yours', 'being', 'over', 'isnt',  
            'through', 'during', 'hell', 'its', 'before', 'wed', 'had', 'lets',  
            'has', 'ought', 'then', 'them', 'they', 'not', 'nor', 'wont',  
            'theyre', 'each', 'shed', 'because', 'doing', 'some', 'shes',  
            'our', 'ourselves', 'out', 'for', 'does', 'be', 'by', 'on',  
            'about', 'wouldnt', 'of', 'could', 'youve', 'or', 'own', 'whats',  
            'dont', 'into', 'youd', 'yourself', 'down', 'doesnt', 'theyd',  
            'couldnt', 'your', 'her', 'hes', 'there', 'hed', 'their', 'too',  
            'was', 'himself', 'that', 'but', 'hadnt', 'shant', 'with', 'than',  
            'he', 'whys', 'below', 'were', 'and', 'his', 'wasnt', 'am', 'few',  
            'mustnt', 'as', 'shell', 'at', 'have', 'any', 'again', 'hasnt',  
            'theyll', 'no', 'when','other', 'which', 'you', 'who', 'most',  
            'ours ', 'why', 'having', 'once','a','-','.',',']  
    for line in value.splitlines():  
        word=line.split(':::')  
        authors=word[1].split('::')  
        title=word[2]  
        for author in authors:  
            for term in title.split():  
                if term not in stop_words:  
                    if term.isalnum():  
                        yield author,term.lower()  
                    elif len(term)>1:  
                        temp=''  
                        for ichar in term:  
                            if ichar.isalpha() or ichar.isdigit():  
                                temp+=ichar  
                            elif ichar=='-':  
                                temp+=' '  
                        yield author,temp.lower()  
  
def reducefn(key, value):  
    terms = value  
    result={}  
    for term in terms:  
        if term in result:  
            result[term]+=1  
        else:  
            result[term]=1  
    return result  
  
# start the server  
  
s = mincemeat.Server()  
s.datasource = source  
s.mapfn = mapfn  
s.reducefn = reducefn  
  
results = s.run_server(password="changeme")  
#print results  
  
result_file=open('hw3_result.txt','w')  
sorted(results.iteritems(), key=operator.itemgetter(1))  
for result in results:  
    result_file.write(result+' : ')  
    for term in results[result]:  
        result_file.write(term+':'+str(results[result][term])+'#')  
    result_file.write('\r\n')  
result_file.close() 