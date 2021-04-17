import os


project_dir = "/".join(os.path.dirname(os.path.realpath(__file__)).replace("\\", "/").split("/")[:-1])
projects_dir = "/".join(project_dir.split("/")[:-1])
secrets_dir = projects_dir + "/" + "0 - Secrets"

discord_token = open(secrets_dir + "/CS110RollBot/discord_token.txt").read()
api_json_path = secrets_dir + "/CS110RollBot/CS110RoleBot-0997a10a9b59.json"
