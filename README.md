# <center> *WhereTo?* <center>

# <center><span style="font-weight: bold; font-size: 18px;">Purpose of Application</center></span>
*WhereTo?* is an application that allows for its users to share their travel stories and reviews of places around the world they have visited with an online community. Not only does *WhereTo?* provide a sense of community for users, it also provides real consumer evaluations of accommodations, dining experiences, and tourism activities so that travelers may feel confident about their vacation plans before they commit.
 

# <center><span style="font-weight: bold; font-size: 18px;"><br>Functionality and Features of *WhereTo?*</center></span>
- The application allows users to post reviews/stories about their previous travel experiences.
- User posts consist of a title, description, destination and category of the subject of their review (for example restaurant, hotel or activity).
- Creators of posts are able to delete their posts if they wish too.
- Users are able to sign up to the site and user authentication is used where appropriate.
- The application is built through using AWS cloud services including: EC2 (both instances and load balancers) and the API Gateway.
- The application utilises DevOps technologies including: version control (git/Github and webhooks) and Docker.

# <center><span style="font-weight: bold; font-size: 18px;"><br>Significant Libraries and Technologies</center></span>
- Flask: The web framework was used to help build the application. Flask's varitey of tools, libraries and technologies aided in the application's construction. Notably, Flask has been used to handle authenitcation throughout the program. 
- SQLite: SQLite is the database technology chosen for the application. 
- EC2: In the application EC2 instances are used for running code on persistent infrastructure. EC2 has been used to run the flask application.
- Load Balancer: Inbound application traffic is distributed over multiple EC2 instances, across several Availability Zones via the load balancer.
- API Gateway:
- Docker: Docker's features and ability for containerising programs that enable development and rapid release make it ideal for the DevOps pipeline. The tool is important to the app since it ensures that any functionality that works in the development platform will also work in the production and staging environments.
- Git/Github:

# <center><span style="font-weight: bold; font-size: 18px;"><br>Appropriate use of Project Management Methodology</center></span>
I chose to use an Agile project management methodology to ensure that I worked efficiently and productively whilst still delivering high quality work. I used a Trello board throughout the project which allowed me to track tasks, label each task with a difficult level, checklists and due dates. Additionally, the use of the Trello board has allowed me to prioritise tasks so I could make sure all the features which matter most to users are included and functional before I attempted to add in extra features. A number of screenshots of the Trello board used throughout the project are attached below.

# <center><span style="font-weight: bold; font-size: 18px;"><br>Appropriate use of Task Delegation Methodology</center></span>
As the sole developer of *WhereTo?* all tasks for the project have been delegated to myself. Consequently, this has made completing the application quite challenging as while I am strong with Python, Flask and building a simple user interface I am new to using cloud and serverless technologies and deploying an application on a Cloud service. While ordinarily developers would be able to rely on their team members in their areas of weaknesses, I have had to use online resources and turn to my tutors in order to make up for my shortcomings and complete the project.


# <center><span style="font-weight: bold; font-size: 18px;"><br>Testing during Development</center></span>
Unittesting and a manual testing suite were used to test all features of the site during development.A screenshot of the Excel file of a manual test suite used for testing during development is attached below.

### <br><center>**Manual Testing Suite (Development)** ###
<img src="docs/images/testing/development_testing_1.png">
<img src="docs/images/testing/development_testing_2.png">


# <center><span style="font-weight: bold; font-size: 18px;"><br>Testing during Production</center></span>
A screenshot of the Excel file of a manual test suite used for testing during production is attached below. Images of a client using/testing the site are also included below.

### <br><center>**Manual Testing Suite (Production)** ###
<img src="docs/images/testing/testing_production_1.png">
<img src="docs/images/testing/testing_production_2.png">

### <br><center>**Photos of a Client using *WhereTo?* during Production** ###

<center>Client Creating a Review
<img src="docs/images/testing/client_create_review.png">

<br><center>Client Testing Homepage
<img src="docs/images/testing/client_create_review.png">

<br><center>Client causing Error Message due to Entering Incorrect Password
<img src="docs/images/testing/client_error_password.png">

<br><center>Client Testing Site on Alternate Computer
<img src="docs/images/testing/client_alternative_computer.png">