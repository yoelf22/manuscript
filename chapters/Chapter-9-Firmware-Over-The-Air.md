# Chapter 9 - Firmware Over The Air

> **From Products to Living Systems**

![Smart Tangibles: Capabilities and Revenue Streams](../images/fig00-00-capabilities-revenue.jpg)
*Arc II layer model: This chapter bridges the **Digital and Connectivity** and **Cloud Support** layers — over-the-air updates require connectivity infrastructure and cloud backend to turn static products into evolving platforms.*

## **Introduction: The Hardware Transformation**



 \- Traditional hardware's "death sentence" at manufacture

 \- How FOTA breaks the hardware rigidity paradigm

 \- The shift from products to platforms

---

## The Long Road to Over-The-Air

To appreciate what FOTA makes possible, it helps to understand what came before it. Firmware — the low-level software that gives hardware its behavior — has always needed updating. What changed, dramatically, is how those updates reach the device.

### Burning and Swapping: The EPROM Era

For the first two decades of programmable electronics, updating firmware meant physically replacing a chip. UV-erasable EPROMs — the Intel 2716, 2732, and their descendants — stored firmware on a silicon die visible through a small quartz window on the chip's surface. To update, a technician removed the chip from its socket, placed it under ultraviolet light for five to fifteen minutes to erase the contents, reprogrammed it using a dedicated device programmer, and reinstalled it on the board. One device at a time.

This was how the world ran. Pac-Man arcade cabinets used Texas Instruments TMS 2532 EPROMs — arcade operators who wanted to modify game behavior had to swap the chip at position 6F on the PCB. Bally and Stern pinball machines stored their entire game logic on Intel 2716 and 2732 chips. Industrial PLCs — the programmable controllers replacing relay logic on factory floors — relied on Intel 2708 EPROMs. Updating a PLC meant a technician visiting the factory with a replacement chip in hand.

The original IBM PC (1981) used mask-programmed ROM for its BIOS — firmware that could not be altered at all after manufacture. Clone makers adopted EPROMs to allow updates, but "allow" is generous: the process required equipment, skill, and physical access to every individual machine. At scale, it was barely feasible.

### The Floppy and the Flash Chip

Around 1995, electrically erasable flash memory replaced UV-erasable EPROMs in PCs, and the update model changed overnight. Firmware could now be rewritten *in place* — no chip removal, no UV lamp, no programmer. All you needed was a bootable floppy disk and a flash utility.

Three vendors — AMI, Phoenix Technologies, and Award Software — dominated the PC BIOS market and each shipped their own flash utilities: AMIFLASH, PHLASH, and AWDFLASH. The procedure was ritualistic: download the BIOS file from a bulletin board (later a website), copy it and the utility onto a bootable DOS floppy, boot from the floppy, run the utility, hold your breath. A power outage mid-flash could brick the motherboard. More advanced BIOSes introduced a protected "boot block" — a small, read-only section that could detect corruption and prompt for recovery media — but many boards lacked even this safeguard.

How real was the bricking risk? In 1998, Taiwanese student Chen Ing-hau created the CIH virus — also known as "Chernobyl." On April 26, 1999, it activated on an estimated 60 million computers worldwide, overwriting the flash BIOS with junk data on vulnerable Intel 430TX-based motherboards. Affected machines were rendered completely inoperable. IBM had shipped several thousand Aptiva PCs with the virus pre-installed just a month earlier. The incident demonstrated, vividly, that field-updatable firmware was both a capability and an attack surface — a lesson the industry would relearn repeatedly.

The 3.5-inch floppy disk peaked in 1996 with billions in circulation, but it held on in PCs far longer than expected — specifically because of its role in BIOS updates and driver distribution. Many motherboard boxes included a floppy with drivers well into the mid-2000s.

### Optical Media: CDs, DVDs, and the Dealership Visit

As update payloads grew beyond what a 1.44 MB floppy could carry, distribution shifted to optical media. Microsoft shipped Windows XP Service Pack 2 (2004) — a 260 MB security overhaul — as a free CD-ROM to customers who ordered it, because millions of users on dial-up connections simply could not download it. PlayStation 3 game discs shipped with mandatory system software updates that installed before the game would launch. Xbox 360's "New Xbox Experience" dashboard overhaul (November 2008) reached users through both Xbox Live and game discs.

But the most consequential optical-media update story belongs to the automotive industry. During this era, ECU firmware updates were distributed to dealerships on CD or DVD. The process: the ECU supplier releases an update, the OEM tests and approves it, the update ships on physical media to dealerships, the customer schedules a service appointment, drives to the dealer, and a technician connects a reprogramming tool to the vehicle's OBD-II port. Every firmware fix — no matter how minor — required a customer visit. As ECU complexity grew and update frequency increased, this model became untenable. It would take Tesla to break it (see FOTA Success Stories below).

### The Internet Changes Everything — Almost

Windows Update, launched with Windows 98 in June 1998, was the first operating system feature to alert users when software updates were available. Fixes for the Year 2000 problem were among its earliest real-world deployments. By Windows XP (2001), the client inventoried the system's hardware and software and sent that data to Microsoft's servers to determine applicable updates — the seeds of fleet-wide, server-managed update distribution.

Consumer networking equipment followed. The Linksys WRT54G, released in December 2002 and the best-selling consumer router of all time, ran Linux internally and accepted firmware uploads through a web-based admin interface. When the open-source community discovered the Linux-based firmware, it spawned OpenWRT and DD-WRT — two of the most influential open-source firmware projects ever created. Linksys (by then owned by Cisco) later switched to proprietary VxWorks, was sued by the FSF for GPL violations, and eventually released the WRT54GL specifically to support third-party firmware. The episode demonstrated both the power and the unintended consequences of internet-distributed firmware.

These were transformative steps — but they still required users to *initiate* the update. Someone had to click "Check for Updates," visit a website, or connect a cable. The device could not update itself. For that, two more pieces were needed: reliable wireless connectivity and a safe way to swap firmware without bricking the device.

### The Reboot Problem: Memory, Partitions, and the Risk of Bricking

Here lies the most treacherous moment in any firmware update: the instant the device must stop running its old software and start running the new one. The firmware being overwritten is the same firmware managing the overwrite. If power is lost, the battery dies, or the write process is interrupted, the device is left with a corrupted, incomplete image — unable to boot, unable to recover. Bricked.

The industry's primary answer is the **A/B partition scheme**. The device maintains two complete copies of its system firmware in separate flash memory partitions. It runs from the active slot (say, Slot A) while the update is written to the inactive slot (Slot B). On completion, the bootloader switches to the newly written slot on the next boot. If the new firmware fails to start, the bootloader rolls back to the previous slot automatically.

Google introduced A/B seamless updates for Android with the Pixel in 2016 (Android 7.1 Nougat). Within months, 95% of Pixel owners were running the latest security patch — compared to 87% of Nexus users without seamless updates. By Android 13, Google mandated Virtual A/B partitioning for all new devices, using snapshots and compression to reduce the storage overhead of maintaining two complete firmware copies.

Protecting the bootloader itself is equally critical. Modern systems validate firmware integrity through cryptographic signatures before allowing boot, and implement anti-rollback protection using hardware fuses (e-fuses) that are permanently burned to prevent downgrading to older, vulnerable versions. Once burned, an e-fuse cannot be reset by software — the change is irreversible.

Even with these protections, bricking still happens. In 2022, a Pixel 6 update to Android 13 left the B partition on Android 12; when the A slot failed, anti-rollback protection *prevented* fallback to the older B slot, permanently bricking the device. The very mechanism designed to prevent exploitation became the mechanism that destroyed the phone. It is a reminder that firmware update engineering is, at its core, a problem of managing transitions under uncertainty — and that the consequences of getting it wrong are measured in hardware, not just software.

### WiFi, Cellular, and True Over-The-Air

The final leap — from internet-available updates to genuine over-the-air delivery — required two enablers: ubiquitous wireless connectivity and fleet management infrastructure.

**WiFi** made OTA updates practical for consumer devices with access to home or enterprise networks. Apple's iOS is the landmark example: before iOS 5 (October 2011), every iPhone update required a physical cable to a computer running iTunes. iOS 5.0.1, released November 10, 2011, was the first public over-the-air iOS update — a shift from tethered updates for ~100 million devices to wireless updates that would eventually reach billions.

**Cellular networks** extended OTA to devices with no WiFi access and, often, no user interface at all. Tesla deployed the first full-vehicle OTA update in September 2012, pushing version 1.9.11 to its Model S fleet over 3G. The update took two hours to install and, among other things, recalibrated the car's rated range. Later updates would improve the Model 3's braking distance by 19 feet following a critical Consumer Reports review — the first time a carmaker improved braking performance through software alone — and add approximately 100 horsepower to Model Y vehicles as a paid software upgrade. Tesla has since resolved NHTSA recalls covering over 2 million vehicles entirely via OTA, prompting NHTSA to add a "Software Update Repairs Recall" icon to its website.

For IoT devices operating on battery power in remote locations — smart meters, agricultural sensors, asset trackers — low-power cellular standards like **LTE-M** and **NB-IoT** now enable FOTA without WiFi, without a user interface, and without physical access. Cloud management platforms (nRF Cloud, Soracom, AVSystem) provide fleet-level visibility, staged rollouts, and monitoring of update success rates across thousands of devices. The update that once required a technician with a UV lamp and a chip programmer now reaches a sensor bolted to a water main in a basement, over a cellular connection, while the device continues operating.

The journey from UV-erasable EPROMs to cellular FOTA spans five decades and represents one of the most consequential shifts in hardware product management: the moment a product's capabilities stopped being frozen at manufacture and became a living, updatable system. Everything that follows in this chapter — the strategic advantages, the business models, the risks — rests on this foundation.

---

##  **The Technology Behind Living Products**



###  **FOTA Infrastructure Essentials**



 \- Secure bootloaders and partition management

 \- Differential updates vs. full firmware replacement

 \- Rollback mechanisms and fail-safe protocols

 \- Authentication and encryption requirements



###  **Delivery Mechanisms**



 \- Over-the-air delivery networks (WiFi, cellular, satellite)

 \- Staged rollouts and A/B testing for firmware

 \- Bandwidth optimization and update scheduling



###  **Strategic Advantages of Living Products**



###  **Continuous Value Creation**



 \- Post-purchase feature additions and improvements

 \- Bug fixes without service calls or recalls

 \- Performance optimization based on real-world data



###  **Competitive Differentiation**



 \- Faster time-to-market with iterative improvement

 \- Responding to competitor features without hardware changes

 \- Creating upgrade paths within existing product lines



###  **Economic Benefits**



 \- Reduced warranty and service costs

 \- Extended product lifecycles and customer retention

 \- New revenue streams through software subscriptions



###  **Real-World FOTA Success Stories**



 \- **Tesla:** Over-the-air improvements to range, performance, and features

 \- **Roomba:** Navigation algorithms and mapping improvements

 \- **Smart TVs:** Interface updates and new streaming services

 \- **Industrial equipment:** Predictive maintenance and efficiency

 optimization



###  **The Dark Side: FOTA Risks and Challenges**



###  **Technical Risks**



 \- Bricked devices and recovery procedures

 \- Network dependency and offline functionality

 \- Version fragmentation across device populations



###  **Security Vulnerabilities**



 \- Update channels as attack vectors

 \- Unauthorized firmware modifications

 \- Trust and certificate management



###  **User Experience Challenges**



 \- Forced updates vs. user control

 \- Feature removal and functionality changes

 \- Notification fatigue and update anxiety



###  **Implementation Strategy for Hardware Companies**



 \- Building FOTA capability into product architecture

 \- Balancing update frequency with user disruption

 \- Legal and regulatory considerations (warranty, liability)

 \- Customer communication and change management



##  **Conclusion: The Living Product Imperative**



 \- Why static products become obsolete

 \- FOTA as competitive necessity, not luxury

 \- Planning for a post-shipment product lifecycle