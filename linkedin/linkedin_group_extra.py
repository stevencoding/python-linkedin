# -*- coding: utf-8 -*-
from linkedin import LinkedInApplication, LinkedInSelector, ENDPOINTS
from utils import *

GROUP_SELECTORS = ("id,category,creation-timestamp,title,summary,"
"creator:(id),"
"likes,attachment:(content-url,title,summary)")

class LinkedInGroupExtra(LinkedInApplication):
    def get_posts(self, group_id, post_ids=None, selectors=None, params=None,
                  headers=None):
        url = '%s/%s/posts' % (ENDPOINTS.GROUPS, str(group_id))
        if post_ids:
             url = '%s::(%s)' % (url, ','.join(map(str, post_ids)))
        if selectors:
            url = '%s:(%s)' % (url, LinkedInSelector.parse(selectors))
        # print url
        response = self.make_request('GET', url, params=params, headers=headers)
        raise_for_error(response)
        return response.json()

    def decompose_post(self, group_id, post_id, params=None, headers=None):
        data = self.get_posts(group_id, {post_id}, GROUP_SELECTORS, params, headers)
        # print data
        post_abs_id = data['values'][0]['id']
        # print "post_abs_id = "+post_abs_id
        creator_id = data['values'][0]['creator']['id']
        # print "creator_id = "+creator_id
        title = data['values'][0]['title']
        category = data['values'][0]['category']['code']
        summary = data['values'][0]['summary']
        attachment_title = data['values'][0]['attachment']['title']
        attachment_summary = data['values'][0]['attachment']['summary']
        # print "title is: "+title
        # print "category is: "+category
        # print "summary is: "+summary
        # print "attachment_title is: "+attachment_title
        # print "attachment_summary is: "+attachment_summary
        return post_abs_id, creator_id, title, category, summary, attachment_title, attachment_summary

