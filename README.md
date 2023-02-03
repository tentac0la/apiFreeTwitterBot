# apiFreeTwitterBot
Using Selenium, allows for automated tweeting without the usage of Twitter's API.

## Tweet List
Tweet content is currently randomly selected from the list in line 13 (tweetList). This is sufficient as a proof of concept.
In the future, this can and should be amended to a dict of scheduled posts possibly linked to date tp avoid chances for repetition.

## Security
Right now, this CAN accept hard-coded usernames and passwords (added as strings in respective "goes here" positions listed below), but it is recommended that the end user establish local variables for username and password.
Once established, the script should call these variables instead of the respective 'username_goes_here_but_local_var_recommended' and 'password_goes_here_but_local_var_recommended' strings.

## Troubleshooting
If this fails, there may be an issue related to your connection speed and the time.delay() functions. For now, please feel free to update these to accommodate your connection speed and any delays between bot actions.

## Future Improvements
- This should run in the background without disturbing the end user. 
- This should be easier to run on a scheduler. 
- This should allow for full containerization
- This should be tested on ECS, an always-on raspberry pi, or similar
- This should allow for media attachment. Currently text-only.

# Windows Setup

-Install Python (3.7 is ideal but should function through 3.9), ideally run out of command prompt, hyper, or similar.
-Install pip3
-Use pip3 to install the requirements through the following command from the top level of this repo:
`pip3 install -r requirements.txt`
-Establish local variables of your bot's twitter username and password with the variable names twuser and twpass respectively:
https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html
-Change the two arguments .bat file to the full path of your python executable (python.exe) and the full path of this repo's .py script (apiFreeTwitterBot.py).
Example:
`"C:\Users\owner\AppData\Local\Microsoft\WindowsApps\python.exe" "C:\Users\owner\Desktop\repos\apiFreeTwitterBot\apiFreeTwitterBot.py"
EXIT /B`
-Schedule the run of the .bat file per instructions here:
https://active-directory-wp.com/docs/Usage/How_to_add_a_cron_job_on_Windows/Scheduled_tasks_and_cron_jobs_on_Windows/index.html
