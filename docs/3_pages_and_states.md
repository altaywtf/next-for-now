#Pages and States
This document contains the information about pages and their states for possible conditions.


---


##Home Page
Visible for all viewers with the same condition.

##About
Visible for all viewers with the same condition. [May be precoded pure html.](http://nextfornow.com)

##Contact
Visible for all viewers with the same condition. Includes a basic contact form.

##Sign Up 
Visible for all viewers with two membership options.
- Sign Up - Form
	- **Case 1**: A form to have contest owner account.
	- **Case 2**: Another form to have an applicant account.

##Log In
Since we will be gathering user credentials with the same format, I think we can use same login form for all users. System should check the user type and render the templates according to it.

##Show Contests
This page contains a search bar and filtering options.

- **Case 1**: Visible for all viewers with optional filters.
	- Show all.
	- Show all ongoing.
	- Show all finished.
	- Show all from a specific category.

- **Case 2**: Same template, but it renders with respect to the contest owners.
	- Example: show all of the contests created by my company.

- **Case 3**: Same template, but it renders with respect to the applicants.
	- Example: show all of the contests an applicant has posted a submission.

##Show an Individial Contest
- **Ongoing Contest**
	- **Case 1**: Visible for non-login users (public). Number of submissions is visible. "Post a submission" button will lead them to the [sign up form.](#sign-up-main)
	- **Case 2**: This is for contest owners. They will be able to see the submissions on this page. They can also have additional buttons like "update contest".
	- **Case 3**: This is for applicants. They will post their submissons from this page with a modal opening when "post a submission" button is clicked. They can't see the other submissions while contest is ongoing.
- **Finished Contest**
	- **Case 1**: Visible for public. Number of submissions and [just the name of winner](2_database_architecture.md/#submissions) are visible. 
	- **Case 2**: For contest owners. 
	- **Case 3**: For applicants. Each applicant can see all the submissions if the contest has finished.

##Account Settings
- **Case 1**: For companies; lists the information provided on sign up process. They can update their parameters from here.
- **Case 2**: For applicants; same as the companies.


---


##Partials
###Navbar
Changes stance with respect to login/logout operations.

###Footer
Same for all pages, includes a sitemap and meta description.


---