import json
with open('image_info_test-dev2017.json') as f:
    data = json.load(f)
    print("Number of images: ",len(data['images']))
    print("Number of categories: ",len(data['categories']))
    max = 0
    imax = ''
    for i in range(len(data['images'])):
        if(data['images'][i]["id"]>max):
            max = data['images'][i]["id"]
            imax = data['images'][i]['file_name']
        if data['images'][i]['file_name']=='000000000001.jpg':
            print("url: ",data['images'][i]["coco_url"])
            print("height: ",data['images'][i]["height"])
            print("width: ",data['images'][i]["width"])
            print("id: ",data['images'][i]["id"])
            
    print(imax)

    


    