print("*****************Remove a key-value pair from the dictionary********************")

dict1 = {'a':1 , 'b':2, 'c': 3, 'd':4}
val = dict1.pop('a')
print(dict1)

print("*******************Convert to Dict JSON Response and Print************************")
dict2 = {

"bookingid": 2384,

"booking": {

"firstname": "PRAMOD",

"lastname": "Dutta",

"totalprice": 432,

"depositpaid": False,

"bookingdates": {

"checkin": "2022-01-01",

"checkout": "2022-01-01"

},

"additionalneeds": "Lunch"

}

}

print("Booking Id :",dict2["bookingid"])
print("checkin :",dict2["booking"]["bookingdates"]["checkin"])
print("checkout :",dict2["booking"]["bookingdates"]["checkout"])
