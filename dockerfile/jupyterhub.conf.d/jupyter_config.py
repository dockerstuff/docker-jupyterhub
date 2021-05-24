# Documentation:
# - https://oauthenticator.readthedocs.io/en/latest/getting-started.html#gitlab-setup

from oauthenticator.gitlab import GitLabOAuthenticator
c.JupyterHub.authenticator_class = GitLabOAuthenticator

# Use Jupyter-Lab interface
c.Spawner.cmd = ['jupyter-labhub']

# import os
# if 'GITHUB_CLIENT_ID' in os.environ:
#     assert 'GITHUB_CLIENT_SECRET' in os.environ
#     assert 'GITHUB_CALLBACK_URL' in os.environ
#
#     # from oauthenticator.github import LocalGitHubOAuthenticator
#     from oauthenticator.github import GitHubOAuthenticator as Authenticator
#
#     c.JupyterHub.authenticator_class = LocalGitHubOAuthenticator
#
#     c.LocalGitHubOAuthenticator.create_system_users = True
#
#     ## Add the administrator(s) to this list
#     c.Authenticator.admin_users = {'user'}
#
#     ## Add allowed users to this list if you want to restrict access
#     #c.Authenticator.whitelist = {'joao','maria'}
#
#     c.LocalGitHubOAuthenticator.client_id = os.environ['GITHUB_CLIENT_ID']
#     c.LocalGitHubOAuthenticator.client_secret = os.environ['GITHUB_CLIENT_SECRET']
#     # c.LocalGitHubOAuthenticator.oauth_callback_url = f'{server_url}/hub/oauth_callback'
#     c.LocalGitHubOAuthenticator.oauth_callback_url = os.environ['GITHUB_CALLBACK_URL']
