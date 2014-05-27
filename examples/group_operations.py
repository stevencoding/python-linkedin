from linkedin import linkedin, linkedin_group_extra
import urllib

#########################
#Import secrets
from secrets import secret

#######################
#Load auth keys
CONSUMER_KEY = secret['API_KEY']
CONSUMER_SECRET = secret['Secret_Key']
USER_TOKEN = secret['OAUT']
USER_SECRET = secret['OAUS']
RETURN_URL = 'http://localhost:8000'
GROUP_ID = secret['Group_ID']

authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, 													 CONSUMER_SECRET,
                                                      USER_TOKEN, USER_SECRET,
                                                      RETURN_URL, linkedin.PERMISSIONS.enums.values())
# Pass it in to the app...
application = linkedin_group_extra.LinkedInGroupExtra(authentication)

# Use the app....
# app_data=application.get_profile(selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations','interests','honors-awards','num-recommenders'])
# print app_data

# Use the app to get group info
# group_info = application.get_group(GROUP_ID)
# print group_info
#
group_posts = application.get_posts(GROUP_ID, post_ids={0,1})
print group_posts

# group_post = application.decompose_post(GROUP_ID, 1)
# print group_post