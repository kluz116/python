def lcm(a,b):
    list = []

    for i in range(300):
        if i > 0 :
            print(i)
            if (i % a == 0 and i % b == 0):
                list.append(i)
                break
                
    
    
    return list

print(lcm(100,200))

tree = {
    'name': "John",
    'children': [
      { 'name': "Hari", 'children': [] },
      {
        'name': "Don",
        'children': [
          { 'name': "Don son", 'children': [{ 'name': "don grandson", 'children': [] }] }
        ]
      }
    ]
  }


for i in tree.values():
    print(i.name)

