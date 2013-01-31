AWS TAGGER
================

This is a simple python script to create and remove aws-tag for any resource in a particular AWS region.
Configuration file and Information file are the two file where user have to define the aws details.
In configuration file we need to mention region,access-key,secret-key,operation (add or remove the give tags) and information file. 
In information file, we have to define the resource and tagging details.

Dependecy : boto, python2.7

Config File
-------------

It contains information for aws and file name. Operation is a keyword where we have to mention, whether you need to remove or add the tags to resource
 
>Each line should have one value, 
>>1. Region should be specified with variable 'region', single colon ':', region value.
>>2. Access key should be specified with variable 'ak', single colon ":" , accesskey value.
>>3. Secret key should be specified with variable 'sk', single colon ":" , secretkey value.
>>4. Filename should be specified with variable 'filename', single colon ":" , filename  value.  
>>5. Operation should be specified with variable 'operation', single colon ":", add or remove, here we have to mention whether we need to add or remove the tags in aws.

#Please refer the sample config file given in repository

Information file
----------------

Values should be stored in a manner that scripts should understand.
Line starting with '#' symbol are treated as comment.
>Values should be given in below format:
>>1. res-id,tag-key:tag-value,tag1-key:tag1-value,tag2-key:tag2-value,... ,tag10-key:tag10-value
>>2. Resource-id should be given first then tag values related to the resource id, all are seperated by comma.
>>3. Every tagkey and tag value should be seperated by colon
>>4. Each tag-key-value pair are seperated by comma.

How to run the script
=====================

#eNoy tagging
