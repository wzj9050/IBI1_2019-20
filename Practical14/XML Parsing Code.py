
import xml.dom.minidom as xdm
import pandas as pd

#Define a function to count the number of childnotes
def count_childnodes(id_i):
    global terms
    count=0
    
    #Get list of is_a
    for term in terms:
        is_a=term.getElementsByTagName('is_a')
        
        for parent in is_a:
            
            #if is_a the parent node
            if parent.childNodes[0].data==id_i:
                count+=1
                
                #count children of the child
                nextno=term.getElementsByTagName('id')[0].childNodes[0].data
                count+=count_childnodes(nextno)

    return count

#create lists
id_list=[]
name_list=[]
defination_list=[]
childnodes_list=[]

#open xml file with minidom parser
domtree=xdm.parse('go_obo.xml')
ontology=domtree.documentElement

#get all terms
terms=ontology.getElementsByTagName('term')

#get all content in <defstr>
for term in terms:
    define=term.getElementsByTagName('def')[0]
    defstr=define.getElementsByTagName('defstr')[0].childNodes[0].data
    
    #if 'autophagosome' found
    if defstr.find('autophagosome')>-1 or defstr.find('Autophagosome')>-1:
        
        #get id, name and add them to lists with defstr
        id_a=term.getElementsByTagName('id')[0].childNodes[0].data
        id_list.append(id_a)
        name_list.append(term.getElementsByTagName('name')[0].childNodes[0].data)
        defination_list.append(defstr)
        
        #get the number of childnotes
        childnodes_list.append(count_childnodes(id_a))

#output into an excel file
data={
      'id':id_list,
      'name':name_list,
      'defination':defination_list,
      'childnodes':childnodes_list
}
dataframe=pd.DataFrame(data)
dataframe.to_excel('Practical14.xlsx')

print('Done!')















