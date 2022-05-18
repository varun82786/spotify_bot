file = open('S:/project spotify/spotify_bot/txt.txt', 'r')
lines = file.readlines()
s=""
for line in lines:
    s=s+","+line.strip()
    
print(s)

d=[['GUNIPALLI VAMSI KRISHNA', 'vamsygunipalli143@gmail.com', '8k4#VTkK'],['JAMINA PRASANNA KUMAR', 'kumarjamina123@gmail.com', 'T0r%D9Wd'],['KADALI BALAJI', 'kadalibalaji45@gmail.com', '4%H<tBVn'],
   ['KATTA BHARGAV', 'kbhargav426@gmail.com', 'r0vXf%Nx'],['KUNCHALA RAJU', 'kunchalaraju965@gmail.com', '=oz7Y?zo'],['MANDADAPU SANDEEP', 'sandeepmandadapu270@gmail.com', 'U18B*qRW'],
   ['MANGI RAJKUMAR', 'mangirajkumar2@gmail.com', 'eVQ=Q8Y4'],['MATCHA DEEPTHI', 'deepdiv98@gmail.com', 'v4Q#GR)('],['METTA ARAVIND', 'aravindkumar.m9@gmail.com', 'B4:scz)#'],
   ['NETALA ARUN RAJ', 'netalasarun@gmail.com', ':m=p3#XT'],['NAGIREDDY DURGA PRASAD','dugaprasadhockey@gmail.co', 'fV/j9(n?'],['PATHINA BHARGAV', 'bhargavpathina962@gmail.com', 'B7>bBsf)'],
   ['SABBAVARAPU ANIL KUMAR', 'anil.sak4694@gmail.com', '#H.C|jS7'],['SABBBAVARAPU BHARGAVA', 'bhargavchandu1999@gmail.com', 'wxO%2W<g'],['SANDURU BHARATH KUMAR', 'bharath.sanduru171@gmail.com', 'm@wJtPP7'],
   ['SHAIK MAHABOOBHUSSIAN', 'shaikhussian786123@gmail.com', '/6:Y4*jK'],['SHAIK MEERAVALI', 'meeravalishaik453@gmail.com', 'Rk4x:G6j'],['SIVAKOTI.HEMASREE', 'hs7sivakoti@gmail.com', '::iyem8M'],
   ['THUMBETI SHANMUKHA SRINIVAS','shanmuksrinivas341@gmail.com', 'SOYI0U*e'],['YAJJALA CHADRA SEKHAR', 'sekharchandryajjala@gmail.com', '*z/I4g=N'],['PAIDI GANGADHARA RAO', 'paidigangadhararaom035@gmail.com', '$M5adA6y'],
   ['VINNAKOTA JYOTHIRMY', 'jyothivinnakota99@gmail.com', 'EcU2F6.3'],['Gopi Krishna', 'gopianaparthi1@gmail.com', 'GF3?g5TK'],['Tarun', 'botsatarun446@gmail.com', 'T#Cpv:f5'],['Ayyappareddy', 'ayyappachagamreddy7799@gmail.com', 'zb2UR1|V'],
   ['Chinthala', 'deepikadeepu58007@gmail.com', 'dm|7VSEg'],['Kranthi', 'kranthikiran276@gmail.com', '1uu>J@p|'],['Suraj', 'surajdevabsa@gmail.com', 'MF*@4gbc'],['YASWANTH', 'gyaswanthsriram18@gmail.com', 'n.3tocVS'],
   ['Manikanta', 'mani.godi789@gmail.com', ')S77IoG1'],['MANIKANTA', 'indalamanikanta007@gmail.com', 'b/7.XHjG'],['Karlapudi', 'donihelena123@gmail.com', '(jQR0i|h'],['Kodamala', 'jaswanthjksv@gmail.com', '>BiE9:qs'],
   ['SAMUEL', 'samueldev99@gmail.com', 'SASh?>j9'],['Gowtham', 'mallavarapugowtham33296@gmail.com', 'oYhNGJ)6'],['Yeswanth', 'yeswanthtejamannam@gmail.com', 'i.Y32KRj'],['Sravani', 'sravanimedam99@gmail.com', 'ZKV?z3Yj'],
   ['Hemanth', 'hemanthmunnangi70130@gmail.com', 's1m@>Q)<'],['Pavan', 'pavankumarneeluri.111@gmail.com', '4ptu8vG*'],['PAIDI', 'bhargavipydi123@gmail.com', 'Yz6p#n~1'],['JOSEPH', 'jrka0328@gmail.com', '7:@34WwT'],
   ['PURNACHANDRA', 'purnachandra.p715@gmail.com', 'Dx72*AV@'],['JAYA BHAGYA', 'bhagyakumari02@gmail.com', '5#I(uuM2'],['Siva', 'pudisiva3243@gmail.com', 'f*/bhT3y'],['RAYASAM', 'Vamsikrishnamohan1996@gmail.com', '#~z6YNKH'],
   ['SIVA', 'savalamsiva99122@gmail.com', 'bPa|PuR6'],['SHAIK', 'ibrahimshaik838@gmail.com', 'x.T?P2k|'],['Siram', 'realkrish2@gmail.com', 'zxx?%Z9.'],['BHANU', 'bhanusirasam2018@gmail.com', 'E%?HiI~3'],['UMAR JEE', 'syedumar123r@gmail.com', 'FiM6h7V<'],
   ['TADIMALLA', 'seshasai.tadimalla@gmail.com', 'g~@%0W3u'],['Pravallika', 'pravallikavungarala.r@gmail.com', 'IH=6>sR9'],['VUTUKURU', 'vutukuruchakradhar639@gmail.com', '~C26t|=s'],['Jayanth', 'Jayanth krishna', 'erK9YB*1'],
   ['Harsha', 'harshavardhan14008c010@gmail.com', 'ugB)1%1='],['DEVENDRA', 'gudiyadevendra28@gmail.com', '2a|~<TUx'],['sri aishwarya', 'sriaishwaryanemalipuri1@gmail.com', '>/g9%2Pt'],['P.Venkata Ramana', 'puttavenkataramana38@gmail.com', ')IJ2Wb?j'],
   ['Sai', 'saisadasivuni9@gmail.com', 'M|%iP1mc'],['Dilip kumar', 'palladilip040@gmail.com', 'cA4%TeS%'],['Aravind', 'arvind.190798@gmail.com', '4gt|O@C.'],['ANNAPUREDDY', 'mani95514340@gmail.com', '4Kwqk6~z'],['Sushma bai', 'sushmabanavath299@gmail.com ', 'Jww8R)FM'],
   ['Deepika', 'deepika018213@gmail.com', '.YW<bx52'],['Rama krishna', 'brl32132@gmail.com', 'NYSRo4n$'],['Bhavara', 'santosh.b1431@gmail.com', 'vDSg<2Wj'],['Naga Sai ', 'jyothibitra123@gmail.com', '$/yE*M2y'],['JOHN PAUL', 'johnpaulb007@gmail.com', '~gR<Uai0'],
   ['Jeevan', 'jeevansunnyhaf@gmail.com', '1b4XAk*('],['Naveen ', 'Naveen420go@gmail.com', 'gb/FkR5q'],['Prasanth', 'prasanthdasari12@gmail.com', '~9zCymcj'],['GANTA', 'Prudviganta2222@gmail.com', 'D7.iwT.p'],['VENKATA SURYA BHARGAV REDDY','gvsbhargavreddy@gmail.com', '4?fg5VdO'],
   ['KALLAGUNTA', 'kallaguntakirankumar@gmail.com', 'im?2TqR.'],['KANCHARLA', 'kancharla3216@gmail.com', 'c$|bBGI0'],['Teja', 'Tejakanna4@gmail.com', 'I?a6=sE>'],['Mohan Reddy', 'karrimohanreddy@gmail.com', 'w2jJ<fK*'],['KILAPARTHI KIRAN', 'kirankilaparthi@gmail.com', '?es9##TO'],
   ['Killamsetty', 'vkrishna1998@gmail.com', 'fj/0Y:T1'],['Kolla', 'jhansikolla7@gmail.com', '>~eb5Z>7'],['LAXMI NARAYANA AYYAPPA', 'ayyappakolla38558@gmail.com', '<i8mVBEK'],['Kumpati .sai', 'Chandrikasai47@gmail.com', 'tT5H:Su<'],['LOKARAPU', 'dileeplokarapu@gmail.com', 'vv9ZH:rc'],['Pavani', 'pavaninaidu.m@gmail.com', '|Wr6<.|6'],
   ['MULLANGI', 'mullangigiri22@gmail.com', '7orHE#a1'],['Divya', 'divyamuppana15@gmail.com', 'T4dEao:3'],['Narendra ', 'nukanarendrakumar0@gmail.com ', 'OW(MHv82'],['Padidhi ', 'bhavanipadidhi@gmail.com ', 'n5.R*7s$'],['Padisetti', 'nikeshpadisetti1999@gmail.com ', '9qg8O?3P'],['PEETHALA', 'peethalamanoj37@gmail.com', 'ES=P7>oP'],
   ['Revathi ', 'revathip008@gmail.com', '$e9).AJN'],['PUNYALA', 'bhavanilakshmi115@gmail.com', '~@2WczY9'],['Sushmasri', 'snehitha641@gmail.com ', 'uM%k3nCU'],['Vamsi Krishna', 'reddyvamsi150@gmail.com', 'hp>5T6NS'],['GAYATRI', 'gayatrimp1@gmail.com', 'r5.:4V(i'],['Sandhyarani', 'sandhyaraniasula88@gmail.com', '<p:Ev8.K'],
   ['Reshma', 'shaikreshma912@gmail.com', '71@x6dpF'],['SHIVAM ', 'shivamsoni4475@gmail.com', '#D%6q.S*'],['Pavan Chand', 'spavanchand@gmail.com', '3gWF%Jbh'],['Suresh', 'sureshtadivalasa178@gmail.com', 'XPP%1O>r'],['ROHINI', 'tainanarohini98@gmail.com', 'RN0em1>@'],
   ['TEJASWI', 'tejuch.4149@gmail.com', 'X.fpMpw5'],['Navya', 'navyalikitha9@gmailcom', '|g31NsX)'],['Jagadesh', 'ju071998@gmail.com', '2?zCpxus'],['Lakshmi bai', 'lakshmibtech22@gmail.com', '$Qk$36n3'],['Sonali', 'sonalivarma8899@gmail.com ', 'qQ|2$aQb'],['Krishna sai', 'saik19199@gmail.com', 'I|eGqd9('],
   ['cheedirala', 'hemapravallika61@gmail.com', '1bP=Xb~s'],['Sowmya Singh ', 'Sowmya1999singh@gmail.com', 'Be%#?7(:'],['Saida Rao', 'saidamende60@gmail.com', 'm9F<9rNH']]
