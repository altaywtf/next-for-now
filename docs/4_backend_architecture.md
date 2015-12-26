#Backend Architecture
This document contains detailed information about the backend architecture of Next For Now.

We are using Django web framework (version 1.9)

---

##Apps
###Users
- Login (/users/login)
- Sign up (/users/sign-up)

###Contests
- View all (/contests)
- View individual (/contests/{contest_id})
- View all contests from a category (/contests/category/{category_name})
- View all contests created by a contest owner (/contests/company/{company_pk})
- Create (/contests/create)
- Edit (/contests/edit)
- Delete (/contests/delete)
- **Submissions**
- Posting a submission (/contests/{contest_id}/apply)
- Submissions (/contests/{contest_id}/submissions)
- Individual submission (/contests/{contest_id}/submissions/{submission_id})

---

##Models
- User Model
- Category Model
- Contest Model
- Submission Model

---

##Views
- User Views
- Contest Views
- Submission Views

---

##Templates

---

##URLs
####Static Pages
- Home (views.IndexView.as_view())
- About (views.AboutView.as_view())
- Contact (contactView)
- Contests (include('nfn_contests.urls'))
- User (include('nfn_user.urls'))
- Admin (admin.site.urls)

####Apps Pages
######Contests URLs
- Category ((category_slug), views.FilterByCategory())
- Company ((company_pk), views.FilterByOwner())
- Ongoing (views.FilterByOngoing())
- Finished (views.FilterByFinished())
- Search (views.FilterBySearch())
**Create (views.ContestCreate())**
- Update Contests ((slug), views.ContestUpdate())
- Delete Contests ((slug), views.ContestDelete())
- View Contests ((slug), views.ContestDetail())
- Contest Winner ((slug), views.ContestWinner())
**Submissions**
- Post ((contest_slug), views.SubmissionCreate())
- Update Submission ((contest_slug)(pk[0-9]), views.SubmissionUpdate())
- Delete Submission ((contest_slug)(pk[0-9]), views.SubmissionDelete())
- View Submission ((contest_slug)(pk[0-9]), views.SubmissionDetail())
- Submission Feedback ((contest_slug)(pk[0-9]), views.FeedbackCreate())
######User URLs
- Signup (views.SignUpView)
- Signup Owner (views.cOwnerSignUpView)
- Signup Applicant (views.applicantSignUpView)
- Login (views.loginView)
- Logout (views.logoutView)
- Settings (views.userChangeView)



---

##Settings

---