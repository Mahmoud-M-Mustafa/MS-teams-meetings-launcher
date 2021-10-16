#
# Microsoft teams  Scheduled meetings Launcher
# By Mahmoud Mustafa  @2021
#
# you can save this file in .pyw extension and move it to the startup folder and update relative paths
import os
import time,datetime 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.command import Command

#write your credentials below
student_email=os.environ.get("ASU_email")
student_password=os.environ.get("password")



# ---- some helper functions-------------
def time_diff(start_h,end_h,start_m,end_m):

	start = datetime.time(hour=start_h, minute=start_m)
	end = datetime.time(hour=end_h, minute=end_m)
	duration = datetime.timedelta(hours=end.hour-start.hour, minutes=end.minute-start.minute)
	diff= str(duration).split(":")
	try:
		seconds=int(diff[0])*60*60+int(diff[1])*60+int(diff[2])
	except:
		return 0
	return seconds 


def browser_init():
	opt = Options()
	opt.add_argument("--disable-infobars")
	opt.add_argument("start-maximized")
	opt.add_argument("--disable-extensions")
	# Pass the argument 1 to allow and 2 to block
	opt.add_experimental_option("prefs", { \
	    "profile.default_content_setting_values.media_stream_mic": 2, 
	    "profile.default_content_setting_values.media_stream_camera": 2,
	    "profile.default_content_setting_values.geolocation": 2, 
	    "profile.default_content_setting_values.notifications": 2 
	  })
	browser = webdriver.Chrome(options=opt, executable_path="chromedriver.exe")
	return browser


def get_status(driver):
    try:
        driver.execute(Command.STATUS)
        return "Alive"
    except :
        return "Dead"


def MS_meetings(meeting_name,browser):

	try:
		browser.get("https://teams.microsoft.com")
	except:
		print("Reconnect to the Internaet and try again")
		return
	time.sleep(5)
	# username ---------------
	username=browser.find_element_by_name("loginfmt")
	username.send_keys(student_email)
	
	_next= browser.find_element_by_id("idSIButton9")
	
	_next.click()
	
	# password ------------------
	time.sleep(3)
	password=browser.find_element_by_name("passwd")
	password.send_keys(student_password)	
	sign_in=browser.find_element_by_id("idSIButton9")
	sign_in.click()

	time.sleep(3)

	# proceed -------------
	submit=browser.find_element_by_id("idSIButton9")
	submit.click()
	
	# wait for teams to set up
	time.sleep(35)

	#click on passed meeting name
	course=browser.find_element_by_xpath(f"//profile-picture[@title='{meeting_name}']")
	course.click()

	# wait to load join button
	time.sleep(30)

	# click on join meeting
	try:
		join_meeting= browser.find_element_by_xpath("//button[@title='Join call with video']")	
		join_meeting.click()
		time.sleep(4)
		browser.find_element_by_xpath("//button[@class='ts-btn ts-btn-fluent ts-btn-fluent-secondary-alternate']").click()
		time.sleep(4)
		browser.find_element_by_xpath("//button[@class='join-btn ts-btn inset-border ts-btn-primary']").click()
		time.sleep(20)
	except:
		print("There is no meeting at the current time: ",datetime.datetime.now())
		browser.quit()

	


############################################################################
############################################################################

if __name__ == "__main__":
	from courses import *

	MScourses=[course(*i) for i in courses]
	MScourses.sort(key=lambda x: x.start_hour) # sort based on start hour

	tm=time.localtime(time.time())
	Today=str(tm)[str(tm).find('wday')+5]

	for course in MScourses:

		if (Today in course.days ):
			# sleep until next meeting 
			time_now = datetime.datetime.now()
			if(time_now.hour <= course.start_hour ):

				sleep_time = time_diff(time_now.hour, course.start_hour,
                                    time_now.minute, course.start_minute)
				
				print(" about to sleep : ",sleep_time/60,"mins")
				time.sleep(sleep_time)

			# drop passed meeting 
			if(time_diff(course.end_hour, time_now.hour,
                             course.end_minute,time_now.minute) > 0):
				print(f"You  missed {course.name} Today :(")
				continue				
			browser = browser_init()
			MS_meetings(course.name,browser)

			counter=0
			# try 5 times if the meeting has not started yet 
			while get_status(browser)=='Dead' and counter<5:
				counter+=1
				print("try again after 4 mins")
				time.sleep(4*60)
				browser = browser_init()
				MS_meetings(course.name,browser)

			if get_status(browser) != 'Dead':
				time.sleep(2*60*60) #  avg meeting duration 
				browser.quit()
	
		else:
			print(f"You have no {course.name} Today")
	

	

