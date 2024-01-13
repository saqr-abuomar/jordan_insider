from ultralytics import YOLO

# Load a model
#model = YOLO("yolov8n.yaml")  # build a new model from scratch


def detect(path,cou) :
    model = YOLO(r"C:\Users\Admin\Desktop\jordan_insider\yolov8m_custom.pt")  # load a pretrained model (recommended for training)

    # Use the model

    results = model(path,conf=0.5,save_txt=True)  # predict on an image
    j=1
    i=cou
    path1="C:\\Users\\Admin\\jordan_insider\\runs\\detect\\predict" + str(i) + "\\labels\\" + str(j) + ".txt"
    path=open(path1)
    index=0
    for line in path:
        line=line.split()
        index=line[0]
        break

    obj=""
    if index==0 :
        obj = "Roman amphitheater"
    elif index==1 :
        obj = "JUST Gate"
    else:
        obj = "JUST Airplane"

    return obj

obj=detect(r"C:\Users\Admin\Desktop\jordan_insider\1.jpg",2)
print("The shap is :" ,obj)


