#!/usr/bin/env python
"""
JobsApi.py
Copyright 2015 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os

from .models import *


class JobsApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def jobs_get(self, **kwargs):
        """List of jobs active for the current user identified by the key.
        It will return the list of jobs for the given user. In order to get the jobs a key or token must be provided:\n  - If the user key is provided all jobs for the current will be return.\n  - If one token is provided it will return the job assigned to that token if any.\n  \nThe request is paginated with an amount of 50 elements per page in any case.\n

        Args:
            status, str: Filter the status of the job. (required)
            token, str: Token for authentication. (required)
            key, str: Api key for the user to filter. (required)
            page, number: Pagination for list of elements. (required)
            

        Returns: list[Job]
        """

        allParams = ['status', 'token', 'key', 'page']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/jobs'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('status' in params):
            queryParams['status'] = self.apiClient.toPathValue(params['status'])
        
        if ('key' in params):
            queryParams['key'] = self.apiClient.toPathValue(params['key'])
        
        if ('page' in params):
            queryParams['page'] = self.apiClient.toPathValue(params['page'])
        

        
        if ('token' in params):
            headerParams['token'] = params['token']
        

        

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'list[Job]')
        return responseObject
        
        
        
    
    def jobs_post(self, **kwargs):
        """Creates a new Job with the user key.
        

        Args:
            key, str: Api key for the user to filter. (required)
            body, Job: Content of the job. (required)
            

        Returns: Job
        """

        allParams = ['key', 'body']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_post" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/jobs'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        
        if ('key' in params):
            queryParams['key'] = self.apiClient.toPathValue(params['key'])
        

        

        

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Job')
        return responseObject
        
        
        
    
    def jobs_job_id_get(self, **kwargs):
        """Get information about a Job
        

        Args:
            token, str: Token for authentication. (required)
            key, str: Api key for the user to filter. (required)
            job_id, str: ID of job that needs to be fetched (required)
            

        Returns: Job
        """

        allParams = ['token', 'key', 'job_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_job_id_get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/jobs/{job_id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('key' in params):
            queryParams['key'] = self.apiClient.toPathValue(params['key'])
        

        
        if ('token' in params):
            headerParams['token'] = params['token']
        

        
        if ('job_id' in params):
            replacement = str(self.apiClient.toPathValue(params['job_id']))
            resourcePath = resourcePath.replace('{' + 'job_id' + '}',
                                                replacement)
        

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Job')
        return responseObject
        
        
        
    
    def jobs_job_id_delete(self, **kwargs):
        """Cancels a job created that haven't been started. (Allow to cancel jobs in process.)
        

        Args:
            token, str: Token for authentication. (required)
            key, str: Api key for the user to filter. (required)
            job_id, str: ID of job that needs to be fetched (required)
            

        Returns: Job
        """

        allParams = ['token', 'key', 'job_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_job_id_delete" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/jobs/{job_id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}

        
        if ('key' in params):
            queryParams['key'] = self.apiClient.toPathValue(params['key'])
        

        
        if ('token' in params):
            headerParams['token'] = params['token']
        

        
        if ('job_id' in params):
            replacement = str(self.apiClient.toPathValue(params['job_id']))
            resourcePath = resourcePath.replace('{' + 'job_id' + '}',
                                                replacement)
        

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Job')
        return responseObject
        
        
        
    
    def jobs_job_id_patch(self, **kwargs):
        """Modifies the job identified by the id, allows to start a created job.
        

        Args:
            body, Job: Content of the job. (required)
            token, str: Token for authentication. (required)
            key, str: Api key for the user to filter. (required)
            job_id, str: ID of job that needs to be fetched (required)
            

        Returns: Job
        """

        allParams = ['body', 'token', 'key', 'job_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_job_id_patch" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/jobs/{job_id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PATCH'

        queryParams = {}
        headerParams = {}

        
        if ('key' in params):
            queryParams['key'] = self.apiClient.toPathValue(params['key'])
        

        
        if ('token' in params):
            headerParams['token'] = params['token']
        

        
        if ('job_id' in params):
            replacement = str(self.apiClient.toPathValue(params['job_id']))
            resourcePath = resourcePath.replace('{' + 'job_id' + '}',
                                                replacement)
        

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Job')
        return responseObject
        
        
        
    
    def jobs_job_id_threads_get(self, **kwargs):
        """Get list of threads defined for the current job.
        

        Args:
            token, str: Token for authentication. (required)
            key, str: Api key for the user to filter. (required)
            job_id, str: ID of job that needs to be fetched (required)
            

        Returns: list[Thread]
        """

        allParams = ['token', 'key', 'job_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_job_id_threads_get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/jobs/{job_id}/threads'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('key' in params):
            queryParams['key'] = self.apiClient.toPathValue(params['key'])
        

        
        if ('token' in params):
            headerParams['token'] = params['token']
        

        
        if ('job_id' in params):
            replacement = str(self.apiClient.toPathValue(params['job_id']))
            resourcePath = resourcePath.replace('{' + 'job_id' + '}',
                                                replacement)
        

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'list[Thread]')
        return responseObject
        
        
        
    

