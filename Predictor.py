import joblib
print("\n -----------------SALARY PREDICTION------------------\n")
model = joblib.load('salary.pk1')
while(1):
    exp = int(input('\tEnter candidate\'s experience: '))

    #Prediction
    predicted = model.predict([[exp]])

    print("Candidate's salaray will be ",predicted)
    ch = input("\nDo you want to continue (Y|N):")
    ch = ch.capitalize()
    if ch != 'N':
        print("\n\tExiting the program .........")
        exit()