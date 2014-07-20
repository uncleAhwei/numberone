task = {
    "2" : "Speak in an American accent for 10 minutes",
    "3" : "Get 10 girls to sign your shirt",
    "4" : "Wear the Hanbao shirt. You must say meow meow meow before you speak",
    "5" : "Play PSS and say I love bacon when you lose and I love Hanbao if you win",
    "6" : "2 minutes of talking like Billy Bob Thornton from Slingblade",
    "7" : "Take half a shot. You're old and need to pace yourself",
    "8" : "Touch Eric's back hair.",
    "9" : "Bad Dave! Get spanked by a person of your choice",
    "10": "Stand at attention and salute when someone says your name. For 5 minutes",
    "11": "For 10 minutes you must say bacon after you have a drink",
    "12": "Sing I'm a little teapot"

}

num = raw_input("Enter a number from 2-12 to get your task:\n")
while True:
    for number in task:
        if number == num:
            print task[number]
    break