# OpenAPI Implementation

## Goals

  - implement a REST API starting from OAS spec
  
---

# Implementing an API

In this practice we will implement a REST API starting from a template
 repository from github.
 
The steps will be:

  1a. setup a minimal QA framework for the project
  1b. write the OAS spec
  2a. identify the test surface and review the QA framework
  2b. implement the tests 
  3a. identify the deployment strategy and review the QA framework
  3b. implement the code
  
 ---
 
 # QA framework
 
 The minimal QA framework we'll setup consists in:
 
 - validating OAS using Spectral
 - checking YAML files using yamllint
 - readme, license file, template for issues, PR

----