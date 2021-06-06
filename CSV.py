import numpy as np
import pandas as pd
import lxml
csv_frame = pd.read_csv('Ch_05.csv')
csv_frame

table = pd.read_table('Sometext.txt',sep='\s+', engine = 'python')
table

new = pd.read_table('new.txt', sep='\D+', header = None, engine='python')
new

print(pd.read_csv('Ch_05.csv',
            skiprows=[0],
            nrows = 6,
            header = None))

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index = ['red', 'blue', 'yellow', 'white'],
                     columns = ['ball', 'pen', 'pencil', 'paper'])
frame.to_csv('Ch_05.csv')

new_frame = pd.read_csv('Ch_05.csv')
new_frame



frame3 = pd.DataFrame([[6,np.nan,np.nan,6,np.nan],
                       [np.nan,np.nan,np.nan,np.nan,np.nan],
                       [np.nan,np.nan,np.nan,np.nan,np.nan],
                       [20,np.nan,np.nan,20.0,np.nan],
                       [19,np.nan,np.nan,19.0,np.nan]],
index=['blue','green','red','white','yellow'],
columns=['ball','mug','paper','pen','pencil'])

frame3

frame_4 = frame3.dropna(how ='all', axis = [0])
frame_4
h_frame = pd.DataFrame(np.arange(4).reshape(2,2))
# print(h_frame.to_html())

n_frame = pd.DataFrame( np.arange(16).reshape((4,4)),
                       index = ['white','black','red','blue'],
                       columns = ['up','down','right','left'])
n_frame

s = ['<HTML>']
s.append('<HEAD><TITLE>My DataFrame</TITLE></HEAD>')
s.append('<BODY>')
s.append(n_frame.to_html())
s.append('</BODY></HTML>')
html =('').join(s)

html_file = open('myFrame.html','w')
html_file.write(html)
html_file.close()

