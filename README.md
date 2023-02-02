# apiFreeTwitterBot
Using Selenium, allows for automated tweeting without the usage of Twitter's API.

# Tweet List
Tweet content is currently randomly selected from the list in line 13 (tweetList). This is sufficient as a proof of concept.
In the future, this can and should be amended to a dict of scheduled posts possibly linked to date tp avoid chances for repetition.


# Security
Right now, this CAN accept hard-coded usernames and passwords, but it is recommended that the end user establish local variables for username and password.
Once established, the script should call these variables instead of the respective 'username_goes_here_but_local_var_recommended' and 'password_goes_here_but_local_var_recommended' strings.

# Troubleshooting
If this fails, there may be an issue related to your connection speed and the time.delay() functions. For now, please feel free to update these to accommodate your connection speed and any delays between bot actions.

# Future Improvements
- This should run in the background without disturbing the end user. 
- This should be easier to run on a scheduler. 
- This should allow for full containerization
- This should be tested on ECS, an always-on raspberry pi, or similar
