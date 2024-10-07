from jira import JIRA,exceptions

def jira_create(project=str,title=str,jira_url=str,jira_token=str, jira_email=str) -> dict:
    try:
        jira = JIRA(jira_url, basic_auth=(jira_email,jira_token))
        jira_description = f"Starting a ticket to: {title}"
        new_isssue = jira.create_issue(project=project, summary=title,
                                    description=jira_description,
                                        issue_type={'name': 'Story'} )
        created_url = new_isssue.permalink()
        created_issue_id = new_isssue.id
        created_issue_subject = new_isssue.get_field('summary')
        slug = created_issue_subject.replace(" ", "-")
        slug = slug.lower()
        response = dict
        response[slug]={'url':created_url,
                        'issue_id': created_issue_id,
                        'summary': created_issue_subject}
        return response
        
    except :
        return exceptions.JIRAError("Error creating ticket: \n")