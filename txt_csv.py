
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 02:04:46 2018

@author: sumit
"""
import re

f_txt=open("WhatsApp Chat with sumit bhaiya (V).txt","r")
f_csv=open("chat_ansh.tsv","w")
f_trash=open("trash_txt.txt","w")
#print(f_txt_read.readline())

for line in f_txt:
    line=line.replace(' - ','\t',1)
    
    pos=line.find(':')
    new_line=line[:pos+1]
    new_line=new_line.replace(', ','\t',1)
    line=line[pos+1:]
    n_pos=line.find(':')
    
    tab_line=line[n_pos:]
    tab_line2=line[:n_pos]
    tab_line=tab_line.replace('\t',' ')
    
    tab_line=tab_line.replace(':','\t',1)
    tab_line=re.sub('[^a-zA-Z\t\n0-9]',' ',tab_line)
    
    tab_line=" ".join(tab_line.split())
    tab_line='\t'+tab_line+'\n'
    
            
    
    line=tab_line2+tab_line
    
    #line=line.replace(': ','\t',1)
    line=new_line+line
    
    lenght=len(tab_line)
    
    if (line.find('Media omitted')!=-1):
        line=""
        
    
    if lenght<100 and lenght>2 and line.count('\t')==3 and line.count(' am\t')+line.count(' pm\t')==1:
        if line.find("media")==-1:
            f_csv.write(line.lower())
            
            #print("true >> "+line)
        else:
            print(line)
    else:
        f_trash.write(line)
            
        #print("else >>"+line)
        
        
print("done!")
    
f_txt.close()
f_csv.close()
f_trash.close()
