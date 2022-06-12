# **companyrepo**
ziyan company repo

## **Intro**

The solution includes API gateway, lambda function and Github webhook to enforce branch protection and request all code commit only happens after a successful code review through pull request.

## **How to setup**

### Lambda
1. Create AWS lambda function based on Python 3.8 runtime;
2. Import PyGithub module by following AWS tutorial;
3. Use lambda_funcion.py code provided in the "companyrepo" repo;


### API gateway
4. Create AWS gateway and select HTTP API;
5. Add the above lambda function as integration service;
6. Allow any method for future expansion (POST, PUT, GET, etc.), and use $default value as resource path;


### Github
7. Create an organization level webhook and select API gateway invoke url as payload url;
8. Select content type application/json;
9. Customize events and check Repositories;

## **Test**

By default, repository is created with our branch protection rule. However, with the Repositories webhook, anytime when a new repository is created or existing repository is modified, our API gateway will catch it and further invoke lambda function to apply branch protection to all repositories within the organization.

You can try to edit an existing repository branch protection rules first, and then create a new repository under the organization. Then when you come back to the existing repository and also check the newly created repository the branch protection rule should have been applied.

