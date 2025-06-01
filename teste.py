def getCalssName(classNo):
    if classNo == 0:
        return 'JOIA'
    elif classNo == 1:
        return 'PAZ E AMOR'
    elif classNo == 2:
        return 'ROCK AND ROLL'

while True:
    success, imgOrignal = cap.read()

    img = np.asarray(imgOrignal)
    img = cv2.resize(img, (32, 32))
    img = preprocessing(img)
    img = img.reshape(1, 32, 32, 1)

    predictions = model.predict(img)
    indexVal = np.argmax(predictions)
    probabilityValue = np.amax(predictions)
    print(indexVal,probabilityValue)

    cv2.putText(imgOrignal, str(getCalssName(indexVal)), (120, 70), cv2.FONT_HERSHEY_SIMPLEX, 2,
                (0, 0, 255), 8, cv2.LINE_AA)
    cv2.putText(imgOrignal, str(round(probabilityValue * 100, 2)) + "%", (120, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2,
                cv2.LINE_AA)

    cv2.imshow("Result", imgOrignal)
    cv2.waitKey(1)
