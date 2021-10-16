# MS-teams-meetings-launcher

## Requirements
- [chrome_driver](https://chromedriver.chromium.org/downloads) its version should match with your chrome version 
see your chrome_version be entering [chrome://version/] at chrome search tab

- run the following code in your terminal (pip install -r req.txt)

## Configuration 
- open courses.py and add your courses
 ```python 
# ToDo:
# 	  add your courses 
courses = [['CSE448 (UG2013) - Embedded Operating Systems  (20847)', 17, 30, ['3'], 19,30], # team 1
           ['Team2', 14, 50, ['0', '2', '5'], 16] # team 2
		   ]
```
- open Microsoft-teams.py and write your credentials
 ```python
#write your credentials below
student_email=os.environ.get("ASU_email")
student_password=os.environ.get("password")
```
# Run
- through your terminal :
```
python Microsoft-teams.py
```
- or  double click on that file
# TIP
 you can save  in Microsoft-teams.py .pyw extension and move it to the startup folder and **update relative paths**
 
1. to open startup press windows key + R  , RUN box will pop up
 
2. enter "shell:startup" then press ok
 
3. place Microsoft-teams.pyw on the startup folder 
 

