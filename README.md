AWS TAGGER
================

This is a simple python script to create aws-tag for any resource in a particular AWS region.
Configuration file and Information file are the two file where user have to define the aws details.
In configuration file we need to mention region,access-key,secret-key and information file. 
In information file, we have to define the resource and tagging details.

Dependecy : boto, python2.7

Config File
-------------

It contains information for aws and file name.
 
>Each line should have one value, 
>>1. Region should be specified with variable 'region', double colon ':', region value.
>>2. Access key should be specified with variable 'ak', double colon ":" , accesskey value.
>>3.Secret key should be specified with variable 'sk', double colon ":" , secretkey value.
>>4. Filename should be specified with variable 'filename', double colon ":" , filename  value.  

**Please refer the sample config file given in repository

Information file
----------------

Values should be stored in a manner that scripts should understand.
Line starting with '#' symbol are treated as comment.
>Values should be given in below format:
>>1. res-id,tag-key:tag-value,tag1-key:tag1-value,tag2-key:tag2-value,... ,tag10-key:tag10-value
>>2. Resource-id should be given first then tag values related to the resource id, all are seperated by comma.
>>3. Every tagkey and tag value should be seperated by colon
>>4. Each tag-key-value pair are seperated by comma.

***eNoy tagging
