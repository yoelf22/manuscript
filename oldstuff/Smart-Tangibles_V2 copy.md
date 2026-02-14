# Smart Tangibles: 

## How to Build Hardware Competitors Can’t Copy and Customers Won’t Leave





### Preface

### Smart Tangibles

*Smart Tangibles* addresses a central challenge for today’s entrepreneurs and executives in the physical realm: **how to create defensible hardware products in the face of rapid commoditization and low-cost imitators.**

The book offers a strategy framework for transforming physical goods into smart platforms by integrating software, services, and ecosystems that extend customer lifetime, drive recurring revenues, and build loyalty competitors cannot easily disrupt. By moving beyond one-time product sales to sustained relationships, smart tangibles reshape both business models and competitive dynamics.

This book fits squarely within the mission of Stanford Business Books: bridging scholarship and practice while providing accessible yet rigorous insights into innovation and entrepreneurship. Drawing on more than 30 years of professional experience in design, engineering, and product strategy, I integrate analytical frameworks with case studies ranging from Apple, Tesla, and Swatch to Nespresso, iRobot, and John Deere.

Its significance lies in equipping both practitioners and scholars with tools to understand and manage the convergence of hardware, software, and services — a transformation redefining industries from consumer goods to mobility and healthcare.

------

# Arc I: Diagnosing Hardware Challenges

*Why ‘hardware is hard’ and how traditional development cycles, cost structures,*

*and validation logic often fail.*

## Chapter 1 - Why is Hardware THAT hard?

_The unique challenges product leaders face with integrated hardware and software products. It emphasizes the importance of early validation to mitigate risks and the difficulties in creating meaningful MVPs due to the monolithic nature of hardware products._



![Ford Model A](./images/73dd11_28fa2f0dce324eae93b3f2889c937d1amv2.webp)

*Ford Model T* 

---



![Tesla Model Y](./images/73dd11_be3afcdc3a904afb8d149ba42d571124mv2.webp)

*Tesla Model Y*

---



![Tesla Interior](./images/nsplsh_5a42576e3544764f306867mv2_d_5456_3284_s_4_2.webp)

*Tesla - Interior*

---

Much has changed in the automotive world in the 115 years spanning the introduction of the Ford Model T, the first mass-produced car, and the start of production for Tesla's Model Y, a battery-powered electric car that is connected to the internet via satellite, yet nearly all contemporary drivers could drive a Model T, and any early 20th-century driver could probably learn to drive a modern car within just a few hours.

… Cut to the basic challenges of creating physical products (cars included), then scaling them up, generating profit in the process. These have not changed. Building hardware products is an extremely hard endeavor.

In the first part of this series, we’ll show how bad the situation is.

Hardware manufacturers, thankfully, have learned a thing or two in their quest to reduce risk and improve the prospects of hardware products, especially in the domain of **development processes**:

Advanced design methods, easy and realistic prototyping, flattened supply chains, improved inventory management, and streamlined production planning have combined to shorten time to market, improve validation, and reduce overall costs.

Challenges, however, remain. Globalization and the resource arbitrage it brings mean that successful products will be copied - posing a new element of risk traditional methods can’t prevent. 

Patents alone are no longer valid protection: While registration is accessible, **litigation** is a major  and risky expense, increasingly eroding this crucial barrier against commodification.

The good news is that the advent of integration of physical and digital capabilities opens for reshaping product and customer lifecycles, and improve on the business models that such products support. 

Moreover, it opens for a range of new services that manufacturers can offer to their users, extending product lifetime, by increasing customer loyalty.

Finally, the new value created has the potential to be much harder to copy.

Now let us get back to the initial predicament of hardware manufacturers - Why is it so hard to reach even initial success?

---

### OK, So Why is Hardware THAT hard?

_Hardware startups face unique challenges, particularly in terms of timing and cost of failure. While software companies can test market adoption with MVPs, hardware ventures must invest heavily in production and distribution, making failure more costly. Despite these risks, hardware is essential for our physical world, and digital technologies can improve the fortunes of hardware startups._

---



Let us first establish the problem.

According to [<u><span>CB Insights</span></u>](https://www.cbinsights.com/research/report/hardware-startups-failure-success/), the average venture success rate for hardware is only 3%, compared to 30% for software, with "success" defined as the survival beyond ten years.

This begs the question: What factors contribute to the difference in success rates between hardware to software ventures, and what insights can we draw to improve the likelihood of success for the hardware venture we are involved in as product managers?

![Comparison of failure rates of Hardware Vs. Software startups](./images/73dd11_fe4b3050ec2246fa8ff712227cfdda4amv2.png)

Comparison of failure rates of Hardware Vs. Software startups

---

Another quite devastating illustration from the same source shows the survival funnel for consumer hardware startups, and let me tell you: The news ain’t good:

![consumer hardware startup success funnel](images/73dd11_b56d52db395f4c1fa879368e35b665c9~mv2.png)

consumer hardware startup success funnel

---



Let's review some of the reasons:

#### Sunk Costs

A sunk cost is an expense already incurred which cannot be recovered. When designing a hardware product for mass production, a significant portion of the development expenses fall into this category. Most of these costs cannot be repurposed for new products in the event of failure and are likely to be completely lost.

Take, for example, a domestic trash bin manufactured by Dolav, produced via HDPE reaction injection molding. The injection mold required for producing the main body consisted of two steel blocks weighing 80 tons in total. In addition to the main mold, several others were needed for the lid, wheels, and various auxiliary parts, weighing several tons each.

![Dolav - residential waste bin](./images/73dd11_b661303193b14b30a1b252b9a7959994mv2.png)

*Dolav - residential waste bin*

![Dolav - resifential waste bin](./images/73dd11_5e0dfd90d9774cd48b7f732a67992d31mv2.png) 

*Dolav - residential waste bin*

![Waste bin mold](./images/73dd11_57bea61a45db4e67b7191eacabf551d3mv2.webp)

*Waste bin mold*

Two semi-trailer trucks were required to transport the main mold from the port to the injection molding facility at Kibbutz Dvir, and other trucks were needed to deliver the smaller molds to the factory at Kibbutz Gadot, where the smaller parts were to be injected.

The cumulative development cost ammounted to millions of Euros, a significant economic risk. A commercial or technical failure could have resulted in additional losses of several million euros due to tied-up production resources (raw materials, labor costs, injection molding machines).

Moreover, such a failure would have turned the the production tooling, ie the molds, into massive scrap metal, left to rust quietly in some warehouse, or sold by the weight for recycling.

Of course, sunk costs are rife in the software industry as well. However, the magnitude of the problem seems smaller:

![Sunk costs for software and hardware products](./images/73dd11_65685187ed63432a91752223542934e0mv2.png)

Sunk costs for software and hardware products



---



#### Lower profit margins

Compared to software companies, hardware ventures bear additional costs for production facilities, factory space, and logistics (PPE), as well as the need to finance raw materials and inventory spread across the supply chain.

These additional costs result in relatively lower profit margins. In a gross profit analysis comparing ventures from both software and hardware sectors, we examined ventures within one standard deviation from the industry average, covering 68% of companies under a normal distribution.

According to this analysis, software companies achieve gross profitability ranging from 75% to 85%, while for hardware companies, the average gross profitability is lower, ranging from 42% to 44%, with significant variation across industry sectors.

![Profit after launch for software and hardware products](./images/73dd11_237b979825aa411bb4b9fecd598f47c4mv2.png)

Profit ranges for software and hardware products (compiled)

#### Data Sources & Methodology:

-   NYU Stern Industry Analysis (January 2025) - 6,062 companies across industries downloaded from https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/margin.html

-   Software sector: System & Application (72.4%), Entertainment (65.4%), Internet (60.8%)

-   Hardware sector: Computers/Peripherals (38.7%), Electronics General (25.2%), Equipment (30.1%)

-   Individual company data from FY 2024 financial reports

-   Sample represents companies within 1 standard deviation of industry mean

-   Code available at: https://colab.research.google.com/drive/1259htZld5APCdHNzsr0aD8uZ7gdJOKcS?usp=sharing

---



#### Higher and earlier project failure

Hardware ventures face a higher risk of long-term failure compared to software startups, with the gap becoming more pronounced around the heavy investments required at the industrialization phase.

![Failure rates for software and hardware products](./images/73dd11_16395dc6507f441e9b1ba512274d5425mv2.png)

Failure rates for software and hardware products

Here are several eye-popping examples of software venture failures from a [<u><span>CBInsights</span></u>](https://www.cbinsights.com/research/report/hardware-startups-failure-success/) study conducted in 2017:

![Epic Hardware startup failures](./images/73dd11_97ddb8f76cbe479a99d0058c7c9021b4mv2.png)

Epic Hardware startup failures

These examples illustrate the substantial amounts required for industrialization, marketing and distribution, all while building the supply chain and inventory necessary for hardware products - and the sheer risks hardware entrepreneurs must undertake to scale.

---



#### Slower growth

Supply chains and distribution channels characteristic of tangible products also impose slower growth and intensive cash consumption (working capital).

These entail constraints such as shipping duration and costs, inventory management, and last-mile delivery challenges — all of which are thankfully absent from the business model of most software products.

One of the main outcomes of these constraints is slower growth for hardware ventures, especially in comparison to software.

![Growth for software and hardware products](./images/73dd11_7f99e80b193546698d69e041a91ba333mv2.png)

Growth for software and hardware products

Source: [<u><span>Equidam</span></u>](https://www.equidam.com/average-growth-rate-for-startups/) and author's processing

---



#### Longer ROI period

If you also visualize a startup's success by sketching the famous hockey stick graph of its cash balance over time, you can compare the average curve for hardware and software products and see that it takes much longer to achieve a return on investment.

![Cash balance for software and hardware products](./images/73dd11_ba90b6ef0a204f54b25c536794d960b4mv2.png)

Cash balance for software and hardware products

Note: This refers to a return on investment from organic sources, meaning from the company’s revenues and profits, rather than from an exit event where new investment or debt replace early equity.

---



#### Where capital flows to

The above might be interpreted as suggesting that hardware products should be avoided at all costs... but that’s not my intention. It’s true that the factors mentioned earlier weigh heavily on the initiation, industrialization, and distribution of hardware products.

Undoubtedly, increasing competition and regulatory burdens make it even harder to successfully launch hardware products.

Other trends in recent decades, however, have had a strongly positive impact on hardware product development, and by implication, on new ventures in the field. These include improved design and prototyping processes, supply chains simplification, and, not least, the rapid growth of the global market, which has brought billions into the global economy and into production and consumption cycles.

It’s reasonable to think that these positive trends have contributed to the proliferation and success of physical products: The significant rise in purchasing power among a growing number of people needing clothing, housing, transportation, essential products, and entertainment represents a powerful positive force (yes, I am ignoring environmental externalities here).

The point is that these same trends that enabled the growth of recent decades also made information technology even more successful compared to hardware. Countless software products have been launched with reduced risk and plummeting development costs, resulting in lower damage in the event of failure.

One reason for this is that, unlike hardware, software products are developed as layers built upon the foundations established by industry leaders, who themselves continue to advance.

Phenomena like cloud-based infrastructure as a service (SaaS, PaaS, IaaS) further reduce costs and accelerate the creation of new software products.

Indeed, it’s interesting to examine venture capital flows in recent years.

![VC allocation for software and hardware startups](./images/73dd11_62309ad0574b41cd832c3944f9feab96mv2.png)

VC allocation by sectors. Source: KPMG

As software continues "eating the world," a consistent ratio between investments in software and hardware can be observed, allowing us to infer the availability of capital for the hardware sector (and perhaps the availability of investors capable of committing to the marathon required).

---



#### Slow ramp-up, longer time-to-revenue

The production, transportation, and installation of the molds in the previous example took approximately a calendar year, a timeline almost unheard of in the software industry, but sadly by no means an exception in the hardware industries. A new car, for example, can easily take [<u><span>up to six years</span></u>](https://www.caranddriver.com/news/a15350381/how-a-car-is-made-every-step-from-invention-to-launch/) from conception to manufacturing.

General and administrative expenses, including development and maintenance costs, are, of course, common in the software industry as well. However, the time required to launch and begin generating revenue from the product—and consequently, the waiting period until the breakeven point and return on investment—tends to be significantly longer for hardware companies. This increases the financial burden on investors.

![Time-to-market for hardware and software products](./images/73dd11_527c808a575041a2a86988076d0fcb6cmv2.png)

*Time-to-market for hardware and software products*

Several studies highlight significant differences between software and hardware ventures, to the detriment of the latter:

<table data-hook="table-component"><colgroup><col><col><col><col></colgroup><tbody><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-mxmrc28543"><span><strong><span>Metric</span></strong></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-n13mh28546"><span><strong><span>Software</span></strong></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-z709028549"><span><strong><span>Hardware</span></strong></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-wygqt28552"><span><strong><span>Multiplier</span></strong></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-lplux28556"><span><span>Time to market</span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-715kr28559"><span><span>9</span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-co8fq28562"><span><span>18</span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-pwraa28565"><span><span>2.0</span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-w23ah28569"><span><span>Time to breakeven</span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-onk1328572"><span><span>21</span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-861u128575"><span><span>30</span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-vg25s28578"><span><span>1.43</span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-h01er28582"><span><span>Time to ROI</span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-8ky1928585"><span><span>24</span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-lqshh28588"><span><span>71</span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-neqd728591"><span><span>2.93</span></span></p></td></tr></tbody></table>

We will later revisit the impact of prolonged waiting periods on investor considerations in hardware ventures.



---



#### Interim Conclusion (1)

Don't. Do. Hardware!... Or maybe, this was a bit too harsh...

In the upcoming posts, I will discuss trends that help alleviate some of the pains associated with establishing hardware ventures.

In particular, we will examine the effects of the convergence between hardware and software in the form of smart or connected products.

Additionally, I will explore several product management practices that can (and must) be implemented as part of hardware product development.  


---

'***'

---



# Chapter 2 - Points of failure - Hardware startup validation traps

![Better Place - A painful experience ](./images/73dd11_e6e020b903d04ec2bf300e3374faa5c6mv2.png)

*Better Place - A painful experience*



Let us discuss the challenges for hardware ventures:

-   **Physical & Technical**: Is your product based on sound technical ground? Does the widget perform as advertised?
    
-   **Supply Chain**: Can you source the components, raw materials, labor and other manufacturing input? Can you then distribute it economically?
    
-   **Unit economics**: Can you set up the production facility require to manufacture this product at quality and scale desired? Would the units produced generate profit margins?
    
-   **Scaling**: How to get a wide audience? You need to build and finance a distribution network, account for working capital, suffer wear and tear of inventories.
    
-   **Adoption**: How much will they want, how fast, and at what price?
    

![Points of failure for hardware startups, their cost and their timing](./images/73dd11_206c8e90aab44d2fb79511fe39dadfb5mv2.png)

Points of failure: Time, Cost

The graph above shows how these failure points are distributed along the life cycle of hardware products. Notably, each differs in timing and financial impact.  

You'll notice that as times goes by, the cost of failure increases. Consider the following illustration:

![SW - HW financial aspect of failure (illustration)](images/73dd11_17d2bd68a87d4258baad8819b9d1cc7fmv2.png)



SW - HW financial aspect of failure (illustration)

In this illustration the curved areas represent a point cloud of failure events for either software or hardware startups. These are laid along the time axis, with the launch event somewhere in the midst of the time line (startups can fail before or after a major launch for hardware companies. For software companies, this point in time denotes the scale-up effort). These points are also laid along the vertical axis, denoting nominal damage.

You'll notice a different distribution of failure points for each industry, following the characteristics we discussed: Hardware entails building production capacity, inventories, and a distribution network, which weigh on the company's finance after launch, while software companies' risk normally increases in the scale up phase, then subsides dramatically.

---



#### Cost of timing

All things being equal, a late failure is more hurtful. Time cannot be reversed, both for investors and entrepreneurs, who'd rather succeed. Must they fall, they'd prefer failing quick, so they can entertain other opportunities, and such is the case for investors.

A simplistic approach to this question is looking at the book value of the startup in question, starting at capital injection with the amount investment, then dwindling, year after year, by the losses accrued - until (if successful) the course is reversed and returns on investment start to accumulate.

In this analysis,

**_Residual Value = Book value - accrued losses_**

Hence the conclusion of preference for <u><span>early failure</span></u>, as losses tend to increase over time for failing startups.

---



#### Cost of Production ramp-up

This is almost unique for hardware ventures. While R&D engineers may cost the same, physical infrastructures and inventories tend to be much more significant for those. Consider the costs for:

-   PPE - Plant, Property, and equipment (lease property, buy machinery and production tools)
    
-   Raw materials and components - which should be purchased in advanced, sometimes with order quantities pledged to insure lower cost
    
-   WIP and distribution warehouses, ex works and overseas
    
-   WIP and finished goods inventories
    
-   Distribution channel set-up and management
    

In the example below, I've listed only the direct expenses accrued in a single product development and production ramp-up process - a subset of the above list:

-   R&D (Engineering)
    
-   Prototypes
    
-   Tooling
    
-   Trial Runs
    
-   Testing
    
-   Regulation
    
-   Raw Materials & Components
    
-   WIP Inventories
    
-   Finished Goods Inventory
    

![Production Ramp Up NRE Accumulation](./images/73dd11_eed7d4f1d0c04392943919e7405c98bbmv2.png)

Production Ramp Up NRE Accumulation

Most of this (hardware specific) investment will be scrapped in case of liquidation, further increasing the negative impact of a potential collapse of the venture.

---



A good example of the fire sale residual value of Modu - an iPhone predecessor smartphone manufactured in 2007, now selling for $50 (about a third of original list price)

![Obsolete products may linger long](./images/73dd11_be414f30731343228267c09d5bcf03a9mv2.webp)

Obsolete products may linger long

---



Another, much more ubiquitous example, are off-season fashion items, which could go as low as 20% off list price:

![Seasonal price changes can be brutal](./images/73dd11_a938db7b4a9446c1a4992a05e6a1ec9cmv2.webp)

Seasonal price changes can be brutal



These stress the fact that once a product is discontinued, or becomes irrelevant, its residual price can plummet, effectively deepening the venture's loss.

---



#### Adoption Risk

Once we clear the development risks, a significant hurdle remains for all ventures, software or hardware related: Market adoption. For nothing can force adoption of your product, can it?

Luckily for software products, **lean methods** enable early testing of acceptance.

MVP (Minimal Viable Product), as it name implies it can be developed to a bare minimum, providing a key functionality, just to assess traction within the target audience.

![Scatter plot titled "Startup Failure Points: Stage vs. Financial Impact" with labeled points on challenges. "Consumer Adoption" is circled.](./images/73dd11_94c0f5834a204dadb68d62dced67fd30mv2.png)

Software startup failures: Stage vs financial impact

This way, further efforts can be made or avoided, both minimizing risk, or shuttering the business if feasibility is not proven. In fact, successful MVPs have become a standard, if not mandatory, requirement for many pre-seed investments.

As demonstrated above, this is hardly the case for a hardware product. Manufacturers will have to go the whole nine yards from conceptualization through production, accumulating direct and indirect costs, at risk.

![Graph titled "Hardware Startup Failure Points: Fatality vs. Financial Impact," with points on challenges like "Consumer Adoption" highlighted.](./images/73dd11_c994cc9bdde54b00bfa99e1ae9b18e70mv2.png)

HW startup fatality and financial impact

![Ford Edsel - Notorious F.L.O.P](./images/73dd11_4ae2a8f54acd4e4ca93780246c07f0e0mv2.png)

Ford Edsel - Notorious F.L.O.P

A spectacular example of such flop was the Ford Edsel. The first car designed by Ford from scratch in the post WW2 period.

It was such an important project for the company, it was named after the founder's son, as was the division dedicated to its production.

Market analysis, conducted by the corporate America traditions and standards, sounded pretty logical at the time, with the target audience identified as middle-class, up and rising, young families, and young executives.

The company designed several models, built mockups and prototypes, ran through focus groups, and during years 1956-1957 built Capacity, and launched with a marketing splash on what was named as "E-day"...

Two years later in 1959, all 18 models were pulled off the showrooms, at a stated write-off of $250 million, approximately $2.6 Billion in 2024 prices.

![Better Place: Where swappable batteries won't do](./images/73dd11_891c0b07b7834d87894cc058258c2dc9mv2.png)

Better Place: Where swappable batteries won't do

The Ford Edsel example is by no means to say they could - or should - have known better: Apparently, they played by the book, saved no expenses. But here is the thing: Doing everything right cannot and will not obliterate market adoption risks. This risk can be "managed" but not obliterated. And the sunk costs involved in hardware products make it especially painful.

Consider the market adoption failure of Better Place - the visionary swappable battery electric car by Shay Agassi in a major Joint Venture with Renault. As the first product of this startup, its spectacular failure sank the ship altogether, wreaking havoc in investors' finances - for the gamble was big: The $900 million dollars invested in the company, $1.2Billion in 2024 prices, went don the drain when the company bankrupted.

Notably, most of this capital was captured somewhere in the supply chain, effectively evaporating when sales and production stopped, and as the company liquidated.

---



### Interim conclusion (2)

Dont. Do. Hardware... That is to say, if you have a choice.

However, the physical world is the one we live in, don't we? We live in houses made of tangible materials, drive metal cars, use plastic implements, and eat food made of crops and living stock.

We **must** build physical goods - hardware, if only to have them run software.  

In the upcoming posts, I will describe how digitation and software improve also the fortunes of hardware products in general, and hardware startups in particular.


---

'***'

---

# Chapter 3 - Digital interface: Changing the rules of the game, for hardware

---
_Digital interfaces, evolving from simple dials and gauges to sophisticated touchscreens and beyond, have revolutionized hardware products. They offer greater flexibility, enabling iterative design and software-defined interactions, while also facilitating over-the-air updates and remote monitoring. As technology advances, the fusion of multi-modal input methods and communication protocols will further transform the user experience, blurring the lines between hardware and software._



![The humble 7 segment alphanumeric display](./images/73dd11_6bb2d511ffbd481ca3517473fe66e500mv2.png)

The humble 7 segment alphanumeric display

---



### Human machine interface - a historic journey

### Dials and Gauges

Remember that in their pure functional form, many products do not require human interface at all. Let's call this "Interface Generation 0"

![19th century bicycle. What interface does it need?](./images/73dd11_f53f768ba60e4ffea2b2a7630f8cb948mv2.png)

19th century bicycle. What interface does it need?

But then again, other products **must** have some kind of safety indicators: Left unattended, kettles would burn, Steam pipes could burst, and emptied fuel tank could stall your car - or worse. Enter Generation 1 interfaces, providing critical information to the operator, so they can adjust inputs to control critical processes.

The analogue devices that were developed to that purpose were dials and gauges

![Thermometer - you're still in the safe zone](./images/73dd11_866cfea541ca4fafb3efd9814cf774b8mv2.jpg)

Thermometer - you're still in the safe zone

---



### Digital interface for hardware changes it usage patterns

Something happened in the two centuries passed since dials were introduced: The information age stormed into our lives, with some of its initial manifestation: Digital interfaces, which I'll refer to as Generation 2 interfaces: Digital interfaces - hard coded and programmed, driven by integrated circuits:

![The humble 7 segment alphanumeric display](./images/73dd11_6bb2d511ffbd481ca3517473fe66e500mv2.png)

The humble 7 segment alphanumeric display

While early generations of these displays were built using LED arrays, the next generation used Liquid Crystal Displays. Each contiguous area is a single segment, wired to one of the IC IO ports.

![Liquid Crystal Display - much more flexible](./images/73dd11_a6caf4acbdf94e2eb6bebbafb22f5795mv2.jpg)

Liquid Crystal Display - much more flexible

You'll notice the graphic flexibility enabled in this 7 segment like display, although the size variations, and some lettering suggest that there is more at play than rigid diodes.

In the next example, a lot more artistic freedom is allowed, showing the limitation is in the IO count of the driving board.  

![Graphic LCD - with free form segments](./images/73dd11_285fd00880d042cc935aeb1db5cff172mv2.png)

Graphic LCD - with free form segments

I have made several of those: as free-form as they look, the initial setup took notes from chip lithography, and is quite rigid: Once you have the vector graphics, it is converted into a mask, and several weeks later, the prototype is ready (while you feverishly prepare the low code driver). Any error or change sends you back to the initial point.

The need to flexibility in design resulted in the dot matrix display, where a sophisticated IC driver control a lattice of columns and rows to lighten dots: A 100 by 10 matrix provides 1,000 pixels, but requires only 110.

![Dot matrix LCD](./images/73dd11_43ccf465f090401884bdacc482b32786mv2.jpg)

Dot matrix LCD

And as the industry progressed, higher refresh rates, higher pixel counts, and the introduction of color (let alone the introduction of sound) culminated in the displays we have come to accept as the standard.

![Nintendo Gameboy: Color dot matrix and rich sound](./images/73dd11_44e1dda8bc744391969fa164c4835695mv2.jpg)

Nintendo Gameboy: Color dot matrix and rich sound

A whole world of gaming, but also interface conventions, grew out of this platform.

------



### Touch! and more

As touch interface came in, physical buttons, with their rigid placement and behavior, gave way to software defined interface.

Designers can place buttons and model complex interactions almost regardless of physical limitations, focusing instead on ergonomics and cognitive human factors, and - even more importantly, with the ability to iterate furiously.

![The touch feature is just another layer](./images/73dd11_92f86aeb131f4c25855be4cf127dd3ffmv2.png)

The touch feature is just another layer

The initial paradigm stems from PC graphical interface (using single touch mouse click and drag). Soon enough, however, multi touch gestures, such as pinch, spread, and rotate, evolved, as single touch gestures evolved, to create a rich interactive environment.

---



### On Air!

This section should be named: "How I Learned to Stop Worrying and Love recalls". Those of you in the manufacturing domain know how dearly recalls cost: The loss of face, the cost of shipping back and forth, the possibility of sending a technician to mount a pole 5 hours drive from the nearest airport, just to update some firmware... Could all this be gone?... 🥹

Enters FOTA (Firmware Over The Air), with pioneers such as Red Bend (acquired by Harman International) and provided the magic capability of downloading a new version of an operating software, and rebooting safely to the new version without losing data.

Ubiquitous today, for any smart phone, it was revolutionary at the time. It is still a game changer today, with players such as Tesla, totally disrupting the mobility world with its electric drive train, but also with its magic-like overnight upgrades:

![Tesla: Overnight firmware update - for your car](./images/73dd11_81e851d1d4a6447abf7706eaac101e96mv2.png)

Tesla: Overnight firmware update - for your car

If you are a Tesla owner, you could have find one morning, that the range has increased by a 100Km, or that 0 to 100Kph was cut by more than 50%, in steps called "Insane" and "Ludicrous" modes.

While 0 to 100Kph is a car-nut thing (can't use "petrol head" for an electric car, sorry about that), the effective range of eCars is a huge pain point.

Another user delighting feature was when, one Christmas eve Tesla owners found their heating system turned into a virtual fireplace:

![](./images/maxresdefault.jpg)

https://youtu.be/iWI8bfK2wAQ?si=5ASYlXL6aXdj_fPr

I mean, these are very effective differentiating features, and traditional car manufacturers just cannot cope with such ferocious tactics.  

As a matter of fact, digital interfaces are perceived today as the most differentiating factor for cars. Consider this, though: Ford Model T and today's most flashy cars perform a very similar task: Allow a driver transport themselves and their passengers as fast, and as agreeably as possible.

![Ford Model T and digitally enabled car](./images/73dd11_dd265fe3e5d84afebdc2482729e40572mv2.jpg)

Ford Model T and digitally enabled car

But in the nearing future where driving will be a thing of the past - what is a car, if not a smartphone on wheels?

![The driverless car - a smartphone on wheels](./images/73dd11_3fbd62e23148418d9fe773a3ec6d8e59mv2.png)

The driverless car - a smartphone on wheels

---



### Fusion

The last frontier is the fusion of multi-modal input methods, some explicit and others which do not require user action, into the interface of hardware products: Accelerometers, heartbeat, temperature, visible and hyper-spectral imaging sensors (I mean, cameras), as well as sound sensors are all now integrated, allowing advanced functionality.

![multi modal input methods for mobile and wearable devices](./images/73dd11_31bbddd7e48345b7ab03570cac0a8f17mv2.png)

multi modal input methods for mobile and wearable devices

Inputs are by no means the end of it, as communication protocols supported by our devices proliferate for data transfer, monitoring, and activation. Digital interface for hardware takes center stage offering new user interaction, creating new value.

![NFC - Near Field Communication - used for activation](./images/73dd11_11592be716dc48018c4c953299d9938emv2.png)

NFC - Near Field Communication - used for activation

---

'***'

---

# Chapter 4 - Product Managers in the Hardware industry

---
_The rise of digital user experience and interfaces in hardware products, particularly in the automotive industry, necessitates a shift in product management practices. This involves a focus on software-driven interface design, continuous customer feedback, and post-launch improvement, similar to software product management. Product managers in the physical world face challenges like validation, which involves market research, user testing, and data analysis to ensure product success._

---



![Hermeus Quarterhorse - Is this Product management?](./images/73dd11_579ba8f1b84e48658c37716973d2904fmv2.png)

Hermeus Quarterhorse - Is this Product management?



### Product management for hardware is now a thing, too.

As we saw in the previous chapter, the importance of digital user experience and interfaces has risen dramatically, overshadowing other parameters, as shown for the example of the automotive industry:

-   Brand and design aesthetics?
    
-   Fuel efficiency? sustainability?
    
-   Other hard wired features?
    

It seems as if these are now commoditized, expected as a bare minimum as part of the emerging electric car trend.

The user interface is an increasingly important part of what makes a product useful, and this calls for software design and product management practices to build these features successfully. Product management for hardware is now a thing, too.



![Interface design as a differentiator in the automotive industry](./images/73dd11_a14779c82b2f4cf9aab48bf7694f7e91mv2.png)

Interface design as a differentiator in the automotive industry

What's more, the relative effort and cost of interface design increases as its importance grow, and as it emerges as the most differentiating competitive factor.

Is it just a coincidence that companies such as Apple and Samsung contemplate entering the automotive market?

In a world where physical features are the base norm, it only makes sense.

![Relative cost of interface design in physical goods](./images/73dd11_ea2f8b844fcd4e9abd20f44026f1e22bmv2.jpg)

Relative cost of interface design in physical goods

---



### Why should product managers care?

As digitization seep into the physical world, we see the shift in focus for hardware product departments, from design aesthetics, comfort and luxury towards (software driven) interface design.

![digitization drives software product management style](./images/73dd11_5bb42dd2f1c94444811010ad754aa572mv2.png)

digitization drives software product management style

As software processes enter the physical product world, the industry reacts by borrowing roles from pure software, leaving only a few hardware specific ones:

![Product management role shift](./images/73dd11_dbda3939057a47c28f9417a4bf78da06mv2.png)

Product management role shift

Contributing to this is the opportunity for maintaining a continuous relationship with customers, exchanging feedback with continuing revenue (all this by delivering continuous improvement).

![Can physical products be sold as a service?](./images/73dd11_1e1e2e1e3d2f48fdbe2f12c02a98cb99mv2.png)

Can physical products be sold as a service?

Indeed, when products are - at least partially - connected and digitized, there is a lot that can be done **after** launch to improve usability, strengthen customer satisfaction, and reinforce brand loyalty.

![PM activities migrate post launch](./images/73dd11_43c799f2053644b0b9993cc2ac6918f2mv2.jpg)

PM activities migrate post launch

Now look at the activities surviving launch:

-   Remote troubleshooting and support
    
-   Iterative design improvement (also firmware updates and maintenance)
    
-   Data collection and analysis
    
-   End of life management (this is hardware specific)
    
-   Warranty and support
    

Aren't these ringing a bell? Did I hear someone saying CI/CD?...

While many aspects of continuous development and integration are technical, this practice calls for involvement of product managers, that would collect and integrate user inputs into actionable roadmaps.

The long and short of this is: There are more challenges, more opportunities, and increasing demand for product management talent in the physical product space.

---



### Validation - the most strategic task for physical products PMs

The most strategic role of product managers is - in physical products as well - deciding what products do we build. This role is divided into two sub tasks:

1.  **Initiation**: This is the part where market trends, competitive edge, and positioning combine to create an initial assumption of what the product would be. The most fundamental decisions: Materials, functionality, price points, and a myriad other characteristics are baked into a product that should deliver a unique selling point, matching the go to market and the positioning statement for this product, within the context of that particular firm.  
    
2.  **Validation**: This is the tricky part, where you prefer to avoid the substantial commitments to production capacity and inventories just to prove a point (what is you are disproved?)
    

The crux of that painful experience was that sometimes, even if you do everything right, the real world might not embrace your product, regardless of the focus groups, the alpha and beta testers, the design partners, and whatever you put into validation - even before the first specimen rolls off the production line.

Contrary to pure software products, there is much less room for pivots: You are saddled with those up-front investment, bound to turn into sunk costs and a hole in your financials.

The risks of physical production still linger today as well, but luckily, the all-important digital layer offers opportunities for improvement before and after launch.

Validation would then mean the following activities:

-   Market research, focusing on positioning and product features
    
-   Qualitative user research - How would, and this pertains both to b2c and b2b users, this product fit into the customers lives?
    
-   Quantitative, to the extent possible - measure usage, purchasing patterns, price sensitivity, support calls, maintenance...
    
-   Mockups, prototypes, proof of concepts: Test as many aspects of the product as possible: For example, I had the chance to use a demo console and infotainment unit by Ford mobility - physically emulating the steering wheel, screens, dials, and all controls to test applications built for its app-store.
    
-   Once the product is launched, and assuming a connected device, measure streams of data to validate the success of the user flows we had in mind.
    
-   Optimization and continuous improvement, through software updates, bug and security fixes

---



### Validation. Yes, but how?

Hermeus is on an ambitious mission to develop a hypersonic (4 Mach) plane. It is a challenging exercise in validation, where physics, mechanics, fluid dynamics, avionics are stretched to new limits.

![Hermeus Quarterhorse: Ambitious goals](./images/73dd11_fd3179b0f1264e38bcfaaaf306787068mv2.jpg)

Hermeus Quarterhorse: Ambitious goals

The first steps of validation are prototypes and proof of concept experiments, gradually testing system components and their integration. No users are to be seen, but test beds, wind tunnels, thermal and mechanical tests - everything needed to ensure this technological marvel takes off to the sky and returns in one piece.

![RAMJET is tricky. Assembly floor](./images/73dd11_6412a35190dc4e54b39da7668dc9e3cbmv2.jpg)

RAMJET is tricky. Assembly floor

The validation here is risk mitigation at the system-engineering level. This is pertinent to any hardware product facing real world mechanical challenges, even before full scale build and operation by humans.

![](./images/maxresdefault.jpg)

https://youtu.be/M35y-sZz1r8?si=1ZqVzxGet3wlh6cf

The aviation industry is 120 years old, and many of the obstacles are known, but - as we've seen recently, with Boeing 737 Max debacle(s) - knowing about them and dealing with them are not synonymous.

![Flight 1282: Safety is a product feature](./images/73dd11_1a2345ce76294da2899a3356e5f4f7e6mv2.jpg)

Flight 1282: Safety is a product feature

Boeing obviously failed on the base of the pyramid - Safety. Apparently, with the notoriety Series 737MAX earned, there is a cultural problem with the company...

![The requirement pyramid. Ashby, M., & Johnson, K. (2003)](./images/73dd11_beb673ef0f654a669b47e5b55ab3c8b3mv2.jpg)

The requirement pyramid. Ashby, M., & Johnson, K. (2003)

In the coming chapters, I focus on the higher echelons of this pyramid, and how they pertain to product management practices.

---

'***'

---

# Chapter 5 - Physical Products: Early Validation is Key



Throughout this book, I hope I made clear of the "one-shot" nature of physical product launches. The resources required are high enough to sink most ships. An established company may take the blow, but for startups for which the launch is of their first and only product, any failure could be one too many.

This is different to pure software products, which are by nature much more agile, and could pivot at a tolerable cost and over a reasonable timeframe.

This is all to demonstrate why early validation is key for physical products. Timely validation is so important for physical products, and by "timely" I mean: before unrecoverable resources and precious time are spent.

The questions for validation, though, remain the same:

-   Do users need your product?
    
    -   Does your product fulfill its functional promise?
        
    -   Is it safe?
        
    -   Reliable?  
    
-   Can users make use of your product?
    
    -   In all of its usage scenarios
        
    -   Does it require appropriate level of training (as in self explanatory for consumer goods)?
        
    -   Do you offer adequate support?  
    
-   Is your product perceived favorably by users?
    
    -   Can your users experience your unique value proposition?
        
    -   Is your USP in synch with your positioning?
        

The challenge with physical products is how to expose them so that validating signals are strong enough.

---



### Cyclebe - A cautionary tale

### The problem

![Bicycle positioning beacon. Design by Yamma](./images/73dd11_40499f92daeb4f1a8c3b0c66f28d1bbamv2.jpg)

Bicycle positioning beacon. Design by Yamma

This bicycle positioning beacon was born to answer a major safety need: Riders cycling along country roads risk being swept aside by car and truck drivers bypassing them. A potentially fatal hazard, tragically materializing more often and not.

The solution is a dual facing system, collecting positional data from a GPS enabled device, sending them to the cloud, where navigation software access these data so drivers are aware of pelotons and drivers ahead.

Great idea, which was initially materialized as a mobile app. This solution, though, encountered headwinds: Battery life turned to be too short, and other sports applications, namely Strava, started to provide a very similar functionality, eroding Cyclebe's competitive advantage.

---



### Solution

The company decided to look for hardware as a differentiator - a physical device, that would pack the location and mobile communication (a GPS / M2M cellular module) with a strong taillight - all within an iconic packaging.

![Cyclebe: Sub assembly and components](./images/73dd11_4357197978774dd2ab6b7ab3eb915bc6mv2.png)

Cyclebe: Sub assembly and components

As we moved along, the industrial design of the unit was completed, engineering issues addressed:

-   Shock resistance
    
-   Water tightness
    
-   RF communications (m2m module)
    
-   Battery life cycle and charging
    
-   Taillight stroboscopic elements
    
-   Prismatic lens
    

Initial prototypes and mockups were built:

![Cyclebe: design prototype](./images/73dd11_6c4b635677024948bf770007872f2a5emv2.jpg)

Cyclebe: design prototype

We also performed initial unit economics:

-   BOM (Bill Of Materials)
    
-   Labor costs
    
-   Packaging, shipping
    
-   NRE (Non Recurring Expenses)
    
    -   Production tooling
        
    -   Testing equipment
        
    -   Minimal inventories
        

All these to establish unit costs (as a function of quantities produced), and to find BEQ (Break Even Quantities) that would be the lower limit to production, to serve in the go-no go decision.

---



### Omissions:

What did we fail to take into account?...

-   Users willingness to pay: This device's BOM poses a hard lower limit on cost. Would users pay this non trivial amount?
    
-   What would be the cost of the alternatives / competing products? As it turned out, virtually $0...
    
-   What were the trends in this domains? Here too, mobile phone turned to be the Swiss army knife, that may not excel at anything, but can do most things satisfactorily. 
    
    ---
    
    

### Lessons Learned

Decision time has come for Cyclebe, and - attractive as it may look and feel - the company had to kill it off.

There was no way the additional cost would be justified by users, and the significant effort required to develop this multi disciplinary product turned to be redundant.

The lessons learned, though, is that sometimes one must explore ideas by developing them. This is how you unearth hidden costs, physical obstacles, engineering constraints.

This is how you can find out about your up front (NRE) and current expenses (unit economics), and how you learn about the problem you are solving, through early validation, and early go-no go decisions.

> In established companies, this is part of the innovation effort, budgeted to run similar experiments, picking one of many to progress to manufacturing and launch.
> ---

---

'***

---

# Chapter 6 - Validated Ideation

The Fiona Effect: As products progress towards production, the balance between imagination and maturity shifts.

---
### The "Fiona effect" in (physical) product validation

_Concept cars evolve from fantastical to realistic during the validation process. Manufacturers use these evolving designs to test market acceptance and refine features, balancing imagination with practicality and risk. Autonomous vehicle concepts illustrates this process, with technology and user needs shaping the final product._



![Rolls Royce 103EX concept driverless car - revolutionary interiors](./images/73dd11_c4dbae10b68d4865b09c73b50992b7d7mv2.webp)

Rolls Royce 103EX concept driverless car - revolutionary interiors

---



### Shrek: The Movie

Remember Princess Fiona, the female protagonist, who were cursed by a witch, and while she continued to be a beautiful lady during the days, transformed into an ogre by night?

![Fiona charm removed: Be careful what you wish for](./images/73dd11_7e138f01b6f040bdadc1765b60302e67mv2.jpg)

Fiona charm removed: Be careful what you wish for

The bitter sweet ending of this film removes the curse of her, but the end result is that she finds peace as the ogre bride of Shrek. Tears and joy!

Now how this "Fiona Effect" translates into the product world?....

---



### Motor shows and the fantasy concept car

Beside being major industry events, auto-motor shows are a rite of passage for usually young, male, motor-heads and would-be product designers, who wander the isles of these consumer heavens with awe widened eyes, drooling on fantasies they would probably never put their hands on.

![Motor show](./images/73dd11_d6b14d78aacf42eb937a031cebb93351mv2.jpg)

Motor show

The technology industry has similar expos, meticulously orchestrated to spur demand, not only for the current fiscal year, but for the upcoming generations of products as well.

This is where manufacturers test acceptance for their wildest ideas and for their progressively maturing concepts. In the case of auto-motor shows, of the ultimate consumer product - the car.

The farther away the future a concept model describes, the bolder it is:

![The Rolls no one will presumably ever drive](./images/73dd11_3084e11266b5486f898e6f9672cf2154mv2.webp)

The Rolls no one will presumably ever drive

---



### Validated ideation and the development cycle

Consider the development cycle of a passenger car. While the time it takes shrank since the 1980's from 8.6 to "just" [<u><span>6.7 years</span></u>](https://www.cargroup.org/automotive-product-development-cycles-and-the-need-for-balance-with-the-regulatory-environment/) ", costs continue to be excruciatingly high. [<u><span>Development budgets</span></u>](https://www.autoblog.com/2010/07/27/why-does-it-cost-so-much-for-automakers-to-develop-new-models/) vary from $1billion and $6 billion US, depending on whether it's built on an all-new platform with new engine and transmission systems, or not.

It is easy to see how high the stakes at hand are. I have referred extensively to the cost of failures in the [<u><span>second chapter</span></u>](https://www.theroadtlv.com/post/product-management-for-the-physical-world-part-ii) of this series to discuss these ramifications.

The trouble is manufacturers cannot know before hand what would the world look like 7-8 years in the future, and to what extent would decisions made early in the design process prove successful at launch, billions of dollars sunk into the process.

That is why you see all these eye popping concept cars and flying soccers, so to speak, in industry shows. Part of the design is indeed meant to attract media and enthusiasts attention, but another part is dedicated to testing the acceptance of feature sets - progressively approaching reality (and some would say dithering) as the launch date comes near, and the final bets are placed.

![From ideation to launch - intermediate validation](./images/73dd11_90bbc040a3ac4eb2ae8ef2d4235691b8mv2.png)

From ideation to launch - intermediate validation

---



### Fantasy and Reality during the Validation cycle

Going to these shows, one can see that as concept cars progress towards production, the balance between imagination and maturity shifts, while the commercial risk level decreases.

![Imagination, maturity, and risk on the validation cycle](./images/73dd11_dde6e9d71c244319be0c6e5d7a651dc3mv2.jpg)

Imagination, maturity, and risk on the validation cycle

Initially, concept cars are embodiments of pure creativity and futuristic thinking, showcasing bold designs, innovative technologies, and radical ideas.

However, as a concept car moves closer to production, practical considerations such as safety standards, manufacturing feasibility, cost-effectiveness, and market demand shape its evolution. This process may lead to the dilution of the original concept's most ambitious elements to meet these real-world constraints, resulting in a production model that retains the essence of the concept but in a more refined and practical form.

---



### The Driverless car: A case at hand

![Rolls Royce 103EX Will this version of the future ever materialize](./images/73dd11_c4dbae10b68d4865b09c73b50992b7d7mv2.webp)

Rolls Royce 103EX Will this version of the future ever materialize?

I will not dive too deep into the autonomous vehicle debate in this post. Suffice to say that the technology is a few years ahead, and naysayers would argue that it shall always remain that way.

It is neither clear what underlying technologies would enable this radical change of the passenger car, from a driven vehicle to an autonomous cocoon.

Would these technologies include Lidar? Hyper spectral cameras? High density mapping? Continuous connectivity? Would a bypass option be mandatory?

The concept above entertains the possibility of complete, permanent, hands off travel experience, with your chauffeur poignantly missing (maybe they're on the roof stand, whipping the horses, and we're back at the 19th century.

Will the next two version of this luxury car manufacturer be that autonomous? I seriously doubt it. After all to most Rolls Royce customers, the driver is a mandatory feature, and anyway, who'd open and close the doors for you?

What we do learn from this design exercise, for this is what concept cars are, is how different elements combine to embody a certain vision. The vision will necessarily change over time. A more realistic understanding of the possible use cases for autonomous vehicles will emerge as manufacturers and regulators make necessary concessions, and marketers identify segments where this concept serves best.

![Waymo - Zeeker: Rider-first autonomous vehicle platform ](./images/73dd11_af7832e4f19845d2a049c271368b0362mv2.jpg)

Waymo - Zeeker: Look Ma, no hands!

What a drab, or rather, a sobering vision...

True: No driver in this Waymo / Zeeker Rider-first autonomous vehicle platform. But forget of the country roving luxury car for now...

---



### Lessons learned

> The autonomous vehicle is a hard nut to crack: A combination of user needs, economic realities, regulatory constraints, technology hurdles will allow for initial business cases to test, and if they succeed, the envelope will gradually push the envelope.
> ---

---

'***'

---

# Chapter 7 - Lean hardware? Yes, We Can



![Espro i-Led IR Beacon](./images/73dd11_9b88cf19c42f46a6a15dac586758672cmv2.jpg)

The Unsung Hero of Modern Museum Experiences: Espro's IR-Beacon

Ever found yourself wandering through Moma, a sleek audioguide pressed to your ear, telling you about the artwork you're standing in front of? Did you wonder how it knew exactly which masterpiece had caught your attention? Let me introduce you to the humble ceiling-mounted infrared beacon – possibly the most important museum innovation you've never noticed.

---



## When Punching Numbers Became Passé

For those who've visited internationally acclaimed museums over the past quarter-century, you're likely familiar with the ritual: approach artwork, locate small numbered placard, punch digits into handheld device, listen to cultured voice explain why that blob of paint is worth more than your house. It's a time-honored tradition, like gift shop sticker shock or accidentally setting off alarms by leaning too close to the Picassos.

![Espro Audioguide](./images/73dd11_05e6c4dbc5144220befdeae7b38661b7mv2.jpg)

Espro Audio- guide

But museum curators, ever the visionaries, began dreaming of a more seamless experience – one where visitors could flow through exhibits like enlightenment-seeking salmon, absorbing cultural knowledge without the indignity of number-punching. The future, they declared, was hands-free.

---



## Enter Espro Systems

When Espro Systems (later acquired by Acoustiguide) set out to revolutionize their audioguide technology, they split the challenge in two: Redesigning the handheld device (handled in collaboration between Cortex design, Tiko Design and Aran R&D) – and creating the ceiling-mounted IR beacons that would silently trigger the right audio at the right moment – a task that fell to me.

---



## The Brief: Invisible Magic

My assignment was deceptively simple: create a device that would collect power and coded signals from ceiling wiring, then beam infrared codes downward to activate passing audioguides. The beacon needed to precisely control which areas would trigger which information, all while remaining as inconspicuous as a security guard at a royal wedding.

![Original sketches for the briefing](./images/73dd11_accb351752974313b3a75bfb5f1d6c9emv2.png)

Original sketches for the briefing

---



### Stage Lights for Invisible Shows

![A classic stage spotlight](./images/73dd11_09e4f29f7eba47feb2959154be47c268mv2.png)

A classic stage spotlight

Since infrared light behaves like visible light (just with worse taste in wavelengths), I turned to the world of theater for inspiration. The humble stage spotlight offered everything we needed:

-   **Focal adjustment** to control beam spread (because nothing ruins a museum experience like hearing about the wrong ancient pottery)
    
-   **Directional flaps** for defining beam boundaries (keeping the Monet commentary from bleeding into the Manet section, a faux pas of the highest order)
    
-   **Rotation and tilt mechanisms** for precise aiming (critical for ensuring visitors hear about the dinosaur they're standing under, not the one that would eat them three exhibits away)
    
-   **Stencil holders** for creating irregular coverage shapes (think Batman's signal light, but for triggering audio about Renaissance sculptures instead of summoning caped vigilantes)
    
    ![Batman stencil casts batman shaped light](./images/73dd11_b090de89851d4d3094a9e3df4f770a27mv2.jpg)
    
    Batman stencil casts batman shaped light
    
    ---
    
    

### The Hidden User Experience

The true "users" of this spotlight system weren't museum visitors, who ideally would never notice its existence, but the installation technicians – those unsung heroes in work clothes who would mount these devices, connect the wiring, and painstakingly adjust beam patterns while standing precariously on ladders.

Once installed, these beacons would blend into the ceiling architecture like introverts at a networking event – present but unnoticed, silently doing their job for years while taking none of the credit.

![Sketch drawing of the beacon ](./images/73dd11_76a58cf3e0cc469d822efbd6e69e97bamv2.jpg)

Sketch drawing of the beacon

---



### Lessons from the Invisible Infrastructure - Lean Hardware Product Management

What can we learn from this seemingly simple device that helped transform museum experiences worldwide? And why this project turened to be an exercise in lean hardware product management?

#### 1\. Scenario Before Solution

Before diving into design, we established clear usage scenarios. Where would visitors walk? How would they interact with exhibits? What information needed to be triggered where? These spatial and behavioral patterns determined every aspect of the physical design.

#### 2\. Form Follows Function (But They're Still Dating)

Once requirements were clear, the merger of form and function happened naturally. The spotlight archetype wasn't chosen for aesthetic reasons – it was the perfect existing solution to the physics problem at hand.

#### 3\. Design for Real Life

Beyond just manufacturing concerns, we had to consider the full lifecycle – installation, adjustment, maintenance, and eventual replacement. A beautiful design that can't be installed correctly is like a priceless painting hung facing the wall.

#### 4\. The Bill Always Comes Due

Finally came production reality: tooling, assembly processes, and the sobering revelation of manufacturing costs. As with any hardware product, the distance between prototype and mass production is measured in compromises and currency.

#### 5\. Lean Hardware means...

In this case, the whole process from idea to manufacturing took 5 weeks, while the use of fast tooling for small production batch kept schedule and costs at bay. And here is the lesson: Quick experimentation at reasonable costs allow for better product market fit, so elusive in the hardware industry.

### Hardware: It's Systems All the Way Down

What this project reinforced was that hardware product management is often more systems engineering than anything else. While the software world can deploy updates with the click of a button (and fix the inevitable bugs with another click tomorrow), hardware demands getting it right the first time.

The humble ceiling beacon required considering everything from electrical standards across different countries to the patience threshold of installation technicians to the walking pace of museum visitors. It needed to work flawlessly for years without attention, bring joy to users who would never know it existed, and do it all on a budget tight enough to make a museum accountant smile.

Next time you're in a museum, enjoying the seamless experience of information appearing in your ears just when you need it, glance up at the ceiling. That inconspicuous little device you probably won't even notice? That's my silent spotlight, still stealing the show after all these years.

---
'***'

---

# Chapter 8 - Product Valhalla: When Service Evolves Into Relationship

## 

> Connected products enable creation of continuous customer relationships and value added services.

---
_Connected hardware products offer vendors the opportunity to provide continuous value to users through firmware updates and services, creating lasting relationships and increasing revenue. This shift in business model, exemplified by companies like Tesla and Apple, enables vendors to generate significant revenue from services and user engagement. Product management plays a crucial role in identifying and capitalizing on these opportunities for product innovation and user-centric development._

---



### Product Management for the Physical World Series: Part VII

![](./images/maxresdefault.jpg)

https://youtu.be/iWI8bfK2wAQ?si=R-3I_4kdh8kpfDiH (link to video)

---



### Service and relationship opportunities

Consider the scenario depicted in the video above. One morning in late November 2018, Elon Must tweeted the following:

![Elon Musk announces new Tesla features](./images/73dd11_8111524cfc4843618fd386a1d8218b12mv2.png)

Elon Musk announces new Tesla features

The next morning, some Tesla owners woke up to find "Romantic mode" as they tried to heat their cars in the chilly morning of November 30th.

![Automated FOTA message](./images/73dd11_97f7241586b44436b29245cdf4ee8955mv2.png)

Automated FOTA message

The update, automatically available after an overnight firmware update, also included gems such as "fart mode" which emulates flatulent sounds when the passengers take their seat. Class was never the hallmark of Mr Musk's endeavors, if one ever needed a reminder.

This FOTA functionality - Firmware Over The Air - allows technology vendors constantly improve their field deployed hardware, without recalling them to the lab or service station.

This approach bears many benefits at the operational level, reducing costly recalls, and ensuring broader standardization of the install base (think of the automatic updates of iOS, MacOS, Windows operating systems, constantly improving user functionality and security).

Funny and delighting as they might be, the Romantic / Fart modes offered by Tesla were far from the most radical, though.

In a series of other [<u><span>regular updates</span></u>](https://electrek.co/2019/11/01/tesla-model-3-long-range-increases-range-price/#:~:text=Tesla%20is%20as%20much%20a,to%20date%20and%20new%20cars.), users found their car's range (a coveted and anxiety inducing quantity for any electric vehicle owner), speed, and acceleration augmented overnight increasing.

Compare this to the slow progress offered by traditional car makers. You'd get a significant improvement in next year model, if at all.

---



### The power of (commercial) relationships

Take a look at the following layer model for connected hardware products. You'll notice higher abstraction (and gradual distancing) from the physical hardware, and moving into the domain of services - not in the technical meaning of the word, but more in the sense of continuous value bestowed on the users, as long as the vendors want, that is:

![Proposed Layer model for connected products, and the value added services they offer](./images/73dd11_c0c67db1012b466682cdcfb97524e0cdmv2.png)

Proposed Layer model for connected products, and the value added services they offer

Indeed, these value added services (iTunes, Chrome browser and search, car navigation systems) create significant value to users, providing significant revenue opportunities, and reinforce customer loyalty: Users abhor the need to migrate their personal data between platforms, and value dearly the promise of a one-click hardware upgrade. We see that the technology of connected devices opens for improved (technical) service, but even more so, to increased opportunities for creating a lasting, meaningful, and positive customer relationship, that would pay in the next hardware replacement cycle.

---



### Shifting the business model

Vendors place high value on the possibility to create and maintain a constant, meaningful, and positive relationship with their customers. Connected products offer this possibility for the first time, and industry pioneers are experimenting with it, creating a lot of additional value from it.

![Apple Inc. Revenue sources](./images/73dd11_b2d1ce74fdac4757abc34ab64ca59e6emv2.png)

Apple Inc. Revenue sources

Apple, originally a hardware vendor, manages to generate significant revenue from the Services segment, with a high gross margin of 71%, **mostly enabled by connected hardware.**

---



### Conclusion

This series draws to an end, at least discussing the strategic trends driving hardware product innovation, and its impact on product management.  

Indeed, if Product Management embodies the discipline of identifying 'what to build', we are seeing new opportunities for early validation, de-risking, and building products users love.

> Further, we can try and identify new opportunities for product evolution from a inert mass into a living and breathing ecosystem of physical and abstract capabilities, expanding user engagement and eventually increasing economic potential and value.
> ---

---

'***'

---

# Chapter 9 - Validate, Before It's Too Late: De-risking physical products

> The urgent need and strategies for physical products early validation, and focusing on differentiating aspects and features.

---
_Physical product validation is crucial due to the high costs and inflexibility of hardware development. Market need and positioning analysis are essential, followed by feature validation through mockups, prototypes, and user testing. This process helps identify and prioritize features, ensuring the product meets user needs and aligns with market demands._

---



![Analytic dashboard showing events of interest](./images/nsplsh_4168344636672d4f6d6749mv2_d_4032_3024_s_4_2.jpg)

Analytic dashboard showing events of interest

---



### Physical product validation MVP Challenge

An MVP, or a Minimally Viable Product, is a development stage used to create a new product with enough features to attract early adopter customers and validate an idea early in the development cycle.

While software products are easily amenable to this strategy, in part for their modularity and the vast underlying infrastructure in place.

Consider a mobile application, or a web app. Most of what's going on are infrastructures that cater to ALL apps, and are reused innumerable times.

![Software development - Standing on the shoulders of giants](./images/73dd11_93d837a0b2b14520bbc9dd38f8828387mv2.png)

Software development - Standing on the shoulders of giants

Note how shared web infrastructures, cloud included, are built to serve billions of users (beside your own app users).

It is fair to say app developers stand on the shoulders of giants, and as a result, the pace and scale of innovation they can bring is without match, notably because the infrastructure is built to support multiple tech-stacks and business cases, so that, should you pivot, you are not to loose a lot of the things that make your product tick.

---



**That is not the case with physical products.**

The challenge with meaningful MVP creation in hardware products is that, from a functional point of view, they are often <u><span>integrated monoliths</span></u>.

By this, I refer to the need to recreate almost every part of critical functional layers, with limited potential for component reuse.

Consider the main subsystems for a typical passenger car. These subsystems are characterized by different availability and development costs.

Notice that with the exemption of infotainment and control systems, the most differentiating factors are also the most expensive parts of any car development.

![Car Subsystems: Specificity, Cost, Value](./images/73dd11_288b543e7d204ee9b6a21fbea5e4e82bmv2.png)

Car Subsystems: Specificity, Cost, Value

The lead time and cost of recreation of manufacturing infrastructures and replenish critical inventories for these systems are much too prohibitive, and in fact are equivalent to the launch of a new model altogether.

Passenger cars are at the extreme of this continuum, but in general, physical product face similar rigidity in their development process, meaning that unless they operate within an extremely cash rich environment, physical product innovators have one bullet in their proverbial pistol.

This makes the challenge of early validation even more acute:

-   How can you experiment?
    
-   Can you bring your product in the hands of users, before all costs are sunk?

---



### Problem Validation

> _"Fall in love with the problem, not the solution" (Uri Levine)_

This quotation addresses one of the most common fallacies within early stage product companies: Talented and motivated teams could and frequently would fall into the building stage fast. This is a symptom of a problem known as "a solution in search of a problem".

![A screaming robot. Sure you don't need one?](./images/73dd11_8d44e7d2a34d42ccbbc189b9d9626942mv2.jpg)

A screaming robot. Sure you don't need one? Source: *Green, K. (2013, January 9).* *On Fire* *[Comic strip]. Gunshow.* https://gunshowcomic.com/513

But whereas pivoting software products might still be possible (at cost), steering massive manufacturing infrastructures efforts oftentimes proves impossible. Usually there is not enough time, and not enough money to change course.

Validation, therefore, is key to success. But how does one do that?

---



### Market need and Positioning

First comes a sound understanding of market dynamics (size, trends, and gaps), the competitive landscape, and customer needs.

From there, analyzing competitors’ features, language, and messaging allows us to build **positioning maps** – visualizing the “lines of battle” along which brands compete for space in customers’ minds. These dimensions form the axes for plotting different brands.

With established categories, this can be enriched with perception surveys: first asking a broad sample of customers which factors matter most to them (a qualitative research), then prioritizing these and having respondents rate brands along the selected attributes (a quantitative research). 

The aim is to capture perceptions – how customers *experience* and *rank* these qualities – rather than technical specifications, since positioning maps reflect the market’s mental landscape, not the manufacturer’s.

---



Consider as an example the following (hypothetical) perceptual map for the smartphone market, which is centered in this case around "feature - like" qualities: the available **range** of models, and the perceived **level of technology** integrated into the brand's product.

![Feature based perceptual map for smartphones](./images/73dd11_89b4b0146c914892a0ba4e4937514baamv2.png)

Feature based perceptual map for smartphones - [Interactive feature](https://yoelf22.github.io/positioning-map/perceptual_mapping_dashboard.html)

Were you a product manager for Pixel 7a in this example, you should be worried about the perception of your brand within the surveilled audience. There is a gap between the group of leaders and the rest - and your product is lagging.

If I were a product manager with Pixel 8Pro, I'd be thinking really hard how to build up performance and camera quality, to move further up the leaderboard.

Such perceptual maps help us understand our place (for existing brands), or where do we want to be, when planning new products. They show us what are the needs important to users and customers within the market segments we're after, therefore enabling us to design features tailored to better cater to them.



---



### Feature scoping by competitive analysis

Consider the following competitive feature review by [<u><span>Insight Quantum</span></u>](https://www.linkedin.com/pulse/mastering-market-step-by-step-guide-crafting-comprehensive-wgfbc/), listing key features and their relative scores

| Car Model    | Horsepower (out of 5) | Torque (out of 5) | City MPG (out of 5) | Highway MPG (out of 5) | Crash Test Rating (out of 5) | Infotainment System (out of 5) | Driver Assist Features (out of 5) |
| ------------ | --------------------- | ----------------- | ------------------- | ---------------------- | ---------------------------- | ------------------------------ | --------------------------------- |
| Kia Seltos   | 4                     | 4                 | 4                   | 4                      | 5                            | 5                              | 4                                 |
| Competitor 1 | 3                     | 3                 | 3                   | 3                      | 4                            | 2                              | 2                                 |
| Competitor 2 | 5                     | 5                 | 5                   | 5                      | 5                            | 5                              | 4                                 |

Table 1: Competitive feature review (Insight Quantum)

The table can be translated into a spider graph:  

![Kia Seltos competitive analysis spider graph. Source: Insight Quantum](./images/73dd11_4b86e5789b7a4a758073fc4f3d68477emv2.png)

Kia Seltos competitive analysis spider graph. Source: Insight Quantum

When **building** a product, in contrast to **marketing** it, such competitive analysis is used to identify the areas where we want to shine, so that we can create our positioning statement and value proposition: In this example, a humorous one could be: "Crash safely with the music blasting on" – positioning Kia Seltos as the safest car with the best infotainment system.



---

### Feature validation

The crucial part of the validation process are the insights we gained:

-   First we identify and prioritize the features according to our positioning
    
    -   These feature may be contradictory (such as performance vs. fuel efficiency)
-   We then stack the differentiating features on top of the conventional, foundational ones
-   Now we find a way to present these features to users, and have them experience them to the best of our ability.
    
    -   For instance, when we market automobiles, we can only inform consumers of our model's average fuel consumption, one tested in controlled environment to an industry agreed benchmark. This is only an indicative measure of economy, as no two drivers, trips, or load are the same, and the same goes for the actual fuel consumption consumers will experience eventually.
        
    -   In another context, when marketing future versions of complex products, we use **mockups** for the look and feel, well before starting production, and thus gage the audience's response prior to the large investments we are about to plough into the project.
        

CAF (Construcciones y Auxiliar de Ferrocarriles) is a spanish company which manufactures railway vehicles and equipment and buses.

Catering to the public transportation sector, their process includes bidding for open or close tenders, in which they present mockups showing their vision for the design and usability of the railroad car - ticking the boxes for the particular demands of the tender at hand.

![CAF mockup for a railroad car - NS sprinter](./images/73dd11_177c43641fa742b3a18b6efc10abcfe5mv2.jpg)

CAF mockup for a railroad car - NS sprinter

In this mockup for the [<u><span>NS sprinter</span></u>](https://www.facebook.com/reizigersov/posts/1079652722052431) series, for Dutch operator Nederlandse Spoorwegen, CAF shows the bodywork, as well as interiors, including electric sockets for passengers' devices, separate trash bins and toilets.

They have focus groups (including target users and customer representatives) experience this solution first hand, gage their responses, and draw necessary conclusions translated into design modifications

It is no small feat, either. Building a similar mockup can take nearly a year and cost up to a million euros. But once the green light is given, the manufacturer can confidently proceed with their multi-billion-euro project, which includes:

-   Investments in manufacturing equipment
    
-   Tooling
    
-   Logistics (inventory provisioning for components and raw materials)
    
    ---
    
    

### Limitations of user feedback

Of course, not every feature can be validated through mockups or public trials. To most users, the technicalities of drivetrains, energy consumption, or HVAC systems are little more than “tech babble.” Testing these in public would be nearly impossible, since most trial-and-error takes place in labs or on the factory floor, far from user experience.

Instead, these aspects are validated through proof-of-concepts carried out by the vendor under the oversight of the tender issuer, and are later bolstered through **technical specifications and performance guarantees** contractually committed, often as part of multi-decade operation agreements.

Together, these approaches highlight the dual nature of validation: user-facing features of look and feel are tested and refined through direct experience, while technical features are validated through experimentation, industry standards, and contractual commitments. Both dimensions are essential to building trust in complex products.

---



### Validation as a Journey

Validation is never complete until users themselves perceive the value. Structured proxy methods – surveys, mockups, contractual guarantees – do provide a limited upfront confidence. Ultimately, the market decides in a moment: when a customer first touches, sees, or tries the product. The next chapters explore these decisive arenas of experiential validation, from the theater of public demos and unboxing to the disruptive force of killer features.

---

'***'

---

# Chapter 10 - First Impressions

**"You never get a second chance to make a first impression"**

​	*(Was it Will Rogers or even to Oscar Wilde that coined this eternal truth?)*

![Launch event with presenter and cheering audience](./images/73dd11_37004660726c4562927200288193bb1cmv2.webp)

Launch event with presenter and cheering audience. Generated with FLUX.1 Krea Dev. Retrieved from ./images/73dd11_37004660726c4562927200288193bb1cmv2.webp



---



### Public Reveals

Key for demand generation are the launch events we have become accustomed to over the past decades. These are the theater of innovation – the promise of a shinier, better future, embodied in the coveted purchase of the latest gadget that claims to make us smarter, stronger, richer...

(Or, as Veblen argued, in *The Theory of the Leisure Class* (1899), at least appear so. Conspicuous consumption, in his view, functions as a marker of social status. Unsurprisingly, virtue signaling through conspicuous consumption is well and alive 135 years later.



### Trade Shows as Stages of Progress

Modern day launch events are precedented by the lavish events held by the car and aviation industries. Detroit Auto Show and Frankfurt Motor Show (now rebranded IAA) are still very much a thing, although Auto Shangai seems to still the show, so to speak, happening in one of the most vibrant markets - both for purchasing power and innovation.

These weren’t just commercial expos but **cultural milestones**, shaping the public’s imagination of technology and progress.

![](./images/73dd11_d6b14d78aacf42eb937a031cebb93351mv2.jpg)

hpgruesen. (2016, January 11). *Geneva International Motor Show [Photograph]*. Pixabay. https://cdn.pixabay.com/photo/2016/01/11/13/13/geneva-1133601_1280.jpg

---



This is where the industry unveils new models and prototypes, gaging the crowds and professional sentiment and acceptance years – in the following example decades – before an actual first vehicle rolls of the production line.

![](./images/73dd11_3084e11266b5486f898e6f9672cf2154mv2.webp)

*Rolls-Royce 103EX concept car.*

Reproduced from Rolls-Royce Motor Cars Pasadena (2022), Dealer Inspire. https://di-uploads-pod23.dealerinspire.com/rollsroycemotorcarspasadena/uploads/2022/05/Rolls-Royce-103ex.jpg.

---



### Apple and the Theater of Innovation

Steve Jobs, for his showmanship, transformed the product launch into a ritual, fusing drama, exuding charisma and Reality distortion field. True, technology and design played great roles, too, but Jobs mesmerising role is matched by a rare breed of business leaders.

![](./images/1218px-Steve_Jobs_WWDC07.jpg)

Steve Jobs at WWDC 2007  - Creative Commons Attribution-ShareAlike 2.0 (CC BY-SA 2.0)

Beyond specs and availability, such launch events create shared cultural moments, a resonance that bonds developers, distributors, customers, media, and fans into a community of anticipation and belonging. At times, even of heated debate and controversy.

Apple events, notorious for their tight-lipped secrecy before launch, came to rival blockbuster film premieres, attracting tens of millions of simultaneous viewers – a load carried by a burgeoning breed of content delivery networks (CDNs) by Akamai. The suspense, carefully built over weeks and months, broke at the moment of broadcast, unleashing global attention and triggering immediate surges in demand – a true tour de force in modern media management.

These events are not designed merely to inform; they shape perception and set the emotional stage for adoption at the individual level, with subsequent queues amassing in front of the new shrines of digital consumption – Apple Stores.

---



### MacBook Air and the Art of Showmanship: Driving the Point Home



One of the most electrifying launch events Steve Jobs ever led was the unveiling of the MacBook Air. It was one of those rare pitches that didn’t just impress — it sent me, and countless others, straight to the store.

![Steve Jobs unveiling the MacBook Air ](./images/73dd11_cdf8a41eb1554a548d7e1887c0d5c165mv2.jpg)

Steve Jobs unveiling the MacBook Air (AP Photo/Paul Sakuma, via Alamy, https://www.alamy.com/image540086783). **Publication rights pending**



By then I had already spent a decade hauling around heavy business laptops, my shoulders bearing the cost of piecemeal portability. Then came this moment: Jobs received a plain manila envelope on stage, and from it slid a MacBook so thin and conspicuousely light – I was bought in right away.



The effect was mesmerizing. In a single gesture, Jobs demonstrated, in the purest “show, don’t tell” tradition, the defining feature of this laptop. That *killer feature* (which I explore in depth next), instantly resonated with weight-weary professionals. It turned the MacBook Air into a demand magnet, drawing men and women to Apple Stores in droves.



Other considerations – Apple’s bold choice to rely on wireless connectivity while omitting the DVD drive and the RJ45 jack – were important, but secondary. Those moves had their merits, yet they were not the spark that drove demand.

Indeed, during Apple’s fiscal 2008 second quarter (ending March 29, 2008), the company shipped 2,289,000 Macintosh computers, marking 51 percent unit growth and 54 percent revenue growth over the year-ago quarter — gains widely attributed to the MacBook Air ([MacDailyNews, 2008](https://macdailynews.com/2008/05/01/apple_last_quarters_mac_sales_were_driven_primarily_by_sales_of_macbook_air/)).



This moment captures the very essence of what a launch event can achieve.



---



### A Note on Risk

Live demos occasionally falter – a reminder of their high stakes. Tesla’s Cybertruck “Armor Glass” window shattering live in 2019 is just a recent, though famous example.

![](./images/73dd11_271c737539544904940a57ed2420c51bmv2.png)

*Tesla Cybertruck launch event: “Unbreakable” window shatters during live demo.*

Reproduced from CNBC Television (2019, November 22), *Oops! Tesla Cybertruck’s unbreakable windows break during demo* [Video]. YouTube. https://www.youtube.com/watch?v=dwfaCpWe0zY



---



### Unboxing

Launch events aside, the real journey often begins with the much-hyped unboxing – a ritual celebrated endlessly on YouTube. And yet, in practice, it is fleeting: consumers perform it once, then toss the packaging or stash it away. Still, this first encounter carries disproportionate weight.

Unboxing is not just about packaging; it is the orchestrated journey of first impressions – when users touch the product, feel its weight, and form an instinctive judgment of quality and value. In software, we call this onboarding, or the Aha! moment. 

In hardware, unboxing compresses that same dynamic into a tactile, sensory instant where the brand promise must materialize.

![Packaging by Lynx](./images/73dd11_188261216e174f80a869cab4292e2787mv2.jpg)

Lynx Designers. (2020, December). *Lynx blog image [Photograph]*. Lynx Designers. https://lynxdesigners.com/blog/wp-content/uploads/2020/12/Lynx-Blog-2.jpg



---



#### Apple Powerbook Unboxing Experience

Unsurprisingly, no one has mastered the art of unboxing more than Apple. Behold the following unboxing video from Everyday Tech. If you are attentive to textures and physical nuances, you will be thrilled by the attention to the tiniest details designed to make you feel you are opening a treasure chest.

![](./images/maxresdefault.jpg)

MacBook Air Unboxing video - Everyday Tech. (2025, August 7). *2025 MacBook Air M4 - unboxing, setup and first look!* [Video]. YouTube. https://www.youtube.com/watch?v=MIAjIkknlfc

Not unlike a Japanese tea ceremony, it is designed to augment a daily experience, exuding sheer intentionality. Every layer is choreographed: the gentle sigh of air as the lid lifts, the precisely angled pull tabs, the glowing machine waiting at the center as if on an altar. You are not simply opening a cardboard container – you are being inducted into a ritual.

This ritual achieves several things at once. First, it confirms the value of what you just paid for. The sturdiness of the box, the satin feel of the paper stock, the absence of clutter: all remind you this is not a commodity purchase but an initiation into a brand. 

Then comes anticipation. Each reveal – device and accessories – keeps you leaning forward, rewarding curiosity with suspense.

Apple also designs the moment for ease. There is nothing awkward, no plastic to wrestle with, no cords tangled. The first touch is frictionless, the very opposite of the shrink-wrap and twist-tie nightmare of older electronics. And then, almost magically, the machine already has power: lift the lid, and you are welcomed into the Apple world with no delay.

Importantly, this packaging –though intricate and exquisite – differs from that of luxury goods like high-end watches. The MacBook is not framed as a jewel to be admired, but as a precision tool for professionals. The unboxing assures them they now possess the finest instrument available, one that will enable them to perform at their best and, ultimately, to become the best version of themselves.

Finally, there is the sense of theater beyond the individual. Apple knows you might film this moment, share it, turn it into content – hence the video above. The packaging is not only for you – it is a stage set for the internet. A million micro-advertisements generated by people experiencing the same ceremony, each reinforcing the myth of Apple as the custodian of modern luxury.

---

'***'

---

# Chapter 11 - Killer Features



![Screenshot: Merriam-Webster online dictionary entry for *killer app*](./images/73dd11_6004cdc905b2421dae898c04d0d6ec31mv2.jpg)

Screenshot: Merriam-Webster online dictionary entry for *killer app*. Retrieved from [https://www.merriam-webster.com/dictionary/killer%20app](https://www.merriam-webster.com/dictionary/killer app)

---

### Market Magnets

What is a **killer feature**, anyway? We keep hearing this term, in its pure software version –*Killer App.*

The expression’s origin is unattributable, but it surfaced in the early 1980s when technology circles spoke of VisiCalc, the spreadsheet program that became the single sufficient reason for businesses to buy the Apple II. It wasn’t “just software”; it was the first serious business application that made a long stride toward democratizing computer use.



For the first time, small businesses — from mom-and-pop shops to midsize enterprises — had a reason to invest in an entire computer platform. The Apple II was no longer a hobbyist’s toy or an educational aid; VisiCalc transformed it into a business machine.

![Apple II running VisiCalc, widely regarded as the first “killer app".](./images/73dd11_828ade7189944a4ba15705a454eaa47cmv2.jpg)

Apple II running VisiCalc, widely regarded as the first “killer app". Photo by Jean-Edouard Rozey, [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/). Retrieved from https://www.flickr.com/photos/jean-ed/1661870646/



This pattern would repeat throughout computing history. Photoshop became the anchor for the Macintosh in creative industries. Microsoft Office, with Excel dethroning VisiCalc, secured Windows as the corporate standard. Each time, a single capability proved magnetic enough to drive platform adoption en masse.

---



### Redrawing Competition Lines



In hardware, killer features — whenever they appear (and they are rare!) — exert this same pull, but with a substantial twist. Hardware’s much longer and more expensive development cycles, component interdependence, and fiercely defended IP cause competition to struggle for quite some time before it can recuperate from such a blow — either through a workaround or by launching a killer feature of their own.



By definition, killer features redraw the lines on the field, in what Clayton M. Christensen coined as **Disruptive Innovation** (1995). They shift the very dimensions of value along which competitors align and position themselves – if they only could.

---



### A Brief History of Disruption



It is worth revisiting the moments when killer features reset the rules of competition. Each example below shows how a single capability – often at the intersection of physical design and digital intelligence – pulled markets in a new disruptive direction and left rivals scrambling to respond.

---



#### Sony Walkman (1979)



The realization: *music is now portable, personal, and private.* It wasn’t the audio fidelity — it was slipping a cassette into your pocket and listening on the move. This shift redefined leisure culture itself.

![Sony Walkman with headphones, symbol of the portable music revolution](./images/nsplsh_9acc6c7c30e04791aaaa9a14685e60a9mv2.jpg)

Sony Walkman with headphones, symbol of the portable music revolution. Photo by Florian Schmetz on Unsplash. Retrieved from https://unsplash.com/photos/a-cassette-player-with-headphones-attached-to-it-Rks6FTfX5OU



> When the Walkman first launched in Japan in July 1979, Sony’s marketing team realized that conventional advertising wouldn’t be enough to explain such a radical product – small, lightweight, and designed for private listening. To overcome skepticism, they hired young people to stroll through Tokyo’s Ginza district wearing Walkmans and offering strangers the chance to listen.
>
> 

![Sony Walkman promotion event in Japan, 1979.](./images/73dd11_38e0b4777e7b4d53a33293fa6be06524mv2.png)

Sony Walkman promotion event in Japan, 1979. Young demonstrators showcased the device in public spaces to spark curiosity and encourage trial. From *The History of the Institute of Electrical Engineers of Japan, Vol. 40, No. 5*, p. 318. Retrieved from http://www2.iee.or.jp/ver2/honbu/30-foundation/data02/ishi-03/ishi-0405.pdf



> This hands-on introduction bypassed the need for abstract messaging. Passersby could experience the product’s essence immediately: portable, personal music. The campaign was as much demonstration as promotion, and it proved decisive in turning curiosity into demand. Within two months, Sony had sold more than 30,000 units, far exceeding expectations.

[Extract from Sony Corporation. (n.d.). Sony history: The Walkman. [Sony.net](http://sony.net/). Archived from the original on June 26, 2010. Retrieved September 10, 2025, from [webarchive.org](http://webarchive.org/)]

---



The true takeaway from the Walkman’s launch is how profoundly disruptive its killer feature was: **music made portable as well as personalized**. For the first time, listening to a self-curated music selection was no longer tethered to a living room stereo, a car radio, or the heavy cassette decks from companies like Panasonic, Sharp, or JVC (it took the industry four year to catch up, in which the brand "Walkman" became a household name, and a generic term. 



Suddenly, one could place the unit on their belt, and listen in private to their own selection of music – while . Another innovation was Sony’s lightweight headphones 



(and the humble 3.5mm stereo jack went with it, to: As a side note, Sony had already introduced it in 1958 for its transistor radios, but it was the Walkman that popularized it globally – turning a small hardware detail into a lasting industry standard.)



Yet this very leap made the Walkman difficult for consumers to grasp. The concept was so novel that even marketers and retailers struggled to articulate its commercial potential. Market education quickly became essential, and the only effective approach was to **show, not tell**. Sony deployed live street demonstrations, staged press events, and seeded celebrity photo shoots that conveyed coolness and aspiration. On the retail side, cautious allotment was needed to reassure store owners that they would not be left holding unsellable stock of such an untested product.



In other words, the Walkman’s revolutionary nature demanded an ecosystem of education. The marketing effort was not an embellishment but a structural requirement – a bridge between a world that had never imagined private, mobile listening and a future where it would become second nature.



---



#### Apple Macintosh Reshapes Computing (1984)



At its launch in 1984, the Macintosh’s disruptive feature was its graphical user interface – icons, windows, and a mouse that made computing visual and intuitive rather than text-based.



Initially pioneered at **Xerox PARC** (Palo Alto Research Center), Steve Jobs and members of the Apple Lisa and Macintosh teams, were initiated to the concept of Graphical User Interface  (GUI) running a Xerox Alto computer – **bitmapped screen, overlapping windows, icons, and the mouse** – the building blocks of what would become the graphical user interface. ([Computer History Museum](https://computerhistory.org/blog/the-xerox-alto/), [Smithsonian](https://www.smithsonianmag.com/innovation/how-xerox-invented-modern-computers-180960168/?utm_source=chatgpt.com)).



Jobs later described the experience as an epiphany:

> “I thought it was the best thing I’d ever seen in my life. Within 10 minutes, it was obvious to me that all computers would work like this someday.”

(*Steve Jobs, quoted in Walter Isaacson’s biography, 2011*).







Reviewers immediately recognized this as the breakthrough. The New York Times noted the Macintosh display was “refreshingly crisp and clear,” setting it apart from the command-line machines of the era (Sandberg-Diment, 1984). BYTE magazine admitted the machine had hardware limitations but concluded: 

> “You can do useful work with it, and the user interface beats all others cold” (Webster, 1984).

This usability shift reframed the basis of competition. The Mac didn’t need to win on raw specifications – its GUI redefined what a “personal computer” meant. IBM and Microsoft were forced to follow, accelerating the spread of graphical interfaces across the industry and pulling the personal computing revolution into a new era.

![The original Macintosh 128K (1984), the first mass-market computer with a graphical user interface](./images/73dd11_5f102797c1cd4cf1a4870ef0d03bb2d5mv2.webp)



The original Macintosh 128K (1984), the first mass-market computer with a graphical user interface. Photo by MATEUS_27:24&25. Retrieved from [Smithsonian Magazine](https://www.smithsonianmag.com/history/what-reviewers-said-about-first-mac-when-it-debuted-180949448/)

It took competition in the personal computing about a decade to catch up.

![Apple Inc. stock price (1983–1995, raw historical values) with the launch of the Macintosh (January 24, 1984) highlighted](./images/73dd11_6cc72b48b8fa474380e9d1dac8cd7cfemv2.jpg)

Apple Inc. stock price (1983–1995, raw historical values) with the launch of the Macintosh (January 24, 1984) highlighted. Data from Yahoo Finance. Chart generated by the author



The Macintosh launch in 1984 gave Apple a sharp (though brief) lift. Unit sales topped **372,000 in the first year**, well above expectations, and revenues jumped nearly **50 percent to $1.5 billion**, pushing market share into the 10~11 percent range.



[Watch the notorious, or famous, Super Bowl ad](https://archive.org/details/1983-30sec), iconic and almost earth-shattering, directed by Ridley Scott, his dystopian imagery echoing the visual language of Alan Parker’s 1982 Pink Floyd: The Wall. 



The faceless system that could not be named – though the bluish hues hinted strongly enough – was alluded to as the IBM/Microsoft duo, the emerging force in personal computing. 



Yet, as history proves, even the strongest “killer feature” cannot secure lasting advantage on its own; without an ecosystem to sustain it, disruption's effect may prove short lived. Eventually, industry’s giants will trample ahead, regardless of any temporary setback.

---



#### Dyson bagless vacuum (early 1990s)



When James Dyson introduced his first "Cyclone" vacuum (the G-Force, the DC01, and later models), it broke with decades of convention. Until then, vacuum cleaners were designed around **disposable paper bags** – not just as dust containers but also as filters. Performance inevitably declined as the bag filled, and consumers had to buy a constant supply of replacements.

![Dyson DC07 bagless vacuum cleaner](./images/73dd11_1df5d484cadf45538a3a9941062bfb4dmv2.jpg)

Dyson DC07 bagless vacuum cleaner. Photo by Arpingstone. Public domain, via Wikimedia Commons. Retrieved from https://commons.wikimedia.org/w/index.php?curid=66714

By ditching paper bags, Dyson removed a recurring pain point: the cost and hassle of consumables. For households, this meant **lower ongoing costs**, easier emptying, and no more frustration of running out of bags. 



For the industry, however, this was a shock: established players like Hoover, Electrolux, and Panasonic relied on **bag sales as a profitable annuity model**. Dyson’s innovation didn’t just improve the product; it undermined the incumbents’ business model.



The multi-cyclone design wasn’t only about eliminating bags. By spinning dust out of the airflow, it maintained **constant suction performance**, even as the bin filled. This addressed a long-standing flaw in bagged vacuums, where suction would degrade steadily as the bag clogged. Dyson emphasized this in advertising, reframing expectations: why tolerate performance drop-off when technology could avoid it?



The transparent dust bin was more than a design flourish. It gave users immediate feedback that the vacuum was working: dirt and dust swirling in plain sight. This shifted the competitive axis away from abstract “suction power” numbers to a **visceral, demonstrable result**. Customers didn’t need to trust spec sheets – they could *see* effectiveness with their own eyes.



The combination of visible feedback, lower running costs, and consistently high performance created a **compelling killer feature bundle**. By the mid-1990s, Dyson had captured significant share in the UK, displacing Hoover from its century-long leadership. By 2001, Dyson was the best-selling vacuum brand in the UK, and by the 2000s it had expanded globally, commanding premium prices.



Dyson’s cyclone vacuum shows that killer features can not only rely on superior engineering or clever design – it is the way those improvements converge with economics. Consumers got a vacuum that cleaned more effectively, showed its performance in real time, **and** cost less to own over its lifetime. 



By collapsing **better product experience** and **lower total cost of ownership** into a single offering, Dyson rewrote the rules of competition. Rivals still tied to bag sales could not follow without cannibalizing their own profits, leaving Dyson free to capture market share and redefine value in an otherwise stagnant category.

---



#### Nintendo Wii motion controller (2006)



When Nintendo launched the Wii in 2006, the bundled **Wii Remote** looked nothing like the standard controllers of the era. A **Core Differentiator** it reframed gaming around motion. Shaped like a television remote rather than a bulky gamepad, it replaced complex button layouts with a **motion-sensing wand**. Inside were accelerometers and gyroscopes, paired with an infrared sensor bar that let players point and swing with remarkable accuracy.

![Nintendo Wii Remote controller](./images/73dd11_0433872bc5a349e2963bdd42d6e754c8mv2.png)

Nintendo Wii Remote controller. Image via Wikimedia Commons. Licensed under CC BY-SA 3.0. Retrieved from https://commons.wikimedia.org/wiki/File:WiiRemoteController.png



This was a radical departure from the industry’s trajectory. Sony and Microsoft were locked in an arms race over **processing power, graphics fidelity, and cinematic immersion**. Nintendo reframed the competition: instead of asking how realistic a game could look, they asked how **intuitive and inclusive** it could feel. With the Wii, the act of play became physical – a swing of the arm to serve in tennis, a flick of the wrist to throw a bowling ball, a tilt to steer a kart.



The benefits were immediate. Gaming became accessible to **families, children, and even older adults** who found traditional controllers intimidating. *Wii Sports*, bundled with the console, turned living rooms into playgrounds and sparked global tournaments among players who had never touched a PlayStation or Xbox. Beyond fun, the Wii introduced the idea of **exergaming**, with titles like *Wii Fit* merging entertainment and fitness.



The impact was seismic. The Wii sold over **100 million units**, outselling both the PlayStation 3 and Xbox 360 during its peak years. Unlike its rivals, Nintendo profited on each console thanks to modest hardware costs, while driving additional revenue through games and accessories like the Balance Board and MotionPlus. 

![Estimated global market share of Nintendo Wii, Sony PlayStation, and Microsoft Xbox (2001–2016)](./images/73dd11_813fcc20a2cd46fcab2576839eb8d9admv2.jpg)

Estimated global market share of Nintendo Wii, Sony PlayStation, and Microsoft Xbox (2001–2016), with key milestone events highlighted. Based on synthesized data.



Just as important, the Wii **expanded the total addressable market for gaming**, pulling in demographics the rest of the industry had largely ignored.



The Wii Remote proved to be a killer feature by being a core differentiating factor redefining the rules of engagement, thus increasing total addressable market to new audiences and age groups. Locked in their by shifting gaming from a contest of specs to an experience of shared, physical fun. 

---



#### iPhone (2007)



The 2007 launch of the iPhone shook the mobile world to its core. Within a few years, it dethroned Nokia from its long-held dominance and forced once-formidable rivals like BlackBerry, Sony Ericsson, and others out of the market. More than a product launch, it was a total rewrite of the competitive rulebook. Same as in nature (there are no vacuums in business) the space cleared by the obliteration of the top tier of competition was filled not only by iPhone’s rise, but was soon filled with an entirely new class of competitors.

---



I strongly recommend watching Steve Jobs present the iPhone in 2007 — a launch event for the ages for anyone in product. It’s a masterclass in presentation showmanship and, more importantly, a clear demonstration of the nature of killer features (a term Jobs himself uses) and the transformative impact they can have on a product.

![ *Steve Jobs introduces iPhone (2007)*](./images/73dd11_d560d59c507e4c3a878971b98277e6ccmv2.jpg)

Apple. (2007, January 9). *Steve Jobs introduces iPhone (2007)* [Thumbnail image]. YouTube. https://youtu.be/vN4U5FqrOdQ?si=alU0JuIZlHhdqOGZ

---


The splash from this launch – heard across the technological world – was powered by a stack of killer features, each amplifying the others and together disrupting device makers, carriers, and entire ancillary industries.

![iPhone 2007](./images/73dd11_39aaa7dbc76341f3b2d22be84b8ff2b9mv2.jpg)

iPhone 2007.From Carl Berkeley, Riverside California, 2009, *Wikimedia Commons*, [**https://commons.wikimedia.org/wiki/File:IPhone_First_Generation.jpg**](https://commons.wikimedia.org/wiki/File:IPhone_First_Generation.jpg) (CC BY-SA 2.0).

---



##### New UI paradigm for the mobile world



The most fundamental shift was the creation of a **new UI (User Interface)**, a result of acute identification of the shortcomings of then extant Smartphones: small screens, tiny, crammed keyboards, rigid controls, and inability to adapt UI to specific applications.

![BlackBerry Classic (Q20) smartphone with physical keyboard](./images/73dd11_23247ae4fd1b4f72925e283226757dd0mv2.jpg)

BlackBerry Classic (Q20) smartphone with physical keyboard. Photo by Unsplash user [Linh Nguyen](https://unsplash.com/@lnhngyn), 2022. Retrieved from https://unsplash.com/photos/graphical-user-interface-application-RtijMFhL_ns.



In contrast, the iPhone’s capacitive touchscreen was accurate and responsive enough to replace physical buttons entirely, while also serving as a true multi-touch pointing device. Sensors detected when the phone was held to the ear, automatically disabling input to prevent accidental touches, while orientation sensing let the screen switch seamlessly between portrait and landscape to suit the task.



Apple’s virtual keyboard incorporated skeuomorphic feedback cues – visual key pop-ups and audible clicks – to compensate for the absence of physical keys. At the same time, innovative gestures such as pinch-to-zoom, tap, and inertial scrolling expanded the pointing interface, enabling direct manipulation of on-screen elements and eliminating the tedious scroll-and-select navigation of earlier devices.

![Screenshot of iPhone virtual keyboard with visual key pop-up visual feedback shown.](./images/73dd11_4c364d91d16f40e2a061f4f8563ab905mv2.jpg)

Screenshot of iPhone virtual keyboard with visual pop-up feedback shown. Image captured by the author, 2025.

---



These leapfrogging design choices alone were enough to disrupt the mobile phone industry. They created unmistakable differentiation by delivering greater user value in ways anyone could understand.

| Patent Number                                                | **Covered Feature(s)**                        |
| ------------------------------------------------------------ | --------------------------------------------- |
| [US 7,479,949](https://patents.google.com/patent/US7479949B2/en) | Multi-touch heuristics (swipes, pinches, etc) |
| [US 7,657,849](https://patents.google.com/patent/US7657849B2/en) | Slide-to-unlock gesture                       |
| [US 7,812,826](https://patents.google.com/patent/US7812826B2/en) | Multi-touch on mobile device, sensor input    |
| [US 7,812,828](https://patents.google.com/patent/US7812828B2/en) | Ellipse fitting for multi-touch surfaces      |

This competitive advantage drove instant demand to the hot, new, cool, 'reinvented' phone, forcing incumbents – Motorola, Nokia, Blackberry, Palm – into a defensive chase after attributes they could not easily replicate.

An extensive suite of patents were filed prior to the launch, with both hardware and software elements covered, some of them listed below. IP strategy and patents played an important role in planning the commercial exploitation, and crucially fending against future competition.

| Patent Number                                                | **Covered Feature(s)**                        |
| ------------------------------------------------------------ | --------------------------------------------- |
| [US 7,479,949](https://patents.google.com/patent/US7479949B2/en) | Multi-touch heuristics (swipes, pinches, etc) |
| [US 7,657,849](https://patents.google.com/patent/US7657849B2/en) | Slide-to-unlock gesture                       |
| [US 7,812,826](https://patents.google.com/patent/US7812826B2/en) | Multi-touch on mobile device, sensor input    |
| [US 7,812,828](https://patents.google.com/patent/US7812828B2/en) | Ellipse fitting for multi-touch surfaces      |

A case of interest is **Apple v. Samsung** (2011–2018) – a landmark patent battle of the smartphone era. Apple accused Samsung of copying iPhone features like *slide to unlock* (US 7,657,849), and its icon-grid design, winning an initial $1.05 billion verdict (later reduced to $539 million). 



Though costly and protracted, the case became a proxy fight with Android and highlighted how design and software patents could shape the industry’s competitive landscape. Conversly, it also shows the limitations of such litigations in mitigating fierce competition.

---



##### "The Real Internet"



In that iconic launch, Jobs pointed to the then state-of-the-art smartphones, highlighting not only their cramped physical keyboards but also the inadequate, stripped-down versions of internet browsing they offered.

> *The most advanced phones are called smart phones, so they say. And they typically combine a phone plus some email capability, plus they say it’s the Internet – it’s sort of the baby Internet ...*

![](./images/73dd11_5dfb472766f64112bf95607758ae49e0mv2.png)

WAP browser rendering the English Wikipedia main page on a mobile device. From Wikimedia Commons, by Wikipedia user "Wap", 2008. [**https://upload.wikimedia.org/wikipedia/commons/0/02/Wap-wikipedia-en.png**](https://upload.wikimedia.org/wikipedia/commons/0/02/Wap-wikipedia-en.png). Licensed under CC BY-SA 3.0.



Jobs contrasted this with his vision of a phone equipped with a fully functional, HTML-compliant web browser — made possible by iOS, Apple’s Unix-derived operating system.

> *This is a breakthrough Internet communicator built right into iPhone. The first rich HTML email on a phone. The first real Web browser on a phone. Best version of Google Maps on the planet, widgets and all with EDGE and Wi-Fi networking. We’re very, very happy with this.* 
> *… It’s the Internet in your pocket for the first time ever.*

Quotes from Steve Jobs during the Macworld 2007 keynote introducing the iPhone. Transcript retrieved from *Steve Jobs introduces iPhone in 2007* (Macworld Keynote, January 9, 2007)



This leap immediately exposed the weakness of the existing carrier-driven model. For years, mobile operators had forced users through Wireless Application Protocol (WAP) portals that were slow, costly, and designed to keep customers inside their branded gardens. They dictated which phones were sold, what features were enabled, and how revenue was extracted, from SMS and ringtones to tightly controlled downloads. 



The iPhone broke that structure. Apple insisted on end-to-end control, barring AT&T in exchange for launch exclusivity, from disabling Wi-Fi, pre-loading portals, or even branding the device.

---



##### The Carrier Power Shift



The shift transformed consumer behavior. For the first time, people chose their carrier based on who offered the iPhone, not the other way around. In the U.S. this meant flocking to AT&T; in the UK it meant O2; in France it meant Orange. 



Carriers became secondary to the device itself, while customers began to identify as iPhone users rather than as subscribers to a particular network. Buying direct from Apple or choosing an unlocked handset became viable alternatives, reducing the lock-in power of bundled contracts.



The iPhone’s appetite for full web access and data-rich apps also forced carriers to abandon per-megabyte billing and move toward unlimited plans. The mobile carrier industry faced cannibalization, and AT&T executives - once approached by Apple, understood it was better “to have the cannibal in the family” than to lose millions of subscribers to rivals. 



The precedent Apple set reshaped the industry: carriers, once the gatekeepers of the mobile experience, were reduced to pipes, while the real value and loyalty shifted to ecosystems built by Apple and, later, Google.

---

##### Together, Not Alone



Each of these features mattered, but their power was cumulative.



- Without the keyboard-less glass slab, the “real internet” would have been unusable.
- Without multi-touch, the full screen would have been clumsy.
- Without breaking carrier control, the openness of the web and later apps would have been throttled.
- Without approachable design, mass adoption might have lagged.



The result was not merely a better phone, but the template for the modern smartphone and a reset of the industry’s balance of power.



Apple’s “phone reinvention” moment unleashed a pack of killer features fusing usability breakthroughs, software openness, and value-chain disruption into a single device.



---



#### Tesla OTA - Over The Air System updates (2012)



Tesla had been touting over-the-air (OTA) updates since the launch of the Model S in 2012, promising that “your Tesla gets better over time.” Much like a smartphone, the car could receive new features and fixes remotely: navigation tweaks, interface refinements, performance modes, and even the early rollout of Autopilot.



While the rest of the industry still required a dealer visit for most software adjustments, Tesla positioned OTA as a defining differentiator – proof that a car could continue to evolve after it left the factory.

![Tesla Model S over-the-air (OTA) update screen](./images/73dd11_0cfa7f5c169346e0a413821734586c42mv2.jpeg)

**Tesla Model S over-the-air (OTA) update screen.** Image retrieved from *Stuff* (“The top car technology of 2017,” 2017). Fair use for scholarly/educational purposes. Source: https://www.stuff.co.nz/motoring/top-cars/98426802/the-top-car-technology-of-2017



For years, most of these updates felt incremental or playful. In December 2017, for instance, Tesla introduced a Christmas-themed “Romance Mode,” complete with sleigh graphics and festive music that transformed the heating screen into holiday theater.

![Tesla. (2018). Romance Mode Easter Egg](./images/73dd11_1ae07c50aa204574ab0dbea910d9c911mv2.jpg)

**Tesla. (2018). Romance Mode Easter Egg [Video]. YouTube.** [**https://youtu.be/iWI8bfK2wAQ?si=x4xF4wOw1dSO0BIH**](https://youtu.be/iWI8bfK2wAQ?si=x4xF4wOw1dSO0BIH)



Owners came to expect such flourishes as part of the brand’s personality: updates were convenient, surprising, even fun.



But in September 2017, as Hurricane Irma bore down on Florida, the same capability proved lifesaving. Tesla remotely and temporarily unlocked extra battery capacity in Model S and Model X 60 kWh versions — cars that actually contained 75 kWh packs but were software-restricted. Overnight, evacuees gained an additional 30 to 40 miles of range, enough to help them escape the storm.



That intervention caught the attention not only of technology enthusiasts but also of the national press. [*The Washington Post* observed](https://www.washingtonpost.com/news/innovations/wp/2017/09/11/as-hurricane-irma-bore-down-tesla-gave-some-florida-drivers-more-battery-juice-heres-why-thats-a-big-deal/):



*The decision highlights one of the most innovative aspects of owning a Tesla. The company’s ability to use software to instantly add range to a vehicle is something no conventional car can achieve. You can’t simply make a gas tank bigger at the click of a button.”*



By 2021, the same newspaper concluded that Teslas were effectively *“iPhones on wheels,”* [noting in a headline](https://www.washingtonpost.com/technology/2021/05/14/tesla-apple-tech/):

> *Tesla is like an ‘iPhone on wheels.’ And consumers are locked into its ecosystem.*

(Yes, this new killer feature had a dark side to it, too)



Together, these episodes elevated OTA updates into a textbook ***killer feature\***. For users, the benefit was unmistakable: their cars no longer depreciated in utility the moment they left the showroom. Instead, features could be added or improved over time, turning ownership into an evolving experience rather than a static one.



For competitors, this was deeply threatening. Traditional automakers were still bound to dealer networks and hardware-bound feature sets, while Tesla had shown that the most compelling value could be delivered with a keystroke – instantly resetting expectations for what a modern car should offer.



And for Tesla itself, OTA updates opened the door to a different business model. Controlling code meant not only delivering upgrades in real time but also monetizing them – from optional feature unlocks to subscription programs – reshaping the economics of car making as profoundly as the innovation reshaped the product itself.

---

### The Essence of Killer Features



Killer features differ fundamentally from incremental improvements: they act as disruptive wedges that redefine the terms of competition. By reframing what customers value, they render existing benchmarks obsolete. 



The Walkman redefined leisure; VisiCalc justified computers for business; the iPhone reset usability; the MacBook Air elevated portability; and Tesla proved that adaptability itself could be a feature.



A useful framework is to view killer features as operating along three axes:

- **User benefits** – filling a gap and meeting previously unmet needs.
- **Competitive disruption** – undermining established industry conventions and resetting expectations.
- **Business model change** – altering the underlying economics of value creation and capture.

![](./images/73dd11_8f763bbffc5e4c8ea4318e76d4bd1422mv2.png)



Illustration of killer feature dynamics (subjective interpretation). Created by the author.



Competitors caught unawares still compete on yesterday’s dimensions – more keys, faster processors, larger batteries – suddenly looking irrelevant. Killer features matter because they do more than add value; they shift the basis of competition, pulling the entire market toward a new axis of differentiation.



Equally important, they reshape business models. Consumers begin paying for different things, at different times, and often at different price points. What once was a one-time transaction becomes a recurring relationship, or a bundle of services layered on top of hardware.



For firms, this makes careful strategic planning essential. To fully capitalize on the R&D behind such breakthroughs, companies must not only design the killer feature itself but also anticipate how it will alter demand patterns, revenue flows, and competitive dynamics.

---

### **Killer Features - Key takeaways**



- A killer feature reframes value for users, disrupts competitors’ assumptions, and changes the revenue logic.
- Adoption speed and defensibility determine how long the advantage lasts.
- Ecosystems turn one feature into a flywheel: distribution, complements, and IP convert differentiation into dominance.
- Strategy must pair invention with capture: pricing, subscriptions, upgrades, and timing.

---

'***'

---

# Chapter 12 - The Machine That Goes PING

> ###### Black Boxes: Communicating Product Value



!["The machine that goes PING" by Monty Python ](./images/73dd11_1c51ae9f24c64079963cce5baa80298emv2.png)

"The machine that goes PING" by Monty Python [GIF]. *The Meaning of Life (1983)*.




The canonical (and hilarious) Monty Python *Meaning of Life* scene portrays the Mother, the Husband, and – eventually – the Newborn, all sidelined by the marvels of a mysterious machine that goes *PING!* at random.

What follows is even more absurd: an administrator drones on about “reclassification of the machine’s cost to current accounts, rather than to capital expenditure,” prompting obedient applause from the glazed-eyed medical staff.

Why bring this up? Because beyond the laughs, the sketch captures the alienation that arises when cryptic technology intrudes on our lives without explanation.

Product leaders and technology marketers cannot – and should not – risk their products being met with indifference or dismissal. When products are shrugged off as baffling – or worse, alienating – the business suffers. To avoid this, product leaders must clearly communicate the product’s value to all stakeholders, laymen and specialists alike.

---



### The Problem with black boxes: 1

![The Black box model. What's missing?](./images/73dd11_1e592b909b34424ab0f6de5dacdc3fbemv2.png)

The Black box model. What's missing? Illustration by the author

This scene came to mind during a conversation with a fellow product manager who specializes in monitoring devices for intensive care units. The product is used with patients who are only partially conscious and have very limited motor abilities. It monitors their level of awareness, provides auditory stimulation aimed at reducing delirium (ICU syndrome), and serves as a one-way communication channel that allows family members and medical staff to reach out.



**The problem, however,** is that to bystanders – including ICU personnel – the device fails to provide *system status visibility* ( See Jakob Nielsen’s first usability heuristic, which states that *“the system should always keep users informed about what is going on”* ([Nielsen Norman Group](https://www.nngroup.com/articles/ten-usability-heuristics/))). 

It remains a black box, offering no indication that it is powered on, correctly installed, or still in place. In practice, even if someone were to detach it from the comatose patient  – a scenario not unlikely in a busy ICU – there would be no visible sign that anything had changed.

To me, this is not just a design flaw but an implementation gap – and therefore a product opportunity. If stakeholders could readily see that the device is working, attached properly, and calibrated, they would begin to perceive real value. 

Even minimal feedback would transform their interaction from a seemingly meaningless ritual into a justified practice, one that feels worth the cost, installation effort, and ongoing service.



---



### The Problem with black boxes: 2

![Consumer grade UPS by Gamtronic, circa 1998](./images/73dd11_e87e22cf477499fd64ae34ed26e4b449.jpg)

Consumer grade UPS by Gamtronic, circa 1994. Credit: Studio r2d2

UPS units (Uninterruptible Power Supplies) were once all the rage. For 99.99% of the time after installation, there was little one needed – or could – do with them. They simply stood there, quietly gathering dust. But every so often, when the mains current failed or surged, the UPS would kick in and keep your system alive for a few precious extra minutes.

When they didn’t, the consequences were costly: lost information, corrupted files, and an entire workday gone, if not worse.

(As a side note, all this reminded me of the first electronic device I ever designed, together with Vered Shlomo, my then co-owner at Studio r2d2.)

**The trouble is,** you can never really be sure a UPS is functional. 

- Are all its sensors active? 
- Is its battery charging? 
- Will it actually kick in when the power fails? 

With barely any indication of its inner workings, you are left guessing.

---



### Black box: communicating product value

#### The Machine that goes 'Ping'

For 'Stand-by' category of products, users need proof of value, in the sense that the product is indeed operating.

Since there is no immediate output execpt for a digital log on some remote computer, users need to know:

-   Is the electricity on
    
-   Is the device on
    
-   Did periodic self check succeed
    

Finally, on site personnel want to know they made a reasonable effort to check of some equipment is indeed alive and well. It is part of the value such products confer, and a way to communicate it to users. Some measures include the following:



---



#### Status LEDs

![Wireless router with active indicator lights](./images/nsplsh_4c525f77585f6b6c4f504dmv2_d_5353_3503_s_4_2.jpg)

**Wireless router with active indicator lights.** Photo by Compare Fibre on Unsplash. Retrieved from https://unsplash.com/photos/white-modem-outer-is-turned-on-LR_wX_klOPM

This is what the humble status LEDs stand for. They fulfill a simple, yet crucial, task: Provide a visual proxy to the health of the system.

With a quick glance, users can learn whether several key functions – each critical to overall operation – are working as intended. 

Examples include:

-   **Power:** Is the machine on? This indicates whether power is being supplied past the AC–DC converter, a critical and failure-prone component.
    
-   **Battery charging:** Is the battery charging? A multi-state indicator confirms proper charging, reflecting the status of both the battery and the charging circuit – another failure-prone subsystem.
-   **Internet connection:** Is there an active connection? This LED conveys the success or failure of the modem’s periodic ping test.
-   **RX/TX:** Is the system receiving and transmitting data?
-   **Wi-Fi:** Is the wireless network enabled?
-   **Phone/Fax:** Is the PSTN bypass active, allowing audio calls over the same infrastructure?
-   **Mobile signal:** For modems that rely on cellular data, is there adequate network coverage?

Support teams rely on these indicators because they require little skill to interpret. During an initial call, the field user can quickly run basic checks – disconnecting and reconnecting the equipment, pressing the reset button, and so on – to determine whether the issue can be resolved on the spot or needs to be escalated to a qualified technician.



---



#### Minimal control: Resets and tests

![Sony PlayStation glorious Reset button. Source: Unsplash](./images/nsplsh_44335a6466427141346e51mv2_d_5184_3456_s_4_2.jpg)

Sony PlayStation's glorious Reset button. Photo by Nikita Kachanovsky on Unsplash. Retrieved from https://unsplash.com/photos/black-sony-game-console-D3ZdfBqA4nQ

Sometimes something gotta give. A software glitch or a hardware failure requires the system to be shut down and restart with its initial parameters pulled from firmware. Meet the humble Reset button, in one of its most glorious fashions – shown above adorning the Sony PlayStation front. Usually it is a mere pinhole you push a paperclip in. Here, the Reset and Power were integrated into a single physical button, with a distinct activation sequence.

We know soft reset and hard resets, each with different level of flushing the unit's memory, all the way down to factory reset.

The Reset button is here is in plain sight for a reason:

Humble as the reset button looks, it serves a noble cause: Keep technicians away, and avoid costly maintenance, shipping back and forth, or – in extremis, God forbid – travel. A button well spent!...

---



![Ground Fault Circuit Interrupter (GFCI) outlet with self-test and reset buttons](./images/73dd11_d585aaca5c9e45cfb55517d6a1aae1d0mv2.webp)

Ground Fault Circuit Interrupter (GFCI) outlet with self-test and reset buttons

Another example is the series of actuators and indicators alarmingly placed on the front panel of an electric outlet to externalize the functionality of GFCI (Ground Fault Circuit Interrupter). The device is a critical safety feature in home and industrial electric systems, ensuring electric appliances are not posing risk of electric shock. Once a leak current is detected, the device is designed to snap to disconnect the electric current.

Again, this appartus is meant to do its work unintrusively. Electro mechanical in nature, however, it is in itself prone to malfunction. Not as unlikely as we'd hope to think, Should a compound failure occur – of this safety device and a connected appliance – users would be exposed to a serious, even fatal, risk.

The solution here comprises of hardware button that initiates a series of self tests. It is coupled with an alert LED set to blink on fault, and a reset button to quell false alerts.

Apparently users are required to periodically test it, checking system integrity. Am I satisfied with this embodiement, relying on users' diligence just to keep them from electric malfunction? Not one bit, but here we are...

A resonable approach, perhaps more accessible in the era of smart hardware would be a fully automated unit, performing self tests, responding to check up sanity check pings from a smart home management unit.



---



#### Peace of mind

So, this is what we users seek when we look for status indicators and successful tests from our own black boxes.

Although these devices may be visually inert, opaque about their inner workings, we do want to be sure our money was not spent in vain, and we want to make sure these inert objects will indeed come to life when needed.

To what extent we want to externalize these indicators and test buttons remains a design choice depending on day to day operations, but also on other consideration, from brand image and aesthetic design, to access and installation.

In some cases, such as in the ICU, the blinking LED has a deeper meaning: keeping users, and mainly the medical staff, happy. They need too know they had performed their job well, the equipment is indeed properly installed, and – at the time of test – it is still running, doing what's it's supposed to do.



---
'***'

---

# Chapter 13 - When Software Features Outcompete Physical Products:

###### Lessons from a (Failed) Bicycle Safety Beacon

_Durable goods (AKA physical products) leaders must carefully evaluate competitive landscape, especially when existing software-based solutions exist. Software features, easy to implement and distribute at negligible cost, tend to render most standalone devices obsolete..._ A cautionary tale.

![A peloton racing](./images/nsplsh_47506d33626f584d745951mv2_d_4212_2808_s_4_2.jpg)

Road cyclists are always at risk

In the competitive landscape of tech innovation, not every promising idea makes it to market success.

Today, I want to share the story of an ambitious bicycle safety hardware project that ultimately couldn't overcome the efficiency of mobile technology and the power of feature integration.

The journey offers valuable lessons for hardware entrepreneurs and product developers navigating similar challenges.

## The Safety Problem and Initial Opportunity

Road safety for cyclists remains a critical concern worldwide. With increasing traffic and distracted driving, cyclists face significant risks daily.

A promising solution emerged when beacon software began facilitating communication between cyclists and drivers through navigation applications. By broadcasting a cyclist's location to nearby drivers' navigation systems, the technology created an invisible safety net, alerting drivers to be cautious around vulnerable road users.

Initially, Cyclebe developed a standalone mobile application.

However, the landscape shifted when major training software platforms like Strava incorporated the beacon functionality as a feature within their existing apps. Cyclists could now ride with an added layer of protection, all through the software they were already using for training and route tracking.

## The Hardware Alternative

Seeing how quickly beacon functionality was being absorbed into existing software platforms, the team identified what it believed was a market opportunity: transitioning from a software-only approach to a dedicated hardware device.

The product concept combined GPS and cellular communication capabilities with an integrated backlight – creating a comprehensive safety solution in a single device.

The vision was compelling: a purpose-built safety beacon that wouldn't drain your phone battery, wouldn't require mounting your expensive smartphone to your handlebars, and would include critical visibility features.

![Beacon mounted on the saddle stem, by Yama design](./images/73dd11_cf96d097f61f4ced8a16f2121c0eae7amv2.png)

Beacon mounted on the saddle stem, by Yama design

## Development Process

We approached development systematically, first determining the hardware architecture based on available modules. We needed reliable GPS positioning, energy-efficient cellular communication, and bright, long-lasting LED technology for the backlight feature.

Yqm design, Our industrial design partner, then created a beautiful, weather-resistant housing with a secure stem attachment system. The design prioritized aesthetics while ensuring the device would remain firmly attached during rides over any terrain.

The team produced impressive renderings and physical mockups that garnered positive feedback from potential users and investors alike.

On the business side, we established comprehensive costing models covering NRE (Non Recurring Expenses), Unit economics built on the BOM (bill of materials) assembly, shipping and handling costs, testing protocols, as well as establishing production and logistics systems.

The numbers, however, did not look promising: Hardware products are hard to come by, and the unit costs for any conceivable quantity forecast reached or surpassed the unit cost of a mobile phone - translating into eye watering consumer price.

![Cyclebe beacon: Parts and assembly](./images/73dd11_96d07f39c80343a69cf51f9c9da70753mv2.jpg)

Cyclebe beacon: Parts and assembly

## Why It Failed - Features Outcompete Products

Despite meticulous planning and genuine enthusiasm, the project ultimately failed to launch. The obstacles proved insurmountable for several key reasons:

### 1\. Feature vs. Product Battle

The most significant challenge was that we were attempting to create a standalone product to compete against what had already become a feature within popular applications.

When functionality becomes integrated into existing platforms, creating a separate product specifically for that function faces steep adoption barriers.

Users were already getting beacon functionality through their training apps, making a dedicated device redundant. In this case, the feature outcompete the additional stand alone product.

### 2\. The Mobile Efficiency Factor

Smartphones are the modern day swiss utility knife - an incredibly efficient solution for many uses.

Already sporting GPS location and (obviousely) cellular communications capabilities, cyclists carry them anyway. Cyclebe's dedicated hardware couldn't compete with a strong enough user benefit that would justify the purchase price.

### 3\. Duplicative Features

The backlight feature, which was positioned as a key differentiator, also faced competitive pressures.

-   High-quality bicycle lights are widely available at relatively low price points, with options ranging from $15 to $50 for most riders' needs. This meant our integrated light solution wasn't providing enough unique value to justify the additional cost of a dedicated device.  
    
-   One of our strongest selling points was addressing the battery drain issues that plague smartphone-based solutions. However, the market had already solved this problem in a simpler way: portable battery packs. For around $20, cyclists could purchase compact external batteries that would keep their phones charged throughout even the longest rides, eliminating our key advantage at a fraction of our device's projected retail price.
    

## Lessons Learned

This project's trajectory offers valuable insights for anyone considering hardware product development:

### 1\. Beware the Feature Integration Trend

When functionality becomes integrated into existing platforms as features rather than standalone products, the market often shifts permanently. Before developing dedicated hardware, honestly assess whether your target functionality has already been absorbed into existing ecosystems where users prefer consolidated solutions.

### 2\. Value Proposition Must Exceed Alternatives

For a hardware product to succeed against software alternatives, it must offer substantial advantages that cannot be easily replicated. Our beacon device offered incremental improvements but lacked truly transformative benefits that would justify its cost and the hassle of carrying another device.

### 3\. Consider the Full Product Journey

Hardware development requires navigating design challenges, engineering complexities, production ramp-up issues, and unpredictable supply chains. These hurdles demand a product with enduring value that can survive delays and challenges. Our beacon concept simply didn't have enough sustainable competitive advantage to justify this difficult journey.

## Conclusion

While Cyclebe's bicycle safety beacon showed initial promise, it ultimately couldn't compete with the efficiency of mobile solutions and the rapid integration of beacon functionality into existing training platforms.

What began as a standalone opportunity had quickly become a standard feature, leaving little room for a dedicated device.

For entrepreneurs and product developers, the lesson is clear: when considering hardware solutions in today's market, ensure your value proposition can withstand both feature integration and the efficiency of multipurpose devices. Your hardware must solve problems in ways that are so superior or unique that users will gladly pay for and carry another device.

Sometimes the wisest decision in product development is recognizing when to pivot or abandon a concept, however elegant its design or noble its intentions. In this case, cyclists are ultimately better served by continued improvements to mobile beacon solutions rather than introducing another device to their already crowded handlebars.

---

'***'

---

# Chapter 14 - Smart AND Secured? Think Again.

> ## <Add in context>
> <!--https://krebsonsecurity.com/2025/10/ddos-botnet-aisuru-blankets-us-isps-in-record-ddos/--> smart products be made to be secured? Listing attack vectors, and strategies to improve safety, data security, and privacy of smart connected and IoT products.

---
## [Part 1: Threats]

![A safe combination lock](./images/73dd11_d7c2e70fc657481181fe067d5cc421b7mv2.jpg)

Have the code? Are you the only one?

> _Smart tangibles present enhanced utility, but also increased security, privacy and safety challenges._

How smart tangibles are susceptible to both edges of this blade, is yet to be fully understood, as this stands at the core of differentiation for companies like Apple, and conversely, weaponized - rightfully or not - by governments in their trade wars.

## Table of Contents

-   Introduction
    
-   A Brief Introduction: The OSI Model
    
-   Cybersecurity and the OSI Model
    
-   OSI Model Adaptation to IoT
    
-   Notorious Smart Products Cyber Attacks
    
-   Further Reading
    

## What Seems to be the Trouble?

### A brief introduction: The OSI Model

The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes the functions of a telecommunication or computing system into several abstract layers, where each serves specific tasks and communicates with its adjacent layers, enabling interoperable network communication across heterogeneous systems.

![ISO 35.100 OSI model diagram](./images/73dd11_f66d8b412bf746a0a274305810e3179amv2.png)

Developed in the late 1970's this model was specifically adapted for client-server computer networks, and proved suitable for the internet era and the reality of widespread personal computers connecting to remote servers, and later to cloud services.

### Cybersecurity and the OSI Model

The layered structure of the OSI model also serves as a useful framework for understanding cybersecurity risks.

Each layer - from physical hardware to application logic - can be a vector for attack, and mitigation strategies are often layered accordingly, from firewalling at the network level to authentication and encryption at the application layer.

![Common security threats](./images/73dd11_fb36776648c74780b8a699937dc96089mv2.jpg)

### OSI Model Adaptation to IoT

Internet of Things (IoT) category of products introduces increased complexity as diversified hardware, connectivity, and interaction layers are introduced. This is captured in a slightly different OSI model, showing how devices, network infrastructure, protocols, and visualization tools interact in a layered stack - from raw hardware at the bottom to user-facing applications at the top.

![IoT adaptation of OSI model](./images/73dd11_ab5f118e689f4dabbe6f3314c6851089mv2.jpg)

Crucially, the IoT paradigm necessitates special attention to the hardware layer, as it consists of a vast variability of use cases, and to the application layer, as it is now split between the edge device and the web:

-   Inputs (keyboards and mice give way to other input devices)
    
-   Outputs (Screens vary wildly or are missing altogether)
    
-   Energy supply (the default AC mains give way to PoE, batteries, solar...)
    
-   Sensors and actuators (to some extent, the core purpose of this whole category)
    
-   Application (split between the device, the cloud, and web interface)
    

![Expanded layers of OSI for smart tangibles](./images/73dd11_afa31c462bdc4551aad428317fd0a357mv2.png)

Expanded layers of OSI for smart tangibles

### Smart and (not) Secured: New Structures - New Threats

Looking at smart and IoT products and their version of OSI structure, it becomes clear that unique vulnerabilities emerge at the embodiments of the physical layer, as well as at the extension to the cloud and beyond.

### Cyber attack vectors examples:

#### Physical Layer:

Tampering, side-channel attacks, sensor spoofing, power supply manipulation (battery draining, over-voltage), environmental sabotage (e.g., heat or vibration).

##### BrickerBot

-   **What happened**: Malware known as BrickerBot forcibly disabled (“bricked”) IoT devices. It targeted poorly secured devices at the firmware/hardware level, executing malicious commands that destroyed storage and cut network access - aligning with physical-layer sabotage.
    
-   **Smart elements exploited**:  by exploiting open Telnet services and weak/default credentials
    
-   **Impact**: More than 2 million devices were bricked before it faded away in late 2017.
    
    ------
    
    

#### Data Link:

Eavesdropping on unencrypted RF signals (e.g., BLE, Zigbee), MAC spoofing, jamming, replay attacks over local wireless protocols.

##### <u><span>Tesla Keyless Entry App Hijack (2016-2024)</span></u>

![Tesla keyless phone app](./images/73dd11_ea0db35779ca45fa9f62b75935d39866mv2.png)

Tesla keyless phone app. Source: [<u><span>Taslem</span></u>](https://talsem.com/blogs/tesla-tips/understanding-tesla-phone-key-functionality)

-   **What happened**: Security researchers exploited flaws in Tesla’s keyless entry system via the app’s Bluetooth Low Energy (BLE) connection. Using a relay attack, they tricked the vehicle into thinking the authorized phone was nearby and gained unauthorized access.
    
-   **Smart elements exploited**: Exploit used BLE signal relay to trick the vehicle into unlocking, targeting weaknesses in BLE communication (MAC spoofing, signal replay).
    
-   **Impact**: Demonstrated how over-the-air convenience features can become physical vulnerabilities.

------



##### <u><span>Flaws in Smart Locks (Various, 2016–2020)</span></u>

![](./images/73dd11_75c53ece672c485eab3f36c9c39c5783mv2.webp)

![](./images/73dd11_0ebf05f2a22746d48d15718ec5e72172mv2.webp)

-   **What happened**: Bluetooth sniffing and weak BLE protocols exposed device control, a data link level failure.
    
-   **Smart elements exploited**: BLE communication, cloud management interfaces, firmware updates.
    
-   **Impact**: Erosion of consumer trust in smart home security products.
    
    ------
    
    

##### <u><span>Coffee Shop MAC Spoofing</span></u>

-   **What happened**: Owners learned from their Internet Service Provider (ISP) that the spoofers were using the coffee shop’s network to Nmap scans.
    
-   **Smart elements exploited**: Nmap scanning is a way to look for open ports on a network to gather information about the devices connected to that network.

------



#### Network Layer:

Address spoofing (e.g., IPv6-related), insecure mesh routing, location tracking via IP leaks, exposure from gateway misconfiguration.

------



##### <u><span>VPNFilter Botnet</span></u>

The VPNFilter malware infected over 500,000 home routers and NAS devices around the world. It could intercept and alter network traffic - corrupting packet routing and enabling espionage, with capabilities including address spoofing and network misconfiguration. 

------

​	

#### Transport Layer:

Exploitation of lightweight protocols (e.g., CoAP, MQTT) with limited handshake/authentication, man-in-the-middle (MITM) attacks on UDP-based communication.

##### <u><span>CoAP Amplification Attacks</span></u>

Research has revealed that IoT devices using **CoAP** (a UDP‑based protocol) can be weaponized for reflected DDoS. Attackers send tiny spoofed CoAP requests that trigger amplified responses, overloading targets - an exploit at the transport layer. CoAP-based DDoS attacks can involve tens to hundreds of thousands of compromised IoT devices, drawn from a global pool of over 580,000 known vulnerable endpoints. These attacks generate highly amplified traffic, often reaching volumes of several hundred gigabits per second. The resulting financial impact is comparable to other large-scale DDoS incidents, with potential losses exceeding $200,000 per attack depending on the target and duration.

------



#### Session Layer:

Session hijacking due to weak or absent session management in embedded systems, protocol downgrade attacks.  

------

##### <u><span>FireSheep / DroidSheep</span></u>

Tools like **FireSheep** (for desktop) and **DroidSheep** (on Android) captured session cookies over unsecured Wi‑Fi, allowing attackers to hijack logged-in sessions. This is a textbook session hijacking attack at the session layer. Launched in October 2010, FireSheep was downloaded by approximately **200,000 users worldwide** soon after release. Each person using it could target dozens of devices on the same network in public hotspots.

------



#### Presentation:

Malformed data injection in minimal-format environments, encoding exploits in constrained parsing modules.

------



##### <u><span>Ping of Death</span></u>

Although not strictly IoT-specific, the **ping-of-death** attack sends oversized ICMP packets that overflow buffer-handling routines in networking stacks. It exemplifies malformed-packet attacks - presentation-layer exploits.

------



### Application:

Unauthorized remote control, firmware over-the-air (FOTA) hijacking, malicious update injection, insecure API endpoints, data leakage from sensor payloads.

- It seems that this layer is more vulnerable than others, or at least easier to detect.

- Some Notorious cases:

  ##### <u><span>St. Jude Medical (Abbott) Pacemaker Vulnerabilities (2017)</span></u>


![Pacemaker by Abbott](./images/73dd11_7311678703c24264bfd879b9f98bb9f1mv2.jpg)

Hacked: Pacemaker by Abbott

Security researchers, followed by confirmation from the FDA, revealed that St. Jude’s pacemakers and defibrillators were vulnerable to remote hacking through their wireless telemetry systems. The core vulnerabilities lay in the firmware update mechanisms and remote monitoring features, which exposed insecure APIs and allowed unauthorized remote control. As a result, a major recall was issued, accompanied by a public awareness campaign that affected over 400,000 devices.

------



##### <u><span>Jeep Cherokee Hack by Charlie Miller and Chris Valasek (2015)</span></u>

![Andy Greenberg/WIRED](./images/73dd11_7317e138097c4bfbaa3d9aa83f98b148mv2.webp)

Andy Greenberg/WIRED

Researchers demonstrated that the Jeep Cherokee’s Uconnect system could be exploited to gain full remote access to vehicle functions by targeting application-layer commands. The attack leveraged cellular connectivity, software update channels, and the integration between the infotainment system and critical vehicle controls. In response to the severity of the threat, Fiat Chrysler issued a recall affecting 1.4 million vehicles.

------



##### <u><span>Mirai Botnet Attack on IoT Devices (2016)</span></u>

![screenshot of malware code](./images/73dd11_bc190e604fc449499f893c9e28f068efmv2.jpg)

Screenshot / Tech Crunch

The Mirai botnet attack exploited default login credentials in embedded, internet-facing devices to gain remote control at the application layer — a textbook case of poor security hygiene. These devices, often shipped with hardcoded or unchanged credentials, were easily hijacked and conscripted into a massive botnet. The resulting DDoS attack targeted DNS provider Dyn, disrupting major services like Twitter, Netflix, and Reddit, and also overwhelmed the security blog KrebsOnSecurity with a 620 Gbps traffic surge.

------



##### <u><span>Ring Doorbell Camera Hacks (2019)</span></u>

![Ring doorbell camera](./images/73dd11_af062bdbdf1b4eeb9bdadf598b4d5620mv2.jpg)

Ring doorbell camera / abc news

Attackers exploited weak passwords and the absence of two-factor authentication to hijack video feeds through the Ring app’s cloud APIs. This security gap allowed unauthorized access to users’ home camera systems, sparking public outrage. In response, Ring implemented mandatory 2FA and enhanced its security communication to rebuild user trust.

------



##### <u><span>Nest Thermostat Ransom Attack (2019)</span></u>

![Image / Trend Micro](./images/73dd11_73edc07654d44c53950872d0bb9e5147mv2.jpg)

Image / Trend Micro

Nest users fell victim to credential stuffing attacks, where hackers used previously breached usernames and passwords to gain unauthorized access to their online accounts. This allowed attackers to remotely manipulate smart home devices, such as thermostats. In response, Google urged users to adopt stronger passwords and enabled two-factor authentication to mitigate future risks.

Read about mitigation in Part 2: [<u><span>Smart Product Cyber Threat Mitigation</span></u>](https://www.theroadtlv.com/post/smart-and-secured-think-again-part2)

**_Are you, too, considering security and privacy of your connected product users?..._**

------



#### Read more:

-   [<u><span>This is a part of the Hardware is Hard blog series. You can read it online here</span></u>](https://www.theroadtlv.com/post/product-management-for-the-physical-world-series).
    
-   [<u><span>"Smart Tangibles", the book, is due 2026. You can read about it here</span></u>](https://www.theroadtlv.com/post/smart-tangibles).
    
    ------
    
    

#### Further reading:

-   [<u><span>Federal Trade Commission</span></u>](https://www.ftc.gov/business-guidance/resources/careful-connections-keeping-internet-things-secure) Careful Connections: Keeping the Internet of Things Secure
    
-   BrickerBot:
    
    -   [<u><span>The Daily Swig</span></u>](https://portswigger.net/daily-swig/iot-protocols-are-leaking-data-like-sieves?utm_source=chatgpt.com) IoT protocols are leaking data like sieves
        
    -   [<u><span>Wikipedia</span></u>](https://en.wikipedia.org/wiki/BrickerBot?utm_source=chatgpt.com) BrickerBot
    
-   VPN filter botnet
    
    -   [<u><span>Hacker News</span></u>](https://thehackernews.com/2018/05/vpnfilter-router-hacking.html) Researchers unearth a huge botnet army of 500,000 hacked routers
        

-   Coffee Shops MAC spoofing:
    
    -   [<u><span>Stack Exchange</span></u>](https://security.stackexchange.com/questions/261310/identification-of-a-laptop-using-a-spoofed-wifi-mac-address) MAC Address Spoofing: How It Works and How to Protect Yourself
        

-   Tesla hacks:
    
    -   [<u><span>The Guardian</span></u>](https://www.theguardian.com/technology/2016/sep/20/tesla-model-s-chinese-hack-remote-control-brakes), Sep 2016: Team of hackers take remote control of Tesla Model S from 12 miles away
        
    -   [<u><span>Auto Evolution</span></u>](https://www.autoevolution.com/news/researchers-discovered-that-teslas-are-easy-to-steal-despite-adopting-new-keyless-tech-234343.html), May 2024: Researchers Discover That Teslas Are Easy To Steal Despite Adopting New Keyless Tech
        
    -   [<u><span>The Byte</span></u>](https://futurism.com/the-byte/teslas-stolen-wifi-charging-research), Nov 2024: Teslas can be stolen by hijacking WiFi at charging stations, researchers find
    
-   St Jude pacemaker hack:
    
    -   [<u><span>American Heart Association Journals</span></u>](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.118.037331) Nov 2018: Pacemaker Recall Highlights Security Concerns for Implantable Devices
    
-   Jeep Cherokee Hack:
    
    -   [<u><span>Wired</span></u>](https://www.wired.com/2015/07/hackers-remotely-kill-jeep-highway/) Jul 2015: Hackers Remotely Kill a Jeep on the Highway - With Me in It
    
-   Mirai Botnet Attack:
    
    -   [<u><span>Tech Crunch</span></u>](https://techcrunch.com/2016/10/10/hackers-release-source-code-for-a-powerful-ddos-app-called-mirai/) Oct 2016: Hackers release source code for a powerful DDoS app called Mirai
    
-   Ring Doorbell Camera Hacks:
    
    -   [<u><span>ABC News</span></u>](https://abcnews.go.com/US/ring-security-camera-hacks-homeowners-subjected-racial-abuse/story?id=67679790), Dec 2019: Ring security camera hacks see homeowners subjected to racial abuse, ransom demands
    
-   Flaws in Smart Locks:
    
    -   [<u><span>The Verge</span></u>](https://www.theverge.com/circuitbreaker/2018/6/13/17461612/tapplock-smart-lock-hack-bluetooth-low-energy) Jul 2018: This fingerprint-verified padlock is extremely easy to hack
        
    -   [<u><span>BGR</span></u>](https://bgr.com/tech/researchers-find-smart-door-locks-are-easy-to-hack-surprising-no-one/) Aug 2016: Researchers find ‘smart’ door locks are easy to hack, surprising no one
    
-   Nest Thermostat Ransom Attack:
    
    -   [<u><span>Trend Micro</span></u>](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/hacker-compromised-family-s-wi-fi-taunted-family-with-thermostat-camera-for-24-hours) Sep 2019: Hacker Compromised Family’s Wi-Fi, Taunted Family With Thermostat, Camera for 24 Hours
        

-   US ban on Huawei
    
    -   [<u><span>U.S. Restrictions on Huawei Technologies: National Security, Foreign Policy, and Economic Interests</span></u>](https://www.congress.gov/crs-product/R47012#:~:text=In%20November%202021%2C%20Congress%20acted,from%20the%20Entity%20List%20(S.)
        
    -   [<u><span>Huawei Says US Sanctions Will Reduce Revenue by $30 Billion</span></u>](https://www.wired.com/story/huawei-says-us-sanctions-reduce-revenue-dollar30-billion/)
        
    -   [<u><span>UK defence firms warn staff against connecting phones to Chinese-made EVs amid espionage fears</span></u>](https://www.computing.co.uk/news/2025/security/uk-defence-firms-warn-staff-against-connecting-phones-to-chinese-made-evs-amid-espionage-fears)
---
'***'

---

# Chapter 15 - Smart Product Cyber: Threat Mitigation.

---
## [Part 2: Mitigation]

![A safe combination lock](./images/73dd11_92ff41ad8d0c4eea85e4f0338a831b7fmv2.jpg)

Have the code? Are you the only one?

> _Smart tangibles present enhanced utility, but also increased security, privacy and safety challenges._

As the line between software and physical product continues to blur, mitigation becomes more complex as it is essential. Protecting smart tangibles demands an integrated approach - where supply chain security, firmware integrity, and cloud-based safeguards are treated as a unified surface of risk.



------



### What's To Be Done?

As a product manager specializing in [<u><span>smart tangibles</span></u>](https://www.theroadtlv.com/smart-tangibles), Security (with a capital S) is yet one more system requirements that should be taken into account, with minimal friction through user experience. While most aspects would be baked into hardware and backend levels, some will be externalized to the users, especially at the authentication layer.

Here are some recommendations, though your milage may vary:

1.  #### Designing for Resilience
    

-   **Principle**:
    
    Smart tangible products should assume hostile environments and users.
    
-   **Practices**:
    
    Threat modeling early in the product design; designing with fail-safes, redundant paths, and hardware-level integrity checks.
    
-   **Examples**:
    
    Physical anti tamper on higher security devices provide visible evidence to enclosure tampering. this may include [<u><span>adhesive graphic scratch off tapes</span></u>](https://evergreater.en.made-in-china.com/product/lOrEMLhCXtWD/China-Adhesive-Scratch-off-Red-Rolls-of-Anti-Tamper-Evident-Seal-Security-Stickers-Scratch-Stickers.html), [<u><span>labels</span></u>](https://www.pfwlabels.com/product/security-labels-tamper-proof/), [<u><span>wax seals</span></u>](https://durablesupply.com/dytaprtoma.html?srsltid=AfmBOoq5Ri_4TdN8sW2RdG-9lkL2xY_hcxiaoDLa4cs5_8V7OqZcX2DY) (just as in the Roman Empire), and single use [<u><span>snap-off bands</span></u>](https://worldwide.espacenet.com/patent/search/family/025454592/publication/US4732293A?q=pn%3DUS4732293).
    

2.  #### Mandating Secure Authentication Defaults
    
    ![Mandating Secure Authentication Defaults](./images/73dd11_437632bde01d4739859ccb5bc9339a23mv2.jpg)
    
    Image / Palmetto Security Group
    

-   **Principle:**
    
    Smart devices must not rely on insecure, hardcoded, or shared default credentials. Authentication mechanisms should be resistant to common attack patterns, anticipating real-world user behavior and adversarial access attempts.
    
-   **Practices:**
    
    -   Eliminate universal or default login credentials before shipping.
        
    -   Require users to create strong, unique passwords during initial setup.
        
    -   Enforce two-factor authentication (2FA) where remote access is available.
        
    -   Use account lockout and rate-limiting to prevent brute-force attacks.
        
    -   Restrict unauthenticated network access by default.
        
    -   Secure local interfaces (e.g., Bluetooth, USB, debug ports) with user consent prompts or authentication.
        

These practices are aligned with [<u><span>FTC guidance</span></u>](https://www.theroadtlv.com/post/smart-and-secured-think-again-part2#viewer-i8sgm363422), which stresses limiting unauthorized access by requiring authentication, limiting failed attempts, and logging authentication events to monitor for anomalies.

**Examples:**

-   **Roku** mandated 2FA in 2024 following a breach impacting over half a million accounts, enhancing login security across its ecosystem.
    
-   **Ring** added mandatory 2FA and better authentication UX only after significant public backlash in 2019, showing the pitfalls of reactive security design.
    
-   **Nest (Google)** experienced credential-stuffing attacks in 2019 due to password reuse, highlighting the need for built-in safeguards like breached credential detection.
    
-   **Ezlo Smart Home** proactively adopted multi-factor authentication as part of its onboarding and account setup flow, helping prevent unauthorized control of home devices.
    

3.  #### Security by Update
    
    ![Apple’s Secure Enclave](./images/73dd11_e61ce5245096440c911abaa7ec115b53mv2.jpg)
    
    **Apple’s Secure Enclave / Apple**
    
    -   **Principle:**
        
        Devices must be designed to accommodate secure, ongoing updates to fix vulnerabilities discovered post-deployment.
        

-   **Practices:**
    
    -   Implement secure update mechanisms using digitally signed firmware.
        
    -   Prevent rollback to older, vulnerable firmware versions.
        
    -   Notify users when updates are available and explain what changes are being made.
        
    -   Design fail-safes to recover from interrupted or failed updates.
        

-   **Examples:**
    
    -   **Apple’s Secure Enclave** ensures firmware updates are signed and authenticated before installation.
        
    -   **Google Nest** devices use over-the-air (OTA) encrypted updates with user transparency.
        

4.  #### Standardization and Regulation
    

![US Cyber Trust Mark](./images/73dd11_eebac5f070974846a01088b5211e699dmv2.jpg)

US Cyber Trust Mark

-   **Principle:**
    
    Regulatory frameworks help unify baseline security expectations and provide consumers with trust signals across products.
    
    Relying on established standards, manufacturers can accelerate innovation while drawing on best practices that also reduce legal risks.
    
-   **Practices:**
    
    -   Align development practices with recognized IoT security standards.
        
    -   Participate in voluntary labeling programs to signal compliance.
        
    -   Design for transparency and auditability in regulated environments (e.g., healthcare, automotive).
        

-   **Examples:**
    
    -   [**<u><span>ETSI EN 303 645</span></u>**](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf&ved=2ahUKEwidsdPJ6aaNAxW4MDQIHaZCOm8QFnoECAoQAQ&usg=AOvVaw1HKW4L2ShvvNyWbGEbuQ28): This is a globally applicable standard for consumer IoT cyber security. It covers all consumer IoT devices while establishing a good security baseline..
        
    -   [**<u><span>US Cyber Trust Mark</span></u>**](https://www.fcc.gov/CyberTrustMark): A voluntary FCC-led labeling initiative launched in 2023 to help consumers identify compliant, secure IoT devices.
        
    -   [**<u><span>FDA guidance</span></u>**](https://www.ftc.gov/business-guidance/resources/careful-connections-keeping-internet-things-secure): Mandates secure design and update strategies for networked medical devices, such as insulin pumps or pacemakers.
        

5.  #### Privacy as Product Differentiator
    

![Privacy and data security image](./images/73dd11_b803ed0d79a343949e6920ba9ba74b2bmv2.jpeg)

Image / IBM

-   **Principle:**
    
    Respecting user privacy by design can become a competitive advantage, not just a compliance checkbox.
    
-   **Practices:**
    
    -   Minimize data collection to only what is essential for functionality.
        
    -   Enable on-device processing where possible to reduce cloud dependency.
        
    -   Provide clear user consent flows and data visibility controls.
        

-   **Examples:**
    
    -   **Apple** promotes on-device data handling (e.g., health metrics, FaceID processing) to reduce cloud exposure and position itself as privacy-centric - and is willing for now to pay the price in ai performance.
        
    -   [**<u><span>EU GDPR</span></u>**](https://gdpr-info.eu/) requires data minimization and user access to collected personal data - principles increasingly echoed globally.
        

6.  #### Third-Party Audits and Certifications
    

![Trust Layer audits and certification](./images/73dd11_f2bcc6234f9447bfba062ab564369271mv2.png)

Audits and certification / Trust Layer

-   **Principle:**
    
    Independent security assessments validate vendor claims for seecurity, safety, and privacy by identifying vulnerabilities that developers may overlook - before products reach mass production.
    
-   **Practices:**
    
    -   Engage third-party security labs for penetration testing and protocol validation.
        
    -   Launch vulnerability disclosure and bug bounty programs.
        
    -   Use third-party compliance frameworks to demonstrate maturity.
        

-   **Examples:**
    
    -   [**<u><span>HackerOne</span></u>**](https://www.hackerone.com/product/code-security-audit) and [**<u><span>Bugcrowd</span></u>**](https://www.bugcrowd.com/resources/guide/ultimate-guide-to-crowdsourced-security-for-saas-companies/) power responsible disclosure and bug-bounty programs for companies like DJI, Fitbit, and General Motors.
        
    -   [**<u><span>SOC 2</span></u>**](https://www.imperva.com/learn/data-security/soc-2-compliance/#:~:text=SOC%202%20is%20an%20auditing,when%20considering%20a%20SaaS%20provider.), [**<u><span>ISO/IEC 27001</span></u>**](https://www.iso.org/isoiec-27001-information-security.html), and [**<u><span>Common Criteria</span></u>**](https://www.commoncriteriaportal.org/) certifications are increasingly applied to IoT platforms handling sensitive data.
        
    -   **Google** and **Microsoft** routinely publish security audit results and threat modeling outcomes.
        

-   #### Empowering Users
    
    ![Empowering users](./images/73dd11_832e9f4fcdf54af684a87d6853d06c3bmv2.jpg)
    
    Empowering users / Wix Ai
    
    -   **Principle:**
        
        Users are the first line of defense. They must be given clear information and tools to protect their own device and data.
        

-   **Practices:**
    
    -   Provide educational prompts during onboarding about security and privacy settings.
        
    -   Show clear device states (e.g., “camera is on” lights, permission icons).
        
    -   Offer simple interfaces for permission management, device logs, and firmware updates.
        

-   **Examples:**
    
    -   **Ring** added a security control center within its app after high-profile hacks to help users manage linked devices and logins.
        
    -   **iOS** and **Android** show ongoing indicators (dots, status bars) when sensors like camera or microphone are in use.
        
    -   **TP-Link** allows users to view and revoke cloud access via its mobile app’s “device status” dashboard.
        

8.  #### The Limits of Automation
    

![Charlie Chaplin's Modern Times](./images/73dd11_ab421989b452455cb48fdf8c6b8c26admv2.jpeg)

Charlie Chaplin's Modern Times / Britannica

-   **Principle:**
    
    Automation can enhance usability but must not obscure control or security-related transparency.
    
-   **Practices:**
    
    -   Allow users to override or disable automated decisions, especially when data is shared externally.
        
    -   Avoid black-box machine learning that affects safety-critical functionality without explainability.
        
    -   Require explicit user input for actions like unlocking doors or authorizing transactions.
        

-   **Examples:**
    
-   **Tesla** allows manual override of its Auto-Pilot system and requires driver engagement for safety.
    
-   **Smart thermostats** like Ecobee allow manual control even when running AI-based energy optimization routines.
    
-   **AI-driven door locks** should include fallback PINs or key overrides to mitigate lockouts from false positives.
    

9.  #### Toward Ethical Smart Design
    

-   **Principle:**
    
    Security, privacy, safety, and user autonomy must be baked into the product development and operational lifecycle, not treated as afterthoughts.
    
-   **Practices:**
    
    -   Cross-functional collaboration between product, security, legal, and ethics teams during ideation and testing.
        
    -   Prioritize user agency: require consent, offer opt-outs, and make data use legible and granular.
        
    -   Consider long-term social consequences of data collection, behavioral nudging, and opaque monetization models.
        

-   **Examples:**
    
    -   **Mozilla Foundation** publishes an annual [**<u><span>Privacy Not Included</span></u>**](https://www.mozillafoundation.org/en/privacynotincluded/) report to spotlight ethical gaps in consumer devices.
        
    -   [**<u><span>Framework Laptop</span></u>**](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://frame.work/%3Fsrsltid%3DAfmBOooLUbPTVGYhD9zvzMyop4tjF1MH0wi8xJRjjHJKhs2AvV2A-FvY&ved=2ahUKEwiWhoqE9aaNAxXQKDQIHXM7MNgQFnoECAsQAQ&usg=AOvVaw0rk_5Q36h3fOcdyxynEGN_) and [**<u><span>Fairphone</span></u>**](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.fairphone.com/&ved=2ahUKEwiHsoCU9aaNAxWYITQIHa7GMOsQFnoECBAQAQ&usg=AOvVaw0QXxgTcYex_b0x7n_MjZ5T) embody repairability, transparency, and ethical sourcing in product design.
        
    -   [**<u><span>Apple’s App Tracking Transparency</span></u>**](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://developer.apple.com/documentation/apptrackingtransparency&ved=2ahUKEwju67Oi9aaNAxWLDTQIHZskNikQFnoECA4QAQ&usg=AOvVaw2N-ozC716J7qPyUmpMwu_X) lets users deny cross-app tracking - reflecting a growing demand for ethical default settings.
        

## What's Not To Be Done?

### Out in the Open

Governments declare and conduct policies, along with international governing bodies, standards organizations - to protect their citizens from cyber security threats. These actions may start in legislation, regulatory actions, international cooperation.

On the other hand, governments have been known in the past to use regulation as a non-tariff-barrier in order to impede entry or rapid expansion of foreign companies, protect domestic manufacturing.

An outstanding example to this practice is the US ban on Huawei, the Chinese telecommunication giant:

In May 2019, the U.S. added Huawei to the Department of Commerce’s Entity List, barring American firms from doing business with it without a license. This followed the 2019 NDAA, which had already banned federal use of Huawei gear over national security concerns tied to the company’s links to the Chinese government.

The FCC later banned Huawei equipment sales, citing security risks. These actions disrupted Huawei’s global operations, cut revenues, and pushed it to develop alternatives to U.S. technology. U.S. pressure also led allied nations to reassess Huawei’s role in their critical infrastructure.

(You can read more about the impact on Huawei business in [<u><span>Wired article</span></u>](https://www.wired.com/story/huawei-says-us-sanctions-reduce-revenue-dollar30-billion/) from June '17)

While the official rationale emphasized national security, many analysts highlight protectionist motives. Huawei’s leadership in 5G challenged U.S. tech dominance, especially given the lack of a domestic telecom giant.

The ban aligned with broader efforts to decouple from Chinese supply chains and stimulate domestic tech investment. Outlets like [_<u><span>The Economist</span></u>_](https://www.economist.com/special-report/2019/05/16/trade-can-no-longer-anchor-americas-relationship-with-china) _<u><span>(Here too)</span></u>_, [_<u><span>Brookings</span></u>_](https://www.cfr.org/report/securing-5g-networks), and [_<u><span>CSIS</span></u>_](https://www.cfr.org/report/securing-5g-networks) view the policy as both strategic and economically motivated.

An even more recent the ban on Chinese electric vehicle use in government agencies in the UK was cast In 2025 by the UK government implementing measures restricting the presence of Chinese-made electric vehicles (EVs) at sensitive military sites.

Reports indicated that staff at facilities like RAF Wyton were instructed to park such vehicles at a distance from key buildings due to cybersecurity concerns. The Ministry of Defence’s directive was based on fears that embedded technology in these EVs could be exploited for espionage, potentially compromising sensitive data.

While not a blanket ban, this policy reflects the UK’s cautious approach to foreign technology in critical areas. The move aligns with broader efforts to safeguard national security amidst increasing integration of connected technologies in everyday assets.

### In the Shadows

While governments publicly champion the protection of citizens and businesses from espionage, they frequently employ similar tactics themselves - typically under the banner of national security. Yet in some cases, these actions extend to surveilling political rivals, activists, and journalists, often without clear justification or judicial oversight, revealing a troubling use of power beyond legitimate defense.

Governments have repeatedly engaged in covert surveillance of their own citizens, targeting journalists, activists, and political opponents. In [<u><span>Hungary</span></u>](https://www.theguardian.com/world/2021/jul/19/hungarian-journalists-targeted-with-spyware-in-government-backed-attacks), Pegasus spyware was used to monitor investigative reporters and critics of the regime.

In [<u><span>Italy</span></u>](https://www.politico.eu/article/italy-prosecutors-investigate-intelligence-agency-over-illegal-spying-allegations/), intelligence officials were investigated for unlawfully surveilling judges and journalists tied to anti-corruption and mafia cases. In the U.S., the [<u><span>NSA’s mass surveillance</span></u>](https://www.theguardian.com/world/2013/jun/06/nsa-phone-records-verizon-court-order) programs, exposed by Edward Snowden, revealed widespread, warrantless data collection.

Germany’s [<u><span>BND</span></u>](https://www.dw.com/en/german-intelligence-agency-spied-on-journalists-worldwide/a-19079783) also spied on domestic and foreign reporters. These cases show how democratic governments, citing security, often bypass oversight to suppress dissent.

### **Security Product Leadership**

What can - and should - product leaders do about these tendencies?...  

Product leaders occupy a critical junction between innovation, user experience, and responsibility. As smart products become vectors for surveillance - whether by governments, third parties, or internal misuse - leaders must take an active stance in defending user trust and civil liberties.

1.  **Design with abuse scenarios in mind**
    

Anticipate not only technical failure, but **intentional misuse** of features (e.g., always-on microphones, location sharing). Ask: **_What happens if this is used against the user?_**

2.  **Push for transparency and control**
    

Ensure clear communication around data collection, storage, and sharing. Give users **genuine control** - not just buried toggles or legalese.

3.  **Advocate for secure, privacy-respecting defaults**
    

Don’t wait for regulators. Enforce **end-to-end encryption**, disable unnecessary telemetry, and avoid dark patterns that coerce consent.

4.  **Challenge questionable business requirements**
    

Push back when leadership or clients demand functionality that compromises user agency. Align product integrity with **long-term brand trust**.

5.  **Lead internally by example**
    

Foster a culture where security, ethics, and **user respect are non-negotiable**. Collaborate with legal, privacy, and engineering teams early in the roadmap.

**_Are you too considering security and privacy of your connected product users?..._**

##### Read more:

-   [<u><span>This is a part of the Hardware is Hard blog series. You can read it online here</span></u>](https://www.theroadtlv.com/post/product-management-for-the-physical-world-series).
    
-   [<u><span>"Smart Tangibles", the book, is due 2026. You can read about it here</span></u>](https://www.theroadtlv.com/post/smart-tangibles).
    

##### Further reading:

-   [<u><span>Federal Trade Commission</span></u>](https://www.ftc.gov/business-guidance/resources/careful-connections-keeping-internet-things-secure) **Careful Connections: Keeping the Internet of Things Secure**
---
'***'

---



# Chapter 16 - Smart Business Models for Smart Tangibles



Blending Goods and Services Economics

![calculating costs](./images/nsplsh_e7f8a18b1daa415b97179cc704e958b9mv2.jpg)

getting smart about unit economics

## Rationale

This chapter is about the underlying economic forces that drive users and buyers' behavior - as well as vendors' fortunes - in the space of smart tangibles: Things that think, interact, and communicate.

Production Economics, Cost accounting, and Managerial Accounting are well trodden concepts as they pertain to either physical goods or digital wares. However, successfully melding them together to crate smart business models for the sake of better value offering and extraction is a delicate balancing act.  

It is this careful balancing act, though, that opens for extraordinarily lucrative opportunities, so we learned from smart tangible vendors, such as Apple or Tesla. 


---

## a. Contribution Margin and Break Even Quantities: Economic Viability Assessment

![Business models](./images/nsplsh_f3af97add28145769389b85281455487mv2.jpg)

Business models start simple



### What Is Contribution Margin?

At the heart of every productive activity lies the need to generate profit for stakeholders. This profit is derived from the difference between the product’s sale price and its Cost Of Goods Sold (COGS), commonly known as the gross margin, or more precisely, the contribution margin.

This concept disposes of the cost of infrastructures, the complexities of deferred payments, the intricacies of purchasing, inventory management, and ongoing liabilities - as it ignores the expneses involved with R&D and the notorious G&A (General and Administrative). The focus is therefore purely on the economics of a single unit manufactured and sold.

### Contribution Margin Formula: Unit Economics

As simple as it fundamental to economic life, the principle of "Buy low, sell high" is exemplified in manufactured goods by the imperative to sell products at profit - at the very least at the unit level.

Can't go around it.

> ***CM = Revenue - COGS\***

Where:

-   CM: Contribution Margin
    
-   COGS: Cost of Goods Sold

https://preview--formula-flow-fc2a90fc.base44.app/FormulaDetail?slug=contribution-margin

### The Reality of Fixed and Variable Costs

Contribution margin, however, presents an over simplistic version of industrial reality. Operating a business requires infrastructure, which brings about fixed costs.

Such infrastructure must be adapted to the production scale, and in addition to ongoing operational costs, it often includes financing and long-term commitments.

Therefore, when pricing a future product, one must ensure that the projected revenues from anticipated sales volumes cover both fixed and variable costs. This leads to an analysis based on costs, volumes, and profitability.

***P = q × (R − VC) − FC\***

Where:

-   P: Profit
    
-   q: Number of units sold
    
-   R: Price per unit
    
-   VC: Variable cost per unit
    
-   FC: Fixed costs

https://preview--formula-flow-fc2a90fc.base44.app/FormulaDetail?slug=profit-formula

### Break-Even Quantity Explained

Let us consider a simplified company, which sells a single product only. The break-even quantity is the number of unit the company must sell to start turning profit.

**Q=FC/(R-VC)**

Where:

-   Q: Minimum quantity required to break even
    
-   FC: Fixed costs
    
-   R: Price per unit
    
-   VC: Variable cost per unit

https://preview--formula-flow-fc2a90fc.base44.app/FormulaDetail?slug=break-even-quantity

This quantity is of important especially when planning: Will sales be able to commit to these numbers within a given budget, and within a timeframe?

It serves as also as a reality check for the convergence of price, cost, quantities - and whether management can envision how these parameters sync .

### Break-Even Quantity as a ratio between fix costs and margins

Beyond operational costs, infrastructure setup also entails capital investment. This too is expected to be recovered through future sales. A standard tool for evaluating this is Break-Even Analysis, which determines how many units must be sold to cover all fixed and COGS.

To do so we first integrate sales and COGS - through use of the contribution margins. The

> **BEQ=TFC/CM**

Where:

-   BEQ: Break-Even Quantity
    
-   TFC: Total Fixed Costs (including capital expenditures)
    
-   CM: Contribution Margin

https://preview--formula-flow-fc2a90fc.base44.app/FormulaDetail?slug=break-even-cm

An important question following this analysis is whether the expected market can absorb the required sales volume – ie, is the project/product/service viable?

### Strategic Levers: Price and Infrastructure

There is often more than one possible outcome to this analysis, as several parameters are under managerial control:

-   Infrastructure: Lower investment may reduce fixed costs but could increase unit costs.
    
-   Price: Adjusting unit price affects market acceptance and demand.
    

---

'***'

---

## b. The Cost of Capital



### Time Value and Risk Premium

![Business models](./images/nsplsh_f3af97add28145769389b85281455487mv2.jpg)

Business models start simple

### Scope:

In the [<u><span>previous chapter</span></u>](https://www.theroadtlv.com/post/business-models-contribution-margin), we explored costs, volumes, and contribution margin. However, two critical dimensions were left unexamined:

Time, and Risk. 

These factors are fundamental in shaping a project’s true profit potential, as they define the **opportunity cost of capital** - the value of the best alternative foregone when choosing one investment path over another of similar risk.

A clear understanding of both internal and external factors enables management to make fair comparisons—_oranges to oranges_. A project must first meet its own internal profitability threshold. Only then can it be meaningfully evaluated against other available opportunities that carry comparable risk.

### What Is the Time Value of Money?

The **cost of capital** is partly determined by the time during which money is committed.

If you borrow money today, the lender expects compensation not just for the amount itself, but for the fact that it is unavailable to them during the loan period.

One reason or justification is simple: A Dollar today is worth more than a Dollar a year from now. Inflation alone accounts for that, as the cost of living increases over time: the purchase power of that coin erodes over time.

This compensation is expressed through **interest**.

There are two primary ways to calculate interest: **simple** and **compound**.

### Simple Interest

In this model, interest is calculated linearly based on the original amount (the principal).

*Bₙ = B₀ + n ×* *R × B₀*

Where:

-   Bₙ: Total repayment at the end of period _n_
    
-   B₀: Initial borrowed capital
    
-   n: Number of periods
    
-   R: Interest rate per period
    

**Example:** Borrowing $100 at 7% interest for 5 years → _Bₙ = 100 + 5 x (1.07)⁵ ≈ $135_

https://preview--formula-flow-fc2a90fc.base44.app/FormulaDetail?slug=simple-interest

------



### Compound Interest

Here, interest is calculated on both the principal and the accumulated interest from previous periods.

Unlike simple interest, compound interest grows exponentially over time.

*Bₙ = B₀ × (1 + R)ⁿ*

Where:

-   Bₙ: Total repayment at the end of period _n_
    
-   B₀: Initial borrowed capital
    
-   n: Number of periods
    
-   R: Interest rate per period
    

**Example:** Borrowing $100 at 7% compound interest for 5 years: ➔ _Bₙ = 100 × (1.07)⁵ ≈ 140.3_



This is nearly 4% more than the simple interest scenario.Over longer periods, the gap becomes dramatic - after 20 years, for instance, compound repayment is **over 60%** higher.

As Albert Einstein most probably did not say:  

> _Compound interest is the most powerful force in the universe._
>
> https://preview--formula-flow-fc2a90fc.base44.app/FormulaDetail?slug=compound-interest
>
> ------
>
> 

#### Product Implications - Focus on features that accelerate revenue generation

Features or products that generate revenue (or learning) sooner are more valuable than those that take years to pay off.

**MobileAccess Example**:

This is a pure hardware example. Mobile Access (Then Foxcom, later [<u><span>acquired by Corning</span></u>](https://www.corning.com/worldwide/en/about-us/news-events/news-releases/2011/03/news_center_news_releases_2011_2011030201.html)) came with ModuLite, a series of multi carrier multiplexers channeling RF signals over fiber optics from external antennas to in-campus base stations.  

![ModuLite multiplexers](./images/73dd11_12d53b203231439187cbd16efffedd5fmv2.jpg)

ModuLite multiplexers

From the outset, this series was planned to be mass produced. The enclosure material being Aluminum to help dissipate residual heat was supposed to be die cast - a process that would result in low cost, high quality moldings. The problem: Injection dies manufacturing is a lengthy process, with duration of 3 – 6 months for similar products, only then you have to ship the dies to a local facility, or - alternatively - inject overseas and ship the empty enclosures for assembly and testing: Account for additional weeks in transport, customs clearance.

This project, however, was not born in vacuum: A pressing order was due, critically important to the financial prospects of the company.

The solution found for this dilemma was to manufacture the first batch of several hundred units using machining - a much slower, much expensive, and in the long run unsuitable for mass production.

The decision lenses were:

-   How fast can you get to the market?
    
-   How fast can you start charging for your product?
    
-   How much would you lower your margins to expediate revenue?
    

True, in software the answer is usually clearer, with marginal costs approaching 0...

------



### Risk and Risk Premium

The time value of money, with the relatively constand fact of inflation, does not, however, comprise the whole picture when it comes to the cost of capital.

*Enter Risk.*

While time is an absolute, **_Risk_** is a little more subjective, and it is assessed by the lender (or investor) -based on rating agencies, industry analysts, and the investor's own assessment, based on their domain knowledge and experience. No way to avoid uncertainty: Will the borrower repay on time? Will the return on investment be positive?

To compensate for this , well diversified\* lenders apply a **risk premium** on top of the baseline ("risk-free") rate. \* A well-diversified investor spreads investments across a variety of asset classes, sectors, and geographies to reduce exposure to individual risks and achieve more stable long-term returns.

> *iT = R<sub><span>f</span></sub> + R<sub><span>p</span></sub>*

**Where:**

-   iT: Total interest rate
    
-   R<sub><span>f</span></sub>: Risk-free rate (e.g., government bonds)
    
-   R<sub><span>p</span></sub>: Risk premium (reflecting borrower/investment risk)
    

**Example:** If government 10-year bonds (until recently considered 'risk-free') yield 0.9% interest, and a venture is considered high-risk, the investor might require a total return of 12%-20% from the venture.

https://preview--formula-flow-fc2a90fc.base44.app/FormulaDetail?slug=risk-premium

Let's discuss this example a bit more.

Suppose you are a lender extending credit to 100 borrowers, of which 5% will default. Let's also assume for simplicity risk premium is the only interest you charge.

If you lent $1 each, and 5% default, you are bound to be $5 in the hole, at the of the cycle.

In order for you just to recoup your initial capital of $100, you must require ~5.3% interest.

This would be the **Risk Premium.**

The problem is, of course, you cannot know in advance the amount of defaults in any single cohort – all you have are assessment and actuary calculations, depending on the nature of the loan (or investment), the time frame, the heterogeneity of borrowers, and the overall economy.

#### Product Implications - Choose MVPs that de-risk future investments

The more uncertain a project’s outcome, the higher the expected return must be to justify pursuing it. PMs must frame early efforts as risk-reduction activities. After all, isn't the whole 'Lean' movement just about that?

#### tvDots MVP:

> Your Newspaper. Now on TV.

Ambitious as it was in pre-LLM 2020, the startup combined text-to-speech and video-creation technologies to convert any news site into an automated, live, TV broadcast grade channel stream.

![tvDots](./images/73dd11_460422361e98470f9e6df54f55ebf10bmv2.png)

tvDots News to Video Pipeline

The technical challenges were substantial. How can you automatically ingest and parse news stories into a narrator ready text? How do you avoid silly errors and monotonous mechanical narration? Can you do it at scale?

Instead of building the full pipeline, AudioDots opted for integrating 3rd party services both for the TTS and video generation, at a cost of limited control, and substantial uni cost: Each newsclip incurred significant production costs, that would have been minimized with homebrew technology stack.

The decision lenses were:

-   What’s the smallest version of this initiative that reduces uncertainty and still yields usable data?
    
-   How fast can you get in front of paying customers and design partners?
    

### The Opportunity Cost

At the core of every investment decision lies a fundamental question:

> “Do I have better use to this capital?”

Investing a significant amount in a new product doesn’t just commit funds - it closes the door, at least temporarily, on other potential opportunities. Those alternatives might be more profitable, carry less risk, or deliver returns faster.

This trade-off is what defines the opportunity cost of capital. It's not just a financial calculation - it's a reflection of strategic priorities, resource constraints, and competing bets on the future.

In product development, where risk is high and resources are limited, understanding this cost is essential. It helps ensure that capital is not just used wisely, but used where it creates the most value.

#### Product Implications - Ruthless prioritization

Given the competitive nature of all industries, let alone startups racing for supremacy necessary for survival, the cost of capital question boils to prioritization.

What should we build now, what will have to wait?

Prioritization is worth a chapter in its own, especially when addressing smart tangibles (which weigh differently: Hardware gambles are riskier and longer). However, I find RICE the most relevant to the issue of opportunity cost of capital.  

RICE – Reach, Impact, Confidence, Effort  – helps prioritize features by estimating their potential value vs. the effort required.

Considered great for growth and roadmap decisions, it allows comparison between competing strategic alternatives, through the lens of financial planning.

---

'***'

------

## c. NPV: Profitability Assessment, Done Right:

## Integrating Time, Risk, and Alternative Costs

![Business models](./images/nsplsh_f3af97add28145769389b85281455487mv2.jpg)

Business models start simple



### Is My Project Profitable?

There are several methods used to answer this question, and as any finance professor will tell you, the preferred method is the **Net Present Value (NPV)** calculation.

But first, let address the lexical meaning of this quite complex term:

-   "Net" means after all inflows and expenses
    
-   "Present" means bringing future (positive and negative) cashflows to current date, accounting for the time value of money and the risk premium assigned to the project.
    

(Truth to be told, you rarely know all the parameters needed to answer, uncertainties are baked in, and there are many shortcut methods about - each to their benefit and use.)  

NPV addresses the question:

> _What is the present value of a series of future cash flows?_

**Positive** NPV indicates that the project is profitable .

**Negative** NPV suggests the project is expected to lose money.

The calculation takes a series of future cash flows, in their nominal <u><span>future values</span></u>, and **discounts** them -meaning it reduces each cash flow based on the cost of capital relative to the present.

An expense of $500,000 today is worth exactly $500,000.

But an expected income of $500,000 a year from now is worth **less** today – depending on the cost of capital, and we need to **_discount_** it by the discount factor based on the time frame and associated risk.  

This is why it is also called DCF - Discounted Cash Flow.

### NPV Calculation:

The **present value (PV)** of a future sum (FV) is calculated by dividing the future amount by a **discount factor**:

> **_Discount factor =  (1 + R)ⁿ_**

Where:

-   **R** is the interest rate per period
    
-   **n** is the number of periods

Critically, this discount factor is exactly the "Cost of Capital" mentioned in [<u><span>section 2</span></u>](https://www.theroadtlv.com/post/the-cost-of-capital) when we discussed risk premium. While I will not further detail here the making of the cost of capital, you can find further discussion [<u><span>here</span></u>](https://www.theroadtlv.com/post/valuation-financing-strategy).

The present value for a cash flow at a future period n is:

Where:

-   **PV** is the present value
    
-   **FVₙ** is the future value at period _n_
    
-   **Rₙ** is the interest rate applicable to that period
    

The value of a series of future cash flows is:

>  **_NPV₀ = FV₀ / (1 + R₀)⁰ + FV₁ / (1 + R₁)¹ + FV₂ / (1 + R₂)² … + FVₙ / (1 + Rₙ)ⁿ_**

(Do note that some of these cashflows can - and will - be negative)

Let’s consider a hypothetical project:

An initial expense of **$500,000 today**, and an expected income of **$500,000 in one year**, accruing interest at period rate of **5%**.

The present value of the future income is:

➔ PV = FV / (1 + R)ⁿ = 500,000 / (1 + 0.05)¹ = 500,000 / 1.05 = 476,190

The Net Present Value (NPV), however, is negative, accounting for the initial expense at period 0:

➔ NPV = -500,000 + 476,190 = -23,810

In other words, there’s no reason to invest in this project. Try it yourself:

https://preview--formula-flow-fc2a90fc.base44.app/FormulaDetail?slug=npv



It’s important to note that the the formula provided took a single interest value R, but in real life, **variable interest rates** (lower one, hopefully) can apply to later stages, when the business stabilizes and the risk decreases.

Indeed, the risk of a project that has already demonstrated, for instance, profitable sales is very different from the risk of a project that is still just a concept.

Additional factors should be incorporated into the NPV model, such as:

-   Inflation
    
-   Long-term continuity
    
-   Revenue growth
    
-   Planned project termination
    

The core principle, however, remains the same.

Note that there are advanced tools to calculate more complex scenarios - but in the above example I chose clarity over sophistication.

Read about Capital Budgeting in Part 4: Extending Customer Lifetime Value

​	
---
'***'

---

# Chapter 17 - From Recurring Revenue to Customer Loyalty and Beyond



## Winning the Long Game with Smart Products

![Business models](./images/nsplsh_f3af97add28145769389b85281455487mv2.jpg)

Business models start simple

###### Business Models for Smart Products - Section 4

### The Durable Goods Predicament - One and done

Consider any durable good you can think of: A chair, a TV, a car, a mobile phone. A common trait of durable goods is implied from the very name: They're **durable**. Once procured, they are used through a long period of time, until their (almost) inevitable succumb to wear and tear.

There is no intrinsic relationship between the maker and the users of this product. Next time consumers go shopping for a waste bin, they are more likely to purchase other brands' bin than this particular one. Way of the world.

Consider an archetypal durable good, such as a residential waste bin (Could be any product, really, but I vouch for this particular one, having designed it in 1998):

![Dolav 300l Waste Bin](./images/73dd11_e414bd4f5032299e899de95e2b4d12a9.jpg)

Dolav 300L Waste Bin

What is the business model sustaining the manufacturer of such products?...

#### Unit Economics

In this example, we have the BOM (Bill Of Material) cost of all parts

\* All costs are for reference and do not rely on actual data

\*\* Assume capital investment was already amortized

| Part / Process       | Cost       |
| -------------------- | ---------- |
| Main Body            | $12.00     |
| Wheels               | $8.00      |
| Axle                 | $3.00      |
| Cover                | $2.00      |
| Cover hinges         | $3.00      |
| Assembly / Packaging | $2.00      |
| **Total**            | **$30.00** |

Now consider a hypothetical sales price of $40 per unit, and there, you have it: A profit of $10, just above 25% margin - not unheard-of for durable goods. Of course, this is an Ex-Works calculation, ignoring costs and price inflating as we go down the distribution chain.

All this is common knowledge, you might say, and what seems to be the problem, then?...

#### Cost of Acquisition

Well, manufacturing is not enough to put products into the hands of consumers: Marketing and Sales are to be accounted for: Generating awareness, raising interest, and convincing prospective buyers spend their hard won money on our product, (and do it now!), is a costly business.

We attribute marketing and sales costs to the number of units sold, so that we can bake them into the unit economics. Let's say the marketing expenses for said waste bin were $100,000 for 50,000 units sold - this puts the average Cost of Customer Acquisition at $2.00, eating our margins by 20% (but what can you do - this is the way of the world).

#### One and done? Product Life Cycle

I still have one of these 1998 bins. It works... No real reason to replace it, is it? This is my consumer's point of view. Manufacturers' perspective differ dramatically, since they are in the business of churning products - they have to keep the machine going. Consider the sales chart of a single typical durable good: I have plotted an idealized Gompertz derived sales cycle in blue, and the more sinister reality of industrial goods, declining sharply once competition and alternatives kick in.  

![Typical durable good sales cycle](./images/73dd11_0590e2cb46af4309987cbc15c210e0a0mv2.png)

Typical durable good sales cycle

Let us now consider the overall financial picture of a successful product:

![single product - financial life cycle](./images/73dd11_c67d0b9aa0604f0c918ce2902f3bcaf0mv2.png)

Financial life cycle of a single product

As you can observe, there is an accumulation of Non Recurring Expenses (and resulting losses) prior to the launch - this is where R&D, tooling, and provisioning ramp up.

In the waste-bin example above, tooling costs were at 1998's $1.5M range. Post launch, NRE stop, and variable costs kick in, resulting in profit margins (this example is modeled at 35%).

As the products penetrates and saturates the market, revenue dwindles, and manufacturers must, therefore, come with new products, find market for them, build manufacturing capacity, market again - or sales would dwindle to zero. All this, while running the risk of launch failure or mediocre sales performance.

![Expenses peak before and during launch - here seen for successive launches
](./images/73dd11_16f779c4ad7b49d39db513097717d38bmv2.png)

Expenses peak before and during launch - shown for successive launches

As you can see in the chart above, launch expenses peak towards and during launch events. Crucially, this is a periodic, repeating phenomenon, requiring capital allocation, deteriorating manufacturers' financial health in the process.  

#### A Side Story: Planned Obsolescence

You know what's in the picture, don't you?  

![The Centennial Light Bulb from Livermore, CA](./images/73dd11_0a6409b2ac5541ae85dc0c9a4eb9b90emv2.jpg)

The Centennial Light Bulb from Livermore, CA

–"It's a light bulb"

True, but the full story is that this lightbulb is constantly illuminated since 1901. Yes, you got that right. It is still running 124 years on.

The **Phoebus cartel** - a consortium formed in 1924 between major lightbulb manufacturers including Philips, Osram, and General Electric - took notice of that longevity in horror. While initial market penetration was in full swing, what would manufacturers do when every household and office in the US bought their lifetime-and-beyond enduring lightbulb? This would drive them out of business...

In their infinite wisdom, they set a 1,000 hours lifetime limit on all the lightbulbs produced henceforth, "for the greater good", meaning to increase the purchase frequency, and consequently, their profit, Sherman Anti-Trust Act be damned.

This only goes to show the acuity of the durable good predicament - its durability, and how it impacts the lifecycle, consumer choices, and market behavior.

### Recurring Revenue Models for Hardware Manufacturers

Although the Phoebus cartel is infamous for its dubious methods, there are plenty of legitimate business models for increasing product revenue.

Companies can, for example, use disposables instead of multi use products: Think of single use surgical masks and gloves. But there are other business models ammenable for recurring revenue.

#### Razor and Blades

Invented and perfected by Gillette, the razor-and-blade approach taken by brands like Gillette and Nespresso saw them rise to global dominance, with varying levels of success.

The first Nespresso machine, Turmix C100, was sold at a whopping $600US, positioning it towards small businesses.

![Nespresso Turmix C-100, 1990](./images/73dd11_bf83194a8c9147949ccb060a041b0afamv2.png)

Nespresso Turmix C-100, 1990

Similarly to the Gillette blades model, priced at $.60 a capsule - $6.00 a sleeve, the capsules proved to be a huge recurring business - much in line of the FMCG (Fast Moving Consumer Goods) roots of Nestlé.

![Nespresso capsules](./images/nsplsh_3d79bba0ee4b4337bd454c1f3bc62771mv2.jpg)

Nespresso Capsules

So much so, that a succession of models followed, each at a decreasing price point, culminating at the Nespresso Inissia, retailed at rock-bottom $99.  

![Nespresso Inissia](./images/73dd11_8182128f4e914f64961294282e950981mv2.webp)

Nespresso Inissia

Interestingly, once Nestlé's [<u><span>patent</span></u>](https://patents.google.com/patent/US4136202A/en) on the capsule design expired, an army of competitors rushed in - driving capsule price down.

Until then, at least, Nestlé ran a very healthy consumables business, with customer Life Time Value estimated in the thousands:

<table data-hook="table-component"><colgroup><col><col></colgroup><tbody><tr><th data-hook="table-plugin-cell"><p dir="auto" id="viewer-9szuh149217"><span><strong><span><span>SKU</span></span></strong></span></p></th><th data-hook="table-plugin-cell"><p dir="auto" id="viewer-lb6kf149220"><span><strong><span><span>Cost</span></span></strong></span></p></th></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-go9so150047"><span><span>Nespresso Inissia - machine</span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-nh110153934"><span><span>$99.00</span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-6n6ov149231"><span><span><span>Annual capsule consumption (capsules per machine)</span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-f8lt8149234"><span><span><span>850~1250</span></span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-1c8ts149238"><span><span><span>Customer Lifetime in years</span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-qv86d149241"><span><span><span>3~5</span></span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-nl6ss149245"><span><span><span>Total expected consumption (capsules)</span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-2b9r1174452"><span><span>2,550~6,250</span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-3lqxh149259"><span><span><span>Capsule price</span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-328v8184357"><span><span>$.60</span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-maact176388"><span><span>Total expected consumption (USD)</span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-fw395184880"><span><span>$1,550~3,930</span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-3zo9h149266"><span><strong><span><span>Total Customer Lifetime Value</span></span></strong></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-guw57186984"><span><strong><span>$1,650~4,030</span></strong></span></p></td></tr></tbody></table>

Now let us look at the revenue schedule for this machine+consumable hybrid:

![Customer revenue trajectory for machine / consumable hybrid](images/73dd11_261a5b57344543a19c384b2a346b870f~mv2.png)

Customer revenue trajectory for machine / consumable hybrid

Ask your finance people: Is it easier or harder (= expensive) to finance this kind of revenue stream, compared with the saw toothed pattern of the 'one-and-done' unit sale?

#### Product Service Systems

Another recurring business model - originally pioneered by Xerox with their leasing and pay-per-print services - is John Deere’s Product-Service System (PSS). This model combines advanced machinery with digital technology and bundled services.

Rather than simply selling equipment, John Deere offers “Solutions as a Service,” giving customers access to the latest agricultural technology at lower upfront cost. Farmers only pay for the features and services they actually use, while also benefiting from continuous updates and retrofits.

![John Deere PSS in action](./images/73dd11_58bac83b3a0e4715b97eec1e3ba3b8ebmv2.jpg)

Recurring revenue roaming the fields

#### Infrastructure as a Service

The internet age brought a special class of products: Infrastructure as a Service, (AKA PaaS - Platform as a Service).  

![Servers in a rack - the real hardware behind the cloud](./images/73dd11_808e7c37f6a1492d88eaf9b38bb3177emv2.jpg)

Offered by providers such as AWS, Azure, Google Cloud, Dropbox, and many many others, it allows users \- consumers and business alike - connect remotely, running CPUs, storage devices, and basically pay-as-you-go, through a variety of models - rent the machine, pay per traffic, pay per storage, per compute, per user... Huge capital investments and large operational resources are split between myriad users, each obtaining fractional functionality from a vast, bottomless, pool.

### Platforms and Ecosystems - Smart Models for Smart Tangibles

The latest advances in this business model ingenuity aare closely tied to the rise of smart products. These foster long-term relationships between users and vendors, creating multiple touchpoints throughout the product’s extended lifecycle, even as customers upgrade to newer models.

#### Critical Components of Being 'Smart'

I have found that there are several critical components that must (or are, at least, desirable) for products to become really smart, and sustain smart business models:

-   The physical product must have a digital layer of interaction
    
-   It has to have a connectivity layer, connecting it reliably to the vendor's servers
    
-   Products can be upgraded and services 'over the air'
    
-   Content delivered, and data collected must be stored in a personalized, user specific, space in the cloud
    
-   Users entities must be managed across (physical) model upgrade
    
-   Having a payment enablement layer is rally good
    
-   Having a market place for 3rd parties even better
    

Let's discuss the 3 first points. Here we are dealing with basic functionality. My La Marzocco Linea Micra espresso machine comes with a companion mobile app, allowing me to easily configure it. Compared with arcane buttons and levers industrial control competitors, this is light years ahead.  

![La Marzocco's mobile dashboard](./images/73dd11_66a855312b0342e88e83916edd2ea54amv2.png)

La Marzocco's mobile dashboard

With comparable products I'd need a technician servicing the machine, or poring over YouTube for hours on end, just to remember the exact sequence of button presses...

This app reminds me to clean the machine periodically, and keeps the exact recipe of back-flush and brew steps to do it. It also enables an automatic standby mode, so when I leave home at 5:40 I've already had my first cupo' with the machine waking up automatically to warm up.

It has already updated and upgraded the firmware several times since I bought the thing, introducing new features and well received functionality. What can I say? A success.

When we discuss content, a good example would be the photo apps (Google's and Apple's) that keep your photographic history for you, for ever, even when your phone breaks or gets stolen. Now here's a great opportunity for upsell, as the vast amount of online storage offered 'for free' is rarely enough. Smart or not?

Entity management is really key, as it detaches the ownership - and whatever functionality it confers - from the physical object, making it really hard to switch platforms, in an ever so gentle vendor lock-in.

Sinister as it may sound, however, we users get a lot of benefits, mostly for free: All our installed apps and configurations, our photos and videos, our music, our calendar, contacts, and notes, our purchase history - in a nutshell, our digital personality - is kept for us, easily recovered when a device is lost, and relatively protected from thieves and intruders.

Next, the commercial enablement of these smart products is one masterful blow: Apple requires credit card data just to unbrick the thing, resulting in a button-push away future expenses, in a secure environment.  

What's more, as a payment enabler, Apple Pay, and Google Pay can collect numerous, however tiny, fees from vendors. Apple's move to issue its own credit card enlarges the potential for processing fees even more.

Finally, the payment enablement led to the creation of the App Store, Google Play, laying ground for important market places for games, music, videos, and apps - generating revenue in the (multi) billions, at very handsome profit margins, too.

In this move, both platforms harness 3rd party developers and content creators, leveraging these platform as their main distribution channel, for a (sometimes hotly contested) distribution channel - and they are not alone.

![Source: App economy Insight](./images/73dd11_9d328ad12e804b7f90109ab124ac9365mv2.webp)

Apple's services (19% of overall revenue) grew +11% Y/Y. It includes the App Store, Apple Music, Apple Pay, AppleCare, Apple TV+, Apple Arcade, Apple Fitness+, iCloud+, and more. They also include that juicy annual payment from Google to remain the default search engine on Apple devices (estimated at [<u><span>$20 billion</span></u>](https://www.appeconomyinsights.com/p/alphabet-cloud-overshadows-ad-rebound) per year).

Another example is Roku's Channel Store, scheduled to generate just over $4 billion - which trades video advertising slots programmatically and splits revenue between broadcasters and the platform.

![Roku Channel Store](./images/73dd11_9f47102e91c04e2c873e237a04b671e0mv2.png)

Roku Channel Store

Roku's hold on users, by the way, is also based on a range of physical devices. Interestingly, the user accounts may be linked to paid for services (such as Apple TV), but the main source of revenue is its programmatic advertising network, available to broadcasters and advertising agencies, in a classic B2B2C model.

![Roku streaming devices](./images/73dd11_571c8f2551d8429eb183d6f6ed4cbc36mv2.jpg)

Roku streaming devices

### Smarting up the Business Model

In this post, I described how traditional durable goods suffer from a “one-and-done” model: once sold, the manufacturer’s relationship with the customer effectively ends. Margins are limited, sales cycles peak and decline, and companies face constant pressure to launch new products, absorb high pre-launch costs, and risk failure.

Strategies like planned obsolescence (Light bulbs, as well as the notorious inkjet cartridge lifetime deprecation) have extended revenue streams, but often artificially and not without enraging consumers and regulators.

Smart products redefine this dynamic. By embedding connectivity, digital interaction, and cloud services, they transform one-time transactions into ongoing relationships. Features like over-the-air updates, content storage, entity management, and built-in payment layers create the inrastructures needed for business model expansion.

The intrinsic, vendor generated, increased value conferred on customers increase loyalty and stickiness, and elongate customer life time and value - even when contained within the vendor's core offering. But when really smart vendors manage to build marketplaces, attracting 3rd party creators, they create a solid revenue source, based on recurring touch-points that lock in users, generation after generations of the initial product.

#### Expected Financial Impact of Smart Business Models

Consider three consecutive upgrade cycle for two comparable  (average model) products:

-   Samsung Galaxy phone
    
-   iPhone
    

Let's start with a typical Samsung Galaxy (average model):

-   Average selling price (ASP): ~$950
    
-   Gross margin: ~42% → ~$400 gross profit per device sold
    
-   Upgrade cycle: ~3 years
    
-   Loyalty: ~76% (customers who return to Galaxy at their next upgrade)
    

The customer lifetime value in this case is about $933

![Samsung galaxy customer gross profit streams](./images/73dd11_4215728634f64b978090d9464bc03a4cmv2.png)

Samsung galaxy customer gross profit streams

Now let's review iPhone as a comparable product:

• Average selling price (ASP): ~$950

• Gross margin: ~58% → ~$550 gross profit per device sold

• Upgrade cycle: ~3 years

• Loyalty: ~89% (higher than Samsung, meaning fewer users drop off each cycle)

If Apple relied on hardware alone, its profit curve would look much like Samsung’s: Three spikes at years 0, 3, and 6, gradually shrinking with attrition. Hardware alone yields about $1,478 gross profit per starting customer over 9 years, already higher than Samsung thanks to stronger margins and loyalty.

But Apple’s model doesn’t stop there. It layers recurring revenue streams that smooth out the troughs between upgrades:

• Apple Services (iCloud, Music, TV+, Arcade, Fitness+, etc.): ~$70 gross profit per year.

• 3rd-party App Store commissions (“Apple Tax” at an average 20% of app sales): ~$11 gross profit per year.

• Apple Pay & financial services fees: ~$7 gross profit per year.

Together, these add ~$88/year of high-margin recurring profit, accumulating steadily even when no new iPhone is purchased.

![iPhone customer gross profit streams](./images/73dd11_f2cab17009964dad98a0ada4db079f47mv2.png)

Samsung galaxy customer gross profit streams

Over three upgrade cycles, the iPhone generates ~$2,270 gross profit per starting customer, more than double Samsung’s.

#### Customer Loyalty - The Gift that Keeps on Giving

An often overlooked aspect of products becoming “smart” is the way they foster **greater customer loyalty**, provided the offering is designed to encourage it.

Take **upgrade loyalty** as evidence : CIRP (Consumer Intelligence Research Partners) reports that **89% of iPhone users** stay with iPhone when upgrading - once every 2.9 years, compared to **76% of Samsung Galaxy users**, once every 2.5 years.

The gap is partly explained by differences in **vendor lock-in**. For Android devices like Galaxy, **device** lock-in is minimal. User data, media, and digital identity are largely tied to the Android ecosystem itself, and by extension, to Google.

Android licensing, enforce manufacturers such as Samsung to pre-install Google apps and provide access to the Play Store. This ensures seamless continuity for users but also cements Google’s dominance in search and data collection.

The flip side is that **switching costs between Android brands are low**. Buy any new Android phone, and your experience is almost instantly replicated. For Samsung, that makes customer retention far more difficult.

A survival analysis shows that for the Samsung Galaxy brand, customer lifetime is about 4 years:

Where:

-   **Churn** is the percentage of users quitting each upgrade cycle
    
-   **Cycle** is the duration in years of an upgrade cycle
    

Therefore:

> _Galaxy Customer Life Time = 1 / 24% \* 2.5 = 10.4 years_

With iOS the story is very different. Exiting Apple’s ecosystem is cumbersome: apps often need to be bought again, media libraries manually transferred, and contacts reorganized. Most assets are tied to an Apple ID, which has little value once you move to Android.

This high switching friction is a major reason behind iPhone’s strong loyalty. Equally important is the ecosystem stickiness: the effortless integration across iPhone, Mac, Apple Watch, Apple TV, and iPad –whether a user owns the full suite or just a few devices – makes staying within Apple’s orbit all the more compelling.

The resulting survival analysis support a much longer customer life time - consequently impacting the lifetime value, as shown above.

> _iPhone Customer Life Time = 1 / 11% \* 2.9 = 26.4 years_

### Winning the Long Game

That’s how smart products makers can win the long game, with layered cumulative revenue, building platforms that harness the business of 3rd parties, increasing customer's utility and consequently, customer loyalty, life time, and overall revenue.

![Product Capabilities Linked Revenue](images/73dd11_0b92f228f82c496483131707d652d041~mv2.jpg)

Product Capabilities Linked Revenue

---

'***'

---

# Chapter 18 - Can Swatch Outsmart its Nokia Moment?



## Could Style-Platform become a Viable Smartwatch Strategy?

![Apple Watch and Swatches on display](./images/73dd11_487b38b5eb304374b12dc3dea62c330amv2.png)

Apple Watch is coming for Swatch

### Abstract

Swatch, long known for transforming watches into affordable fashion statements, is - like most traditional timepiece maker - heavily disrupted by smartwatches in general, and Apple Watch in particular.

![Google trends comparing Apple Watch and Swatch interest](./images/73dd11_5e233ef1ed6049e3911b06ae7b678270mv2.png)

Interest over time in google trends: Guess which is which

Swatch's legacy and knowhow, however, especially in the domains of design fluency, cultural agility, and accessibility do position the brand to come with a strong, differentiated offering: A style platform - grounded in low entry cost, modular physical design, and software-based personalization.

By enabling users to refresh their watch’s appearance through digital watch faces, artist collaborations, and creative tools, Swatch can foster ongoing engagement beyond the initial sale.

This approach opens the door to **recurring revenue, user experimentation, and strategic learning**, all aligned with Swatch’s heritage of democratizing wearable design.

### The Shrinking Clocktower: From Civic Time to Personal Ritual

Mechanical watches are **vestigial artifacts** - refined remnants of a time when precise timekeeping was a necessity rather than a stylistic choice. Their functional supremacy was first challenged by the quartz revolution, which democratized accuracy and ushered in inexpensive, maintenance-free alternatives. The shift continued with the advent of digital watches, and later with the omnipresence of smartphones, which quietly absorbed the role of timekeeper into their multitasking core. **Smartwatches**, in contrast, have all but abandoned the rudimentary job of telling time as their defining purpose. First developed targeted at narrow verticals such as sports and health, they quickly evolved into **wearable terminals**: interfaces for managing notifications, identity verification, health tracking, payments, and communication - in addition to the time keeping functionality, relegated to a fancy screen saver.

Smartwatch utility lies not in ticking hands but in seamless digital integration, and more recently, becoming a hub for any functionality user fancy. Against this backdrop, mechanical watches persist not out of necessity, but as **objects of craftsmanship, cultural symbolism, and personal expression**—beautifully obsolete, yet deeply human.

![The archetypal clocktower](./images/73dd11_dfbe6f38a2d24f00bb0092e28a3b7a9cmv2.jpg)

The archetypal clocktower

#### Some History First

The evolution of the watch is a story of **miniaturization and symbolism**, tracing humanity’s changing relationship with time. Once projected from **church spires and town hall façades**, timekeeping was a communal experience - heard and seen from afar, a reminder of civic order and divine rhythm.

The transition from longcase and mantel clocks to pocket watches marked a shift: **time became personal**, portable, and increasingly tied to individual routines. The leap to wristwatches further transformed the watch into a **wearable object**, merging function with fashion and making time a constant companion.

This compression of monumental technology into something that fits in a hand - or worn on a wrist - was an **miniaturization tour de force**, shrinking the cathedral clock into **functional jewelry**, a personal shrine in the cult of Cronos. Watches became not only tools, but **tokens of inheritance, achievement, and identity** - heirlooms that tick through generations.

![luxury wristwatch](./images/73dd11_0b9ec7e9567543daba64821787a69b16mv2.jpg)

That Clocktower? Now on your wrist

#### Industrialization

Industrialization and mass production, once stepping in, transformed the watch market by introducing high-volume, low-cost production - dramatically lowered prices and expanded access. This shift created clear pricing tiers: luxury (low volume, high price), premium (moderate volume, aspirational pricing), mid-range (mass-produced, affordable quality), and mass market (very high volume, low price).

In this competitive landscape, Brands pulled price, quality, and production volumes levers to differentiate themselves and find their own audience.

#### First Disruption: Quartz

For over two centuries, watchmaking economics were shaped by two key cost drivers: **materials and labor**.

On the outside, precious metals, sapphire crystals, and fine leathers signaled prestige (or bling - make your pick). **Material** choices communicated whether a watch was a **heirloom jewel** or a **disposable object**. Even a non-functioning high-end watch retained value if its form was enduring, and retained its original sheen.

Internally, **labor** was king. Traditional mechanical movements, especially in haute horlogerie, could include thousands of hand-assembled micron-precision components. Designing, tooling, manufacturing, calibrating, and assembling such a movement often took **months, even years**, per unit.

This painstaking process wasn’t hidden; it was proudly displayed: **a meta-investment of time into a timepiece**, marketed as a virtue. Scarcity, effort, and narrative became price multipliers.

![watch movement complications](./images/73dd11_495f67f8d13a40de8fa0904007c54898mv2.jpg)

Watch movement with (some) complications

At the lower end of the market, it took **nearly ninety mechanical components** just to make a watch tick.

**Quartz** changed everything. By replacing complex gear trains with a handful of electronic parts, it slashed both complexity and cost. Movements that had once cost for hundreds of Swiss francs could now be manufactured for **just a few francs**, while accuracy rose as dramatically as the need for maintenance.

Winners of this disruption were primarily **Japanese manufacturers** and innovative newcomers, who embraced cutting-edge technology and scale. Brands such as Seiko, Citizen, and Orient quickly scaled up operations, ramped up production, and began offering highly affordable, highly accurate electro mechanical watches.

![Citizen](./images/nsplsh_6b304338315947766f514dmv2_d_5184_3456_s_4_2.webp)

Citizen

--

![Seiko 5](images/73dd11_237d6ba54b85412e873ec57df1d8fccb~mv2.avif.png)

Seiko 5

--

![Orient](./images/nsplsh_7934496250624c67696245mv2_d_4000_2666_s_4_2.webp)
Orient

------

To make things worse (for the Swiss watch industry, that is), the advent and eventual integration of liquid crystal displays made clockwork redundant altogether: Enter **digital watches**. You could now have a solid state, dirt cheap timepiece telling you the time at untold accuracy, affording functionality hitherto unimaginable at a click of a button. (and the manufacturing cost of the whole thing?... less than CHF10.00)

Does Casio G-Shock rings a bell?

![Casio - pioneering Digital watches](./images/nsplsh_dba657965b1746379d8e6ec5dd8fbbbemv2.webp)
Casio 0 pioneering Digital watches

--

![Digital and rugged G-Shock](./images/nsplsh_f7213680e96b43eb875ec8e960389b95mv2.webp)
Digital and rugged G-Shock

--

![Digital and rugged G-Shock](./images/nsplsh_78f367620f4c46218a991572421c53f4mv2.webp)
Digital and rugged G-Shock

------



#### Initial Response

By the late 1970s, Switzerland’s once-dominant watchmakers were unraveling. **SSIH** (parent of Omega and Tissot) and **ASUAG** (home to ETA movements) found themselves on the verge of collapse, blindsided by the low-cost quartz revolution sweeping in from Japan.

In 1983, business strategist **Nicolas G. Hayek** orchestrated a last-ditch merger of the two groups, laying the foundation for what would become the **Swatch Group**. His weapon of choice? The **Swatch**: a Swiss-made, quartz-powered watch with just **51 parts**, radically simplified, and priced to win back the market from the bottom up.

![Initial Swatch prototypes](./images/73dd11_57fc82411d2e43369c2a4d1d2eee50b8mv2.jpg)

The Swatch platform was built around a molded plastic case, crystal, and strap, paired with a radically simplified 51-part movement aptly dubbed **System 51**. A key innovation lay in assembling the movement from the dial side, eliminating the need for an internal chassis. Most crucially, the design enabled fully automated assembly, slashing production time to just 2.8 seconds per watch today \[[<u><span>Swatch Prototypes blog</span></u>](https://swatchprototypes.com/) sheds further light on technical and design aspects of the brand\].

Ingenuity ded stop here. Cost reduction alone could not compete with the ruthless efficiency of the digital watch - where the Swiss watchmaking industry could not compete with Japan - the land of electronic gadgets.

Swatch capitalized on a major weak spot of digital displays - their uninspiring visuals. With dull grey LCD display that feel more like basic calculators than jewelry, digital watches offer almost no room for differentiation or emotional connection.

Swatch's response came from design duo Marlyse Schmid and Bernard Müller, who infused the dial with bold, vibrant color patterns that clashed deliberately with the case and reverberated through the strap material.

Drawing inspiration from the Italian postmodernist Memphis Group, they pulled watchmaking into the world of fast fashion, wielding graphic design as their weapon of choice.

![Kiki Picasso Swatches](./images/73dd11_5a67d016afbd4582b230b688a9bc2b7bmv2.webp)

Buying a watch - once reserved for milestones like graduations or retirements - had now become as casual as picking up a blouse at the mall, if not quite as impulsive as grabbing chewing gum at the checkout.

By combining technical and design innovation with sharp marketing insight, Swatch managed to carve out a market segment it could dominate - a win that helped fund the Swatch Group’s expansion for decades to come.

### Nokia's Nokia Moment

**“All good things must come to an end,”** but in Nokia’s case, that end wasn’t due to fate - it was a leadership failure. When Apple introduced the iPhone in January 2007, at several voices within Nokia sounded the alarm - they recognized that Apple’s touchscreen-centric, software-driven device posed a serious competitive threat. Externally, however, top executives publicly downplayed the risk, assuring investors and mobile operators of Nokia's ongoing market dominance.

![The original 2G iPhone](./images/73dd11_899959175e7d4543a216560c96c25285mv2.jpg)

In [<u><span>June 2007, Nokia’s Anssi Vanjoki</span></u>](https://www.reuters.com/article/technology/nokia-says-iphone-quite-interesting-report-idUSL11674918/) called the iPhone “quite interesting” but noted its lack of 3G and modest sales goal of 10 million units in 2008 - roughly 1 percent of the number of mobile phones sales forecast for that year.

Another public quote downplaying the significance of the iPhone came from Olli-Pekka Kallasvuo, then Nokia CEO, [<u><span>just a year after the Cuppertino smartphone launch</span></u>](https://www.speakersconnect.com/rasmus-ankersens-new-keynote-create-hunger-paradise/), saying that _“From a competition perspective, the iPhone is nothing but a niche product.”_

Behind the polished public image, Nokia’s innovation pipeline was stagnant. During a 2004 visit to their Espoo labs, I saw a lackluster showcase of so-called “next big things”- more a graveyard of outdated hardware demos than a glimpse of the future. Meanwhile, rivals like BlackBerry with the 850 series and Sony Ericsson’s P900, just across the border in Sweden, were already charting the early course of the smartphone era.

![Blackberry 850](./images/b4a5a88e42c9499db8d5e575aa5a9cec.jpg)
Blackberry 850

--

![Nokia feature phone](./images/nsplsh_4635563664376e50734c51mv2_d_5472_3648_s_4_2.webp)

Nokia feature phone

--

![Sony Ericsson P900. Source: https://hamariweb.com](images/73dd11_fa753be56fc544bca8a148b77d1ec8a2~mv2.jpg)

Sony Ericsson P900. Source: https://hamariweb.com

------

For Nokia, that meant prioritizing its main distribution channel - mobile operators - needs. Its leadership leaned on its perceived hardware engineering legacy, relying on Symbian and MeeGo as a default and ignoring the rising importance of software ecosystems and touch-first user experience.

With every incentive aligned to sustain its dominant model, Nokia became structurally incapable of pivoting. Like so many before it, it didn’t fail for lack of vision - it failed because it was too successful at the wrong things.

Nokia Oyj presents: Hubris and its consequences... True, there was clearly more to milk from the feature-phone cash cow, but this good thing eventually did come to its end.

![Hubris and iPhone's Juggernaut Effect - Source: Yahoo! finance ](./images/73dd11_fef3614b8a8a472bb34e02d55b3019ccmv2.png)

### Swatch Moment: The Bastards Changed The Rules

The context outlined above clarifies the challenge Swatch faces in responding to the existential threat the Apple Watch poses—especially to the lower tiers of the analog watch market and to Swatch Group itself.

![Apple Watch](./images/nsplsh_3277466f613034306d3867mv2.jpg)

Apple Watch

Much like Nokia’s early dismissal of the iPhone, Swatch CEO Nick Hayek brushed off the Apple Watch as an “interesting toy that can’t last more than 24 hours,” in an August 2015 interview with [<u><span>The Guardian</span></u>](https://www.theguardian.com/technology/2015/aug/24/swatch-ceo-apple-watch-interesting-toy).

One can’t help but recall:

_“There are many devices in a man’s heart; nevertheless the counsel of the Lord, that shall stand.”Proverbs 19:21 (KJV)_

Here's what the Market counseled, soo to speak about this:

![Swatch share price since 2014](./images/73dd11_010fe85e8ced4b228482f4d94ef758b6mv2.png)

#### Apple Disrupts - Again

It's time we discuss just **how** Apple Watch disrupts the lower to mid tiers of analog watch, impacting heavily Swatch, Tissot, and Certina.

<table data-hook="table-component"><colgroup><col><col><col><col></colgroup><tbody><tr><th data-hook="table-plugin-cell"><p></p><h6 dir="auto" id="viewer-fzv5l29605"><span><span>Brand/Tier</span></span></h6><p></p></th><th data-hook="table-plugin-cell"><p dir="auto" id="viewer-pasuv29608"><span><strong><span><span><span>Tier</span></span></span></strong></span></p></th><th data-hook="table-plugin-cell"><p dir="auto" id="viewer-muzgz29611"><span><strong><span><span><span>Impact Level</span></span></span></strong></span></p></th><th data-hook="table-plugin-cell"><p dir="auto" id="viewer-wh6kv29614"><span><strong><span><span><span>Est. Units/Year</span></span></span></strong></span></p></th></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-svlxw29624"><span><strong><span><span><span>Swatch</span></span></span></strong></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-ofivh29627"><span><span><span><span>Entry-Level</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-25ky129630"><span><span><span><span>Very High</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-g0z8c29633"><span><span><span><span>~5 million</span></span></span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-2w77g29643"><span><strong><span><span><span>Tissot / Certina</span></span></span></strong></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-2btvw29646"><span><span><span><span>Mid-Tier</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-cav9h29649"><span><span><span><span>High</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-2nisp29652"><span><span><span><span>Tissot ~3.1 million</span></span></span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-ir34e29662"><span><strong><span><span><span>Hamilton, Mido, Rado</span></span></span></strong></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-521bc29665"><span><span><span><span>Mid-to-Premium</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-4b8fn29668"><span><span><span><span>Moderate</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-nynjb29671"><span><span><span><span>—</span></span></span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-aoyuz29681"><span><strong><span><span><span>Longines</span></span></span></strong></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-atfr429684"><span><span><span><span>Upper Mid-Tier</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-lh59b29687"><span><span><span><span>Low–Moderate</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-wcud329690"><span><span><span><span>~0.95 million</span></span></span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-94pq929700"><span><strong><span><span><span>Omega / Breguet / Blancpain</span></span></span></strong></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-1fpaq29703"><span><span><span><span>Luxury / Haute Horlogerie</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-704k529706"><span><span><span><span>Minimal</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-fn8j429709"><span><span><span><span>—</span></span></span></span></p></td></tr></tbody></table>

#### Axes of differentiation

Earlier, I discussed the material and labor dimensions — and how they translate into customer value in both **functional** and **emotional** terms.

Let's review how Apple Watch disrupts both:

##### Functional disruption

**Accuracy**: While all digital watches use quartz oscillators, the Apple Watch goes further: GPS and network connectivity enable effortless, automatic updates for time, date, and time zones - tasks that demand cumbersome user interaction or complex mechanical mechanisms in high end analog watches.

**Flexibility:** In traditional watchmaking, every new function (or _“complication”_ in watchspeak) requires added <u><span>hardware</span></u>: more gears, hands, buttons, and dials. This drives up capital, labor, and logistics costs - multiplying SKUs and inventory complexity.

![Blancpain moonphase and tourbillon](images/73dd11_b931f85a3d664b82a616782f2fcb917b~mv2.avif.png)

Blancpain moonphase and tourbillon

![Blancpain moonphase and tourbillon - movement side](images/73dd11_f5505f12192f49658afd3cf92101f00c~mv2.avif.png)

What it takes, from the inside

------

Apple Watch flips this with a platform approach: a one-time investment in versatile hardware (like a high-resolution color-rich display, location, movement, and physiological sensors, and elaborate inputs, mainly by touch display) making new functionality a pure <u><span>software</span></u> play.

![The almost infinite world of effortless complications](./images/73dd11_dbb6772d4b1743e59f75d53079df6751mv2.png)

The almost infinite world of effortless complications

**Connectivity**: Beyond precise timekeeping, connectivity powers seamless two-way communication: voice, text, images, and data all flow effortlessly, especially within Apple’s tightly integrated ecosystem. More importantly, it lays the foundation for the next major disruption: open software.

**Open Software Architecture**: This allows rapid, scalable feature expansion through both built-in and third-party apps. The latter not only enhances functionality but also opens new revenue streams, following the proven App Store model.

![WatchOs Appstore Screen](./images/73dd11_b12ced82800e4d6698ba5e3247015590mv2.png)

WatchOs Appstore Screen

##### Emotional disruption and the 'Cool factor'

Apple Watch didn’t just enter the wrist-wear market - it disrupted Swatch’s core identity by shifting the idea of “cool” from surface graphics to living, breathing media.

#### From Static to Dynamic: The Death of Print Cool

Swatch built its aesthetic on printed expression: bold colors, witty patterns, and artist collaborations turned each watch into a miniature poster. But Apple Watch made that model feel dated. Its high-resolution, vibrant, interactive display could recreate, animate, and personalize visual content on demand - not per production run, but in **real time**.

Think of how smartphones eclipsed the allure of printed books as attention magnets. The Apple Watch did something similar to wristwear: it replaced static design with **programmable identity**.

#### Extreme Personalization

Look around: how many Apple Watches look the same? Almost none. Users take Apple’s relatively limited range of casings and transform it through a mix-and-match of watch face complications, fonts, colors, and images - tailored to mood, context, or outfit. What starts as a mass-produced device becomes, through software and connectivity, a deeply personal object - one that transcends the visual uniformity typical of industrial products.

#### A New Definition of Cool

Swatch’s cool was built on rebellion, art, and affordability. Apple’s cool is rooted in **agency**, **fluid identity**, and **connected intelligence**. It doesn’t just match your style - it perceptively adapts to your day, your needs, your data.

#### Why This Hurts Swatch so Much

Apple Watch strikes at the heart of the Swatch Group’s portfolio. At the entry level, it steals Swatch’s thunder, making seasonal designs feel static in a world of dynamic, real-time personalization.

Climb the ladder, and the threat deepens. Brands like Tissot, Longines, and even Omega rely on heritage and craftsmanship. But Apple’s software-driven sophistication now projects its own form of luxury: sleek, intelligent, and always up to date.

In doing so, Apple collapses Swatch Group’s carefully tiered brand architecture into a single, evolving platform - not just in utility, but in image, aspiration, and cultural relevance.

#### Market Segment disruption

![Apple Watch, Swatch sales](./images/73dd11_9a983c97794341e193a6f57ecb704985mv2.png)

Apple Watch, Swatch sales

Swatch built its success on fun, expressive, affordable watches, appealing for a few millions of users. For decades, that was enough. When Apple Watch arrived, blending hardware and software into a device that adapts to each usage scenario, it didn’t just conquered the category, but it expanded far beyond it.

What began as a rival in fashion and lifestyle now spans wellness, productivity, and safety - addressing not just millions of style-conscious youth but hundreds of millions of smartphone users, fitness enthusiasts, and aging adults.

##### Layered Platform Advantage and Market Expansion

Apple Watch is a layered platform where design, hardware, software, and ecosystem combine to cater to diverse verticals.

![Apple Watch Platform Layers](./images/73dd11_858c85ab36374a9e98918d7b61ccf0f8mv2.png)

Apple Watch Platform Layers

#### Industrial design and Hardware

It starts with a range of cases, finishes, straps, and a distinctive digital crown make Apple Watch both personal and wearable across contexts - from workouts to weddings. Underneath, the hardware brings it to life: custom silicon, a responsive touch display, and a suite of sensors that monitor motion, heart rate, blood oxygen, temperature, and more. These are supported by efficient connectivity and a battery designed for all-day use.

#### Operating system and integrated Apps

At its core runs watchOS, a purpose-built operating system that orchestrates everything: handling real-time data, driving haptics, syncing with the iPhone, and enabling dynamic watch faces and complications. Apple layers this with its own suite of apps for health, fitness, communication, and payments, creating out-of-the-box value with tight privacy and ecosystem integration.

#### Open software ecosystem

And on top of that sits a developer layer - a curated app ecosystem with access to select sensors, background tasks, and Apple’s health frameworks. While more focused than the iPhone App Store, it extends the Watch’s utility into niche and professional domains.

#### Platform Advantage and Market Expansion

Unlike smartwatch makers specializing in a single domain - such as fitness (Garmin, Polar) or health monitoring (Withings), the multi-purpose platform adapts to a range of user needs without forcing trade-offs. Whether it’s tracking a workout, monitoring heart health, answering a call, or managing calendar alerts, Apple Watch handles all scenarios within one unified device.

This flexibility is further amplified by its tight integration with the Apple ecosystem, something generic smartwatch makers like Fitbit (Google), Amazfit (Zepp Health), and Huawei struggle to match. While they may offer broad feature sets, they lack the seamless cross-device functionality and software consistency that Apple delivers across Watch, iPhone, Mac, and services like HealthKit or Fitness+.

The aggregate impact is substantial. Compared with the target audience for fashion watches - 100 to 150 million unit sales per year globally in early 2010s, shrinking to around 60–80 million units/year in 2015, **fitness** alone appeals to over 500 million active exercisers. The **health** vertical reaches 1+ billion adults managing or monitoring wellness, and the vertical of **aging populations** addresses the safety needs of over 700 million people aged 65+.

By absorbing rather than competing with these categories, Apple Watch didn’t just take market share from legacy watch brands - it expanded the market and redefined what a watch is for, and who it's for, conquering the fastest growing segment in wristwear.

![Annual unit sales for traditional watches, compared with smartwatches](./images/73dd11_2f5b1056b6da4459b103ac9fe81c40ffmv2.png)

Annual unit sales for traditional watches, compared with smartwatches

On a side note, it is worth mentioning that traditional watch brands are not the only ones to feel the brunt of Apple Watch success. It comfortably dominates the smartwatch market. You can read about this in this [<u><span>fascinating article from Hodinkee</span></u>](https://www.hodinkee.com/articles/us-smartwatch-sales-are-soaring-2019)<u><span>.</span></u>

![Apple dominates Smartwatches](images/73dd11_b934763789a7482e95f41ee73ac0abcf~mv2.avif.png)

### Investors Unrest - and the Peril of Contraction Spiral

I’ve charted the trajectory of Swatch Group shares since 2014. The stock has dropped from a peak of CHF600 to CHF147.85 as of May - a steep decline, of which a 24% plunge in the past year alone, to the dismay of shareholders.

As recently as May 2025, (see this [<u><span>Financial Times</span></u>](https://www.ft.com/content/f3ca259a-56ff-47d9-8c1b-1ff22243ecd7) article) Steven Wood of GreenWood Investors, a US-based investment firm, called out lack of accountability, limited engagement with shareholders, and overly centralized control by the Hayek family, pushing for board representation. It remains uncertain whether his efforts will lead to any restructuring of the company’s voting structure or a reduction in the Hayek family’s influence.

His product mix strategy focuses on Swatch Group's neglected high-potential brands, especially:

Breguet - which currently loses money despite rich heritage; Omega, and Longines - which have seen 20% and 29% sales declines since 2019.

While this approach may indeed boost the group finances in the mod term, even enlarging its market share against rivals such as Rolex, it seems to fall short of averting the group’s decline - along with that of the traditional wristwatch industry.  

------



### The Way Forwards and Upwards

#### Dabbing at Smartwatches

It is not for lack of trying that Swatch did not succeed in the smartwatch segment:

<table data-hook="table-component"><colgroup><col><col><col></colgroup><tbody><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-uqzf5677519"><span><span><span>Model</span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-ojylj677522"><span><span><span>Year</span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-g2z6b677525"><span><span><span>Brief Description</span></span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-tk9fs677529"><span><span><span>theBeep/BeepUp Pager</span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-iw59a677532"><span><span><span>1991–1996</span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-ffqj4677535"><span><span><span>Pager functionality via radio alerts</span></span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-o65ax677539"><span><span><span>Paparazzi (SPOT)</span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-dyb8i677542"><span><span><span>2004</span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-gdzdu677545"><span><span><span>FM-delivered news, weather, stocks via MSN Direct</span></span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-7bucx677549"><span><span><span>Digital Touch &amp; Zero One</span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-8c3kp677552"><span><span><span>2011/2015</span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-bdbef677555"><span><span><span>Touchscreen multifunction with sports sensors and Bluetooth</span></span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-5yz3f677559"><span><span><span>Bellamy</span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-5vv32677562"><span><span><span>2015</span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-9fcpd677565"><span><span><span>NFC contactless payment watch in China</span></span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-lksze677569"><span><span><span>Swatch Pay!</span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-smv1z677572"><span><span><span>2017</span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-wgso3677575"><span><span><span>Cloud-enabled NFC payment globally</span></span></span></p></td></tr></tbody></table>

![Swatch TheBeep, 1990s](./images/file.jpg)

Swatch TheBeep, 1990s

--

![Swatch Paparazzi, 2004](./images/file.jpg)

Swatch Paparazzi, 2004

--

![Swatch Digital Touch, 2011](./images/file.jpg)

Swatch Digital Touch, 2011

--

![Swatch Zero/One, 2015](./images/file.jpg)

Swatch Zero/One, 2015

--

![Swatch Bellamy, 2015](./images/file.jpg)

Swatch Bellamy, 2015

--

![Swatch Pay! , 2017](./images/file.webp)

Swatch Pay! , 2017

------

Beautiful watches, some analog, others digital. None did succeed, though. As per software - the driving force of everything digital - Swatch's only serious attempt at using a 'real' operating system was Microsoft SPOT OS. Not much to write home about, though. That OS, now discontinued never got much traction.

As far as is known, the company abandoned any serious further attempt at smartwatches, withdrawing to fashion watches with its successful MoonSwatch collaboration with Omega, a move that can be viewed as a "toy MoonSwatch" if not a pastiche act of PR for Omega's original, Moon Watch priced about CHF7,000. But all seems quite, for now, on the smartwatch front. Pity.

### A Chink in the Armor

Yes, Apple Watch wins, for now. However, it does have two major weak spots, at least one can be taken advantage by Swatch, of all watch makers:

#### Battery

Of all smartwatch manufacturers, Garmin is the only one breaking the 3 days barrier, with its Instinct 2X Solar (40days) and Enduro3 (36 days). Wow! This is 25X more than Apple Ultra's 36hours.

![low battery icon](./images/73dd11_77db4a56f1f6486b9a23711911f70b3dmv2.jpg)

The bane of low battery

Clearly, battery life, burdened by the bright, always on, constantly refreshing OLED display is the weakest point in Apple Watch hardware suit.

#### Lifetime

If the value of a pre-owned watch represents its useful lifetime, smartwatches are at a steep disadvantege here. A 4 years old smartwatch is, basically, electronic waste.

![Value of pre-owned watches](./images/73dd11_8bccbdbfb8d4413b979d941fc1e22c0amv2.png)

Value of pre-owned watches represents useful lifetime

This remains a core vulnerability of smartwatches - especially premium models like the Apple Watch.

#### Wear and Tear

The pain becomes tangible when something breaks. Replacement straps start at $49 and can climb to $149, while battery replacement runs $99 - roughly a quarter of the price of a new device from the base series.

#### Obsolescence Trap

In this context, innovation cuts both ways. Apple - as other vendors in this fast evolving product category - routinely introduces new features with each annual release, mainly for health and fitness, tempting users to upgrade.

But what happens when it’s not new features that drive replacement, but fading compatibility? As communication protocols evolve and OS support drops, even a fully functional Apple Watch may be rendered obsolete - not by failure, but by ecosystem drift masquerading as progress.

### A Fresh Smartwatch Strategy - The Style Platform

How can Swatch size on the weaknesses exposed by Apple Watch and others?

#### Segmentation and Price Point

While Apple Watch dominates the performance and health-oriented segments, its relatively high price point locks consumers into a **singular, utilitarian aesthetic** - one that demands long-term commitment to justify the investment.

For young fashion-aware users, this creates a tension: wearability is daily, but style is fluid. There is room in the market for a smartwatch that offers **greater stylistic flexibility** without imposing a luxury hardware price. While vendors such as Samsung do offer low cost smartwatches, they have yet to find an appealing and diverse aesthetic Swatch has proven record in making.

![Samsung Galaxy 4 watch](./images/73dd11_e1d5959451164badaf67156133f1baeemv2.png)

Samsung Galaxy 4 watch

#### Hardware Solutions

This is where **Swatch’s unique strength comes into play**. Unlike most tech brands, Swatch has a proven ability to speak the language of **fashion, design, and pop art** - through product-driven cultural fluency, using form, materials, finishes, and color.

Its history of bold designs, artist collaborations, and seasonal collections gives it a toolkit for creating **accessible, expressive, and fast-moving wearables**.

A style-driven smartwatch from Swatch wouldn’t need to out-feature competitors. It would win by delivering **choice, personality, and collectibility** at a price point low enough to **encourage rotation, experimentation, and self-expression** - a proposition that resonates well beyond any single demographic wave.

Hardware considerations must be context-driven. Extended battery life may be essential for outdoor and rugged-use watches, but less so for urban users - the natural audience for a fashion-focused smartwatch. This trade-off opens the door to high-intensity, (and yes, power-hungry) displays, enabling vibrant, dynamic watch faces on par with Apple Watch in visual appeal.

This allows for high intensity yet power hungry displays that will in turn allow rich vibrant dynamic watch faces, matching AppleWatch.What cannot be compromised is a low entry price. In the fashion space, affordability is essential -consumers need the freedom to experiment without the weight of long-term commitment or the psychological barrier of sunk costs.

#### Platform Software Solutions

These industrial design features must be backed by a capable operating system - one that supports seamless connectivity and a sense of continuous presence. Can you switch from one watch to another without the friction of re-syncing your account and data from scratch?

Instead of embedding all value in the hardware, style evolution should be decoupled and delivered through software-based **services** - at least for the aspects of the experience that are temporal, expressive, and easily refreshed.

Digital watch faces offer a natural foundation: they can shift with seasons, moods, cultural moments, or even daily outfits. Bundled collections, time-limited releases, or artist-led collaborations could give wearers an ever-changing sense of identity and participation. Over time, this approach transforms the smartwatch from a static product into a dynamic style platform- one where personalization, not permanence, is the core value.  

Such an offering lays the groundwork for an ongoing relationship between Swatch and its customers - one built not on one-time purchases, but on continued interaction. It creates space for recurring touch-points, upsell opportunities, and a feedback loop for user testing and large-scale experimentation - all of which are essential to uncovering the next big opportunity in digital fashion wristwear.

#### Swatch Time Weaver - Creative Platform for Creative People

Another paradigm shift Swatch could push is finding a unique need characteristic of its core audience: Young fashion aware urbanites try to flee from social class uniform and seek personal expression. Swatch could come up with a creative platform enabling UGC - User Generated Content. Why settle on canned designs and stylistic choices made by others, when you can have your own personal gallery of watch faces, made by you, unique to you, and showcasing the creative aspect of your personality? Enters [_<u><span>Swatch Time Weaver</span></u>_](https://app--swatch-time-weaver-fe936e40.base44.app/).  

Live Demo

(Yes. this ⬇️⬇️⬇️⬇️ is a live prototype. Enjoy!)

![Screenshot 2025-08-10 at 19.22.35](../Screenshot 2025-08-10 at 19.22.35.png)

------

A creative platform in which users can take photos (hell, even selfies!) or pick ones from their camera rolls - and make them a compelling, vibrant, watch face on their Swatch.

![Swatch Time Weaver Mobile App](./images/73dd11_45b52c9a23754d6c9aad0fba4f28f833mv2.png)

(Speculative) Swatch Time Weaver Mobile App

Did I mention this creative platform is offered as a service, at CHF4.99 per month (or whatever Swatch pricing specialists come up with)?

### Conclusion

Apple Watch has redefined the wristwatch- from mere timekeeping to a dynamic platform for health, communication, and identity - disrupting Swatch at its core. Swatch’s past victories in style and affordability now face obsolescence in a world of real-time personalization and app-driven value.

Yet Swatch does not necessarily go quite into the night: by blending its design heritage with a nimble smartwatch strategy focused on style, price, and expressive software, Swatch could reclaim relevance.

Cost and digital longevity are Apple’s key weaknesses - Swatch’s opportunity lies not in beating Apple on tech, but in offering a playful, fashion-first alternative that thrives on change, driven by lasting digital relationship with its customers.

![User-Generated-Content Watch](./images/73dd11_7203e2f8443341d0a2e26761dd685e47mv2.png)

Your User-Generated-Content Watch

---
'***'

---

# Chapter 19 - Reviving iRobot: Build a Marketplace



iRobot, the pioneer of robotic mopping, faces financial struggles due to competition and a failed acquisition by Amazon. Building a marketplace around its control app, iRobot-Home, could offer a way out by providing home maintenance services and generating additional revenue streams.

![iRobot Roomba - the quintessential robot mopper](./images/73dd11_8625424fd37845cfa2390d7d71ae857fmv2.jpg)

iRobot Roomba - the quintessential robot mopper

_Disclaimer: The numbers and calculations in this post, are for illustrative purpose only, and should not be construed as financial guidance or advice._

## A Market Pioneer in Crisis

> _Weren't you surprised last week as iRobot said there was “substantial doubt” about it as a “going concern”?_

At the [<u><span>announcement</span></u>](https://arstechnica.com/gadgets/2025/03/irobot-says-there-is-substantial-doubt-about-it-as-a-going-concern/), iRobot ([<u><span>IRBT</span></u>](https://finance.yahoo.com/quote/IRBT/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAACyHRTIezVoWABP7pduQUmavFkumHH5qK9jsrCOV7vo7o5yvqQC9E-F6O-DUlmiMTEqP8wE9pQ8ME8UG-_TGidBu4IZY7h54OVfjoXnH5grJYuVe8xZ5HcH9o4ZnYvVJ13q1ZZdS3T07dIeg08_1YfqA8dU5QevxHCjhEtHhtT5I)), maker of Roomba vacuum cleaners and Braava mopping robots, said it faced an uncertain future, warning investors of “substantial doubt” about its viability after the failed $1.7 billion Amazon acquisition.

The company has cut 50% of its workforce, seen a 47% revenue drop in Q4, and is exploring strategic alternatives, including refinancing or sale.

Ongoing challenges with demand, competition, and macroeconomic conditions cast doubt on its long-term survival, all too emphasized by the resignation of co-founder Colin Angle as CEO.

The falling share price and rising trading activity spoke volumes about the investors' sentiment about these developments:

![IRBT February - March '25](./images/73dd11_ffe23d58de7b4b22ad9cee5cbb34c7demv2.png)

IRBT February - March '25

This announcement came perhaps less surprising, to those aware of the termination of a $1.7B ($61 per share) acquisition agreement between Amazon and iRobot, signed in August 2022, and the ensuing loss in uphill regulatory battles in the EU and the US alike. The deal was [<u><span>announced dead January 29th 2025</span></u>](https://media.irobot.com/2024-01-29-Amazon-and-iRobot-agree-to-terminate-pending-acquisition), and it all went south from there, with the share price almost 94% down from its acquisition quote.

## Doubling Down

![The new Roomba lign-up, launched March 2025](./images/73dd11_8d2e7ef484694e1ca88a78ca64168d07mv2.webp)

The new Roomba lign-up, launched March 2025

Despite financial struggles, in what seems to me more of death throes, the company [<u><span>launched eight new Roomba models</span></u>](https://www.theverge.com/news/627751/irobot-launches-eight-new-roombas-with-lidar-room-mapping) with lidar navigation and AI features, aligning pricing with competitors like [<u><span>Roborock</span></u>](https://global.roborock.com/) and [<u><span>Ecovacs</span></u>](https://www.ecovacs.com/global).

Harsh words, indeed, and the reason for me saying so, is that this launch might go into infamy as one deepening the rut, rather than pulling ahead saving this once innovative pioneer of the robotic mopping market.

Previously the copycats, Chinese consumer good companies have long taken the lead - in design, cost efficiency, and the ability to thrive in a commoditizing market. Crying foul won't do much: After all, the benefits of cheap labor and manufacturing were exploited by the very same ailing iRobot.

Back to the recent barrage of new launches: While the question remains, whether these new Roombas succeed, one thing is sure: Victory in a single battle doesn't win the war - especially not a pricing war.

## The Failure of iRobot's Attempt at Hardware as a Service

Every physical product manufacturer faces the stiff reality of the revenue schedule, as they show in the following charts:

First, consider the revenue from a typical consumer: Purchasing their first unit at Y0, then buying consumables before they replace to a newer model, then repeat.

Of course, this schedule is decaying, for churn is inevitable.

![Revenue over time from a typical consumer](./images/73dd11_17c35269e38f4bd4a25da0b8536eed31mv2.png)

Illustration: Revenue over time from a typical consumer

Next, consider the aggregate revenue from a single product: A big launch brings it to the awareness and demand generation phase, then revenue declines gradually, until it's time to release a new version - generating new hype and demand.

![Revenue from a durable good over the model lifetime](./images/73dd11_45e15d4529dc402f9e3cff8b058e2dc1mv2.png)

Illustration: Revenue from a durable good over the model lifetime

This reality not only contributes to the cyclicality in durable goods manufacturers' revenue. Combined with the stark possibility that the market shuns your latest and greatest in favor of new entrants: iRobot's business model becomes somewhat brittle.

## iRobot Select (not) to the rescue

![discontinued iRobot Select program](./images/73dd11_76b7f0e11765447fbd4510083bb90590mv2.png)

(Spoiler: Discontinued) iRobot Select program

iRobot Select **was** a subscription-based program introduced by iRobot that provided members with a premium robot vacuum, accessory replenishments, a protection plan, and personalized support for a monthly fee. The program also offered eligibility for a new robot upgrade every three years.

I have analyzed the potential Life Time Value for subscribers in this program:

#### <u><span>iRobot Plan NPV</span></u>

**Active Subscribers Over 48 Months**

\- Months 1-12: Assume no **churn**, meaning all subscribers remain active.

\- Months 13-48: Each month, 5% of the remaining subscribers leave (churn):

![Active Users](./images/73dd11_9fa1a1735e0149cfa26d83bd13d40950mv2.png)

A(t) = Active users at month t

**Compute Present Value of Monthly Cash Flows**

-   Each month's revenue is given by:
    

![Month subscription revenue](./images/73dd11_2a4eb63ac5c9419b9af9c00cf9efb818mv2.png)

Month subscription revenue at present value

-   Summing over 48 months:
    

![Total subscription revenue for the period, at present value](./images/73dd11_bd8a0561808c47229105d9b8123f15f6mv2.png)

Total subscription revenue for the period, at present value

-   Add the program's activation fee ($149), which is paid upfront (no discounting needed).
    
-   Deduct $179.67, the Cost of Producing a New Roomba Unit
    

![ree](./images/73dd11_3e9490a0897c4f6dac8b38012b4c8966mv2.png)

**Final Result: NPV of iRobot subscribers**

-   The net present value (NPV) of the iRobot Select plan, considering churn from month 13 onward, is approximately **$729.37** per subscriber.
    

**Assumptions**

-   Monthly Subscription Fee: $29
    
-   One-Time Activation Fee: $149
    
-   Annual Discount Rate: 5%
    
-   Monthly Discount Rate: 5% / 12 = 0.004167
    
-   Subscription Duration: 48 months (4 years)
    
-   Production Cost of a Roomba Unit: $179.67
    
-   Churn Rate: 0% for the first 12 months, then 5% per month thereafter
    

#### <u><span>Alternative Cost and Cannibalism</span></u>

This plan needs comparison with the alternative, the NPV of a customer that pays $799.99 up front for their unit, then buys consumables (although only 66% rate), then holds the appliance for 4 years.

**NPV of iRobot buyers**

The Net Present Value (NPV) of a customer who buys a Roomba upfront, then purchases consumables at 66% of the subscription rate, and holds the unit for 4 years, is approximately **$1,116.54** after deducting the production cost.

#### <u><span>Cash Flow Impact</span></u>

Can we discuss for a minute the impact on iRobot's cash flow? by deferring much of the sales revenue (in excess of 3 years) while incurring production costs upfront, a hole would appear in the ledger, even if the NPV were positive. How large would that be?  

It is often said that US companies excel in execution, and I tend to agree.

Launched in 2021, and - [<u><span>being consumer cash friendly</span></u>](https://www.techhive.com/article/2010908/is-irobot-select-worth-it.html) - at least for a larges swath of prospective consumers, I made an educated guess about the number of subscribers per year.

For 50,000 such subscribers, the cash flow impact would then be:

<table data-hook="table-component"><colgroup><col><col><col><col></colgroup><tbody><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-cq7v8249423"><span><strong><span><span><span>Year</span></span></span></strong></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-talvh249426"><span><strong><span><span><span>Aggregate Subscriber Cashflow</span></span></span></strong></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-tt5pr249429"><span><strong><span><span><span>Aggregate Non-Subscriber Cashflow</span></span></span></strong></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-3cijx249432"><span><strong><span><span><span>Difference</span></span></span></strong></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-eab5y249436"><span><span><span><span>Year 1</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-lqy6l249439"><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 16,200,000</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-hj24s249442"><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 45,000,000</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-2e8yd249445"><span><span><span><span>&nbsp; (28,800,000)</span></span></span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-uniuq249449"><span><span><span><span>Year 2</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-ubitt249452"><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 16,200,000</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-ac9py249455"><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5,000,000</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-go0ji249458"><span><span><span><span>&nbsp;&nbsp; 11,200,000</span></span></span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-ii0tt249462"><span><span><span><span>Year 3</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-gmp5a249465"><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 16,200,000</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-oph3y249468"><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5,000,000</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-szuvs249471"><span><span><span><span>&nbsp;&nbsp; 11,200,000</span></span></span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-djvwx249475"><span><span><span><span>Year 4</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-8xb9e249478"><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 16,200,000</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-70q9n249481"><span><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5,000,000</span></span></span></span></p></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-4ngdl249484"><span><span><span><span>&nbsp;&nbsp; 11,200,000</span></span></span></span></p></td></tr><tr><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-mx1j2249488"><span><strong><span><span><span>Total</span></span></span></strong></span></p></td><td data-hook="table-plugin-cell"></td><td data-hook="table-plugin-cell"></td><td data-hook="table-plugin-cell"><p dir="auto" id="viewer-kndgn249495"><span><strong><span><span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4,800,000</span></span></span></strong></span></p></td></tr></tbody></table>

With iRobot losing money, that pesky $28.8M yearly reduction in revenue is surely painful.

#### The fate of iRobot Select

What have we done?... must any executive in iRobot ask, for last time I checked, **$729.37 < $1,116.54**

Compounded by the growing yearly revenue referral of $28.8M, I believe no tears were shed when they decided to scrap this program.

If there is a lesson to learn, is that <u><span>financing is not a service</span></u>, not one that adds value, anyway.

## Digital Services

#### <u><span>iRobot Home</span></u>

Founded in 1990, iRobot is no stranger to innovation and digitization, and has launched its control app - [<u><span>iRobot Home</span></u>](https://www.irobot.com/en_US/irobot-home-app.html) back in 2015.

![iRobot Home mapping](./images/73dd11_05918190c97f4fbab0ea98162ff43edbmv2.png)

iRobot Home mapping

The **iRobot HOME App** (iOS & Android) lets users control and customize **Roomba** and **Braava** robots remotely.

Key features include:

-   **Scheduling** Including personalized schedules
    
-   **Smart mapping (Imprint™)** Geofencing, allowing Room-specific cleaning, and keep-out zones.
    
-   **Alexa & Google Assistant** Support for voice commands
    
-   **Advanced Ai features** Cleaning recommendations
    
-   **Various norification mechanisms** Real-time notifications, maintenance alerts, and software updates
    
-   **Multi-robot and multi-user control**
    

<u><span>Limited Service Offering</span></u>

Interestingly, there is not much of a service offering here. Yes, you can order consumables, you may even be able to schedule repairs, but that's it. Not much of a money maker for iRObot, I suspect.

## iRobot Concierge - Build a Marketplace, Create an Ecosystem

### The Opportunity

As seen, both the defunct iRobot-Select program and the iRobot-Home App are what I would call "introspective", meaning they focus on the existing functionality of the Roomba mopping robot.

They are built for improving the existing user experience, rather than expanding the horizons to cover a more holistic universe of home maintenance, to which the cleaning bots are so central.

There is an opportunity here: Build a marketplace around your product, focusing on a host of routine services such as

-   Lawn mowing
    
-   Snow shoveling
    
-   Gutter cleaning
    
-   Cleaning maid services
    
-   Pet grooming and walking
    

The average annual expenditure per household in the US for this host of services approximates at $842.

Additional expenditures include cleaning and gardening materials, pet food, totaling in $2,408.

There are 8.8 million engaged, connected iRobot customers in the US.

Assuming iRobot charges a 5% commission on services booked through its marketplace, the TAM is:

**8.8M x $2,408 x 5% = $1,059M**

Who knows what portion of this opportunity can iRobot grab, but at $681.8 million sales in 2024, this seems as a perfectly adequate one to explore.

### Comparables: Apple AppStore and Facebook Market

Apple's hand was all but forced to open its appstore to the general developer community, and boy! did that work marvels for them: The birth of the App economy and its explosive growth pays handsomely to the bottom line of Apple:

![App store commission as part of total revenue](./images/73dd11_fabd24b738c44cb4bb4094afb434887emv2.png)

Approximations. Apple consolidates services revenue

Originally meant to strengthen the hardware offering, opening the App Store up to third parties created a strong revenue source, and generated immense customer value. The concept was soon to be copied in Android and by other vendors. Why not for iRobot?...

Another use-case, although detached from a hardware offering is facebook market. This case is interesting because of its local orientation. Most pre-owned products on the market are shown based on geo-location vicinity.

-   With Global Gross Merchandise Volume (GMV) of $26 billion in transactions In 2022, and an estimated Return on Ad Spend (ROAS - a common benchmark for Facebook Ads) of 3:1, Facebook Marketplace sellers [<u><span>might have spent around $8.67 billion on ads</span></u>](https://savemyleads.com/blog/other/what-is-the-average-roas-for-facebook-ads?utm_source=chatgpt.com).
    
-   If we attribute 50% of this activity to the U.S. market (given its significant user base), the estimated ad spend by U.S. sellers would be approximately $4.34 billion for facebook market in the US
    

These numbers hint to a possibility to generate demand that would create a locally oriented eCommerce ecosystem of products and services revolving about iRobot as the center of the modern household.

### iRobot Concierge - Product

The hardest part is in: The iRobot-Home can be easily harnessed to this end, by implementing the following additions.

A short list of potential enhancements to the user experience of the existing app ensues, with what I believe exposes value that consumers might respond to

-   Add timely featured offerings to the main dashboard
    

![Add timely offerings](./images/73dd11_fe8d21e59ecc45568f9ed0f82bae6abbmv2.jpg)

Add timely offerings

-   Add a marketplace pane. Offerings are local and timely
    
    ![proposed iRObot marketplace](./images/73dd11_fb6a0bbbcdd34699bdc11e46cc18f31amv2.png)
    
    proposed iRObot marketplace
    
-   Enrich notification pane with up-sell and 3rd party offerings
    
    ![Enriched notifications ](./images/73dd11_62bb430619a74d04b206c8574fc318bdmv2.jpg)
    
    Enriched notifications
    
-   Schedule area beefed with timely offerings
    
    ![Schedule area beefed with timely offerings](./images/73dd11_5cee6369622547198e158b720f902ddbmv2.png)
    
    Schedule area beefed with timely offerings
    

These offerings are bound to convert some iRobot owners, offering a fresh stream of revenue at marginally low cost: There will be an effort to build, maintain and market this new experience to consumers, as there will be an effort to market this virtual e-Commerce venue to local vendors and service providers.

### iRobot - Concierge: The Vendor platform

I have depicted an initial flow for registering businesses and offering services:

![Business registration page](./images/73dd11_d1dac89c4e7c4f67974e53fc284796e4mv2.png)

Busines registration page

![service page](./images/73dd11_5c88ad3cac5f415eb539e1f075be340fmv2.png)

Service page

![Business profile](./images/73dd11_4304f4fccb594727a373086c36b3f4a7mv2.png)

Business profile

![Customer service preview](./images/73dd11_5c88ad3cac5f415eb539e1f075be340fmv2.png)

Customer service preview

### The demo

[Homebot portal](https://app--home-bot-hub-5947a1cf.base44.app) 	Customer side

[Business portal](https://app--home-bot-e98bade2.base44.app)	Business side
---

'***'

---



# Chapter 20 - Smarting Up with Ai



### Simple Days of Yore

Why would we even want our devices to incorporate AI? Is it truly adding value, or is it just the latest *cri du jour* – a fashionable technology that manufacturers feel compelled to slap on the brochure so they can look 'cutting-edge'?

Let's start with **the need**.

We previously discussed analog hardware, a reminder of a simpler, more innocent world. Take a simple water tap. You turn it, water flows (if the pipe is full), you turn it back, water stops flowing. Immediate utility, immediate feedback.

![Water faucet](./images/73dd11_a42d80ba6347477abd57c401a907ddedmv2.jpg)



Water faucet. *Photo by Alireza Irajinia on Unsplash.*https://unsplash.com/photos/jGdTiWw77Hw

This simplicity is now only a fond memory in an optimization-crazed world, where manufacturers and customers alike try to squeeze every drop of utility from strained resources:

What if the faucet leaks? What if the pipe was originally dry when we opened it, only to find the faucet now spilling? What if the spout connects to a conduit, leaving us unsure whether water flows at all? And what if the water is too hot, too cold, or – heaven forbid – frozen solid, bursting the pipe?

We wouldn’t know, would we? That is why we need sensors and actuators: a command-and-control system. Perhaps unnecessary for a single tap, but indispensable when managing an entire network.



### Opportunities for Smarting Up

Beyond single devices, the real challenge lies in orchestrating vast constellations of sensors, actuators, and connected assets. As systems scale, the demand grows for **smarter command-and-control (C2) solutions** that can collect information, take action, coordinate across networks, and operate reliably in diverse contexts. These needs span across four broad domains:

#### I. Sensing and Data Collection

![Electronic sensor](./images/73dd11_6556df01cf514c3b80b9c70a7638da3bmv2.jpg)



**Close-up of electronic sensor.** Photo by Denis N., retrieved from [Unsplash](https://unsplash.com/photos/a-close-up-of-a-piece-of-electronic-equipment-zjCc0l9l1cI).

Devices focused on observing, measuring, and reporting.

Sensor networks – cameras, microphones, thermometers, barometers, hygrometers, voltmeters, ammeters, etc.

Asset tracking – location and status sensors embedded in goods or vehicles, or else mounted on humans.

Key value: Turning the physical world into data streams.



 

#### II. Actuation 

![Open solenoid valve diagram. Joey Corbett, CC BY-SA 3.0, via Wikimedia Commons.](./images/73dd11_f66a805c3ceb4ef08ab3d566251c8757mv2.png)



Open solenoid valve diagram. Joey Corbett, CC BY-SA 3.0, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Solenoid_Valve_Open.png).

Devices that take action in the physical world.

Actuator networks – motors, relays, valves, robotic arms, etc.

Key value: Closing the loop between sensing and doing.



 

#### Operation and Oversight Models

![data monitoring](./images/73dd11_49185f02a1e14fa7bea6fe219ecf809emv2.jpg)



Data stream monitoring. Photo by [Chris Liverani](https://unsplash.com/@chrisliverani?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/turned-on-flat-screen-monitor-dBI_My696Rk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

How systems manage workload, intervention, and resilience.

Unattended / automatic solutions – continuous operation with varying degree or no manual supervision.

Event-driven monitoring and escalation control systems – filter noise, handle routine cases, and escalate only anomalies.

Remote management – command, configure, and update from afar (e.g., OTA updates, diagnostics).

Key value: Efficiency, reliability, and minimizing human burden.



 

#### Architecture and Deployment Contexts

![Complex networks](./images/73dd11_c99df8491922429885a52372f5a75a96mv2.jpg)



Complex networks. Photo by [GuerrillaBuzz](https://unsplash.com/@guerrillabuzz?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/diagram-7hA2wqBcSF8?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

Control systems managing complex device topologies and diverse operating contexts.

Organizing sensing and actuation through distributed networks tied to a central processing, balancing local autonomy with centralized coordination.

Enabling smart functionality in dynamic environments such as vehicles, wearables, and field-deployed devices.

Key value: Making distributed systems coherent, dependable, and effective across both fixed and mobile contexts.



 

### Acute Pain

#### The Overload of Command & Control

![Control center data overload](./images/73dd11_daa267d2c4d04553936ecf73ce378c77mv2.jpg)



Control center data overload 

The need for coordination and control of complex systems is not new. With expansion of digital technology and data communication, and the rise of sprawling device networks, it has become far more acute.

As device networks grow and data volumes surge, traditional C2 centers and their operators are overwhelmed by false positives while remaining blind to false negatives. The very rationale for building and staffing C2 begins to collapse, both economically and operationally.

I witnessed an always-on CRT display monitoring a complex network with a flood of events – admittedly, mostly spurious ones – some details were etched into the phosphorous layer, as no one, ever, bothered to clear those events. It has become a useless piece of equipment. That network, let me tell you, was NOT monitored.



 

#### Endpoint maintenance

![Firmware update](./images/73dd11_dfe00e5ca5684c9ba78acf763953268fmv2.jpg)



Firmware update. Photo by [ANOOF C](https://unsplash.com/@anoofc?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/code-written-on-a-screen-likely-programming-related-3v1CT8JoKOE?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

Meanwhile, maintenance of software embedded device  becomes a major operational headache. Cases like Toyota Prius ABS firmware bug (2010–2011) affected 400,000 cars worldwide, and [cost US$2billion ](https://www.rte.ie/news/business/2010/0204/127189-toyota-business/)part of the exorbitant cost stems from the need to physically recall the faulty cars to the service centers for firmware update.

In aother event I witnessed, sending a field engineer to Minnesota, having them climb a 30 ft pole to upgrade a firmware bugfix, was a $5,000 a pop – loosing money on this site installation.



 

#### Autonomy

![Roving bot](./images/nsplsh_113956abe1d34af5a4c25d2301530fdemv2.jpg)



A roving robot. Image by Silver Ringvee, Unsplash

Another compelling use case is the potential in autonomous systems operating in the messy, random, real world – whether it is in semi controlled environemnts, such as warehouse and railway tracks, or in the wild, aka on public highways, with humans erring next to robots.

---

 

### Ai To The Rescue

Once we understand the need, it is obvious why the idea of sentient systems that would step in to help operate complex systes in harsh conditions (data noisy, or operational complexity). 

It has two escalating phases to it:



------



#### a. Monitoring - Discerning Signal From Noise

In this category, the value ML (Machine Learning, as it was once called, before the Ai hype) brings is helping human users of a system sift through the barrage of information streams, discerning the signal from the noise.

This is not completely new. **Business-Rule Heuristics** formalized as if–then–else are at the core of enterprise computing. **Bayesian Filtering** (probabilistic estimation over time) are common in systems such as navigation, robotics, and signal processing, where hidden states must be inferred from noisy, continuous data streams.

Crucially, the gap ML/Ai solves lies past an uncertainty threshold is crossed:

1. **Business rules** excel when the world is well-structured and discrete: if–then–else logic applies crisp cutoffs (compliance, eligibility, transaction approval). They are transparent and easy to audit. Clear as they might be, though, they are 'brittle' in noisy environments. **Business rule Heuristics fail when reality is noisy, ambiguous, or adversarially exploited.** In contrast, ML/Ai is fault tolerant by design 

   

**Example: Device Access – Code Matching vs. Visual Identification**

![Unlocking via face recognition](./images/73dd11_abfa9fb4861a484c97eb9b5f551aa485mv2.jpg)



Biometric face recognition: AI-generated image created using Wix media tools

- **Rule**: *“If entered PIN = stored PIN, then unlock phone.”*
- **Limit**: PINs can be guessed, shoulder-surfed, or brute-forced. The rule is rigid and binary: correct or incorrect, with no awareness of spoofing.
- **Failure**: Security is fragile – a stolen phone with the right PIN becomes fully compromised.
- **AI Edge**: Apple’s **Face ID** replaces rule-based access with **probabilistic facial recognition**. The system fuses depth sensors, infrared imaging, and adaptive ML models. It tolerates natural variations (beard growth, glasses, lighting) while rejecting impostors, continuously learning the owner’s appearance over time.

 

1. **Bayesian filtering** steps in when the system is known but noisy: it refines estimates over time by fusing models with imperfect measurements (navigation, robotics, sensor fusion). It models well-understood underlying dynamics, and analyzes incoming data flows to determine signals nad patterns from noisy fluctuations.

 

**Example: Geolocation Tracking (Navigation & Mobility)**

![Geo location tracking](./images/73dd11_5972cb1ac1f84e7aae3fa4aac15bf38amv2.jpg)



Geo location tracking. Photo by [Maxim Hopman](https://unsplash.com/@nampoh?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/person-holding-black-samsung-android-smartphone--16na5rDDRk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

- **Rule (Bayesian filtering based)**: *Fuse GPS data with inertial sensors (accelerometer, gyroscope) using a Kalman filter to smooth noise to estimate position.*
- **Limit**: While this works well enough in open environments with predictable errors, it is prone to GPS multi-path errors rife in urban canyons, drop offs indoors, or in tunnels, or spoofing. The filter assumes the dynamics are known (e.g., steady walking or driving speed) and keeps updating – but without reliable inputs, it drifts, producing a “clean” but increasingly wrong estimate.
- **Failure**: The navigation system shows the user moving smoothly… through buildings, across rivers, or hundreds of meters off-route. Filtering smoothes out noisy signals, but does not improve accuracy.
- **AI Edge**: ML-based location inference goes beyond. It leverages **contextual signals**: Wi-Fi access points, Bluetooth beacons, cell tower handoffs, compass readings, map constraints (roads, buildings), and even motion patterns learned from population data. By fusing these heterogeneous inputs, the AI models can detect and correct anomalies (e.g., GPS jumping across the street) and maintain accurate positioning in places where physics-based baesian filtering alone fails.

 

**Example: Predictive Maintenance – Hardware Anomaly Detection**

![Predictive maintenance is better](./images/73dd11_b7d9f40e221b4917bc89196848339dd3mv2.jpg)



Predictive maintenance is better. Photo by [Salvatore Tonnara](https://unsplash.com/@salvatoretonnara?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/a-man-working-on-an-engine-in-a-garage-r199doRc-4g?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

- **Rule (Bayesian filtering based)**: *Fuse vibration, temperature sensor data over time with a Kalman filter to smooth noise and estimate the machine’s health state.*
- **Limit**: Bayesian filters can denoise signals and estimate trends, but they assume the underlying dynamics are known and relatively stable. In reality, machines vibrate or heat up for many benign reasons – load changes, temporary imbalance, external forces – which are not true precursors to failure, and may produce false positives.
- **Failure**: Operators receive “clean” vibration estimates, but still face false alarms or missed early warnings. They either overreact (costly downtime) or underreact (missed failures).
- **AI Edge**: ML-based predictive maintenance moves beyond smoothing. It ingests multi-sensor streams (vibration patterns, acoustics, motor current, temperature) and **learns correlations from historical failure data**. Over time, the model distinguishes meaningful precursors from normal operating variability. This enables early, probabilistic alerts – predicting faults well before rigid thresholds or Bayesian filters would have flagged them.



**Example: Smartwatch Health Monitoring**

- **Rule (Bayesian filtering equivalent)**: *Fuse body temperature readings with accelerometer data to filter noise and produce a stable estimate of “true” temperature.*

- **Limit**: This filtering helps distinguish between a real fever and momentary fluctuations (like motion artifacts), but it still assumes fever is the primary signal of illness. Many conditions do not present with elevated temperature, or the fever appears late. A Bayesian filter produces a clean, reliable temperature estimate — but misses the bigger picture of multi-signal health dynamics.

- **Failure**: Users get a “smoothed” but narrow view of their condition. The watch reassures them when no fever is detected, even though other signs (oxygen drop, HRV changes) indicate trouble. Or it falsely alarms when temperature rises from exercise, not illness.

- **AI Edge**: ML-enabled data fusion leverages multiple biosignals — HRV, SpO₂, skin temperature trends, sleep quality, and activity context. Instead of assuming fixed dynamics, the model **learns complex, nonlinear patterns across populations** and **personalizes baselines for each wearer**. By weighing signals probabilistically, it detects subtle deviations indicating infection or stress earlier and more reliably than temperature-based filtering ever could.

  

------

 

#### b. Control – Autonomy and Unattended Automation

Letting AI-assisted systems automatically control equipment is more complex. Unlike the previous mode – monitoring, where humans interpret and act – the “hands-free” promise can easily backfire.

From the unthinking rigidity of automated factory lines, satirized by Charlie Chaplin in Modern Times (1936), to today’s algorithmic “hallucinations” born of statistical misinterpretation or blind trust in flawed sensors, autonomy introduces new kinds of failure alongside efficiency.

There are, however, low-hanging opportunities where the potential risks are minimal and the gains tangible.

**Example: Smart Thermostat**

![Nest Learning Thermostat displaying temperature setting](./images/73dd11_b44b5fe3836d42acbb06beadab7c1f0dmv2.jpg)



Nest Learning Thermostat displaying temperature setting. Image by Raysonho @ Open Grid Scheduler / Grid Engine, CC0 1.0, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Nest_Learning_Thermostat_(cropped).JPG).

- **Rule (PID / Bayesian-Based Control Equivalent):** Maintain target temperature by adjusting HVAC output based on measured deviation, using smoothing filters (like Kalman/Bayesian) to stabilize noisy sensor data
- **Limit:** Produces steady thermal control but assumes predictable conditions and fixed schedules. Ignores occupancy, weather shifts, and personal comfort dynamics.
- **Failure:** Wastes energy by heating or cooling empty rooms and reacts too late to changes. Offers comfort stability but not situational intelligence.
- **AI Edge:** Learning Thermostats apply ML to learn user habits, occupancy patterns, and home thermal response. It anticipates needs, optimizes setpoints proactively, and continuously adapts through cloud-fed predictive models – turning static control into dynamic, context-aware comfort management.

 

**Example: Smart Irrigation**

![Smart irrigation sprinkler controller](./images/73dd11_7fd3e232813c4039ac834ff255ef1a34mv2.jpg)



Smart irrigation sprinkler controller. Photo: Shutterstock

- **Method**: Farmers irrigate according to fixed rules (e.g. “*every day at 6 AM for 30 minutes*”). They may also rely on local wisdom or past experience.
- **Limit**: 
  - Ignores soil moisture dynamics, salinity, root-zone variability
  - Doesn’t adjust for real-time weather, rainfall, or plant growth stage
  - Leads to overwatering (waste) or underwatering (stress)
  - Inefficient electricity usage and labor overhead
- **Gap**: The rigid, one-size-fits-all irrigation plan cannot adapt to site-specific soil & crop conditions. Without real-time feedback, resource use is suboptimal and crop performance suffers.
- **AI Edge**: Advanced smart irrigation platforms combine **data fusion** (merging soil moisture, temperature, salinity, rainfall, pressure, and flow data with weather forecasts) with **pattern recognition** to detect evolving crop and soil conditions. Through **continuous autonomous monitoring**, the system dynamically adapts irrigation schedules, optimizing water and energy use while ensuring healthier plant growth and more sustainable farming practices.



---



### Early Days for GenAi Hardware devices – Notorious Failures

**Samsung Fake Moon shots**

https://www.reddit.com/r/Android/comments/11nzrb0/samsung_space_zoom_moon_shots_are_fake_and_here/



 

**Rabbit Ai: R1**

![The Rabbit R1 AI Assistant Device](./images/73dd11_477b8b5cf9204d96af4a5739bbea6945mv2.jpg)



The Rabbit R1 AI Assistant Device. From https://www.mrpaloma.com/public/eventiallegati/2342-rabbit-assistente-nuovo-dispositivo.webp. This image is licensed under CC0 1.0 Universal (Public Domain Dedication).



 

**Humane: AiPin**

The Humane AI Pin is a screenless, wearable AI device that projects information onto the user's palm and uses voice interaction, designed as an alternative to smartphones.



![The Humane AI Pin Wearable AI Device](./images/73dd11_b5c27c83c5f44ac7ade18624cb110aefmv2.png)



The Humane AI Pin Wearable AI Device . By [renaissancechambara](https://www.flickr.com/photos/renaissancechambara/53320717246/). Licensed under CC BY 2.0 

---

<To be continued>

---

'***'

---

# Chapter 21 - Killer Features: Disruption at Play



![Screenshot of Merriam-Webster online dictionary entry for killer app](./images/73dd11_6004cdc905b2421dae898c04d0d6ec31mv2.jpg)



Screenshot: Merriam-Webster online dictionary entry for *killer app*. Retrieved from [https://www.merriam-webster.com/dictionary/killer%20app](https://www.merriam-webster.com/dictionary/killer app)



 

### Market Magnets

What is a **killer feature**, anyway? We keep hearing this term, in its pure software version –*Killer App.*

The expression’s origin is unattributable, but it surfaced in the early 1980s when technology circles spoke of VisiCalc, the spreadsheet program that became the single sufficient reason for businesses to buy the Apple II. It wasn’t “just software”; it was the first serious business application that made a long stride toward democratizing computer use.

For the first time, small businesses — from mom-and-pop shops to midsize enterprises — had a reason to invest in an entire computer platform. The Apple II was no longer a hobbyist’s toy or an educational aid; VisiCalc transformed it into a business machine.

![Apple II running VisiCalc, widely regarded as the first “killer app](./images/73dd11_828ade7189944a4ba15705a454eaa47cmv2.jpg)



Apple II running VisiCalc, widely regarded as the first “killer app.” Photo by Jean-Edouard Rozey, [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/). Retrieved from https://www.flickr.com/photos/jean-ed/1661870646/

This pattern would repeat throughout computing history. Photoshop became the anchor for the Macintosh in creative industries. Microsoft Office, with Excel dethroning VisiCalc, secured Windows as the corporate standard. Each time, a single capability proved magnetic enough to drive platform adoption en masse.



 

### Redrawing Competition Lines

In hardware, killer features — whenever they appear (and they are rare!) — exert this same pull, but with a substantial twist. Hardware’s much longer and more expensive development cycles, component interdependence, and fiercely defended IP cause competition to struggle for quite some time before it can recuperate from such a blow — either through a workaround or by launching a killer feature of their own.

By definition, killer features redraw the lines on the field, in what Clayton M. Christensen coined as **Disruptive Innovation** (1995). They shift the very dimensions of value along which competitors align and position themselves – if they only could.



 

### A Brief History of Disruption

It is worth revisiting the moments when killer features reset the rules of competition. Each example below shows how a single capability – often at the intersection of physical design and digital intelligence – pulled markets in a new disruptive direction and left rivals scrambling to respond.



 

#### Sony Walkman (1979)

The realization: *music is now portable, personal, and private.* It wasn’t the audio fidelity — it was slipping a cassette into your pocket and listening on the move. This shift redefined leisure culture itself.

![Sony Walkman](./images/nsplsh_9acc6c7c30e04791aaaa9a14685e60a9mv2.jpg)



Sony Walkman with headphones, symbol of the portable music revolution. Photo by Florian Schmetz on Unsplash. Retrieved from https://unsplash.com/photos/a-cassette-player-with-headphones-attached-to-it-Rks6FTfX5OU

> When the Walkman first launched in Japan in July 1979, Sony’s marketing team realized that conventional advertising wouldn’t be enough to explain such a radical product – small, lightweight, and designed for private listening. To overcome skepticism, they hired young people to stroll through Tokyo’s Ginza district wearing Walkmans and offering strangers the chance to listen.

![Sony Walkman promotion in Japan, 1979.](./images/73dd11_38e0b4777e7b4d53a33293fa6be06524mv2.png)



Sony Walkman promotion in Japan, 1979. Young demonstrators showcased the device in public spaces to spark curiosity and encourage trial. From *The History of the Institute of Electrical Engineers of Japan, Vol. 40, No. 5*, p. 318. Retrieved from http://www2.iee.or.jp/ver2/honbu/30-foundation/data02/ishi-03/ishi-0405.pdf

> This hands-on introduction bypassed the need for abstract messaging. Passersby could experience the product’s essence immediately: portable, personal music. The campaign was as much demonstration as promotion, and it proved decisive in turning curiosity into demand. Within two months, Sony had sold more than 30,000 units, far exceeding expectations.

[Extract from Sony Corporation. (n.d.). Sony history: The Walkman. [Sony.net](http://sony.net/). Archived from the original on June 26, 2010. Retrieved September 10, 2025, from [webarchive.org](http://webarchive.org/)]



 

The true takeaway from the Walkman’s launch is how profoundly disruptive its killer feature was: **music made portable as well as personalized**. For the first time, listening to a self-curated music selection was no longer tethered to a living room stereo, a car radio, or the heavy cassette decks from companies like Panasonic, Sharp, or JVC (it took the industry four year to catch up, in which the brand "Walkman" became a household name, and a generic term. 

Suddenly, one could place the unit on their belt, and listen in private to their own selection of music – while . Another innovation was Sony’s lightweight headphones (and the humble 3.5mm stereo jack went with it, too: As a side note, Sony had already introduced it in 1958 for its transistor radios, but it was the Walkman that popularized it globally – turning a small hardware detail into a lasting industry standard.)

Yet this very leap made the Walkman difficult for consumers to grasp. The concept was so novel that even marketers and retailers struggled to articulate its commercial potential. Market education quickly became essential, and the only effective approach was to **show, not tell**: Sony deployed live street demonstrations, staged press events, and seeded celebrity photo shoots that conveyed coolness and aspiration. On the retail side, cautious allotment was needed to reassure store owners that they would not be left holding unsellable stock of such an untested product.

In other words, the Walkman’s revolutionary nature demanded an ecosystem of education. The marketing effort was not an embellishment but a structural requirement – a bridge between a world that had never imagined private, mobile listening and a future where it would become second nature.



 

#### Apple Macintosh Reshapes Computing (1984)

At its launch in 1984, the Macintosh’s disruptive feature was its graphical user interface – icons, windows, and a mouse that made computing visual and intuitive rather than text-based.

Initially pioneered at **Xerox PARC** (Palo Alto Research Center), Steve Jobs and members of the Apple Lisa and Macintosh teams, were initiated to the concept of Graphical User Interface  (GUI) running a Xerox Alto computer – **bitmapped screen, overlapping windows, icons, and the mouse** – the building blocks of what would become the graphical user interface. ([Computer History Museum](https://computerhistory.org/blog/the-xerox-alto/), [Smithsonian](https://www.smithsonianmag.com/innovation/how-xerox-invented-modern-computers-180960168/?utm_source=chatgpt.com)).

Jobs later described the experience as an epiphany:

> *“I thought it was the best thing I’d ever seen in my life. Within 10 minutes, it was obvious to me that all computers would work like this someday.”* 

(Steve Jobs, quoted in Walter Isaacson’s biography, 2011).



 

Reviewers immediately recognized this as the breakthrough. The New York Times noted the Macintosh display was “refreshingly crisp and clear,” setting it apart from the command-line machines of the era (Sandberg-Diment, 1984). BYTE magazine admitted the machine had hardware limitations but concluded: 

> *“You can do useful work with it, and the user interface beats all others cold” (Webster, 1984).*

This usability shift reframed the basis of competition. The Mac didn’t need to win on raw specifications – its GUI redefined what a “personal computer” meant. IBM and Microsoft were forced to follow, accelerating the spread of graphical interfaces across the industry and pulling the personal computing revolution into a new era.

![The original Macintosh 128K (1984), the first mass-market computer with a graphical user interface.](./images/73dd11_5f102797c1cd4cf1a4870ef0d03bb2d5mv2.webp)



The original Macintosh 128K (1984), the first mass-market computer with a graphical user interface. Photo by MATEUS_27:24&25. Retrieved from [Smithsonian Magazine](https://www.smithsonianmag.com/history/what-reviewers-said-about-first-mac-when-it-debuted-180949448/)

It took competition in the personal computing about a decade to catch up.

![Apple Inc. stock price (1983–1995, raw historical values) with the launch of the Macintosh (January 24, 1984) highlighted.](./images/73dd11_6cc72b48b8fa474380e9d1dac8cd7cfemv2.jpg)



Apple Inc. stock price (1983–1995, raw historical values) with the launch of the Macintosh (January 24, 1984) highlighted. Data from Yahoo Finance. Chart generated by the author

The Macintosh launch in 1984 gave Apple a sharp (though brief) lift. Unit sales topped **372,000 in the first year**, well above expectations, and revenues jumped nearly **50 percent to $1.5 billion**, pushing market share into the 10~11 percent range.

[Watch the notorious, or famous, Super Bowl ad](https://archive.org/details/1983-30sec), iconic and almost earth-shattering, directed by Ridley Scott, his dystopian imagery echoing the visual language of Alan Parker’s 1982 Pink Floyd: The Wall. 

The faceless system that could not be named – though the bluish hues hinted strongly enough – was alluded to as the IBM/Microsoft duo, the emerging force in personal computing. 

Yet, as history proves, even the strongest “killer feature” cannot secure lasting advantage on its own; without an ecosystem to sustain it, disruption's effect may prove short lived. Eventually, industry’s giants will trample ahead, regardless of any temporary setback.



 

#### Dyson bagless vacuum (early 1990s)

When James Dyson introduced his first "Cyclone" vacuum (the G-Force, the DC01, and later models), it broke with decades of convention. Until then, vacuum cleaners were designed around **disposable paper bags** – not just as dust containers but also as filters. Performance inevitably declined as the bag filled, and consumers had to buy a constant supply of replacements.

![Dyson DC07 bagless vacuum cleaner](./images/73dd11_1df5d484cadf45538a3a9941062bfb4dmv2.jpg)



Dyson DC07 bagless vacuum cleaner. Photo by Arpingstone. Public domain, via Wikimedia Commons. Retrieved from https://commons.wikimedia.org/w/index.php?curid=66714

By ditching paper bags, Dyson removed a recurring pain point: the cost and hassle of consumables. For households, this meant **lower ongoing costs**, easier emptying, and no more frustration of running out of bags. 

For the industry, however, this was a shock: established players like Hoover, Electrolux, and Panasonic relied on **bag sales as a profitable annuity model**. Dyson’s innovation didn’t just improve the product; it undermined the incumbents’ business model.

The multi-cyclone design wasn’t only about eliminating bags. By spinning dust out of the airflow, it maintained **constant suction performance**, even as the bin filled. This addressed a long-standing flaw in bagged vacuums, where suction would degrade steadily as the bag clogged. Dyson emphasized this in advertising, reframing expectations: why tolerate performance drop-off when technology could avoid it?

The transparent dust bin was more than a design flourish. It gave users immediate feedback that the vacuum was working: dirt and dust swirling in plain sight. This shifted the competitive axis away from abstract “suction power” numbers to a **visceral, demonstrable result**. Customers didn’t need to trust spec sheets – they could *see* effectiveness with their own eyes.

The combination of visible feedback, lower running costs, and consistently high performance created a **compelling killer feature bundle**. By the mid-1990s, Dyson had captured significant share in the UK, displacing Hoover from its century-long leadership. By 2001, Dyson was the best-selling vacuum brand in the UK, and by the 2000s it had expanded globally, commanding premium prices.

Dyson’s cyclone vacuum shows that killer features can not only rely on superior engineering or clever design – it is the way those improvements converge with economics. Consumers got a vacuum that cleaned more effectively, showed its performance in real time, **and** cost less to own over its lifetime. 

By collapsing **better product experience** and **lower total cost of ownership** into a single offering, Dyson rewrote the rules of competition. Rivals still tied to bag sales could not follow without cannibalizing their own profits, leaving Dyson free to capture market share and redefine value in an otherwise stagnant category.



 

#### Nintendo Wii motion controller (2006)

When Nintendo launched the Wii in 2006, the bundled **Wii Remote** looked nothing like the standard controllers of the era. A **Core Differentiator** it reframed gaming around motion. Shaped like a television remote rather than a bulky gamepad, it replaced complex button layouts with a **motion-sensing wand**. Inside were accelerometers and gyroscopes, paired with an infrared sensor bar that let players point and swing with remarkable accuracy.

![Nintendo Wii Remote controller](./images/73dd11_0433872bc5a349e2963bdd42d6e754c8mv2.png)



Nintendo Wii Remote controller. Image via Wikimedia Commons. Licensed under CC BY-SA 3.0. Retrieved from https://commons.wikimedia.org/wiki/File:WiiRemoteController.png

This was a radical departure from the industry’s trajectory. Sony and Microsoft were locked in an arms race over **processing power, graphics fidelity, and cinematic immersion**. Nintendo reframed the competition: instead of asking how realistic a game could look, they asked how **intuitive and inclusive** it could feel. With the Wii, the act of play became physical – a swing of the arm to serve in tennis, a flick of the wrist to throw a bowling ball, a tilt to steer a kart.

The benefits were immediate. Gaming became accessible to **families, children, and even older adults** who found traditional controllers intimidating. *Wii Sports*, bundled with the console, turned living rooms into playgrounds and sparked global tournaments among players who had never touched a PlayStation or Xbox. Beyond fun, the Wii introduced the idea of **exergaming**, with titles like *Wii Fit* merging entertainment and fitness.

The impact was seismic. The Wii sold over **100 million units**, outselling both the PlayStation 3 and Xbox 360 during its peak years. Unlike its rivals, Nintendo profited on each console thanks to modest hardware costs, while driving additional revenue through games and accessories like the Balance Board and MotionPlus. 

![Estimated global market share of Nintendo Wii, Sony PlayStation, and Microsoft Xbox (2001–2016)](./images/73dd11_813fcc20a2cd46fcab2576839eb8d9admv2.jpg)



Estimated global market share of Nintendo Wii, Sony PlayStation, and Microsoft Xbox (2001–2016), with key milestone events highlighted. Based on synthesized data.

Just as important, the Wii **expanded the total addressable market for gaming**, pulling in demographics the rest of the industry had largely ignored.

The Wii Remote proved to be a killer feature by being a core differentiating factor redefining the rules of engagement, thus increasing total addressable market to new audiences and age groups. Locked in their  by shifting gaming from a contest of specs to an experience of shared, physical fun. 

---

 

#### iPhone (2007)

The 2007 launch of the iPhone shook the mobile world to its core. Within a few years, it dethroned Nokia from its long-held dominance and forced once-formidable rivals like BlackBerry, Sony Ericsson, and others out of the market. More than a product launch, it was a total rewrite of the competitive rulebook. Same as in nature (there are no vacuums in business) the space cleared by the obliteration of the top tier of competition was filled not only by iPhone’s rise, but was soon filled with an entirely new class of competitors.



I strongly recommend watching Steve Jobs present the iPhone in 2007 — a launch event for the ages for anyone in product. It’s a masterclass in presentation showmanship and, more importantly, a clear demonstration of the nature of killer features (a term Jobs himself uses) and the transformative impact they can have on a product.

Apple. (2007, January 9). *Steve Jobs introduces iPhone (2007)* [Thumbnail image]. YouTube. https://youtu.be/vN4U5FqrOdQ?si=alU0JuIZlHhdqOGZ

 

The splash from this launch – heard across the technological world – was powered by a stack of killer features, each amplifying the others and together disrupting device makers, carriers, and entire ancillary industries.

![iPhone 2007](./images/73dd11_39aaa7dbc76341f3b2d22be84b8ff2b9mv2.jpg)



iPhone 2007.From Carl Berkeley, Riverside California, 2009, *Wikimedia Commons*, [**https://commons.wikimedia.org/wiki/File:IPhone_First_Generation.jpg**](https://commons.wikimedia.org/wiki/File:IPhone_First_Generation.jpg) (CC BY-SA 2.0).



 

##### New UI paradigm for the mobile world

The most fundamental shift was the creation of a **new UI (User Interface)**, a result of acute identification of the shortcomings of then extant Smartphones: small screens, tiny, crammed keyboards, rigid controls, and inability to adapt UI to specific applications. 

![BlackBerry Classic (Q20) smartphone with physical keyboard](./images/73dd11_23247ae4fd1b4f72925e283226757dd0mv2.jpg)



BlackBerry Classic (Q20) smartphone with physical keyboard. Photo by Unsplash user [Linh Nguyen](https://unsplash.com/@lnhngyn), 2022. Retrieved from https://unsplash.com/photos/graphical-user-interface-application-RtijMFhL_ns.

In contrast, the iPhone’s capacitive touchscreen was accurate and responsive enough to replace physical buttons entirely, while also serving as a true multi-touch pointing device. Sensors detected when the phone was held to the ear, automatically disabling input to prevent accidental touches, while orientation sensing let the screen switch seamlessly between portrait and landscape to suit the task.

Apple’s virtual keyboard incorporated skeuomorphic feedback cues – visual key pop-ups and audible clicks – to compensate for the absence of physical keys. At the same time, innovative gestures such as pinch-to-zoom, tap, and inertial scrolling expanded the pointing interface, enabling direct manipulation of on-screen elements and eliminating the tedious scroll-and-select navigation of earlier devices.

![iPhone virtual keyboard with visual key pop-up feedback](./images/73dd11_4c364d91d16f40e2a061f4f8563ab905mv2.jpg)



Screenshot of iPhone virtual keyboard with visual key pop-up feedback. Image captured by the author, 2025.

The virtual keyboard did not arrive in isolation. It was accompanied by a new vocabulary of multitouch gestures: pinch-to-zoom, flick, swipe, and inertia scrolling—that gave users a direct, stylus-free, and intuitive way to navigate and control content on a large screen.

These UI breakthroughs flattened the learning curve and improved memory retention, expanding the audience beyond tech die-hards to the mainstream – a move increasing the competitive advantage of the iPhone, and its broad consumer appeal.

---

 

These leap-frog design choices alone were enough to disrupt the mobile phone industry. They created unmistakable differentiation by delivering greater user value in ways anyone could understand.

This competitive advantage drove instant demand to the hot, new, cool 'reinvented' phone, forcing incumbents – Motorola, Nokia, Blackberry, Palm – into a defensive chase after attributes they could not easily replicate.

An extensive suite of patents were filed prior to the launch, with both hardware and software elements covered, some of them listed below. IP strategy and patents played an important role in planning the commercial exploitation, and crucially fending against future competition.

| Patent Number                                                | **Covered Feature(s)**                        |
| ------------------------------------------------------------ | --------------------------------------------- |
| [US 7,479,949](https://patents.google.com/patent/US7479949B2/en) | Multi-touch heuristics (swipes, pinches, etc) |
| [US 7,657,849](https://patents.google.com/patent/US7657849B2/en) | Slide-to-unlock gesture                       |
| [US 7,812,826](https://patents.google.com/patent/US7812826B2/en) | Multi-touch on mobile device, sensor input    |
| [US 7,812,828](https://patents.google.com/patent/US7812828B2/en) | Ellipse fitting for multi-touch surfaces      |

A case of interest is **Apple v. Samsung** (2011–2018) – a landmark patent battle of the smartphone era. Apple accused Samsung of copying iPhone features like *slide to unlock* (US 7,657,849), and its icon-grid design, winning an initial $1.05 billion verdict (later reduced to $539 million). 

Though costly and protracted, the case became a proxy fight with Android and highlighted how design and software patents could shape the industry’s competitive landscape. Conversly, it also shows the limitations of such litigations in mitigating fierce competition.



---



##### "The Real Internet"

In that same iconic launch, Steve Jobs pointed to the so-called smartphones of 2007 limited, stripped-down access to the Internet. As he put it, they offered “sort of the baby Internet” rather than the real thing. 

> *The most advanced phones are called smart phones, so they say. And they typically combine a phone plus some email capability, plus they say it’s the Internet – it’s sort of the baby Internet ...*

![WAP browser rendering the English Wikipedia main page on a mobile device. From Wikimedia Commons, by Wikipedia user "Wap", 2008. https://upload.wikimedia.org/wikipedia/commons/0/02/Wap-wikipedia-en.png. Licensed under CC BY-SA 3.0.](./images/73dd11_5dfb472766f64112bf95607758ae49e0mv2.png)



WAP browser rendering the English Wikipedia main page on a mobile device. From Wikimedia Commons, by Wikipedia user "Wap", 2008. [**https://upload.wikimedia.org/wikipedia/commons/0/02/Wap-wikipedia-en.png**](https://upload.wikimedia.org/wikipedia/commons/0/02/Wap-wikipedia-en.png). Licensed under CC BY-SA 3.0.

The iPhone was his counterpoint: a device running Apple’s Unix-derived iOS and equipped with a fully functional, HTML-compliant browser that could deliver the web as people knew it on their computers.

> *This is a breakthrough Internet communicator built right into iPhone. The first rich HTML email on a phone. The first real Web browser on a phone. Best version of Google Maps on the planet, widgets and all with EDGE and Wi-Fi networking. We’re very, very happy with this.*  *… It’s the Internet in your pocket for the first time ever.*

Quotes from Steve Jobs during the Macworld 2007 keynote introducing the iPhone. Transcript retrieved from Steve Jobs introduces iPhone in 2007 (Macworld Keynote, January 9, 2007)

This leap immediately exposed the weakness of the existing carrier-driven model. For years, mobile operators had forced users through Wireless Application Protocol (WAP) portals that were slow, costly, and designed to keep customers inside their branded gardens. They dictated which phones were sold, what features were enabled, and how revenue was extracted, from SMS and ringtones to tightly controlled downloads. 

The iPhone broke that structure. Apple insisted on end-to-end control, barring AT&T in exchange for launch exclusivity, from disabling Wi-Fi, pre-loading portals, or even branding the device.



---



##### The Carrier Power Shift

The shift transformed consumer behavior. For the first time, people chose their carrier based on who offered the iPhone, not the other way around. In the U.S. this meant flocking to AT&T; in the UK it meant O2; in France it meant Orange. 

Carriers became secondary to the device itself, while customers began to identify as iPhone users rather than as subscribers to a particular network. Buying direct from Apple or choosing an unlocked handset became viable alternatives, reducing the lock-in power of bundled contracts.

The iPhone’s appetite for full web access and data-rich apps also forced carriers to abandon per-megabyte billing and move toward unlimited plans. The mobile carrier industry faced cannibalization, and AT&T executives - once approached by Apple, understood it was better “to have the cannibal in the family” than to lose millions of subscribers to rivals. 

The precedent Apple set reshaped the industry: carriers, once the gatekeepers of the mobile experience, were reduced to pipes, while the real value and loyalty shifted to ecosystems built by Apple and, later, Google.



---



##### Together, Not Alone

Each of these features mattered, but their power was cumulative.

- Without the keyboard-less glass slab, the “real internet” would have been unusable.
- Without multi-touch, the full screen would have been clumsy.
- Without breaking carrier control, the openness of the web and later apps would have been throttled.
- Without approachable design, mass adoption might have lagged.

The result was not merely a better phone, but the template for the modern smartphone and a reset of the industry’s balance of power.

Apple’s “phone reinvention” moment unleashed a pack of killer features fusing usability breakthroughs, software openness, and value-chain disruption into a single device.

---

 

#### Tesla OTA - Over The Air System updates (2012)

Tesla had been touting over-the-air (OTA) updates since the launch of the Model S in 2012, promising that “your Tesla gets better over time.” Much like a smartphone, the car could receive new features and fixes remotely: navigation tweaks, interface refinements, performance modes, and even the early rollout of Autopilot.

While the rest of the industry still required a dealer visit for most software adjustments, Tesla positioned OTA as a defining differentiator – proof that a car could continue to evolve after it left the factory.

![ree](./images/73dd11_0cfa7f5c169346e0a413821734586c42mv2.jpeg)



**Tesla Model S over-the-air (OTA) update illustration.** Image retrieved from *Stuff* (“The top car technology of 2017,” 2017). Fair use for scholarly/educational purposes. Source: https://www.stuff.co.nz/motoring/top-cars/98426802/the-top-car-technology-of-2017

For years, most of these updates felt incremental or playful. In December 2017, for instance, Tesla introduced a Christmas-themed “Romance Mode,” complete with sleigh graphics and festive music that transformed the heating screen into holiday theater.

![Tesla. (2018). Romance Mode Easter Egg [Video]. YouTube. https://youtu.be/iWI8bfK2wAQ?si=x4xF4wOw1dSO0BIH](./images/73dd11_1ae07c50aa204574ab0dbea910d9c911mv2.jpg)



**Tesla. (2018). Romance Mode Easter Egg [Video]. YouTube.** [**https://youtu.be/iWI8bfK2wAQ?si=x4xF4wOw1dSO0BIH**](https://youtu.be/iWI8bfK2wAQ?si=x4xF4wOw1dSO0BIH)

Owners came to expect such flourishes as part of the brand’s personality: updates were convenient, surprising, even fun.

But in September 2017, as Hurricane Irma bore down on Florida, the same capability proved lifesaving. Tesla remotely and temporarily unlocked extra battery capacity in Model S and Model X 60 kWh versions — cars that actually contained 75 kWh packs but were software-restricted. Overnight, evacuees gained an additional 30 to 40 miles of range, enough to help them escape the storm.

That intervention caught the attention not only of technology enthusiasts but also of the national press. [*The Washington Post*](https://www.washingtonpost.com/news/innovations/wp/2017/09/11/as-hurricane-irma-bore-down-tesla-gave-some-florida-drivers-more-battery-juice-heres-why-thats-a-big-deal/)[ observed](https://www.washingtonpost.com/news/innovations/wp/2017/09/11/as-hurricane-irma-bore-down-tesla-gave-some-florida-drivers-more-battery-juice-heres-why-thats-a-big-deal/):

*The decision highlights one of the most innovative aspects of owning a Tesla. The company’s ability to use software to instantly add range to a vehicle is something no conventional car can achieve. You can’t simply make a gas tank bigger at the click of a button.”*

By 2021, the same newspaper concluded that Teslas were effectively *“iPhones on wheels,”* [noting in a headline](https://www.washingtonpost.com/technology/2021/05/14/tesla-apple-tech/):

> *Tesla is like an ‘iPhone on wheels.’ And consumers are locked into its ecosystem.*

(Yes, this new killer feature had a dark side to it, too)

Together, these episodes elevated OTA updates into a textbook ***killer feature\***. For users, the benefit was unmistakable: their cars no longer depreciated in utility the moment they left the showroom. Instead, features could be added or improved over time, turning ownership into an evolving experience rather than a static one.

For competitors, this was deeply threatening. Traditional automakers were still bound to dealer networks and hardware-bound feature sets, while Tesla had shown that the most compelling value could be delivered with a keystroke – instantly resetting expectations for what a modern car should offer.

And for Tesla itself, OTA updates opened the door to a different business model. Controlling code meant not only delivering upgrades in real time but also monetizing them – from optional feature unlocks to subscription programs – reshaping the economics of car making as profoundly as the innovation reshaped the product itself.

---



### The Essence of Killer Features

Killer features differ fundamentally from incremental improvements: they act as disruptive wedges that redefine the terms of competition. By reframing what customers value, they render existing benchmarks obsolete. 

The Walkman redefined leisure; VisiCalc justified computers for business; the iPhone reset usability; the MacBook Air elevated portability; and Tesla proved that adaptability itself could be a feature.

A useful framework is to view killer features as operating along three axes:

- **User benefits** – filling a gap and meeting previously unmet needs.
- **Competitive disruption** – undermining established industry conventions and resetting expectations.
- **Business model change** – altering the underlying economics of value creation and capture.

![Killer feature dimensions by Example](./images/73dd11_8f763bbffc5e4c8ea4318e76d4bd1422mv2.png)



Illustration of killer feature dynamics (subjective interpretation). Created by the author.

Competitors caught unawares still compete on yesterday’s dimensions – more keys, faster processors, larger batteries – suddenly looking irrelevant. Killer features matter because they do more than add value; they shift the basis of competition, pulling the entire market toward a new axis of differentiation.

Equally important, they reshape business models. Consumers begin paying for different things, at different times, and often at different price points. What once was a one-time transaction becomes a recurring relationship, or a bundle of services layered on top of hardware.

For firms, this makes careful strategic planning essential. To fully capitalize on the R&D behind such breakthroughs, companies must not only design the killer feature itself but also anticipate how it will alter demand patterns, revenue flows, and competitive dynamics.



---



### **Killer Features - Key takeaways**

- A killer feature reframes value for users, disrupts competitors’ assumptions, and changes the revenue logic.
- Adoption speed and defensibility determine how long the advantage lasts.
- Ecosystems turn one feature into a flywheel: distribution, complements, and IP convert differentiation into dominance.
- Strategy must pair invention with capture: pricing, subscriptions, upgrades, and timing.



------

# Additional Case Studies

<TBD>

------

'***'

# Conclusion

<TBD>