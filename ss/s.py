# import http.client
# import json
#
# conn = http.client.HTTPSConnection("pepe53.api.infobip.com")
# payload = json.dumps({
#     "messages": [
#         {
#             "destinations": [{"to": "998901078055"}],
#             "from": "444",
#             "text": "Salom hasanman men"
#         }
#     ]
# })
# headers = {
#     'Authorization': 'App 626934d76b92205e69eb77589e1e96a7-58531e20-8977-4c6e-a5f3-04a66aeab3bd',
#     'Content-Type': 'application/json',
#     'Accept': 'application/json'
# }
# conn.request("POST", "/sms/2/text/advanced", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))


# next_greater_map = {}
# stack = []
#
#
# for num in nums2:
#     while stack and num > stack[-1]:
#         smaller_num = stack.pop()
#         next_greater_map[smaller_num] = num
#     stack.append(num)
#
# while stack:
#     next_greater_map[stack.pop()] = -1
#
# return [next_greater_map[num] for num in nums1]
# nums1 = [4, 1, 2]
# nums2 = [1, 3, 4, 2]
# print(nextGreaterElement(nums1, nums2))  # Output: [-1, 3, -1]
