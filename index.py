from github import Github, GithubIntegration

private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA003UErSV06XBGHCPRgzIOCAW58p0OwY+lUZMGABvAa/xbIFf
E5qu+tLyZTaoWcOHOPN7pATyqAsms1r6/nxCVmiFF4Z67PSfpcsrKRYKaa0IP9QF
oKEeVnD1gK0KvWfh9/NgrMPbW9WTO4q/vN3iTf8Vbq2qIQS+w4ax6mBTVEkyodQI
Hjh8wMCs1rGwvdhfSKR483BRrnmI7gX5d1aM5QwRRFiVDYSgwF2b73+CGTeW75dK
ic5KltACHK1/HpyO2BH/Hy2wR2CXYH/EXwON6UwBXptI2RbR2BtUdCkc4tAq0a4p
4BdHUjrTyUUitX3piZXX5ntKVfi/m/ZcwWGC5wIDAQABAoIBAQCN4xn/wYFGEGx8
I8EhUZ30ih+3X6vyonvNstmP2GKx6Fod+TVFrb3HsXSQ4EXlmLUpWd3xQl1K18oR
74rQ7dGBwkd0h5ntmUnGg4mk2ib91PHQImfw95+ufcVstUWb77C91ZBaEl4u6Vgn
SED96qR2qU3T9wthhpUuKDk535q04gVAkAARDNnoxj0LsuFrSmFusuQ/tPyoe/hv
K93xZFUUlfpSZ25nDheaPNzkGBaEWphOJtXvfh+1b+3tbtQMzPi7OxmwFXmuprKm
XHfyz4GTTBunDzy9me+0EPBcFrSYuu3Xo2lJDYbZ902FT5fImn8XW88gIYRW4Aq2
FmfHtRwJAoGBAPRftIMbOESmZWirDK4nKDruh9TiKgb/6cGr/j76o/5zx2FUVgCE
ww8kI5pcNXa6ltxkoR4nhpfyEmkB7zIxHGugExY9hKc5QhuQpE/YUdfRXeHG2eX6
Wnqu3wdjvmiWgL9TrBQc1R8PwUlk0gSrSfbLVvLjHw2bYXTsR/D+iNk9AoGBAN1b
W16ijppA/m4DrjHjQwMKu8isB5jW/Oec2PIHXKCBaS3v5SnZRRfXbpH0Pt2sKlf7
hlMRFplYyWwkCm8WvStMN65HAfEdzNksOROIjZV6Lf3JqYxalkPHKJ/lWHCfl8QK
CKoudzqI3NgZ/nOjv24rMRxV6MSMQphLJBlXcWbzAoGAfinm/QURkMfDdT1SB5tp
trstX2gAQKrg2T9dvNAT2KuXlRVAbXYdanTC+M+APrLobhJ56CKJ52pvvMzl3Cjk
vl/fWs0Z7meuTKLpYduRrXWHHahXGNee3NXpiVwiksaY465kGeIk2at9o9GsaAKy
5fpnAnDluFWvA/l0zuPqbRUCgYAOfkPOP3B80xKVm3IVXB7wHQzMh877h+AJPjDK
MAc1jyOW2WU0x0AJ3pYjwk03cGVZW2OhHrZPFgwiI333ZhK+uf/PTmDnK59U/NtD
1yYGCnjmbATI5sl96JVVWsvem+Rw9oM4uVAfKgTjtVf+tFL9YKCXjVxvOgvGMu1L
J3mKVwKBgQDQPPO1nsaDc2ZV2N4yBsSQ9Js6Qj3SzP67PuTfQL7oHabMy0aMfeo9
nFD2T911JIOdHyBd/CRKjYXxfdY6B2ZKitTgh9jw6HQlDCGAskxG7KWjLIp2fruy
go4eYTwGW/iLxdeFZem9eI+C58A60Zclocr/6+KNgxyfHYseWarB1A==
-----END RSA PRIVATE KEY-----"""

# GitHub App settings
app_id = "342306"
private_key_path = "creds.pem"
installation_id = 38202424

# Repository information
repository_owner = 'ypkalra'
repository_name = 'test_json'

# Local file path to upload
local_file_path = 'Message_yash.txt'


def handler(e, ctx):
    # Create a GithubIntegration instance
    try:
        print("Entered into state uploading file")
        integration = GithubIntegration(app_id, private_key)

        # Create an access token for the installation
        access_token = integration.get_access_token(installation_id).token

        # Create a PyGithub instance with the access token
        github = Github(access_token)

        # Get the repository
        repo = github.get_user(repository_owner).get_repo(repository_name)

        # Create a new file in the repository
        file_path = 'message_yash.txt'  # Path where the file will be uploaded in the repository
        commit_message = 'Upload file'  # Commit message for the upload

        with open(local_file_path, 'r') as file:
            content = file.read()

        try:
            repo.create_file(file_path, commit_message, content, branch="main")
        except Exception as e:
            print(e)
    except Exception as e:
        print("Exception occurred in Upload File Function ", str(e))