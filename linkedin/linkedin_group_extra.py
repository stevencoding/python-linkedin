# -*- coding: utf-8 -*-
from linkedin import *
from utils import *

ENDPOINTS_GROUPS = 'https://api.linkedin.com/v1/groups'
GROUP_POST_REQUEST_DETAILED = "posts:(creation-timestamp,title,summary,creator:(first-name,last-name,picture-url,headline),likes,attachment:(image-url,content-domain,content-url,title,summary),relation-to-viewer)"

class LinkedInGroupExtra(LinkedInApplication):
    def get_posts(self, group_id, post_ids=None, selectors=None, params=None,
                  headers=None):
        url = '%s/%s/posts' % (ENDPOINTS_GROUPS, str(group_id))
        if post_ids:
            url = '%s::(%s)' % (url, ','.join(map(str, post_ids)))
        if selectors:
            url = '%s:(%s)' % (url, LinkedInSelector.parse(selectors))
        response = self.make_request('GET', url, params=params, headers=headers)
        raise_for_error(response)
        return response.json()

    def decompose_post(self, group_id, post_id, selectors=None, params=None,
                  headers=None):
        data = self.get_posts(group_id, {post_id}, selectors, params, headers)
        print data
        title = data['values'][0]['title']
        # print title
        return title

