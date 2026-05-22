Using curl to interact with APIs
1. Check curl installation
curl --version

Result: curl is installed and working.

2. GET request (web page)
curl http://example.com

Result: HTML page successfully returned.

3. GET request (API data)
curl https://jsonplaceholder.typicode.com/posts

Result: JSON list of posts received.

4. View headers only
curl -I https://jsonplaceholder.typicode.com/posts

Result: HTTP response headers displayed.

5. POST request
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts

Result: Server returned created object with id 101.

Conclusion

I learned how to:

Use curl commands
Fetch web pages
Work with APIs
Send data using POST requests
