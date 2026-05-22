# Basics of HTTP/HTTPS

## 1. Difference Between HTTP and HTTPS

HTTP (HyperText Transfer Protocol) is a protocol used for communication between web clients and web servers. It allows browsers and servers to exchange data such as HTML pages, images, videos, and API responses.

HTTPS (HyperText Transfer Protocol Secure) is the secure version of HTTP. It uses SSL/TLS encryption to protect the communication between the client and the server.

### Main Differences

| HTTP | HTTPS |
|------|--------|
| Data is sent in plain text | Data is encrypted |
| Less secure | More secure |
| Uses `http://` | Uses `https://` |
| Vulnerable to interception | Protects sensitive data |
| No SSL/TLS | Uses SSL/TLS encryption |

HTTPS is important for protecting passwords, banking information, personal data, and authentication tokens.

---

# 2. Structure of HTTP Requests and Responses

## HTTP Request Structure

An HTTP request is sent from the client (browser) to the server.

Example:

```http
GET /index.html HTTP/1.1
Host: example.com
Accept-Language: en
```

### Parts of an HTTP Request

| Part | Description |
|------|-------------|
| Method | Action to perform (GET, POST, etc.) |
| Path | Resource location |
| HTTP Version | Protocol version |
| Headers | Additional information |
| Body | Optional data sent to server |

---

## HTTP Response Structure

An HTTP response is sent from the server back to the client.

Example:

```http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234
```

### Parts of an HTTP Response

| Part | Description |
|------|-------------|
| HTTP Version | Protocol version |
| Status Code | Result of request |
| Status Message | Short explanation |
| Headers | Additional information |
| Body | Returned resource/data |

---

# 3. Common HTTP Methods

| Method | Description | Use Case |
|--------|-------------|----------|
| GET | Retrieves data from the server | Opening a webpage or fetching API data |
| POST | Sends data to the server | Login forms or creating new resources |
| PUT | Updates existing data | Editing a user profile |
| DELETE | Removes data | Deleting a post or account |

---

# 4. Common HTTP Status Codes

| Status Code | Description | Example Scenario |
|-------------|-------------|------------------|
| 200 OK | Request successful | Webpage loaded correctly |
| 201 Created | Resource created successfully | New account registration |
| 301 Moved Permanently | Resource moved to another URL | HTTP redirected to HTTPS |
| 404 Not Found | Resource does not exist | Wrong URL entered |
| 500 Internal Server Error | Server encountered an error | Backend application crashed |

---

# 5. Observations from Browser Network Tab

Using the browser Developer Tools Network tab, it is possible to observe HTTP requests and responses made by websites.

The Network tab shows:

- HTTP methods
- Status codes
- Request and response headers
- Resource types
- Request timings

When a webpage loads, the browser sends multiple HTTP requests for resources such as:

- HTML files
- CSS stylesheets
- JavaScript files
- Images
- Fonts

This demonstrates how web pages are built from many separate resources fetched through HTTP requests.

---

# Conclusion

HTTP is the foundation of communication on the Web. It enables clients and servers to exchange resources using requests and responses.

HTTPS improves HTTP by adding SSL/TLS encryption, making communication secure and protecting sensitive information.

Understanding HTTP methods, status codes, requests, responses, and browser network activity is essential for web development and REST API development.
