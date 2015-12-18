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

---

##Settings

---