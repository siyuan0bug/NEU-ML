import os
import random

from PIL import Image
originImgDir = 'C:\Users\思源\Documents\大三课程\机器学习\机器学习课程设计\任务三\segmentation\gab\segmentation -plus\train\image'
originLabelDir = 'C:\Users\思源\Documents\大三课程\机器学习\机器学习课程设计\任务三\segmentation\gab\segmentation -plus\train\label'

imgList = os.listdir(originImgDir)
random.shuffle(imgList)
# print(imgList)
outTrainDir = '../dataSetIMake1/trainPro'
if os.path.exists(outTrainDir) != True:
    os.mkdir(outTrainDir)

outValiDir = '../dataSetIMake1/valiPro'
if os.path.exists(outValiDir) != True:
    os.mkdir(outValiDir)

outTrainImg = '../dataSetIMake1/trainPro/image'
if os.path.exists(outTrainImg) != True:
    os.mkdir(outTrainImg)

outTrainLabel = '../dataSetIMake1/trainPro/label'
if os.path.exists(outTrainLabel) != True:
    os.mkdir(outTrainLabel)

outValiImg = '../dataSetIMake1/valiPro/image'
if os.path.exists(outValiImg) != True:
    os.mkdir(outValiImg)

outValiLabel = '../dataSetIMake1/valiPro/label'
if os.path.exists(outValiLabel) != True:
    os.mkdir(outValiLabel)

length = len(imgList)

length1 = int(0.9 * length)
# print(length)
# print(length1)
for i in range(length1):
    # print(imgList[i])
    imgAbsName = os.path.join(originImgDir, imgList[i])
    img = Image.open(imgAbsName)
    img1 = img.rotate(90)
    img2 = img.rotate(180)
    img3 = img.rotate(270)
    img4 = img.transpose(Image.FLIP_LEFT_RIGHT)
    img5 = img.transpose(Image.FLIP_TOP_BOTTOM)
    # img.show()
    # img4.show()
    # img5.show()
    imgIndex = imgList[i][:-4]
    imgName1 = imgIndex + 'a.jpg'
    imgName2 = imgIndex + 'b.jpg'
    imgName3 = imgIndex + 'c.jpg'
    imgName4 = imgIndex + 'd.jpg'
    imgName5 = imgIndex + 'e.jpg'

    # print(os.path.join(outTrainImg, imgList[i]))
    img.save(os.path.join(outTrainImg, imgList[i]))
    img1.save(os.path.join(outTrainImg, imgName1))
    img2.save(os.path.join(outTrainImg, imgName2))
    img3.save(os.path.join(outTrainImg, imgName3))
    img4.save(os.path.join(outTrainImg, imgName4))
    img5.save(os.path.join(outTrainImg, imgName5))
    # img.show()
    labelAbsName = os.path.join(originLabelDir, imgList[i])
    label = Image.open(labelAbsName)
    label1 = label.rotate(90)
    label2 = label.rotate(180)
    label3 = label.rotate(270)
    label4 = label.transpose(Image.FLIP_LEFT_RIGHT)
    label5 = label.transpose(Image.FLIP_TOP_BOTTOM)
    label.save(os.path.join(outTrainLabel, imgList[i]))
    label1.save(os.path.join(outTrainLabel, imgName1))
    label2.save(os.path.join(outTrainLabel, imgName2))
    label3.save(os.path.join(outTrainLabel, imgName3))
    label4.save(os.path.join(outTrainLabel, imgName4))
    label5.save(os.path.join(outTrainLabel, imgName5))
    # label.show()

for i in range(length1, length):
    # print(imgList[i])
    imgAbsName = os.path.join(originImgDir, imgList[i])
    img = Image.open(imgAbsName)
    img1 = img.rotate(90)
    img2 = img.rotate(180)
    img3 = img.rotate(270)
    img4 = img.transpose(Image.FLIP_LEFT_RIGHT)
    img5 = img.transpose(Image.FLIP_TOP_BOTTOM)
    # img.show()
    # img4.show()
    # img5.show()
    imgIndex = imgList[i][:-4]
    imgName1 = imgIndex + 'a.jpg'
    imgName2 = imgIndex + 'b.jpg'
    imgName3 = imgIndex + 'c.jpg'
    imgName4 = imgIndex + 'd.jpg'
    imgName5 = imgIndex + 'e.jpg'

    # print(os.path.join(outTrainImg, imgList[i]))
    img.save(os.path.join(outValiImg, imgList[i]))
    img1.save(os.path.join(outValiImg, imgName1))
    img2.save(os.path.join(outValiImg, imgName2))
    img3.save(os.path.join(outValiImg, imgName3))
    img4.save(os.path.join(outValiImg, imgName4))
    img5.save(os.path.join(outValiImg, imgName5))
    # img.show()
    labelAbsName = os.path.join(originLabelDir, imgList[i])
    label = Image.open(labelAbsName)
    label1 = label.rotate(90)
    label2 = label.rotate(180)
    label3 = label.rotate(270)
    label4 = label.transpose(Image.FLIP_LEFT_RIGHT)
    label5 = label.transpose(Image.FLIP_TOP_BOTTOM)
    label.save(os.path.join(outValiLabel, imgList[i]))
    label1.save(os.path.join(outValiLabel, imgName1))
    label2.save(os.path.join(outValiLabel, imgName2))
    label3.save(os.path.join(outValiLabel, imgName3))
    label4.save(os.path.join(outValiLabel, imgName4))
    label5.save(os.path.join(outValiLabel, imgName5))
