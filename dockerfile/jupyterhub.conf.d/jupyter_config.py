# Documentation:
# - https://oauthenticator.readthedocs.io/en/latest/getting-started.html#gitlab-setup

import os

# Use Jupyter-Lab interface
c.Spawner.cmd = ['jupyter-labhub']

if 'GITHUB_CLIENT_ID' in os.environ:
    assert 'GITHUB_CLIENT_SECRET' in os.environ

    # from oauthenticator.github import LocalGitHubOAuthenticator
    from oauthenticator.github import LocalGitHubOAuthenticator
    c.JupyterHub.authenticator_class = LocalGitHubOAuthenticator

    c.LocalGitHubOAuthenticator.create_system_users = True

    ## Add the administrator(s) to this list
    c.Authenticator.admin_users = {'chbrandt'}

    ## Add allowed users to this list if you want to restrict access
    #c.Authenticator.whitelist = {'joao','maria'}

    c.LocalGitHubOAuthenticator.client_id = os.environ['GITHUB_CLIENT_ID']
    c.LocalGitHubOAuthenticator.client_secret = os.environ['GITHUB_CLIENT_SECRET']
    c.LocalGitHubOAuthenticator.oauth_callback_url = os.environ['GITHUB_CALLBACK_URL']

else:
    if 'GITLAB_CLIENT_ID' in os.environ:
        assert 'GITLAB_CLIENT_SECRET' in os.environ

        from oauthenticator.gitlab import LocalGitLabOAuthenticator
        c.JupyterHub.authenticator_class = LocalGitLabOAuthenticator

        c.LocalGitLabOAuthenticator.create_system_users = True

        ## Add the administrator(s) to this list
        c.Authenticator.admin_users = {'chbrandt'}

        ## Add allowed users to this list if you want to restrict access
        #c.Authenticator.whitelist = {'joao','maria'}

        c.LocalGitLabOAuthenticator.client_id = os.environ['GITLAB_CLIENT_ID']
        c.LocalGitLabOAuthenticator.client_secret = os.environ['GITLAB_CLIENT_SECRET']
        c.LocalGitLabOAuthenticator.oauth_callback_url = os.environ['GITLAB_CALLBACK_URL']
