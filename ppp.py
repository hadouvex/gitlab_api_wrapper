# a = [{"22808408": {"name": "partnerka.education"}}, {"22792198": {"name": "mostbet-codegen"}}, {"22791948": {"name": "Emg-front"}}, {"22791920": {"name": "mostbet-referral-program"}}]

# b = {'a':'a', 'b': 'b'}

# f = []

# for i in a:
#     print(i.keys())
#     f.append(i.keys())
#     print(f)

# x = ({'cock': ['cool', 'man']})
# print(x.keys())

# print(a[0])
# print(b)

# for k, v in a[1]:
#     print(k, v)

a = {"22808408": {"name": "partnerka.education"}, "22792198": {"name": "mostbet-codegen"}, "22791948": {"name": "Emg-front"}, "22791920": {"name": "mostbet-referral-program"}, "22791814": {"name": "mostbet-integration-slotegrator"}}
b = {1:2, 3:4}

for k, v in b.items():
    print(k)

for k, v in a.items():
    print(v['name'])