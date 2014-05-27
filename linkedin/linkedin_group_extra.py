# -*- coding: utf-8 -*-
from linkedin import LinkedInApplication, LinkedInSelector, ENDPOINTS
from utils import *

GROUP_SELECTORS = ("id,category,creation-timestamp,title,summary,"
"creator:(first-name,last-name,picture-url,headline),"
"likes,attachment:(image-url,content-domain,content-url,title,summary),"
"relation-to-viewer")

class LinkedInGroupExtra(LinkedInApplication):
    def get_posts(self, group_id, post_ids=None, selectors=None, params=None,
                  headers=None):
        url = '%s/%s/posts' % (ENDPOINTS.GROUPS, str(group_id))
        if post_ids:
             url = '%s::(%s)' % (url, ','.join(map(str, post_ids)))
        if selectors:
            url = '%s:(%s)' % (url, LinkedInSelector.parse(selectors))
        print url
        response = self.make_request('GET', url, params=params, headers=headers)
        raise_for_error(response)
        return response.json()

    def decompose_post(self, group_id, post_id, params=None, headers=None):
        data = self.get_posts(group_id, {post_id}, GROUP_SELECTORS, params, headers)
        print data
        title = data['values'][0]['title']
        # print title
        return title

