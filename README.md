# Crowdfunding Back End
Shay Zimmerle

[View deployed site here](https://crowdfunding-scifi.fly.dev/projects/)

## Planning:
### Concept/Name
#### SciFi 
SciFi (Science Finance) is a crowdfunding platform for discovering, funding, and sharing scientific research.

### Intended Audience/User Stories
Scientists, research groups, citizen scientists, anyone who wants to be directly involved with funding research and making science more accessible.

### Front End Pages/Functionality
#### Home Page
* Nav bar with Discover, Start a Project, and Login links, as well as a search function.
* Hero image with buttons directed to Start a Project and Browse Projects/Discover
* Featured projects section

#### Discover Projects
* Project categories 
* Search function and filter
* List of projects with brief overview, image, $ goal, amount funded

#### Start a Project
* Form that will allow registered user to create a new project
* Project details: Title, Abstract, Method, Discussion/Results, Authors/Contributors/Affiliations, DOI links, Grants Recieved/Applied For, Images, Funding Goal

#### Project page
Public view:
* Abstract
* Methods
* Discussion/Results
* Authors/contributors
* DOI links
* Institutions
* Grants received/applied for
* Comments
* Likes/follow
* $ goal 
* Amount funded and days to go until funding deadline
* Date created
* Images/videos 

If logged in and project owner:
* Update/delete function

#### User Profile
* Bio
* Image
* Projects started
* Affiliations
* Pledges (projects pledged to)
* Comments
* Date joined
* Projects following
* Messages
* Update/delete functionality

#### Pledges
* Form that will allow a logged in user to donate desired amount to chosen project
* Comment option
* Option to stay anonymous

### Instructions for User and Project Creation in Insomnia
#### How to Register a New User
1) Select a new HTTP Request 
2) Select POST method using the URL path: https://crowdfunding-scifi.fly.dev/users/
3) Select JSON as the text option
4) Enter the following JSON attributes:
```
    {
		"username": "<username>",
		"password": "<password>",
		"first_name": "<first name>",
		"last_name": "<last name>",
		"email": "<email address>"
    }
```
5) Click Send

###### Example New User
![Screenshot of Insomnia with POST method for creating a new user](./images/:users:%20POST.png)

#### How to Recieve Authentication Token
1) Select a new HTTP Request
2) Choose POST method using the following URL path: https://crowdfunding-scifi.fly.dev/api-token-auth/
3) Choose JSON as the text option
4)  Enter the following JSON attributes:
```
    {
		"username": "<username>",
		"password" : "<password>"
	}
```
5)  Click Send

##### Example Auth Token:
![Screenshot of Insomnia with POST method for creating a token](./images/:api-token-auth:%20POST.png)

#### How to Create a New Project
1) Users need to be logged in to create a new project
2) Choose POST method using the following URL path: https://crowdfunding-scifi.fly.dev/projects/
3) Choose JSON as the text option
4) Enter the following JSON attributes:
```
{
	"owner": "<id of owner>",
	"title": "<title>",
	"description": "<description>",
	"goal": <goal dollar amount>,
	"image": "<url of image>",
	"is_open": "<false or true>",
	"date_created": "<date>"
    "category": "<category>"
}
```
1) Open the "Auth" tab and choose "Bearer Token"
2) Enter the token number of the user creating the project
3) Under "Prefix" type "Token"
4) Click Send

##### Example New Project
![Screenshot of Insomnia with POST method for creating a token](./images/:projects:%20POST.png)

### API Spec

|  URL | HTTP Method | Purpose | Request Body | Success Response Code |Authentication/Authorization |
| ---  | ----------- | ------- | ------------ | --------------------- |----------------------------|
|/projects/|POST|Creates a project|Project object|201|Must be logged in|
|/projects/|GET|List of project objects|N/A|200|None required|
|/projects/<int:pk>/|GET|Returns a project|N/A|200|None required|
|/projects/<int:pk>/|PUT|Updates project|Project object|200|Project owner and logged in|
|/projects/?limit=3|GET|Returns number of projects specified by limit query parameter|N/A|200|None required|
|/projects/?is_open=True|GET|Returns projects with the given status for is_open as provided by is_open query parameter|N/A|200|None required|
|/projects/?order_by=date_created|GET|Returns the projects in order of date created|N/A|200|None required|
|/projects/?order_by=num_pledges|GET|Returns projects in order of number of pledges|N/A|200|None required|
|/projects/?order_by=recent_pledges|GET|Returns projects in order of most recently pledged to|N/A|200|None required|
|/pledges/|GET|Returns list of pledges|N/A|200|None required|
|/pledges/|POST|Creates new pledge|Pledge object|201|Must be logged in|
|/pledges/?order_by=date_created|GET|Returns list of pledges in order of date created|N/A|200|None required|
|/users/|POST|Creates new user|User object|201|None required|
|/api-token-auth/|POST|Authentication token|User object|201|Must be logged in|
|   |    |   |   |   |   |

### Insomnia Screenshots
/projects/ POST
![/projects/ POST image](./images/:projects:%20POST.png)

/projects/ GET
![/projects/ GET image](./images/:projects:%20GET.png)

/projects/<int:pk>/ GET
![/projects/<int:pk>/ GET image](./images/:projects:1:%20GET.png)

/projects/<int:pk>/ PUT
![/projects/<int:pk>/ PUT image](./images/:projects:1:%20PUT.png)

/projects/?limit=3 GET
![/projects/?limit=3 GET image](./images/:projects:?limit=3%20GET.png)

/projects/?is_open=True GET
![/projects/?is_open=True GET image](./images/:projects:?is_open=True%20GET.png)

/projects/?order_by=date_created GET
![/projects/?order_by=date_created GET image](./images/:projects:?order_by=date_created%20GET.png)

/projects/?order_by=num_pledges GET
![/projects/?order_by=num_pledges GET image](./images/:projects:?order_by=num_pledges%20GET.png)

/projects/?order_by=recent_pledges GET
![/projects/?order_by=recent_pledges GET image](./images/:projects:?order_by=recent_pledges%20GET.png)

/pledges/ GET
![/pledges/ GET image](./images/:pledges:%20GET.png)

/pledges/ POST
![/pledges/ POST image](./images/:pledges:%20POST.png)

/pledges/?order_by=date_created GET
![/pledges/?order_by=date_created GET image](./images/:projects:?order_by=date_created%20GET.png)

/users/ POST
![/users/ POST image](./images/:users:%20POST.png)

/api-token-auth/ POST
![/api-token-auth/ POST image](./images/:api-token-auth:%20POST.png)





### DB Schema
![Screenshot of database schema](./images/crowdfunding%20back%20end%20schema.png)
------