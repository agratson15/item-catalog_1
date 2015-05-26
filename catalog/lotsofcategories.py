from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Category, Base, CatalogItem, User
 
engine = create_engine('sqlite:///catalogwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#Create dummy user
User1 = User(name="A Grats", email="agrats@dabomb.com", picture='http://www.mr-butler.com/wp-content/uploads/2015/04/The-Rock-wwe-champion-hd-wallpapers.jpg')
session.add(User1)
session.commit()

#1 Items for the Soccer Category
category1 = Category(user_id=1, name = "Soccer")

session.add(category1)
session.commit()

catalogItem1 = CatalogItem(user_id=1, title = "Adidas UCL Training Ball", description = "FIFA inspect training ball. Seamless surface for a better touch and lower water uptake.", price = "$39.99", item_picture = "http://image-load-balancer.worldsportshops.com/Images/watermarked_thumbnail.aspx?img=93369&photoNum=1&t=I&catalog=Soccer&w=600&h=600" , category = category1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, title = "Adidas F50 Adizero TRX FG Messi", description = "Eye-catching cleat inspired by the great Messi. The colors are also part of adidas' Samba Pack, a colorful collection created in honor of 2014 host country Brazil.", price = "$247.99", item_picture = "http://image-load-balancer.worldsportshops.com/Images/watermarked_thumbnail.aspx?img=63191&photoNum=1&t=I&catalog=Soccer&w=600&h=600" , category = category1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, title = "USA 50 States Scarf", description = "All for one. Wave the USA fan scarf and show your pride.", price = "$24.99", item_picture = "http://image-load-balancer.worldsportshops.com/Images/watermarked_thumbnail.aspx?img=79125&photoNum=1&t=I&catalog=Soccer&w=600&h=600" , category = category1)

session.add(catalogItem3)
session.commit()

#2 Items for the Basketball Category
category1 = Category(user_id=1, name = "Basketball")

session.add(category1)
session.commit()

catalogItem1 = CatalogItem(user_id=1, title = "Spalding ABA Official Game Basketball ", description = "Take a step back in time to the days of the ABA with the Spalding ABA Official Game Basketball. Designed with the glitz that the ABA is known for, the ball features alternating red, white and blue panels.", price = "$79.99", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-18993325p275w.jpg" , category = category1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, title = "Spalding 72 Acrylic Arena View Series Basketball Hoop", description = "Turn your backyard into a high energy court with the Spalding 72 Acrylic Arena View Series Basketball Hoop.", price = "$2699.99", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-13569888p275w.jpg" , category = category1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, title = "Nike Men's Zoom HyperRev 2015 Basketball Shoes", description = "Get equipped for championship performance with the Nike Zoom HyperRev 2015 basketball shoe. Delivering optimal stability, this on-court shoe features a lightweight outer shell that provides zonal support and durability.", price = "$124.99", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-20949186p275w.jpg" , category = category1)

session.add(catalogItem3)
session.commit()

#3 Items for the Golf category
category1 = Category(user_id=1, name = "Golf")

session.add(category1)
session.commit()

catalogItem1 = CatalogItem(user_id=1, title = "Puma Men's Cuadrado 2.0 Web Golf Belt", description = "Made of soft, and durable webbing material, the Puma Cuadrado 2.0 Belt will complete all of your golf attire this season. Designed with a bottle opener on the back buckle, and adjustment capabilities, you will love the comfortable convenience out on the course.", price = "$20.00", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-20727373p275w.jpg" , category = category1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, title = "Nike 2015 Air Hybrid Vapor Stand Bag", description = "Fuse cart and stand bag functionality with an Air Hybrid Stand Bag. A 14-way top with full-length dividers and integrated putter well provides secure equipment storage.", price = "$199.99", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-20661946p275w.jpg" , category = category1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, title = "TaylorMade R15 Driver", description = "Leave your course mates in the dust with the R15 Driver. TaylorMade's most technically advanced driver is equipped with a sliding split weight system that features draw, fade, and split positions.", price = "$429.99", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-20217376_alternate3_p275w.jpg" , category = category1)

session.add(catalogItem3)
session.commit()

#4 Items for the Tennis category
category1 = Category(user_id=1, name = "Tennis")

session.add(category1)
session.commit()

catalogItem1 = CatalogItem(user_id=1, title = "Babolat Drive Max 110 Tennis Racquet", description = "Curb the competition with the Babolat Drive Max 110 Tennis Racquet. Power comes from the Elliptic Geometry frame design, which makes the Drive Max 20 percent stiffer and bend-resistant than traditional racquets.", price = "$199.99", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-15075835p275w.jpg" , category = category1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, title = "Tourna Low Compression Stage 3 Tennis Ball", description = "Prepare your child for the biggest match of the year with the Tourna Low Compression Stage 3 Tennis Ball 18 Pack.", price = "$34.99", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-21011689p275w.jpg" , category = category1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, title = "HEAD Core Pro 3 Pack Tennis Bag", description = "A simple, yet fully-functional storage and transportation option for all of your tennis gear, the HEAD Core Pro Tennis Bag is perfect for any tennis athlete on the go.", price = "$34.99", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-15046103p275w.jpg" , category = category1)

session.add(catalogItem3)
session.commit()

#5 Items for the Baseball category
category1 = Category(user_id=1, name = "Baseball")

session.add(category1)
session.commit()

catalogItem1 = CatalogItem(user_id=1, title = "Easton XL1 BBCOR Bat 2015", description = "Designed with an extra-long barrel to give hitters more chance at capitalizing on the sweet spot, the 2015 Easton XL1 BBCOR Bat is perfect for the -3 player looking to add more power and speed to their swing.", price = "$399.99", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-19203454p275w.jpg" , category = category1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, title = "Wilson Hanley Ramirez A2000 Series Glove", description = "Crafted from famous American Pro Stock leather for rugged durability and an unmatched feel, the Wilson Hanley Ramirez A2000 Glove is the perfect mitt for hard-working infielders everywhere.", price = "$239.99", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-19016387p275w.jpg" , category = category1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, title = "Under Armour Junior Solid Molded Batting Helmet", description = "The Under Armour Junior Batting Helmet offers superior protection while maintaining maximum comfort. A high impact resistant ABS plastic shell with large vents throughout the helmet offers maximum breathability for comfort as the game heats up.", price = "$34.99", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-20819463p275w.jpg" , category = category1)

session.add(catalogItem3)
session.commit()

#6 Items for the Football category 
category1 = Category(user_id=1, name = "Football")

session.add(category1)
session.commit()

catalogItem1 = CatalogItem(user_id=1, title = "Wilson NFL Performance Official Football", description = "Preferred by quarterbacks for its exceptional tack and grip, the Wilson NFL Performance Official Football features ACL white pebbled composite laces to increase grip by 174 percent and provide outstanding ball control.", price = "$39.99", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-16455574p275w.jpg" , category = category1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, title = "Nike Adult Vapor Jet 3.0 Receiver Gloves", description = "Engineered to match the speed, skill and intensity of your game, the Nike Vapor Jet 3.0 Receiver Gloves deliver a lightweight feel and superior mobility without sacrificing toughness.", price = "$55.00", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-16767864_alternate1_p275w.jpg" , category = category1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, title = "Schutt Youth Recruit Hybrid Custom Football Helmet", description = "Constructed with a hybrid cushioning system of TPU and patented D30 materials, the Schutt Recruit Hybrid Custom Helmet boasts the most advanced impact-absorbing system in the game.", price = "$99.99", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/p18448747p275w.jpg" , category = category1)

session.add(catalogItem3)
session.commit()

#7 Items for the Hockey category
category1 = Category(user_id=1, name = "Hockey")

session.add(category1)
session.commit()

catalogItem1 = CatalogItem(user_id=1, title = "Bauer Senior Vapor X700 Ice Hockey Skates", description = "Get the game-changing speed and power you need this season with the Bauer Vapor X700 skates.", price = "$399.99", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-20962443p275w.jpg" , category = category1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, title = "Bauer Senior Vapor 1X GripTac Ice Hockey Stick", description = "When the game's on the line, deliver with the Bauer Vapor 1X stick. The AERO-SENSE II blade core with AERO FOAM 3 adds a quick release to your shot and QRT Taper can help the puck explode off your stick and into the back of the net.", price = "$269.99", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-20598628p275w.jpg" , category = category1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, title = "PRIMED PVC Street Hockey Goal", description = "Take your skills to the next level as you pass, shoot and score with the PRIMED PVC Street Hockey Goal. Made with locking elbows, this PRIMED hockey net is easily assembled, set-up and taken down. ", price = "$69.99", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-18917185p275w.jpg" , category = category1)

session.add(catalogItem3)
session.commit()

#8 Items for Cycling category
category1 = Category(user_id=1, name = "Cycling")

session.add(category1)
session.commit()

catalogItem1 = CatalogItem(user_id=1, title = "GT Adult GTS Comp Road Bike", description = "Take the GT Adult GTS Comp Road Bike for a tour around your favorite cycling destination. The durable alloy frame makes climbing hills a breeze.", price = "$849.99", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-20567786p275w.jpg" , category = category1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, title = "Giro Adult Hex Bike Helmet", description = "The Giro Hex&trade Bike Helmet offers slick style with big performance and impressive value. Made for aggressive trail riding, this bike helmet is constructed with a strong in-mold polycarbonate shell.", price = "$89.99", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-17477611p275w.jpg" , category = category1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, title = "Garmin Edge 810 Bundle Bike Computer", description = "Change the way you ride with the Garmin Edge 810 Bundle Bike Computer. Customize your touchscreen display to show your speed, location, calories burned and more.", price = "$699.99", item_picture = "http://www.dickssportinggoods.com/graphics/product_images/pDSP1-15272049p275w.jpg" , category = category1)

session.add(catalogItem3)
session.commit()

print "added catalog items!"
