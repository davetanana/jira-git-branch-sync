import os
import click
import codecs
from dotenv import load_dotenv
from cmd.jira_cmds import jira_cmd
from cmd.git_cmds import git_cmd
load_dotenv()

jira_url = os.getenv('JIRA_URL')
jira_token = os.getenv('JIRA_TOKEN')
github_project = os.getenv('GITHUB_PROJECT')
github_pat  = os.getenv('GITHUB_PAT')

@click.command()
@click.option('-p', '--project', type=str,help="This is the Jira \
             board to use" ,prompt=True, default=lambda: os.environ.get('JIRA_PROJECT', ""))
@click.option('-o', '--org', type=str,help="This is the Github \
             org to use" ,prompt=True, default=lambda: os.environ.get('GITHUB_ORG', ""))
@click.option('-j', '--jira-url', type=str,help="This is the Jira \
             url to use" ,prompt=True, default=lambda: os.environ.get('JIRA_URL', ""))
@click.option('-r', '--repos', type=list, help=" This is the repos \
            you wish to add branches for" \
            ,prompt=True, default=lambda: os.environ.get('JIRA_URL', ""))
@click.password_option('-P','--github-pat', type=str, help="Your Github Personal Access Token" ,\
                        prompt=True, hide_input=True ,default=lambda: os.environ.get('GITHUB_PAT', "") )
@click.password_option('-J','--jira-email', type=str, help="Your JIRA Email Address" ,\
                        prompt=True, hide_input=False ,default=lambda: os.environ.get('JIRA_EMAIL', "") )
@click.password_option('-J','--jira-token', type=str, help="Your JIRA Token" ,\
                        prompt=True, hide_input=True ,default=lambda: os.environ.get('JIRA_TOKEN', "") )
@click.option('--extra-identifier', type=str, 
             help="Extra identifier to pass to git branch")
@click.argument("title" )

def main(project,title,jira_url,jira_token,repos,github_pat,org,extra_identifier,jira_email ):
    """A simple program to allow you to easily create a JIRA Ticket/ Branches for several repos ing git.\
        The command takes a [title] argument and you must have all optionals set"""
    click.echo(f"encoded: {codecs.encode(github_pat, 'rot13')}")
    click.echo(f"encoded: {codecs.encode(jira_email, 'rot13')}")
    click.echo(f"encoded: {codecs.encode(jira_token, 'rot13')}")
    jira_ticket_info = jira_cmd.jira_create(project,title,jira_url,jira_token,jira_email)

    for repo in repos:
        git_cmd.github_create(repo, org, github_pat, extra_identifier, jira_ticket_info)
        pass
    pass

if __name__=="__main__":
    main()