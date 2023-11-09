# FalconSite

## A tool providing transparency into 3rd-party network security.

Welcome to the FalconSite project documentation. Here we will discuss the big idea of the project, its value proposition, implementation, development timeline, methodologies, risks, and additional resources relevant to our goals. 

### A total of 98% of organizations worldwide have integrations with at least one 3rd-party vendor that's been breached in the last two years.

### Only 13% of organizations continuously monitor the security risks of their third parties.

### Global cybercrime is expected to cost $10.5 trillion in damages by the yeaer 2025.

## FalconSite is here to stop this.

This project is being created to address a gaping hole in the cybersecurity world: vendor risk management. According to numerous studies (really, there are a lot), most of today's data breaches are occurring through a third-party, and are impacting the business, and customers of said third-party. The reality is this: it's hard to collaborate across all of your vendors to monitor and assess their cybersecurity risk. With today's world of endless risk assessments, PE firms wanting proof of cyber compliance, and a veil surrounding your organization's view into your vendor's cyber risk management intiatives, many companies don't even know the threats that are being posed to them through their relationships. FalconSite helps address this major concern.

By utilizing publically available data harvested via internet crawlers from a third-party, Shodan, FalconSite accesses up-to-date data on all IP addresses connected to the internet, and does so in an entirely legal, transparent, and efficient manner. The data maps all open ports, or internet-facing ports, that are actively listening for packets to be sent over the internet to them. While open ports are not inherently unsafe, an open port is like leaving your house door unlocked, but keeping the door closed. If someone wants to get in, and the system is not set up to control these infiltrators, they surely will get in. 

### FalconSite observes network traffic automatically, so you don't have to.

Okay... so what... does this program just view open ports? Why does this matter? It matters because it does not JUST view the ports. FalconSite is able to view the IP addresses and the type of port that is open to the internet, view the geographic data of these IPs, the types of operating systems that are ran on these computers, the latest version of said systems, and very important: __the vulnerabilities associated with these specific systems__.

In addition, you don't need access to a DNS lookup service to see specific IPs. You just have to type a name of the entity you wish to explore (Example query:'harvard university') and FalconSite will generate results associated with this entity. The Shodan API that we use is regularly updated, and in general, the entirety of the internet is scanned and logged within the database.

So, say you are an admin within the cyber division of company X, and your sales team is looking to install company Y's latest firmware on their computers. You can't necessarily tour company Y's entire network, see where there are potential risks, quanitify those risks, and map where these risk pose the most threat to your own company. This would be highly inefficient and costly. You also can't scan their network without their permission. You __can__ however, utilize FalconSite to access data of previous web-crawlers that have encountered the computers of company Y, and from this data make an informed decision on the network risk of business with company Y.

This is the goal of FalconSite. The project will explore API integration, user experience, data security, navigating regulation, quantifying business impact, inform data-driven decision-making, and many more topics. Through trustworthy and impactful interaction with our users, FalconSite hopes to bring more transparency into the field of vendor cyberrisk management.

The user-journey will look something like the following:

1. Users are prompted to register, accept the terms of service, and log in with their organization credentials on the FalconSite website. 
2. Users add vendors to their profile (i.e. Company X adds Company Y as a vendor)
3. Users request the report they are seeking of their vendor (i.e. geography of systems, vulnerability report, etc.)
4. FalconSite accesses API data and posts this data to the user's webpage through different visualizations like graphs, charts, maps, etc.
5. more features to come soon...

### Objectives of the FalconSite project:
As the creator of this project, there are many areas where I would like to improve my programming and hacker abilities. For one, I am excited to utilize open source intelligence platforms and data that can help push the project forward. There is an uncaptured value in open source information that many businesses fail to see. I want to take advantage of all of the free resources available online to help me move forward with this project. 

Additionally, I would like to better understand my coding style and habits. As I am a noob to coding, I've yet to really develop a signature style or pizzazz to my coding that I want to see in the future. By having a project of this scale, I will be forced to work, learn how to get better at my work, and eventually better understand what works and what doesn't. This process will eventually build me into a stronger programmer and better equipped professional in today's digital world.

A major area that I would like to improve at is my ability to program elegant UI/UX for users. I have familiarity with HTML, CSS, JavaScript, but I want to build something that stands out from novice sites with lengthy text, bulky styling, and slow response times. I think this area of building a pretty and functional tool will be the most enjoyable part of the project for me, and one that I am really looking to dive into. 

### Implementing FalconSite:
Flask Flask Flask Flask Flask Flask. Flask will definitely be key in this project. I need to learn more about how the framework will enable my project to be successful, and also learn where it may limit my efforts. Additionally, it seems like for now I am working in an agile method, so there isn't really much that I am positive about for the future of the project. So far I have found a library that I am really impressed with -Shodan-, but I'm sure at some point a library that I find will have a better alternative out there. When that point comes I will switch to the better alternative. 

A place that has been very helpful for me in identifying the best libraries and practices for my project has been the r/cybersecurity subreddit, and exchanges on stack overflow. I will continue using sources similar to this, and maybe hacker blogs to find more information that would be helpful. 

### Development timeline:

1. (Week one) - develop initial functionality and refine scope
2. (Week two) - polish functionality and optimize
3. (Week three) - begin flask development for hosting site
4. (Week four) - finish flask for site
5. (Week five) - add styling to site
6. (Week six) - finishing touches and bug fixes

### Collaboration methodology: 

As I am choosing to complete this project alone, I don't have much plans for collaborating with others as of now for DEVELOPMENT. However, I will definitely look to my peers for help with designing my code and having a fresh perspective on my development decision making. Additionally, I will utilize forumns like reddit to ask questions or shine light on areas of difficulty if needed. I will be sure to stay disciplined for this project, and set goals for each week to actively accomplish. Each goal will be broken down into subsections that will allow me to better understand the scope of the work that needs to be done.

### Risk and limitations: 

I am afraid that this project could be interpreted as a tool for malicious use. That is NOT, I repeat, NOT, what I am building it for. The nature of security tools like this is that they are double edged swords. You can use it protect yourself or you can use it for other purposes. I am solely creating it for the purpose of evaluating the risks of vendors that are involved with business with companies or prospective vendors that cannot quantify their cyber risk. Additionally, the information that is accessed by FalconSite is 100% public information. I am not infiltrating any private networks, doing malicious tasks with the information I acquire, or any of the sort. As a newspaper must write on harsh events, I am publishing security flaws for informative purposes. Users that choose to use this service will have to accept a terms of service so that they are legally binded to not use the platform for malicious use, and that we are not liable for such use. We are not scanning networks, flooding packets, pinging servers, or anything of the sort. Instead, we are like a librarian, pointing you in the direction of the published pieces of work that others have written. 

### Additional resources:

FalconSite will foster a collaborative and sponge-like approach to all interactions with security professionals, seeking to learn and grow with time. By utilizing existing resources and tools, the project will tryh to leverage other people's work and my own to create a powerful computing service. FalconSite will continually seek new APIs to better improve our data and security, and additionally alternative resources that can aid in the UX function. A frequented place for such information is GitHub. 

















