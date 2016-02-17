# Django test task 'Students Base' `completed`

## Entities
1. Student: Full name, date of birth, student ID, group(FK for group)
2. Group: Group name, group monitor(FK for student)

### Project use sqlite as data storage and have initial_data.json with initial values for `students_base_app`

## Tasks
1. The list of groups(table with columns: group name, number of students in group, group monitor). When you click on a 
group - page with the list of students of this group. CRUD operations for Students/Groups.
2. Add authorization for these pages (username, password).
3. Create Middleware which for all pages with content_type == 'text/html' adds query time
and number of SQL queries (before `</body>` closing tag).
4. Django Admin. Create admin views for Students and Groups(also Students must be inline for Groups)
5. Templates/Context. Create template-context-processor which adds `django.settings` in template context.
6. Templates/Tags. Create template tag which takes any object and return reference to it
editing in the admin area (for example `{% edit request.user %}`).
7. Signals. Write a signal handler which for any models change create record on its
database about creating/updating/deleting.
8. Commands. Write Django command which prints in to console list of the groups and students in these groups.
9. Django Test. Write Django TestCase(unittest) which logs in to the site and create new group and student in this group. 