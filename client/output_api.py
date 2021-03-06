#!/usr/bin/env python
"""
OutputApi.py
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


class OutputApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def jobs_job_id_output_get(self, **kwargs):
        """Get list of converted.
        

        Args:
            conversion_id, str:  (required)
            input_id, str:  (required)
            x_oc_token, str: Token for authentication for the current job (required)
            x_oc_api_key, str: Api key for the user to filter. (required)
            job_id, str: ID of job that needs to be fetched (required)
            

        Returns: list[OutputFile]
        """

        allParams = ['conversion_id', 'input_id', 'x_oc_token', 'x_oc_api_key', 'job_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_job_id_output_get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/jobs/{job_id}/output'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('conversion_id' in params):
            queryParams['conversion_id'] = self.apiClient.toPathValue(params['conversion_id'])
        
        if ('input_id' in params):
            queryParams['input_id'] = self.apiClient.toPathValue(params['input_id'])
        

        
        if ('x_oc_token' in params):
            headerParams['x_oc_token'] = params['x_oc_token']
        
        if ('x_oc_api_key' in params):
            headerParams['x_oc_api_key'] = params['x_oc_api_key']
        

        
        if ('job_id' in params):
            replacement = str(self.apiClient.toPathValue(params['job_id']))
            resourcePath = resourcePath.replace('{' + 'job_id' + '}',
                                                replacement)
        

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'list[OutputFile]')
        return responseObject
        
        
        
    
    def jobs_job_id_output_file_id_get(self, **kwargs):
        """Get information about an output file source.
        

        Args:
            x_oc_token, str: Token for authentication for the current job (required)
            x_oc_api_key, str: Api key for the user to filter. (required)
            job_id, str: ID of job that needs to be fetched (required)
            file_id, str: Id of the file to download (required)
            

        Returns: list[OutputFile]
        """

        allParams = ['x_oc_token', 'x_oc_api_key', 'job_id', 'file_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_job_id_output_file_id_get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/jobs/{job_id}/output/{file_id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        

        
        if ('x_oc_token' in params):
            headerParams['x_oc_token'] = params['x_oc_token']
        
        if ('x_oc_api_key' in params):
            headerParams['x_oc_api_key'] = params['x_oc_api_key']
        

        
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

        responseObject = self.apiClient.deserialize(response, 'list[OutputFile]')
        return responseObject
        
        
        
    
    def jobs_job_id_output_file_id_delete(self, **kwargs):
        """Deletes a file from the output.
        

        Args:
            x_oc_token, str: Token for authentication for the current job (required)
            x_oc_api_key, str: Api key for the user to filter. (required)
            job_id, str: ID of job that needs to be fetched (required)
            file_id, str: Id of the file to download (required)
            

        Returns: list[OutputFile]
        """

        allParams = ['x_oc_token', 'x_oc_api_key', 'job_id', 'file_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_job_id_output_file_id_delete" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/jobs/{job_id}/output/{file_id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}

        

        
        if ('x_oc_token' in params):
            headerParams['x_oc_token'] = params['x_oc_token']
        
        if ('x_oc_api_key' in params):
            headerParams['x_oc_api_key'] = params['x_oc_api_key']
        

        
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

        responseObject = self.apiClient.deserialize(response, 'list[OutputFile]')
        return responseObject
        
        
        
    


