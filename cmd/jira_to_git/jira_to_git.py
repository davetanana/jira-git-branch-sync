import os
import click
from dotenv import load_dotenv
from jira_cmds import jira_cmd
from git_cmds import git_cmd
load_dotenv()

jira_url = os.getenv('JIRA_URL')
jira_token = os.getenv('JIRA_TOKEN')
github_project = os.getenv('GITHUB_PROJECT')
github_pat  = os.getenv('GITHUB_PAT')

@click.command()
@click.option('-p', '--project', str,help="This is the Jira \
             board to use" ,prompt=True, default=lambda: os.environ.get('JIRA_PROJECT', ""))
@click.option('-o', '--org', str,help="This is the Github \
             org to use" ,prompt=True, default=lambda: os.environ.get('JIRA_PROJECT', ""))
@click.option('-j', '--jira-url', str,help="This is the Jira \
             url to use" ,prompt=True, default=lambda: os.environ.get('JIRA_URL', ""))
@click.option('-r', '--repos', list, help=" This is the repos \
            you wish to add branches for" \
            ,prompt=True, default=lambda: os.environ.get('JIRA_URL', ""))
@click.password_option('-P','--github-pat', str, help="Your Github Personal Access Token" ,\
                        prompt=True, hide_input=True ,default=lambda: os.environ.get('GITHUB_PAT', "") )
@click.password_option('-J','--jira-email', str, help="Your JIRA Email Address" ,\
                        prompt=True, hide_input=False ,default=lambda: os.environ.get('JIRA_EMAIL', "") )
@click.password_option('-J','--jira-token', str, help="Your JIRA Token" ,\
                        prompt=True, hide_input=True ,default=lambda: os.environ.get('JIRA_TOKEN', "") )
@click.option('--extra-identifier', str, 
             help="Extra identifier to pass to git branch")
@click.argument(name="title" )

def main(project,title,jira_url,jira_token,repos,github_pat,org,extra_identifier,jira_email ):
    
    jira_ticket_info = jira_cmd.jira_create(project,title,jira_url,jira_token,jira_email)

    for repo in repos:
        git_cmd.github_create(repo, org, github_pat, extra_identifier, jira_ticket_info)
        pass
    pass
