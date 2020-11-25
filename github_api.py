import requests
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", type=str, dest="name", required=True)
args = parser.parse_args()
repo_name = args.name
# is_private = args.is_private

url = "https://api.github.com"

# if is_private:
# payload = '{"name": "' + repo_name + '", "private": true }'
# else:
payload = '{"name": "' + repo_name + '", "private": false }'


headers = {
	"Authorization": "token " + "bfda1de229fde1ef300a2b4519fa08926b6320fb",
	"Accept": "application/vnd.github.v3+json"
}

try:

	r = requests.post(url+"/user/repos", data=payload, headers=headers)
	r.raise_for_status()

except requests.exceptions.RequestException as err:
	raise SystemExit(err)

try:
	os.system("git init")
	os.system("git remote add origin https://github.com/MondaleFelix/" + repo_name + ".git")
	os.system("echo '# " + repo_name + "' >> README.md")
	os.system("git add . && git commit -m 'Initial Commit' && git push origin master")
except FileExistsError as err:
	raise SystemExit(err)


