#Database Architecture
This document contains the database architecture & schemas of Next For Now.


---


##Database Tables for Users
###Admins
- id
- username (e-mail)
- password

###Contest Owners
- id
- username (e-mail)
- password
- company name
- company address
- website
- contests -> (hasTooMany)

###Applicants
- id
- username (e-mail)
- password
- submissions -> (hasTooMany)


---


##Database Tables for Contents
###Contests
- id
- owner -> (hasOne) from Contest Owners
- title
- category -> (hasTooMany) from Categories
- description
- details
- image
- award
- is_active (boolean) controlled by Admins
- is_over (boolean) controlled by Contest Owner (also related to deadline)
- submissions -> (hasTooMany)
- date_posted
- date_deadline
- winner -> (hasOne) from Submissions

###Submissions
- id
- contest -> (hasOne) from Contests
- applicant -> (hasOne) from Applicants
- details -> filled by Applicant
- files -> uploaded by Applicant
- feedback -> (hasOne) given by Contest Owners
- date_posted

###Contest Categories
- id
- title
- contests -> (hasTooMany) from Contests


---


###Schema Drawings
Will be added soon.


---