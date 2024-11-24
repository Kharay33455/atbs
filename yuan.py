import pyautogui as py
import time
import random
import pygetwindow as pw
#prepare the environment
def left_click(): 
    print("Starting left_click(): ")
    go_list = ['-1', '1']
    py.mouseDown()
    time.sleep(random.uniform(0.1,0.2))
    py.moveRel(int(go_list[random.randint(0,1)]), int(go_list[random.randint(0,1)]))
    time.sleep(random.uniform(0.1,0.2))
    py.mouseUp()
    py.moveRel(int(go_list[random.randint(0,1)]), int(go_list[random.randint(0,1)]))
def double_click():
    print("Starting double_click():")
    py.mouseDown()
    time.sleep(random.uniform(0.1,0.2))
    py.mouseUp()
    left_click()
def prep_stage():
    print("Starting prep_stage():")
    py.FAILSAFE = True
    py.PAUSE = 1
    print("Staged prepped")
#move and click function
def move_and_click(x,y,type):
    print("Starting move_and_click(x,y,type):")
    time.sleep(1)
    call_slide(x,y)
    if type == 'once':
        left_click()
    if type == 'twice':
        double_click()
    if type == 'right':
        py.rightClick()
#locate image and click function
def locate_and_click(type, pic):
    print("Starting locate_and_click(type, pic):")
    x,y = py.center(py.locateOnScreen(pic))
    move_and_click(x,y,type)
#launch chrome
def launch_chrome():
    print("Starting launch_chrome():")
    py.hotkey('winleft', 'm')
    try:
        #chrome has never been launched
        locate_and_click('twice', 'images/chrome.png')
    except(py.ImageNotFoundException):
        try:
        #chrome has been launched before
            locate_and_click('twice', 'images/chrome2.png')
        except(py.ImageNotFoundException):
            #click manually 
            move_and_click(614,161,'twice')
            
    #give program time incase system is slow
    time.sleep(2)
    #how many times should alt-tab be pressed
    count = 1
    while(pw.getActiveWindow().title != 'BlueStacks App Player'):
        py.keyDown('alt')
        i = 0
        while i < count:
            py.press('tab')
            i +=1
        py.keyUp('alt')
        count +=1
    time.sleep(10)
    #py.press('F11')
    print("App started")
    search_count = 0
    search(search_count)

def search(search_counter):
    print("Starting search(search_counter):")
    
    if search_counter > 20:
        restart()    
    print("Starting search function")
    try:
        #find search box
        locate_and_click('once', 'images/search.png')
    except(py.ImageNotFoundException):
        try:
            locate_and_click('once', 'images/search_full.png')
        except(py.ImageNotFoundException):

            #keep looking till found
            search_counter += 1
            search(search_counter)
    #wait a while so it loads
    time.sleep(5)
    #when found, search one of these
    products_purchased_by_women = [
    "Dresses", "Skirts", "Blouses", 
    "Activewear", "Workout clothes", 
    "Outerwear (jackets, coats)", "Shoes (boots, sandals, sneakers)", 
    "Accessories (scarves, hats, jewelry)", 
    "Skincare products (face masks, moisturizers, serums)", 
    "Hair care products (shampoos, conditioners, styling tools)", 
    "Makeup and cosmetics (foundations, eyeshadow, lipsticks)", 
    "Nail care products (polishes, accessories)", "Fragrances and perfumes",
    "Supplements (vitamins, collagen, detox products)", 
    "Yoga and fitness equipment (mats, dumbbells, resistance bands)", 
    "Massagers and relaxation tools (foot massagers, heated blankets)",
    "Home decor items (cushions, curtains, wall art)", 
    "Kitchen gadgets (blenders, coffee machines, air fryers)", 
    "Smart home devices (voice assistants, security cameras)", 
    "Organization products (storage bins, closet organizers, shelving units)",
    "Smartphones and accessories (cases, chargers)", 
    "Headphones, earphones, Bluetooth speakers", 
    "Fitness trackers and smartwatches", 
    "Cameras and photography equipment",
    "Baby clothes, toys, and accessories", 
    "Strollers, car seats, baby carriers", 
    "Educational toys and activities for young children",
    "Bridal accessories (veils, shoes, jewelry)", 
    "Party decorations (balloons, table settings)", 
    "Customizable items (wedding favors, invitations)",
    "Sewing and knitting kits", 
    "Scrapbooking and art supplies", 
    "Beading and jewelry-making kits"
    ]
    length_of_list = len(products_purchased_by_women)
    length_of_list -= 1
    a = random.randint(0, length_of_list)
    to_write = products_purchased_by_women[a]
    write(sentence=to_write)
    py.press('enter')
    print('Finished search function')
    v_count = 0
    verified(v_count)
#writer function to write dynamically and not like a bot
def write(sentence):
    print("Starting write(sentence):")
    for a in sentence:
        test_del = random.uniform(0.1,0.9)
        py.typewrite(a, test_del)

#sort for verified
def verified(vcount):
    print("Starting verified(vcount):")
    print('Looking for verified')
    if vcount > 10:
        restart()
    def go_to_chat(x,y):
        print("Starting go_to_chat(x,y):")
        call_slide(x,y)
        left_click()
        chat_count = 0 
        print("Verified found")
        chat(chat_count)
    def find_verified():
        print("Starting find_verified():")
        #checks all x for a given y
        def check_x(y):
            print("Starting check_x(y):")
            x = 654
            while x < 1261:
                (red,blue,green) = im.getpixel((x,y))
                if x % 1000 == 0:
                    print(f'red is {red}\nblue is {blue}\ngreen is {green}')
                    print(x,y)
                if red > -1 and red < 6:
                    if blue >140 and blue < 146:
                        if green > 250:
                            go_to_chat(x,y)
                x +=1
        y = 494
        while y < 1072:
            im = py.screenshot()
            check_x(y)
            y+=1
        print("Check all...")
        restart()
    find_verified()
                




    """
    try:
        locate_and_click('once', 'images/verified.png')
        go_to_chat()
    except(py.ImageNotFoundException):
        try:
            locate_and_click('once', 'images/verified2.png')
            go_to_chat()
        except(py.ImageNotFoundException):
            try:
                locate_and_click('once', 'images/verified3.png')
                go_to_chat()
            except(py.ImageNotFoundException):
                try:
                    locate_and_click('once', 'images/verified4.png')
                    go_to_chat()
                except(py.ImageNotFoundException):
                    try:
                        locate_and_click('once', 'images/verified5.png')
                        go_to_chat()
                    except(py.ImageNotFoundException):
                        vcount+=1
                        verified(vcount)
                        """
def age(count):
    print("Starting age(count):")
    print('Looking to filter age')
    while count < 10:
        try:
            locate_and_click('once', 'images/age.png')
            print("Seen age...")
            filter_counter = 0
            filter_age(filter_counter)
        except(py.ImageNotFoundException):
            count += 1
            time.sleep(3)
            age(count)
    call_slide(912,945)
    left_click()
    print("No age filter")
    chat_count = 0
    chat(chat_count)
    
def filter_age(filter_count):
    print("Starting filter_age(filter_count):")
    if filter_count > 20:
        restart()
    try:
        locate_and_click('once', 'images/years.png')
        show_count = 0 
        show(show_count)
    except(py.ImageNotFoundException):
        filter_count += 1
        filter_age(filter_count)
def show(show_counter):
    print("Starting show(show_counter):")
    if show_counter > 20:
        restart()
    try:
        locate_and_click('once', 'images/show.png')
        time.sleep(5)
        call_slide(912,945)
        left_click()
        chat_count = 0 
        chat(chat_count)
    except(py.ImageNotFoundException):
        show_counter += 1 
        show(show_counter)
#text
def chat(chat_count):
    print("Starting chat(chat_count):")
    if chat_count > 20:
        restart()
    print(f"Started chat function...{chat_count}")
    try:
        #need to fill captcha
        py.locateOnScreen('images/traffic.png')
        print("Sent to captcha")
        cap_count = 0
        captcha(cap_count)
    except(py.ImageNotFoundException):
        try:
            py.locateOnScreen('images/traffic_full.png')
            print("Sent to captcha")
            cap_count = 0
            captcha(cap_count)
        except(py.ImageNotFoundException):
            try:
                locate_and_click('once', 'images/chat_full.png')
                print("Chat clicked")
                start_count = 0
                start_typing(start_count)
            except(py.ImageNotFoundException):
                try:
                    locate_and_click('once', 'images/chat2_full.png')
                    print("Chat clicked")
                    start_count = 0
                    start_typing(start_count)
                except(py.ImageNotFoundException):
                    try:
                        locate_and_click('once', 'images/chat.png')
                        print("Chat clicked")
                        start_count = 0
                        start_typing(start_count)
                    except(py.ImageNotFoundException):
                        try:
                            locate_and_click('once', 'images/chat2.png')
                            print("Chat clicked")
                            start_count = 0
                            start_typing(start_count)
                        except(py.ImageNotFoundException):
                            x,y = py.position()
                            slide(x + random.randint(-10,10), y + random.randint(-10,10))
                            left_click()
                            chat_count += 1
                            chat(chat_count)
#restart function
def restart():
    print("Starting restart():")
    py.keyDown('winleft')
    py.press('printscreen')
    py.keyUp('winleft')
    print("Restart triggered")
    count = 1
    while(pw.getActiveWindow().title != 'BlueStacks App Player'):
        if count > 10:
            launch_chrome()
        py.keyDown('alt')
        i = 0
        print('Looking for verified')
        while i < count:
            py.press('tab')
            i +=1
        py.keyUp('alt')
        count +=1
    py.keyDown('alt')
    py.press('F4')
    py.keyUp('alt')
    call_slide(1097, 596)
    left_click()
    time.sleep(2)
    launch_chrome()
   # call_slide(1902, 976)
    #i = 0
    #while i <10:
     #   py.hotkey('ctrlleft', 'shiftleft', '2')
      #  i += 1
    #relaunch()

def relaunch():
    print("Starting relaunch():")
    try:
        locate_and_click('once','images/icon.png')
        search_count = 0
        print("Sorted")
        search(search_count)
    except(py.ImageNotFoundException):
        try:
            locate_and_click('once', 'images/icon_full.png')
            search_count = 0
            print("Sorted")
            search(search_count)            
        except(py.ImageNotFoundException):
            restart()
    
    
#captcha
def captcha(cap):
    print("Starting captcha(cap):")
    if cap > 20:
        restart()
    try:
        pass_ver()
#uncomment to use maximized windows instead of full screen
        #call_slide(1028,634)
        #py.mouseDown()
        #py.mouseDown()
        #call_slide(1261,633)
        #py.mouseUp()
        time.sleep(10)
        print("Captcha attempted")
        chat_count = 0
        chat(chat_count)
    except(py.ImageNotFoundException):
        cap += 1
        captcha(cap)
def pass_ver():
    print("Starting pass_ver():")
    try:
        call_slide(857,620)
        py.PAUSE = 0.1
        py.mouseDown()
        #py.mouseDown()
        x = 857 + random.randint(357, 447)
        y = 620 + random.randint(-10,10)
        slide(x,y,2)
        py.PAUSE = 1
        py.mouseUp()
    except(RecursionError):
        py.PAUSE =1
        py.mouseDown()
        py.mouseUp()
        #check if you've already passed captcha before attempting again
        x,y = py.position()
        if x > 857 + 356 and x <857 + 448 and y > 609 and y < 631:
            print("Captcha attempted")
            chat(0)
        else:
            call_slide(random.randint(5,1000), random.randint(5,100))
            captcha(0)
def call_slide(call_x, call_y):
    print("Starting call_slide(call_x, call_y):")
    x,y = py.position()
    x += random.randint(-5,5)
    y += random.randint(-5,5)
    slide(x,y)
    slide(call_x, call_y)
    py.PAUSE = 1
def slide(x_to, y_to, timer = 0.01):
    print("Starting slide(x_to, y_to):")
    time.sleep(random.uniform(0.0001, 0.01))
    py.PAUSE = 0.001
    x_from, y_from = py.position()
    x_dist = make_positive(x_to - x_from)
    y_dist = make_positive(y_to - y_from)
    divider = min([x_dist, y_dist])
    if x_dist%divider == 0:
        x_randomizer = False
    else:
        x_randomizer = True
    if y_dist%divider == 0:
        y_randomizer = False
    else:
        y_randomizer = True
    (current_pos_x, current_pos_y) = py.position()
    move_x = int(x_dist/divider)
    move_y = int(y_dist/divider)
    if move_x > 3:
        move_x = random.randint(1,3)
    if move_y >3:
        move_y = random.randint(1,3)
    if x_to == current_pos_x and y_to == current_pos_y:
        return
    else:
        if y_to < y_from:
            move_y *= -1
        if y_randomizer == True:
            move_y += random.randint(0,1)
        if x_to < x_from:
            move_x *= -1
        if x_randomizer == True:
            move_x += random.randint(0,1)
        move_x += x_from
        move_y += y_from
        py.moveTo(move_x, move_y, timer)
        time.sleep(timer/2)
        slide(x_to, y_to)
    py.PAUSE =1

def make_positive(number):
    print("Starting make_positive(number):")
    if number< 0:
        number *=-1
    if number == 0:
        number+=1
    return number
#start typing 
def start_typing(start_counter):
    print("Starting start_typing(start_counter):")
    if start_counter > 20:
        restart()
    print("Starting typing function")
    def text():
        print("Starting text():")
        def writer():
            print("Starting writer():")
            #type message
            write("Hello dear, good day.")
            py.press('enter')
            write("I would like to purchase some of your products in bulk quantity but i'll first like some samples to at least test the quality and see if it's up to standard with my customers.")
            #send message
            prod_counter = 0
            send_prod(prod_counter)
        time.sleep(3)
        def check_new(check_new_count):
            print("Starting check_new(check_new_count):")
            if check_new_count > 3:
                go_back()
            try:
                py.locateOnScreen('images/atexted.png')
                writer()
            except(py.ImageNotFoundException):
                try:
                    py.locateOnScreen('images/atexted2.png')
                    writer()
                except(py.ImageNotFoundException):
                    try:
                        py.locateOnScreen('images/atexted3.png')
                        writer()
                    except(py.ImageNotFoundException):
                        check_new_count +=1
                        check_new(check_new_count)
        check_new(0)




    try:
        locate_and_click('once', 'images/type.png')
        text()
            
    except(py.ImageNotFoundException):
        try:
            locate_and_click('once', 'images/type_full.png')
            text()
        except(py.ImageNotFoundException):
            start_counter += 1
            start_typing(start_counter)

#send prod
def send_prod(prod_count):
    print("Starting send_prod(prod_count):")
    send_counter = 0
    if prod_count > 10:
        send(send_counter) 
    try:
        locate_and_click('once', 'images/snd.png')
        send(send_counter)
    except(py.ImageNotFoundException):
        try:
            locate_and_click('once', 'images/snd2.png')
            send(send_counter)
        except(py.ImageNotFoundException):
            prod_count +=1
            send_prod(prod_count)


def send(main_send_counter):
    print("Starting send(main_send_counter):")
    def sender(send_count):
        print("Starting sender(send_count):")
        if send_count > 10:
            restart()
        print("Trying to send")
        try:
            locate_and_click('once', 'images/send.png')
        except(py.ImageNotFoundException):
            try:
                locate_and_click('once', 'images/send_full.png')
            except(py.ImageNotFoundException):
                try:
                    locate_and_click('once', 'images/send2.png')
                except(py.ImageNotFoundException):
                    try:
                        locate_and_click('once', 'images/send3.png')
                    except(py.ImageNotFoundException):
                        try:
                            locate_and_click('once', 'images/send4.png')
                        except(py.ImageNotFoundException):
                            send_count += 1
                            sender(send_count)
    sender(main_send_counter)
            #if send_count > 10:
                #Point(x=1239, y=1048)
             #   move_and_click(1239,1048,1)
    def new(message):
        print("Starting new(message):")
        write(message)
        call_slide(random.randint(-200,200), random.randint(-200, -800))
        time.sleep(random.randint(1,3))
        sender(0)
    new("Do you accept bank transfers?")
    new("If you would, please send your WhatsApp number or your WeChat ID.")
    new("I'm looking for a long term partner so i can get some business sorted out in China\nI am also very interested in buying from you.")    
    #working here
    print("Sent")
    go_back()


def go_back():
    print("Starting go_back():")
    i = 0
    call_slide(676, 42) #Point(x=676, y=42)
    while i <4:
        left_click()
        #py.hotkey('ctrlleft', 'shiftleft', '2')
        i += 1
        time.sleep(1)
    search_count = 0
    search(search_count)

#while True:
 #   print(py.position())
  #  time.sleep(3)
#while True:
 #   im = py.screenshot()
  #  print(im.getpixel((py.position())))
   # print(py.position())
    #time.sleep(3)0.1prep_stage()
captcha(0)
print(py.PAUSE)
#prep_stage()
#launch_chrome()

"""
Point(x=1127, y=964)
(2, 143, 255)
Point(x=819, y=966)
(5, 144, 255)
Point(x=668, y=858)
(0, 142, 255)


Point(x=657, y=495)
Point(x=1261, y=494)
Point(x=654, y=1072)
Point(x=1261, y=1067)
"""

