import httpx
import json
from time import perf_counter
url = "http://192.168.10.85:5155/api/confirmation/"

payload = json.dumps({
  "regnum": "СЩ02231493",
  "orgUuid": "0390bc57-5e32-436c-9b27-c7914b82750f",
  "otp": "871634"
})
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiLQo9CjODkwNDEyMjgiLCJyb2xlIjpbIk9QRVJBVE9SIixudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsXSwiZXhwIjoxNjgyMDgwNzI5LCJ1c2VySWQiOjIxNzYsImlhdCI6MTY4MjA2NjMyOX0.z7eUUgd8qh7mL2FdB6wRuRGK4wU0dRgT36SXcN2dQeo',
  'Content-Type': 'application/json'
}
t1_start = perf_counter()
response = httpx.post(url, data=payload, headers=headers, verify=False)
t1_stop = perf_counter() 
 
print("Elapsed time during the whole program in seconds:",
                                        t1_stop-t1_start)