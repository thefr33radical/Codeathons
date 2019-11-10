import boto3, requests,sys
import os
def aws_img_recognize(key,secret_key,img):
    """
    Function to recognize text and faces from images
    """
    
    dct={}
    session = boto3.session.Session(aws_access_key_id=key, aws_secret_access_key=secret_key)
    rekognition = session.client('rekognition')
    try:        
        #response_img = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Stephen_Hawking_David_Fleming_Martin_Curley.png/640px-Stephen_Hawking_David_Fleming_Martin_Curley.png')
        #response_content = response_img.content
        f= img        
        rekognition_img = rekognition.detect_faces(Image={'Bytes': f}, Attributes=['ALL'])
        dct["face"] =rekognition_img["FaceDetails"][0]["Gender"]
    except Exception as e:
         dct["Face"]=e

    try:
        #response_txt = requests.get('https://miro.medium.com/max/2530/1*8yg31-493S7_i--Yw_eO7A.png')
        #responsetxt_content = response_txt.content
        f= img
        rekognition_text = rekognition.detect_text(Image={'Bytes': f})
        
        arr=rekognition_text["TextDetections"]
        
        # Store an array of detected text in a list
        txt_list=[]
        for i in arr:
            txt_list.append(i["DetectedText"])
        dct["text"]=txt_list
        return dct

    except Exception as e:
        dct["Text"]=e
        return dct

if __name__=="__main__":
    #aws_img_recognize(os.path.abspath(__file__),sys.argv[1],sys.argv[2])
    pass


