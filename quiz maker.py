#!/usr/bin/env python
# coding: utf-8

# In[2]:


from q import question
q_list=['what is the symbole of python?\n a.rat\n b.snake\n c.whale\n\n',
        'what is the fastest animal in the world?\n a.cheetha\n b.rabbit\n c.leapord\n\n',
        'what is the fastest car in the world?\n a.buggati chiron \n b.agera\n c.lamborgini\n\n',
        'what will be the colur of the indian national flag?\n a.saffron,white,green\n b.blue,safron,green\n c.saffron,blue,green\n\n',
        'how many datatypes are there in python>\n a.6\n b.3\n c.10\n\n',
        'what is the latest version of python relesed?\n a.3\n b.3.1\n c.3.10\n\n',
        'what is the current usages of python?\n a.web development,ML,AI\n b.game creation,database creation,user interface\n\n',
        'which datatype returns the duplicate values?\n a.dict\n b.set\n c.list',
        'which datatype does not executes the duplicate values?\n a.string\n b.set\n c.tuple',
        'what is the use of ^ in regex of python?\n a.to start the datatype compulsary\n b.we can either start the datatype or continue with the next type\n c.to end the datatype compulsary\n\n']

questions=[question(q_list[0],'b'),question(q_list[1],'a'),question(q_list[2],'b'),question(q_list[3],'b'),question(q_list[4],'a')
          ,question(q_list[5],'a'),question(q_list[6],'c'),question(q_list[7],'c'),question(q_list[8],'b'),question(q_list[9],'a')]

def run_test(questions):
    score=0
    for question in questions:
        ans=input(question.qus)
        if ans==question.ans:
            score+=1
    print('You got',str(score),'/',str(len(questions)),'correct')
    
run_test(questions)


# In[ ]:




