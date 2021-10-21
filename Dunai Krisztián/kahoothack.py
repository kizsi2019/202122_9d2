# Kahoot spammer by Krisztian
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
# Információk elkérése:
print("Kahoot spammer by Krisztian")
pin = input("Játék pin küdja")
name = input("Please enter a name:")
join = input("Please enter a amount of bots to join(Default is 50):")
tab = 0
nameb = str(name)
bot_num = 0
#Start chrome
print("Starting chrome...")
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
#If join feild is blank, then default is 50
if join=='':
    join=50
def namec():
    #Code for clarifying name
    global join, bot_num, nameb
    num=random.randint(1,999)*3
    if join=='1':
        nameb=name
        bot_num = bot_num + 1
    if int(join)>=2:
        if bot_num==join:
            print("Name generation completed")aimport random
import time
import kahootDefs as kDefs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

totalKahootBots = input('Kahoot Bots To Summon\n> ')
try:
    totalKahootBots = int(totalKahootBots)
    print()
except:
    print('Error, Unsupported Input. Default (3)\n')
    totalKahootBots = 3

kahootPin = ''
while type(kahootPin) != type(0):
    kahootPin = input('Kahoot Pin\n> ')
    try:
        kahootPin = int(kahootPin)
    except:
        print('\nUnsupported Input')

URL = 'https://www.kahoot.it/'


def switchTab(tabID):
    driver.switch_to.window(allTabs[tabID])


with open('usernames.txt', 'r') as file:
    usernameList = [line.replace('\n', '') for line in file]
    random.shuffle(usernameList)

# DRIVER OPTIONS
options = Options()
options.add_argument(
    "--incognito --headless --user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.3610"
)

# START DRIVER
driver = webdriver.Chrome(options=options)
driver.get(URL)

# OPEN WINDOWS
for _ in range(totalKahootBots - 1):
    driver.execute_script(f"window.open('{URL}');")
allTabs = driver.window_handles


class badPin(Exception):
    pass


print()

# Start Bots
try:
    # ENTER PIN
    for tabID in range(totalKahootBots):
        switchTab(tabID)
        driver.find_element_by_id('game-input').send_keys(kahootPin)
        driver.find_element_by_class_name(
            'enter-button__EnterButton-sc-1o9b9va-0').click()

        errorNotif = False

        if tabID == 0:
            try:
                time.sleep(1)

                timesTried = 0
                if timesTried < 5:
                    try:
                        driver.find_element_by_id('nickname')
                    except:
                        timesTried += 1
                        time.sleep(0.5)
            except:
                raise badPin

        print(f'BOT ID {tabID + 1}\t:: Setting Up...')

        time.sleep(1)
        try:
            driver.find_element_by_id('error-notification')
            errorNotif = True
            time.sleep(5)
        except:
            pass

        while errorNotif == True:
            try:
                driver.find_element_by_class_name(
                    'enter-button__EnterButton-sc-1o9b9va-0').click()
                time.sleep(2)
                driver.find_element_by_id('nickname')
                errorNotif = False
            except:
                print(
                    f'{" " * (len("BOT ID ")+len(str(tabID+1)))}\t:: Login Timeout... Retrying.'
                )
                time.sleep(5)

    print()

    # ENTER USERNAME
    botUsernames = []
    for tabID in range(totalKahootBots):
        switchTab(tabID)
        botUsernames.append(usernameList.pop()[:11])

        time.sleep(0.25)
        nicknameInputted = False

        while nicknameInputted == False:
            try:
                driver.find_element_by_id('nickname').send_keys(
                    botUsernames[tabID])
                driver.find_element_by_class_name(
                    'enter-button__EnterButton-sc-1o9b9va-0').click()
                nicknameInputted = True
            except:
                time.sleep(0.1)

        print(f'BOT ID {tabID + 1}\t:: {botUsernames[tabID]}\t\t>>\tJoined')

except badPin:
    print(f"Invalid Pin :: '{kahootPin}'")
    driver.quit()
    exit()

switchTab(0)
tempPAGE = driver.current_url
print()

tempScore, totalScore = [0 for _ in range(totalKahootBots)
                         ], [0 for _ in range(totalKahootBots)]

while True:
    if tempPAGE != driver.current_url:
        if driver.current_url == "https://kahoot.it/v2/gameblock":
            try:
                questionCounter = driver.find_element_by_class_name(
                    'top-bar__QuestionNumber-sc-186o9v8-2').text
            except:
                questionCounter = '/?/'

            for tabID in range(totalKahootBots):
                switchTab(tabID)
                viableAnswers = kDefs.findViableAnswers(driver)
                kDefs.pickAnswer(viableAnswers)

                try:
                    driver.find_element_by_class_name(
                        'quiz-board__SubmitButton-sc-1vv00zg-4').click()
                except:
                    pass

                print(
                    f'BOT ID {tabID + 1}\t:: {botUsernames[tabID]}\t\t>>\tQ {questionCounter} >> Answered.'
                )

            switchTab(0)
            tempPAGE = driver.current_url
            print()

        elif driver.current_url == "https://kahoot.it/v2/answer/result":
            for tabID in range(totalKahootBots):
                switchTab(tabID)
                time.sleep(0.25)

                try:
                    totalScore[tabID] = int(
                        driver.find_element_by_class_name(
                            'bottom-bar__Score-sc-1bibjvm-2').text)
                    scoreDiff = totalScore[tabID] - tempScore[tabID]
                except:
                    totalScore[tabID] = '/?/'
                    scoreDiff = '/?/'

                print(
                    f'BOT ID {tabID + 1}\t:: {botUsernames[tabID]}\t\t>>\tCurrent Score >> {totalScore[tabID]} (+{scoreDiff})'
                )
                tempScore[tabID] = totalScore[tabID]

            switchTab(0)
            tempPAGE = driver.current_url
            print()

        elif driver.current_url == "https://kahoot.it/v2/ranking":
            print(f'Game Finshed. Closing All Bots.')
            driver.quit()
            break

input()

        nameb=(name + '.' + str(num))
        bot_num = bot_num + 1
def bot():
    global nameb, driver, tab
    if bot_num==1:
        print("No new window necessary")
    elif bot_num >=2:
        print("Opening new window...")
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[tab])
    print("Navigating to Kahoot...")
    #Navigate to kahoot.com
    driver.get("https://kahoot.it/")
    #Wait untill element is available
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'inputSession')))
    #Finding input box
    inputb = driver.find_element_by_id('inputSession')
    print("Joining game...")
    #Inputting pin
    inputb.send_keys(pin)
    inputb.submit()
    #Entering name
    element = wait.until(EC.element_to_be_clickable((By.ID, 'username')))
    gname = driver.find_element_by_id('username')
    namec()
    gname.send_keys(nameb)
    gname.submit()
    #Checking login
    print("Checking if login was succesfull...")
    try:
       content = driver.find_element_by_class_name('ng-binding') 
    except:
        print("Error checking page:\nId could have changed, or connection could have dropped.")
        x=input("Press any key to exit...")
    print("Success!")
    print("Bot [" + bot_num + "] is now in the game ;)")
    tab = tab + 1
#Code for running a set amoun of times
for x in range(int(join)):
    bot()