from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
artical_data = [
    {
        "id" : 1,
        "image" : "https://media.self.com/photos/5e8e2b54f77fc200080d4122/4:3/w_2560%2Cc_limit/pandas-eating-bamboo.jpg",
        "title" : "Pandas",
        "desc" : "All about Pandas",
    },
    {
        "id" : 2,
        "image" : "https://www.thoughtco.com/thmb/rip9NU8E4ERKbO7hBjwPc98UtfM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/lion-805084_1920-c62a5582169c4bae82553d9a21c1a0bb.jpg",
        "title" : "Lion",
        "desc" : "All about lion",    
    },
    {
        "id" : 3,
        "image" : "https://img.magnific.com/free-photo/closeup-scarlet-macaw-from-side-view-scarlet-macaw-closeup-head_488145-3540.jpg?semt=ais_hybrid&w=740&q=80",
        "title" : "Parrot",
        "desc" : "All about Parrot",    
    },
    {
        "id" : 4,
        "image" : "https://static.toiimg.com/thumb/123482697/123482697.jpg?height=746&width=420&resizemode=76&imgsize=61144",
        "title" : "Rabbit",
        "desc" : "All about Rabbit",    
    },
    {
        "id" : 5,
        "image" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_ghFrKvBAnV7e9HyMIgmGHRJgRCd4Yq6mmokzHjYfPzgc69dLgZrTY34&s=10",
        "title" : "Tiger",
        "desc" : "All about Tigers",    
    },
    {
        "id" : 6,
        "image" : "https://images.indianexpress.com/2026/10/Pallatt-Brahmadathan.jpg?w=1024",
        "title" : "Elephant",
        "desc" : "All about Elephants",    
    }
]

news_data = [
    {
        "id" : 1,
        "image" : "https://th-i.thgim.com/public/incoming/wihm0c/article71555770.ece/alternates/LANDSCAPE_1200/2026-10-07T124511Z_1188760541_RC2CYNA2OSIE_RTRMADP_3_INDIA-POLITICS-PROTEST.JPG",
        "title" : "Rahul Gandhi released after 2-hour detention over anti-CEC protest",
        "desc" : "Opposition Protest Live Updates: A striking scene unfolded near Delhi’s Shangri-La hotel as Priyanka Gandhi Vadra and other women MPs lay on the road, with Priyanka holding up a copy of the Constitution during the Congress protest against the SIR and its demand for the resignation of the Chief Election Commissioner. Rahul Gandhi has been released after two-hours of detention. Priyanka was carried away from the protest site and taken away in a police bus. She later alleged that she was pushed around by the police"
    },
    {
        "id" : 2,
        "image" : "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202610/former-serbian-president-aleksandar-vucic-and-pm-modi-072530256-16x9_0.jpg?VersionId=XexRmlKH5gGgTX7f_WK3hWAJntfcyMPT&size=690:388",
        "title" : "Trying to tear him down: Ex-Serbian president flags bid to undermine PM Modi",
        "desc" : """Former Serbian president Aleksandar Vucic asserted that despite Prime Minister Narendra Modi "raising India to the heavens" and turning it into a force on the global stage, attempts were being made to undermine him. A clip of Vucic's remarks from a podcast went viral on Wednesday as PM Modi marked 25 years of service as head of government.

Vucic, who stepped down as Serbian president last month to run for the parliamentary elections, pointed towards what he called a global trend of attempts to undermine leaders. Singling out PM Modi, Vucic said he made India a major global power and "accomplished huge things"."""
    },
    {
        "id" : 3,
        "image" : "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202610/saurav-dass-attempt-to-tease-shashi-tharoor-over-pm-modis-temple-visit-drew-a-witty-response-from-075943618-16x9_0.png?VersionId=HIh.VzQNcDATaP7Yx4gVmkZJQUsuUCjf&size=690:388",
        "title" : "How Shashi Tharoor denied CJP's Saurav Das the pleasure of a stinging controversy",
        "desc" : """Cockroach Janta Party (CJP) co-convenor Saurav Das tried to bait Congress leader Shashi Tharoor into commenting on Prime Minister Narendra Modi with a video of the BJP leader offering prayers to Lord Shiva and Shashi Tharoor-style English. However, Tharoor, sharp as ever, dodged the bullet, reeling in Das himself. The video had to do with Modi offering prayers visit to a Shiva temple, and Das's bait was obvious in reference to Tharoor's 2018 "scorpion on a Shivling" remark."""
    },
    {
        "id" : 4,
        "image" : "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202610/prime-minister-narendra-modi-is-indias-longest-serving-head-of-an-elected-government--with-25-years-074206967-16x9_0.jpg?VersionId=6o6UYwUUcnqQ2jt3tv2ngk8eYkkudfDz&size=690:388",
        "title" : "From Jyotigram to JAM and Sindoor. Modi's 10 big decisions in 25 years of sewa",
        "desc" : """From Gujarat's power and water reforms to GST, Article 370 to Operation Sindoor, Prime Minister Narendra Modi's 25 years at the helm of governments have been defined by decisions that sought to change systems, reshape delivery models, and, at various times, alter the political grammar itself.

On October 7, 2001, Narendra Modi took oath as Gujarat's Chief Minister. Now, 25 years later, he is the head of the Government of India. He spent nearly 13 years as Prime Minister after his 13-year tenure in Gujarat. Today, Modi marked the milestone of 25 years of serving as the head of governments in his home-state and on the national level."""
    },
    {
        "id" : 5,
        "image" : "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202610/sharif-naqvi-070434779-16x9_0.png?VersionId=PYyfLuokDl2Glvf3gG11iWmP4TdpbO9F&size=982:552",
        "title" : "Some absent for a month: Munir's aide Naqvi lectures after PM Sharif's foreign trip",
        "desc" : """Pakistan Interior Minister and Asim Munir's aide, Mohsin Naqvi, lectured leaders on accountability, saying some leaders were absent from their offices for a month. Pakistan PM Shehbaz Sharif, who returned from a weeks-long trip to the US and the UK, was in the audience. Naqvi's remarks, and his apparent contrast with an unnamed tireless official, come as Pakistan's balance of power tilts further towards Asim Munir and away from the civilian government."""
    },
    {
        "id" : 6,
        "image" : "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202610/netanyahu--hamas-074533754-16x9_0.jpg?VersionId=vMGTIeBBaNvyLGZbc.8CRkSZJy0uAmJH&size=690:388",
        "title" : "October 7 Hamas attack should've ended Netanyahu's career. How did he survive?",
        "desc" : """On October 7, 2023, Israel suffered one of the darkest days in its history. The scars of that morning remain deep. Thousands of Hamas-led militants broke through the Gaza border, killing 1,205 people and taking 251 hostages into the Gaza Strip. Israel responded with a massive military campaign in Gaza that has killed at least 74,347 people, according to the enclave's Hamas-run health ministry.Three years later, the shock of that day still hangs over Israel. The attack exposed profound failures in the country's security system and triggered a war that has changed the equations in the Middle East.
                    The trail of questions from that day leads, again and again, to Israeli Prime Minister Benjamin Netanyahu, who was in charge when Hamas breached the border. The scale of the failure might have been expected to end his political career. Instead, Israel's longest-serving prime minister is once again seeking a mandate from voters."""
    }
]

sports_data = [
    {
        "id" : 1 , 
        "image" : "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202610/hasan-nawaz-09322778-16x9.jpg?VersionId=V.s7Ih2wHTvME0aiwcG2AshL39QhTRUc&size=690:388",
        "title" : "Still hurt at losing Asian Games final to India: Pakistan batter Hasan Nawaz",
        "desc" : """Still hurt by his side's loss to India in the Asian Games final, Pakistan batter Hasan Nawaz admitted that his team made "small mistakes" in the run chase and paid the price despite believing they had a genuine chance of winning the gold medal.""",
    },
    {
        "id" : 2 , 
        "image" : "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202610/smriti-mandhana-072217866-16x9.jpg?VersionId=OabTx5bM9hoD_iWCPNf01iz2tXEd5qtQ&size=690:388",
        "title" : "Smriti Mandhana pays tribute to Harmanpreet amid rumours of rift",
        "desc" : """Newly appointed India women's captain Smriti Mandhana paid tribute to outgoing skipper Harmanpreet Kaur on Wednesday, hours after a report claimed that the two senior players had not been seeing eye to eye over the captaincy. Smriti took to Instagram to acknowledge Harmanpreet's decade-long leadership of the Indian team, saying she hoped the two could continue to bring success to the country together.

"It's been a pleasure playing with you for so many years," Smriti wrote.

"Ten years of your leadership have been fantastic and together, we will strive to bring many more laurels for our nation," she added.

Smriti Mandhana's message came after the BCCI appointed her as India's captain across all three formats, bringing an end to Harmanpreet's tenure as the team's leader.""",
    },
    {
        "id" : 3 , 
        "image" : "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202610/neha-sangwan-224607472-16x9.png?VersionId=9Eqon2sFCVHxtkaF2lboezewnhWliYdD&size=690:388",
        "title" : "USA refuses visas to Indian wrestlers ahead of World Championships. Here's why",
        "desc" : """The WFI said many of the young wrestlers are not formally employed because they are still pursuing their sporting careers and asked the US Embassy to reconsider the refused applications.

"Accordingly, many of these young athletes are understandably still pursuing their sporting careers and are not formally employed," the federation said.

The nine wrestlers named in the WFI's communication are Samarth Gajanan Mhakave, Dheeraj Kumar Malik, Sachin Kumar, Nikhil, Hardeep, Parveen, Ahilya Shatrughn Shinde, Neha Sharma and Neha Sangwan.""",
    },
    {
        "id" : 4 , 
        "image" : "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202610/rohit-sharma-and-virat-kohli-073659159-16x9_0.png?VersionId=fFapVVhd2VmzRfkSzfhwjCHz47GK.eiK&size=690:388",
        "title" : "Everyone had fun with Ro-Ko. Now Rohit and Kohli join the joke in hilarious TV ad",
        "desc" : """'Ro-Ko' are back, and this time they are having fun with it

"Bro, it's been years."

"But it's still as much fun."

Virat Kohli and Rohit Sharma have spent nearly two decades playing together for India, but their latest collaboration has little to do with runs, wickets or cricketing tactics. The two former India captains have joined hands for a hilarious JioStar advertisement ahead of India's ODI series against Sri Lanka, and the biggest joke is one that they have only recently decided to embrace: Ro-Ko.""",
    },
    {
        "id" : 5 , 
        "image" : "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202610/bhuvneshwar-kumar-074729739-16x9_0.jpg?VersionId=YPNMK2LE7tqbQNkAmYhaj6GAlXsJmKvM&size=690:388",
        "title" : "Bumrah-Bhuvi for World Cup 2027? Ashwin's bold claim after Bhuvneshwar's India return",
        "desc" : """Bhuvneshwar's India career had been on hold since the T20 World Cup semi-final against England in Adelaide in November 2022. Nearly four years later, the 36-year-old has forced his way back into the national reckoning with a string of impressive performances in the IPL.

The seamer's consistency for Royal Challengers Bengaluru over the past two seasons has played a major part in his comeback. Bhuvneshwar has claimed 45 wickets across the 2025 and 2026 IPL campaigns, contributing to RCB's title triumphs during that period.""",
    },
    {
        "id" : 6 , 
        "image" : "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202610/gautam-gambhir--ajit-agarkar-072224214-16x9_0.jpg?VersionId=3KE1_pF2wVjkk2A2LYTg_de8abxpDEE5&size=690:388",
        "title" : "Gautam Gambhir has a message for Agarkar's critics in farewell note for selector",
        "desc" : """India men's cricket team head coach Gautam Gambhir paid a touching tribute to outgoing BCCI chief selector Ajit Agarkar after his tenure officially came to a close. The BCCI has formally set the ball rolling to appoint a new member to its Men's Selection Committee, inviting applications for the vacant position following Ajit Agarkar's exit.

In his message on X, Gambhir appeared to take a jibe at critics of Agarkar, stressing that the success that Team India had over the last three years was because of team-first attitude and conviction.""",
    }
]

international_data = [
    {
        "id": 1,
        "image": "https://npr.brightspotcdn.com/dims3/default/strip/false/crop/3693x2462+0+0/resize/900/quality/85/format/webp/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2Fee%2Fe7%2F53c3044445699068c91a3bc54095%2Fap26278401142788.jpg",
        "title": "Israel marks three years since October 7 Hamas attack",
        "desc": """Israel is marking the third anniversary of the October 7, 2023 Hamas attack with memorial events across the country. Families of victims and former hostages gathered to remember those killed and reflect on the continuing impact of the conflict.""",
    },

    {
        "id": 2,
        "image": "https://www.aljazeera.com/wp-content/uploads/2026/10/afp_6ac3539d406e-1791185821.jpg?resize=770%2C513&quality=80",
        "title": "Yemen conflict escalates as fighting intensifies",
        "desc": """The conflict in Yemen has intensified in 2026 as fighting between the internationally recognised government and the Iran-backed Houthis expands. The escalation is creating wider concerns for regional security and international shipping through the Red Sea.""",
    },

    {
        "id": 3,
        "image": "https://i0.wp.com/www.middleeastmonitor.com/wp-content/uploads/2026/07/AA-20260717-42002739-42002731-HOUTHIS_PROTEST_IN_SANAA_IN_SUPPORT_OF_ALHOUTHIS_STATEMENTS.jpg?fit=920%2C613&ssl=1",
        "title": "Houthis claim attacks on Saudi targets amid Middle East tensions",
        "desc": """Yemen's Houthi rebels claimed ballistic missile, cruise missile and drone attacks against several Saudi military facilities and airports. Saudi authorities reported intercepting missiles as regional tensions continued to rise.""",
    },

    {
        "id": 4,
        "image": "https://www.aljazeera.com/wp-content/uploads/2026/10/afp_6ac63b7fd4d5-1791376255.jpg?resize=770%2C513&quality=80",
        "title": "Japan protests after US Marine arrested over alleged killing",
        "desc": """Japan's government has expressed concern following the arrest of a US Marine on Okinawa over the alleged killing of a woman. The incident has renewed long-running tensions surrounding the presence of US military personnel on the Japanese island.""",
    },

    {
        "id": 5,
        "image": "https://i.guim.co.uk/img/media/4f1ca7f53427e4fc2393831d6760ae2c450e3b06/59_0_3334_2668/master/3334.jpg?width=620&dpr=2&s=none&crop=none",
        "title": "Poland pushes for stronger European energy resilience",
        "desc": """Poland is strengthening cooperation with neighbouring European countries as it seeks greater energy security amid continuing tensions with Russia. Warsaw is encouraging closer regional cooperation to reduce vulnerability to energy disruptions.""",
    },

    {
        "id": 6,
        "image": "https://i.guim.co.uk/img/media/a435ef9790efec74113a27f4c9a26279fb435408/87_0_4640_3712/master/4640.jpg?width=620&dpr=2&s=none&crop=none",
        "title": "Ukraine investigates attacks involving vessels in Black Sea",
        "desc": """Ukraine has blamed Russia for an attack involving Bulgarian vessels in the Black Sea, while an investigation into the incident continues. The development adds to growing concerns over maritime security in the region.""",
    }
]

blogs_data = [
    {
        "id": 1,
        "image": "https://platform.theverge.com/wp-content/uploads/sites/2/2026/10/gettyimages-2297765991.jpg?quality=90&strip=all&crop=0%2C0.014430014430019%2C100%2C99.97113997114&w=1080",
        "title": "OpenAI releases 372 groups of mathematical results from an unreleased AI model",
        "desc": """OpenAI has released hundreds of mathematical research results generated with help from an unreleased frontier AI model. The work demonstrates significant progress in AI-assisted mathematical reasoning and gives researchers new material for studying the capabilities of advanced AI systems."""
    },

    {
        "id": 2,
        "image": "https://boldnewsonline.com/wp-content/uploads/2026/10/Screenshot-2026-10-05-120221.png",
        "title": "Google expands AI capabilities across its products",
        "desc": """Google continues to expand its artificial intelligence ecosystem with new Gemini capabilities, connected applications and AI-powered tools. The company's latest updates focus on making AI more useful across productivity, search and everyday tasks."""
    },

    {
        "id": 3,
        "image": "https://images.moneycontrol.com/static-mcnews/2026/10/20261006130353_gs243.jpg?impolicy=website&width=770&height=431",
        "title": "AI coding tools are changing software development",
        "desc": """AI coding tools are increasingly being used by software development teams to improve engineering productivity. Companies are seeing significant gains from agentic coding, although controlling infrastructure and model usage costs remains an important challenge."""
    },

    {
        "id": 4,
        "image": "https://cf-images.assettype.com/newindianexpress%2F2026-10-06%2Fxe8tbauc%2Fimage.png?w=1024&auto=format%2Ccompress&fit=max",
        "title": "AI agents create new challenges for cybersecurity",
        "desc": """The rapid growth of autonomous AI agents is creating new cybersecurity challenges. Developers and security teams are increasingly focused on controlling agent permissions, protecting credentials and preventing AI systems from performing unintended actions."""
    },

    {
        "id": 5,
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1200&q=80",
        "title": "Silicon Labs launches AI SDK for edge development",
        "desc": """Silicon Labs has introduced a public beta of its Simplicity AI SDK, designed to help developers build AI-enabled IoT and Bluetooth Low Energy applications. The tools are intended to make development, debugging and deployment of edge AI applications easier."""
    },

    {
        "id": 6,
        "image": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1200&q=80",
        "title": "Microsoft and NVIDIA prepare new AI-powered laptop",
        "desc": """Microsoft and NVIDIA are preparing a new AI-powered laptop aimed at running advanced AI workloads directly on Windows PCs. The approach could reduce reliance on cloud computing for some AI tasks while bringing more AI processing capabilities to local devices."""
    }
]

about_data = [
    {
        "id": 1,
        "image" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGcWcRw-F3EkpPFOgdBO2T78uHPpTSLKQQT37Oz4E1BefZAKHq35JheWPedpofQhhZzKQ45r9ODbHGF0Qvc6J2LotGTgHdG0Aa0xrEuSKt&s=10",
        "title": "About Our News Platform",
        "desc": """Our platform brings together the latest sports, international and technology news in one place. Articles are organized into different categories to make it easier for readers to discover current and relevant stories."""
    }
]


def home(request):
    context = {"data" : artical_data}
    return render(request,'home.html',context)

def news(request):
    context = {"data" : news_data}
    return render(request,'news.html',context)

def sports(request):
    context = {"data" : sports_data}
    return render(request,'sports.html',context)

def international(request):
    context = {"data" : international_data}
    return render(request,'international.html',context)

def blogs(request):
    context = {"data" : blogs_data}
    return render(request,'blogs.html',context)

def about(request):
    context = {"data" : about_data}
    return render(request,'about.html',context)


def home_read(request,id):
    for i in artical_data:
        if i["id"] == id:
            context = {"data" : i}
    return render(request,'home_read.html',context)

def news_read(request,id):
    for i in news_data:
        if i["id"] == id:
            context = {"data" : i}
    return render(request,'news_read.html',context)

def sports_read(request,id):
    for i in sports_data:
        if i["id"] == id:
            context = {"data" : i}
    return render(request,'sports_read.html',context)

def international_read(request,id):
    for i in international_data:
        if i["id"] == id:
            context = {"data" : i}
    return render(request,'international_read.html',context)

def blogs_read(request,id):
    for i in blogs_data:
        if i["id"] == id:
            context = {"data" : i}
    return render(request,'blogs_read.html',context)

def about_read(request,id):
    for i in about_data:
        if i["id"] == id:
            context = {"data" : i}
    return render(request,'about_read.html',context)