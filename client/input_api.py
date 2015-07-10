#!/usr/bin/env python
"""
InputApi.py
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


class InputApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def jobs_job_id_input_get(self, **kwargs):
        """Get list of binary source files for the conversion.hhh
        Description of the get for the inputs of a specific job.

        Args:
            token, str: Token for authentication. (required)
            key, str: Api key for the user to filter. (required)
            job_id, str: ID of job that needs to be fetched (required)
            

        Returns: list[InputFile]
        """

        allParams = ['token', 'key', 'job_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_job_id_input_get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/jobs/{job_id}/input'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        

        
        if ('token' in params):
            headerParams['token'] = params['token']
        
        if ('key' in params):
            headerParams['key'] = params['key']
        

        
        if ('job_id' in params):
            replacement = str(self.apiClient.toPathValue(params['job_id']))
            resourcePath = resourcePath.replace('{' + 'job_id' + '}',
                                                replacement)
        

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'list[InputFile]')
        return responseObject
        
        
        
    
    def jobs_job_id_input_post(self, **kwargs):
        """Cretes a new input for the current job.
        

        Args:
            body, InputFile:  (required)
            token, str: Token for authentication. (required)
            key, str: Api key for the user to filter. (required)
            job_id, str: ID of job that needs to be fetched (required)
            

        Returns: InputFile
        """

        allParams = ['body', 'token', 'key', 'job_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_job_id_input_post" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/jobs/{job_id}/input'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        

        
        if ('token' in params):
            headerParams['token'] = params['token']
        
        if ('key' in params):
            headerParams['key'] = params['key']
        

        
        if ('job_id' in params):
            replacement = str(self.apiClient.toPathValue(params['job_id']))
            resourcePath = resourcePath.replace('{' + 'job_id' + '}',
                                                replacement)
        

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'InputFile')
        return responseObject
        
        
        
    
    def jobs_job_id_input_file_id_get(self, **kwargs):
        """Get list of conversions defined for the current job.
        

        Args:
            token, str: Token for authentication. (required)
            key, str: Api key for the user to filter. (required)
            job_id, str: ID of job that needs to be fetched (required)
            file_id, str: Id of the file to download (required)
            

        Returns: InputFile
        """

        allParams = ['token', 'key', 'job_id', 'file_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_job_id_input_file_id_get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/jobs/{job_id}/input/{file_id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        

        
        if ('token' in params):
            headerParams['token'] = params['token']
        
        if ('key' in params):
            headerParams['key'] = params['key']
        

        
        if ('job_id' in params):
            replacement = str(self.apiClient.toPathValue(params['job_id']))
            resourcePath = resourcePath.replace('{' + 'job_id' + '}',
                                                replacement)
        
        if ('file_id' in params):
            replacement = str(self.apiClient.toPathValue(params['file_id']))
            resourcePath = resourcePath.replace('{' + 'file_id' + '}',
                                                replacement)
        

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'InputFile')
        return responseObject
        
        
        
    
    def jobs_job_id_input_file_id_delete(self, **kwargs):
        """Removes the input for a job.
        

        Args:
            token, str: Token for authentication. (required)
            key, str: Api key for the user to filter. (required)
            job_id, str: ID of job that needs to be fetched (required)
            file_id, str: Id of the file to download (required)
            

        Returns: InputFile
        """

        allParams = ['token', 'key', 'job_id', 'file_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_job_id_input_file_id_delete" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/jobs/{job_id}/input/{file_id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}

        

        
        if ('token' in params):
            headerParams['token'] = params['token']
        
        if ('key' in params):
            headerParams['key'] = params['key']
        

        
        if ('job_id' in params):
            replacement = str(self.apiClient.toPathValue(params['job_id']))
            resourcePath = resourcePath.replace('{' + 'job_id' + '}',
                                                replacement)
        
        if ('file_id' in params):
            replacement = str(self.apiClient.toPathValue(params['file_id']))
            resourcePath = resourcePath.replace('{' + 'file_id' + '}',
                                                replacement)
        

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'InputFile')
        return responseObject
        
        
        
    


