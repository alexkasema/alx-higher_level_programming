# Python - Network #1
## 0-hbtn_status.py
A Python script that fetches https://alx-intranet.hbtn.io/status
* You must use the package urllib.
## 1-hbtn_header.py
A Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
* You must use the packages urllib and sys.
## 2-post_email.py
Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8).
## 3-error_code.py
Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
* You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code.
## 4-hbtn_status.py
Python script that fetches https://alx-intranet.hbtn.io/status
* You must use the package requests.
## 5-hbtn_header.py
Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
* You must use the packages requests and sys.
## 6-post_email.py
Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
* The email must be sent in the variable email.
## 7-error_code.py
A Python script that takes in a URL, sends a request to the URL and displays the body of the response.
* If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code.
## 8-json_api.py
A Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
* The letter must be sent in the variable q.
* If no argument is given, set q="".
* If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>.
## 10-my_github.py
Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id.
## 100-github_commits.py
Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
