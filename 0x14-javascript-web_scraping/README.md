# JavaScript - Web scraping
JavaScript Object Notation (JSON) is a standard text-based format for representing structured data based on JavaScript object syntax. It is commonly used for transmitting data in web applications (e.g., sending some data from the server to the client, so it can be displayed on a web page, or vice versa). You'll come across it quite often, so in this article, we give you all you need to work with JSON using JavaScript, including parsing JSON so you can access data within it, and creating JSON.
## 0-readme.js 
A script that reads and prints the content of a file.
* The first argument is the file path
* The content of the file must be read in utf-8
* If an error occurred during the reading, print the error object
## 1-writeme.js
A script that writes a string to a file.

* The first argument is the file path
* The second argument is the string to write
* The content of the file must be written in utf-8
* If an error occurred during while writing, print the error object
## 2-statuscode.js
A script that display the status code of a GET request.

* The first argument is the URL to request (GET)
* The status code must be printed like this: code: <status code>
* You must use the module request
## 3-starwars_title.js
A script that prints the title of a Star Wars movie where the episode number matches a given integer.

* The first argument is the movie ID
* You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
* You must use the module request
## 4-starwars_count.js
A script that prints the number of movies where the character “Wedge Antilles” is present.

* The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
* Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
* You must use the module request
## 5-request_store.js
script that gets the contents of a webpage and stores it in a file.

* The first argument is the URL to request
* The second argument the file path to store the body response
* The file must be UTF-8 encoded
* You must use the module request
## 6-completed_tasks.js
A script that computes the number of tasks completed by user id.

* The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
* Only print users with completed task
* You must use the module request
## 100-starwars_characters.js
A script that prints all characters of a Star Wars movie:

* The first argument is the Movie ID - example: 3 = “Return of the Jedi”
* Display one character name by line
* You must use the Star wars API
* You must use the module request
