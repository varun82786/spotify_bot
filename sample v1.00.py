from select import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import random as random
import time
import pandas as pd
#============================================================================
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#important links

csv_file = ""
driver_path = "S:\project spotify\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(driver_path)

def signup(email,password,name):
    signuplink = "https://www.spotify.com/in-en/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F"
    driver.get(signuplink)
   
    month_lis = ["January", "March", "May", "July",
                 "August", "October", "November", "December"]
    
    genders = ['//*[@id = "__next"]/main/div/div/form/fieldset/div/div[1]/label',
               '//*[@id = "__next"]/main/div/div/form/fieldset/div/div[2]/label']
    year=random.randint(1990,2004)
    day=random.randint(1,31)
    month=random.choice(month_lis)
    gender=random.choice(genders)
    #finding the blocks
    email_block = driver.find_element_by_id("email")
    confirm_email_block=driver.find_element_by_id("confirm")
    password_block = driver.find_element_by_id("password")
    displayname_block=driver.find_element_by_id("displayname")
    year_block=driver.find_element_by_id("year")
    #month dropdown
    month_block = Select(driver.find_element_by_id('month'))
    day_block=driver.find_element_by_id("day")
    #gender_block=driver.find_element_by_id(gender)
        
    #filling the data
    email_block.send_keys(email)
    confirm_email_block.send_keys(email)
    password_block.send_keys(password)
    displayname_block.send_keys(name)
    year_block.send_keys(year)
    # select by visible text
    month_block.select_by_visible_text(month) 
    day_block.send_keys(day)
    #gender_block.click()
    time.sleep(10)
    #driver.find_element_by_xpath('/html/body/div[1]/main/div/div/form/fieldset/div/div[1]/input').click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,gender ))).click()
    
    """WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/main/div/div/form/div[6]/div/label '))).click()"""
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/main/div/div/form/div[7]/div/label  '))).click()
    
    
    
    #time.sleep(10)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/main/div/div/form/div[9]/div/button/div[1]  '))).click()
    
    my_channel = "https://open.spotify.com/user/dcxuy5q4jfrkyrgrq8v3xencg"
    time.sleep(3)
    driver.get(my_channel)
    #time.sleep(10)
    #//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[3]/div/button[1]
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[3]/div/button[1]  '))).click()
    #time.sleep(10)
    
    #logout 
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/button/figure/div/div'))).click()

    #//*[@id="context-menu"]/div/ul/li[4]/button

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="context-menu"]/div/ul/li[4]/button'))).click()


""""
name = "ramdev"+random.choice(list(map(chr, range(97, 123)))) + \
    random.choice(list(map(chr, range(97, 123)))) + \
    random.choice(list(map(chr, range(97, 123))))
domain = "@gmail.com"
email = name+domain
print(email)
signup(email,"ratQ129#2!@","Ram dev")"""

"""
ramdevbyd@gmail.com
ramdevgwo@gmail.com
"""

people_data = [
    ['GIRIDHAR', 'giridhar828@gmail.com', 'ohmsi.Y4'], ['SWAPNA', 'swapnabtech5@gmail.com',
                                                        'RP:i)0RZ'], ['Vineeth', 'vineethvinnu9948@gmail.com', 'FGe@ak4N'],
    ['VENKATESH', 'Venkyallavarapu123@gmail.com', '<V#kp90i'], ['SOUNDARYA',
                                                                'soundaryabadri@gmail.com', 'g%y9ADGA'], ['Thasleem', 'thasleemshaik1999@gmail.com', 'urqvX:K4'],
    ['ALLADA SATISH', 'satish.allada123@gmail.com', 'y@SI.O3x'], ['BALAGA LOKESH',
                                                                  'balagalokesh82@gmail.com', '#JDgb<W1'], ['BANDARU RAJ KUMAR', 'raju.knr2@gmail.com', ':G%1efHS'],
    ['BODDEPALLI PAVAN KUMAR', 'bpavankumar1998@gmail.com', 'zBa>Pp3B'], ['BOMMALI RAMESH',
                                                                          'rameshbommali123@gmail.com', 'Y7Ix%/Z?'], ['CHAPPA KIRAN KUMAR', 'kirankumarchappa1999@gmail.com', 'BU52VjT~'],
    ['DAGULAPALLI PRAVEEN', 'dagulapalli.praveen@gmail.com', 'jaG@Ua34'], ['DUGANA SHYAM PRASAD',
                                                                           'shyamsmart155@gmail.com', '@tEW1<37'], ['GANGIDESI SAI TEJASWINI', 'saitejaswi58@gmail.com', 'Un4c#S:.']
]
print(len(people_data))
invalid_data=[]

for data in people_data:
    try:
        email=data[1]
        password=data[2]
        name=data[0]
        signup(email,password,name)
        
    except:
        
        
        invalid_data.append(data)
        
        continue
    

        
        
        
        
#[['ANGANI', 'durgaprasadsiva666@gmail.com', '(QAx0nj='], ['Sai', 'sailakshmi985@gmail.com', 'TQ=uor5d'], ['SWAROOPA', 'swaroopabadipati@gmail.com', '5ruE>ow/'], ['BUDUMURU ', 'syamsundar.1307@gmail.com ', 'Pw@Okz1|'], ['Bunga', 'saiharishbunga04@gmail.com', '#/4N#z|c'], ['DURGA', 'prasaddnp97@gmail.com', 'p1#OJq)J'], ['RAGHAVA', 'Raghavgopasina@outlook.com', '1CIud*|G'], ['AJAY ', 'ajayshankar969@gmail.com', 'Y%4h0X@='], ['Jarugulla', 'ramanajaragulla@gmail.com ', '4hvWVaB|'], ['KANCHARLA', 'durgakancharla24@gmail.com', '$1x0e5BD'], ['UMA SAI', 'dp1317056.1@gmail.com', '92|y1GaM'], ['Maddela', 'maddela.sindhuja2000@gmail.com', '4~A~Nf|Q'], ['Vamsi Avinash', 'Vamsimendem113@gmail.com', 'RWm*)4TB'], ['KUSHMA', 'mkushma123mkushma@gmail.com ', '8Sxh=Iz:'], ['BLESSY', 'blessy984@gmail.com', 'MzI::b16'], ['Usha', 'ushashamily@gmail.com', '=/Kw(s5w'], ['Kavitha', 'kavithabetech@gmail.com', 'rf~V~f9%'], ['Sri Satya', 'satyasreepothala114@gmail.com', 'T=dM6Mcn'], ['Ramya', 'ramyarevu3@gmail.com', 'Q<0@fu2V'], ['Afroz', 'skafroz188@gmail.com', 'q@rnF=V0'], ['SURU', 'priyanka98.suru@gmail.com', 'v=hjMW3U'], ['Sweta ', 'swetasingh6543@gmail.com', '0(QM$v.u'], ['Vandana', 'tiruveedhulavandana@gmail.com', 'b)m(zn9Y'], ['URLANA', 'upenderurlana@gmail.com', 'Gwx4<7AO'], ['Uma', 'umasai3628@gmail.com', '@rBf~7rV'], ['DEVI', 'devisaipriya1@gmail.com', 'IDWZ%01f'], ['MADHAVI', 'mavimouni@gmail.com', 'b*k7BBk5'], ['Nandini', 'Jydnhhepsi@gmail.com', 'Q$0c1?>F'], ['YOGITHA', 'yogithabtech@gmail.com', '8d(kE|=<'], ['Dharani', 'beenadharani@gmail.com', 'JQI.zO5J'], ['SRIDEVI', 'sridevibillakurthi@gmail.com', 'tHeK/)F1'], ['Poojitha', 'chitturipoojitha1@gmail.com', '~FT*sA34'], ['Prathyusha', 'dandugulaprathyusha19@gmail.com', 'B~V5dFi('], ['Krishnaveni', 'krishnavenigedadeesi@gmail.com', 'QDGxF)W4'], ['NEELESH', 'neeleshnnn0512@gmail.com', 'PN5M%WCd'], ['ROHIT', 'rohitkancherla1019@gmail.com', '1::<.aJ|'], ['Bhagyalaxmi', 'kalivarapubhagya@gmail.com', 'G9<*HwKo'], ['BHAVYA', 'kanaparti.bhavya7699@gmail.com', '(8KpYf=E'], ['Surya Sri', 'harshasuryasri@gmail.com', 'K#.x4Gh~'], ['SAI VENKATA ROHITH', 'rohith.stu10@gmail.com', '5PIX<Pep'], ['LAVANYA', 'lavanyamummunuri@gmail.com', '(<y6UdBj'], ['Lavanya', 'nandalavanya123@gmail.com', 'WzZ$v3/K'], ['Madhuri', 'Madhusrinandigam@gmail.com', 'TsdP0C#d'], ['Chakradhar', 'chakradharpalakonda1999@gmail.com', '%D>N0g<N'], ['Jayasree', 'jayasreepalaparthi45@gmail.com', '7s1m#QIr'], ['GOWTHAM', 'parregowtham@gmail.com', 'PzW/Iqd6'], ['venkat naga', 'pasamindrani.eee@gmail.com', 'a8@IHvg2'], ['SATYAVANI', 'Satyavani.ponnana@gmail.com', 'u:6iGnmr'], ['GAYATRI', 'gayatri.janasri@gmail.com', 'S>uQz5|>'], ['GIRIDHAR', 'giridhar828@gmail.com', 'ohmsi.Y4'], ['Jhansi', 'jhansiramakuri456@gmail.com', '%7#jpHK1'], ['SWAPNA', 'swapnabtech5@gmail.com', 'RP:i)0RZ'], ['Vineeth', 'vineethvinnu9948@gmail.com', 'FGe@ak4N'], ['NAVEEN KUMAR', 'naveenee5499@gmail.com', 'MKo1f8Q|'], ['VENKATESH', 'Venkyallavarapu123@gmail.com', '<V#kp90i'], ['CHAITANYA', 'chaitu1897@gmail.com', 'X)S~dcI0'], ['SOUNDARYA', 'soundaryabadri@gmail.com', 'g%y9ADGA'], ['Thasleem', 'thasleemshaik1999@gmail.com', 'urqvX:K4'], ['ANIMIREDDY VEERENDRA', 'veerendraanimireddy@gmail.com', 'Jnp|B6U>'], ['ALLADA SATISH', 'satish.allada123@gmail.com', 'y@SI.O3x'], ['ATHOTA BASANTH', 'basanth7425@gmail.com', 'J(H1Nvvy'], ['BALAGA LOKESH', 'balagalokesh82@gmail.com', '#JDgb<W1'], ['BALLA KIRAN KUMAR', 'chinnualone7@gmail.com', '$C(fx9cr'], ['BANDARU RAJ KUMAR', 'raju.knr2@gmail.com', ':G%1efHS'], ['BENDALAM BHARGAVI', 'bendalambhargavi833@gmail.com', '$xZ%FWq3'], ['BODDEPALLI PAVAN KUMAR', 'bpavankumar1998@gmail.com', 'zBa>Pp3B'], ['BOMMALI RAMESH', 'rameshbommali123@gmail.com', 'Y7Ix%/Z?'], ['BORIGI SAI SIVA PRASAD', 'saisivaprasadborigi1997@gmail.com', '<e/~R4cp'], ['CHAPPA KIRAN KUMAR', 'kirankumarchappa1999@gmail.com', 'BU52VjT~'], ['DAGULAPALLI PRAVEEN', 'dagulapalli.praveen@gmail.com', 'jaG@Ua34'], ['DEKKA ARJUNAMMA', 'arjunadaddy@gmail.com', 'cn5:?kOp'], ['DUGANA SHYAM PRASAD', 'shyamsmart155@gmail.com', '@tEW1<37'], ['GALLA KARISHMA', 'gallakarishma78@gmail.com', ':22F0xP>'], ['GANGIDESI SAI TEJASWINI', 'saitejaswi58@gmail.com', 'Un4c#S:.'], ['GUNIPALLI VAMSI KRISHNA', 'vamsygunipalli143@gmail.com', '8k4#VTkK'], ['HAREESH GEDELA', 'gedelahareesh078@gmail.com', 'gT6d)bmo'], ['JAMINA PRASANNA KUMAR', 'kumarjamina123@gmail.com', 'T0r%D9Wd'], ['JONNADA PRASAD', 'jpky143@gmail.com', 'gm%6*VS6'], ['KADALI BALAJI', 'kadalibalaji45@gmail.com', '4%H<tBVn'], ['KARTHU SASHANK NAIDU', 'sashankkarthu1682@gmail.com', 'gtI@J%9o'], ['KATTA BHARGAV', 'kbhargav426@gmail.com', 'r0vXf%Nx'], ['KONATHAM HARSHINI', 'harishinichinni1@gmail.com', 'MxFBt:K5'], ['KUNCHALA RAJU', 'kunchalaraju965@gmail.com', '=oz7Y?zo'], ['MANDADAPU SANDEEP', 'sandeepmandadapu270@gmail.com', 'U18B*qRW'], ['MANDALA PRAVEEN', 'mandalapraveen777@gmail.com', '>Oa1TXmV'], ['MANGI RAJKUMAR', 'mangirajkumar2@gmail.com', 'eVQ=Q8Y4'], ['MATCHA DEEPTHI', 'deepdiv98@gmail.com', 'v4Q#GR)('], ['METTA ARAVIND', 'aravindkumar.m9@gmail.com', 'B4:scz)#'], ['MUNASA NANI BABU', 'nanimunasa0108@gmail.com', 'zJz8k7.G'], ['NETALA ARUN RAJ', 'netalasarun@gmail.com', ':m=p3#XT'], ['NAGINENI LAKSHMI LALITHA', 'lalithanagineni74@gmail.com', '@>uhRBv3'], ['NAGIREDDY DURGA PRASAD', 'dugaprasadhockey@gmail.co', 'fV/j9(n?'], ['PAILA ARAVIND', 'pailaaravind1998@gmail.com', '3/26Fz:='], ['PATHINA BHARGAV', 'bhargavpathina962@gmail.com', 'B7>bBsf)'], ['PENDEM KALYAN KUMAR', 'pendamkalyankumar@gmail.com', 'fMu:z#4v'], ['SABBAVARAPU ANIL KUMAR', 'anil.sak4694@gmail.com', '#H.C|jS7'], ['SABBBAVARAPU BHARGAVA', 'bhargavchandu1999@gmail.com', 'wxO%2W<g'], ['SANDURU BHARATH KUMAR', 'bharath.sanduru171@gmail.com', 'm@wJtPP7'], ['SHAIK CHANDBASHA', 'chandbashay1649@gmail.com', 'V*($2r0b'], ['SHAIK MAHABOOBHUSSIAN', 'shaikhussian786123@gmail.com', '/6:Y4*jK'], ['SHAIK MEERAVALI', 'meeravalishaik453@gmail.com', 'Rk4x:G6j'], ['SIVAKOTI.HEMASREE', 'hs7sivakoti@gmail.com', '::iyem8M'], ['THALATHOTI SOWJANYA', 'sowjanya12101999@gmail.com', '|xYQNik1'], ['THUMBETI SHANMUKHA SRINIVAS', 'shanmuksrinivas341@gmail.com', 'SOYI0U*e'], ['TURPATI SARADHI', 'pardhuvishal@gmail.com', 'eN6iYq@i'], ['YAJJALA CHADRA SEKHAR', 'sekharchandryajjala@gmail.com', '*z/I4g=N'], ['YENNI NAGABHUSHAN', 'yenninagabhushan@gmail.com', '9XZk>?Pf'], ['PAIDI GANGADHARA RAO', 'paidigangadhararaom035@gmail.com', '$M5adA6y'], ['VINNAKOTA JYOTHIRMY', 'jyothivinnakota99@gmail.com', 'EcU2F6.3'], ['Gopi Krishna', 'gopianaparthi1@gmail.com', 'GF3?g5TK'], ['Babi', 'adireddibabi02@gmail.com', '1Va0=?U.'], ['Tarun', 'botsatarun446@gmail.com', 'T#Cpv:f5'], ['Ayyappareddy', 'ayyappachagamreddy7799@gmail.com', 'zb2UR1|V'], ['Mary', 'Marybabu13121@gmail.com', '3YJuN#Q2'], ['Chinthala', 'deepikadeepu58007@gmail.com', 'dm|7VSEg'], ['Blessy', 'blessythanmayi12345@gmail.com', 'Z6Rg<Vd)'], ['Kranthi', 'kranthikiran276@gmail.com', '1uu>J@p|'], ['Sudheer', 'darsisudheer3@gmail.com', '/2%frZVU'], ['Suraj', 'surajdevabsa@gmail.com', 'MF*@4gbc'], ['Archana', 'archana050998@gmail.com', 'Hu#t?BZ2'], ['YASWANTH', 'gyaswanthsriram18@gmail.com', 'n.3tocVS'], ['Subbaraogella rao', 'subbaraogella@gmail.com', 'OHh@/7I8'], ['Manikanta', 'mani.godi789@gmail.com', ')S77IoG1'], ['Anil', 'gollapallianilkumar1999@gmail.com', '4$x.*4vY'], ['MANIKANTA', 'indalamanikanta007@gmail.com', 'b/7.XHjG'], ['Sita', 'sitalucky2@gmail.com', '>Wu1?ODz'], ['Karlapudi', 'donihelena123@gmail.com', '(jQR0i|h'], ['Sai', 'ksrinivasku@gmail.com', ':qf)2bFS'], ['Kodamala', 'jaswanthjksv@gmail.com', '>BiE9:qs'], ['SAMUEL', 'samueldev99@gmail.com', 'SASh?>j9'], ['Naveen', 'naveenkumar.labhana@gmail.com', '1o$WYi$j'], ['Gowtham', 'mallavarapugowtham33296@gmail.com', 'oYhNGJ)6'], ['Yeswanth', 'yeswanthtejamannam@gmail.com', 'i.Y32KRj'], ['Hymambika', 'manyamhymambika6@gmail.com', 'ijhH8h*4'], ['Sravani', 'sravanimedam99@gmail.com', 'ZKV?z3Yj'], ['Mekala', 'akhil.preetham444@gmail.com', 'f7:O*G3o'], ['Hemanth', 'hemanthmunnangi70130@gmail.com', 's1m@>Q)<'], ['Pavan', 'pavankumarneeluri.111@gmail.com', '4ptu8vG*'], ['VARDHINI', 'pillavardhini9246@gmail.com', 'Zbi4~/0R'], ['PAIDI', 'bhargavipydi123@gmail.com', 'Yz6p#n~1'], ['JOSEPH', 'jrka0328@gmail.com', '7:@34WwT'], ['PURNACHANDRA', 'purnachandra.p715@gmail.com', 'Dx72*AV@'], ['Pilli', 'pilli.deepak789@gmail.com', '6fX>uK|g'], ['JAYA BHAGYA', 'bhagyakumari02@gmail.com', '5#I(uuM2'], ['Ponnpalli', 'mallikarjunasai174@gmail.com', '*xj0UcaZ'], ['Siva', 'pudisiva3243@gmail.com', 'f*/bhT3y'], ['RAYASAM', 'Vamsikrishnamohan1996@gmail.com', '#~z6YNKH'], ['Sharath', 'sharathkumarbfbf@gmail.com', 'kaz(r)A6'], ['SIVA', 'savalamsiva99122@gmail.com', 'bPa|PuR6'], ['FAMIDA', 'famidashaik001@gmail.com', 'JK1q#bBw'], ['SHAIK', 'ibrahimshaik838@gmail.com', 'x.T?P2k|'], ['Mastani', 'javeri.sk910@gmail.com', 'h=g/UCo0'], ['Siram', 'realkrish2@gmail.com', 'zxx?%Z9.'], ['VINAY', 'vinay.siraparapu@gmail.com', 'fH*hmz3O'], ['BHANU', 'bhanusirasam2018@gmail.com', 'E%?HiI~3'], ['UMAR JEE', 'syedumar123r@gmail.com', 'FiM6h7V<'], ['TADIMALLA', 'seshasai.tadimalla@gmail.com', 'g~@%0W3u'], ['Pravallika', 'pravallikavungarala.r@gmail.com', 'IH=6>sR9'], ['VUTUKURU', 'vutukuruchakradhar639@gmail.com', '~C26t|=s'], ['Jayanth', 'Jayanth krishna', 'erK9YB*1'], ['Harsha', 'harshavardhan14008c010@gmail.com', 'ugB)1%1='], ['DEVENDRA', 'gudiyadevendra28@gmail.com', '2a|~<TUx'], ['sri aishwarya', 'sriaishwaryanemalipuri1@gmail.com', '>/g9%2Pt'], ['P.Venkata Ramana', 'puttavenkataramana38@gmail.com', ')IJ2Wb?j'], ['Sai', 'saisadasivuni9@gmail.com', 'M|%iP1mc'], ['Dilip kumar', 'palladilip040@gmail.com', 'cA4%TeS%'], ['Aravind', 'arvind.190798@gmail.com', '4gt|O@C.'], ['ANNAPUREDDY', 'mani95514340@gmail.com', '4Kwqk6~z'], ['Sushma bai', 'sushmabanavath299@gmail.com ', 'Jww8R)FM'], ['Deepika', 'deepika018213@gmail.com', '.YW<bx52'], ['Rama krishna', 'brl32132@gmail.com', 'NYSRo4n$'], ['Bhavara', 'santosh.b1431@gmail.com', 'vDSg<2Wj'], ['Naga Sai ', 'jyothibitra123@gmail.com', '$/yE*M2y'], ['JOHN PAUL', 'johnpaulb007@gmail.com', '~gR<Uai0'], ['Jeevan', 'jeevansunnyhaf@gmail.com', '1b4XAk*('], ['Naveen ', 'Naveen420go@gmail.com', 'gb/FkR5q'], ['Prasanth', 'prasanthdasari12@gmail.com', '~9zCymcj'], ['GANTA', 'Prudviganta2222@gmail.com', 'D7.iwT.p'], ['VENKATA SURYA BHARGAV REDDY', 'gvsbhargavreddy@gmail.com', '4?fg5VdO'], ['KALLAGUNTA', 'kallaguntakirankumar@gmail.com', 'im?2TqR.'], ['KANCHARLA', 'kancharla3216@gmail.com', 'c$|bBGI0'], ['Teja', 'Tejakanna4@gmail.com', 'I?a6=sE>'], ['Mohan Reddy', 'karrimohanreddy@gmail.com', 'w2jJ<fK*'], ['KILAPARTHI KIRAN', 'kirankilaparthi@gmail.com', '?es9##TO'], ['Killamsetty', 'vkrishna1998@gmail.com', 'fj/0Y:T1'], ['Kolla', 'jhansikolla7@gmail.com', '>~eb5Z>7'], ['LAXMI NARAYANA AYYAPPA', 'ayyappakolla38558@gmail.com', '<i8mVBEK'], ['Kumpati .sai', 'Chandrikasai47@gmail.com', 'tT5H:Su<'], ['LOKARAPU', 'dileeplokarapu@gmail.com', 'vv9ZH:rc'], ['Pavani', 'pavaninaidu.m@gmail.com', '|Wr6<.|6'], ['MULLANGI', 'mullangigiri22@gmail.com', '7orHE#a1'], ['Divya', 'divyamuppana15@gmail.com', 'T4dEao:3'], ['Narendra ', 'nukanarendrakumar0@gmail.com ', 'OW(MHv82'], ['Padidhi ', 'bhavanipadidhi@gmail.com ', 'n5.R*7s$'], ['Padisetti', 'nikeshpadisetti1999@gmail.com ', '9qg8O?3P'], ['PEETHALA', 'peethalamanoj37@gmail.com', 'ES=P7>oP'], ['Revathi ', 'revathip008@gmail.com', '$e9).AJN'], ['PUNYALA', 'bhavanilakshmi115@gmail.com', '~@2WczY9'], ['Sushmasri', 'snehitha641@gmail.com ', 'uM%k3nCU'], ['Vamsi Krishna', 'reddyvamsi150@gmail.com', 'hp>5T6NS'], ['GAYATRI', 'gayatrimp1@gmail.com', 'r5.:4V(i'], ['Sandhyarani', 'sandhyaraniasula88@gmail.com', '<p:Ev8.K'], ['Reshma', 'shaikreshma912@gmail.com', '71@x6dpF'], ['SHIVAM ', 'shivamsoni4475@gmail.com', '#D%6q.S*'], ['Pavan Chand', 'spavanchand@gmail.com', '3gWF%Jbh'], ['Suresh', 'sureshtadivalasa178@gmail.com', 'XPP%1O>r'], ['ROHINI', 'tainanarohini98@gmail.com', 'RN0em1>@'], ['TEJASWI', 'tejuch.4149@gmail.com', 'X.fpMpw5'], ['Navya', 'navyalikitha9@gmailcom', '|g31NsX)'], ['Jagadesh', 'ju071998@gmail.com', '2?zCpxus'], ['Lakshmi bai', 'lakshmibtech22@gmail.com', '$Qk$36n3'], ['Sonali', 'sonalivarma8899@gmail.com ', 'qQ|2$aQb'], ['Krishna sai', 'saik19199@gmail.com', 'I|eGqd9('], ['cheedirala', 'hemapravallika61@gmail.com', '1bP=Xb~s'], ['Sowmya Singh ', 'Sowmya1999singh@gmail.com', 'Be%#?7(:'], ['Saida Rao', 'saidamende60@gmail.com', 'm9F<9rNH']]