# Test Driven Development 101



---


## Goal

  - Design an API with testing in mind
  
---

# REST and RPC

The historical API approach was to view any interaction like a function call.

In a network environment this is seen as a `Remote Procedure Call`.
SOAP web services have this approach, where you bind:

 * a service to an URL 
 * and different functions to invocation methods.

----

Even today there are a lot of non-SOAP APIs using an RPC approach, 
including Slack APIs and Google RPC.

The widespread of HTTP as a distributed computation protocol,
 and the rise of data give birth to REST.

----

REST, aka REpresentation State Transfer, is not a protocol,
 but an architectural style which mimics the distributed characteristics of the web.

In REST, everything is a `resource`:

- identified by an Uniform Resource Locator URL;
- which is conveyed by a `representation`. A given resource 
could be represented as `application/json` or 
as [`application/xml`](https://tools.ietf.org/html/rfc7303), 
in different languages (see `Content-Language`)
 and differently encoded (see `Content-Encoding`);
- whom state is transferred between an Origin Server
 and a User Agent (see RFC7230);

---- 

There are no "functions" but everything is modeled as a resource. 
Moreover all the HTTP semantics (RFC7231) applies, including idempotent 
and non-idempotent methods and caching.

The REST architectural style allows us to 
**leverage the distributed nature of the web** and
 the features of HTTP which are redesigned with REST in mind 
 (see RFC723x and the new http-core Internet-Drafts).

While REST is not a silver bullet, we 
**acknowledged that public services are usually about data and resources**
 making a REST style a good approach in service modeling. 

Moreover a semantic approach to URIs simplifies routing and auditing
 based on http status, method and path.

---

# Describing APIs

Providing **usable** digital services requires:

- publishing interfaces;
- involve stakeholders/users in the service lifecycle.

You must **COMMUNICATE**:

- technical specifications;
- service metadata;
- documents and references.

---

## Interface Description Language

Digital service description requires an Interface Description Language. 
That's a **machine readable
language** that can be used to describe the interface. 
The most famous IDL is WSDL used by SOAP web services. 

**For REST APIs the standard IDL is OpenAPI v3 aka OAS3**.

For example, a web service accepting the following request `GET /echo` and
 returning a json object could be described in OAS3 like the following:

```yaml
...
paths:
  /echo:
    get:
      responses:
        "200":
          application/json: {}
...
```

This allows to disambiguate the API definitions and usage.

---

## Contract first, Code first

There are two paths for API writing:

- code first: where one develops a function on a specific language 
  and then uses some tool to generate the
  IDL. An example function generating the above IDL could be
  
  ```
  def echo():
      item = {"hello": "world"}
      status_code = 200
      headers = {'content-type': 'application/json'}
      
      return item, status_code, headers
  ```
  
- contract first: one writes down the interface in an IDL,
 then let the tools generate the code stubs.

---

## Contract first improves standardization

While lazy developers prefers to use code-first, 
as they could focus on writing the actual code and leave 
the interface as an underproduct, 
this approach rarely works in a large ecosystem where

  * different actors 
  * in a long timeframe 
  * works with different frameworks and enviroments.

----

A contract-first approach has many advantages:

- allows to focus on the actual design of the API, without 
  being entangled by implementation details;
- it's independent from which framework or language people uses
  for its client/server implementation and from how frameworks generate the
  specs (which may be buggy);

Focusing on the specs allows to create *API modeling iterations* that enable
the API to change fast and involve stakeholders in the modeling and in the 
API lifecycle.

NB: this doesn't mean iterations don't involve testing that the actual code works ;)
