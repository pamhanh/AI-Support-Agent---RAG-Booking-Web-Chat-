import requests

url = "http://localhost:5678/webhook-test/dee9c822-0f07-4bdb-afad-afeadb405957"

payload = {
    "leads": [
        {"name": "Alice",   "email": "alice@shop.com",  "company": "Hacomm"},
        {"name": "Bob",     "email": "bob@store.com",   "company": "Lala"},
        {"name": "Alice Again", "email": "alice@shop.com", "company": "Tala"},
        {"name": "Charlie", "email": "charlie@web.io ", "company": "WebCo"},
        {"name": "Diana",   "email": "DIANA@mail.com",  "company": "Mailer"},
        {"name": "Evan",    "email": "diana@mail.com",  "company": "Mailer"},
        {"name": "Frank",   "email": "dss@gmai.com","company": "Ghost Ltd"},
        {"name": "salllaa","email": "helen@site.org",  "company": "SiteOrg"},
    ]
}

r = requests.post(url, json=payload)
print(r.status_code)