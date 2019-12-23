BRAND_CATEGORY_CHOICES = ['Food & Dining', 'Media & Entertainment', 'Electronics', 'Telecom', 'Sports', 'Health', 'Beverages', 'Household/Home', 'Personal Care & Beauty', \
        'Retail & Fashion', 'Auto', 'Financial Services', 'Travel' \
    ]

AGE_RANGE_CHOICES = (
    ('17_under', 'Age 17 and under'), 
    ('18_20', 'Age 18 to 20'), 
    ('21_24', 'Age 21 to 24'), 
    ('25_29', 'Age 25 to 29'), 
    ('30_34', 'Age 30 to 34'), 
    ('35_44', 'Age 35 to 44'), 
    ('45_54', 'Age 45 to 54'), 
    ('55_64', 'Age 55 to 64'),
    ('65_over', 'Age 65 and over')
)

PERSONAL_INCOME_CHOICES = ['Under $10,000' , '$10,000 - $19,999', '$20,000 - $29,999', '$30,000 - $39,999', '$40,000 - $49,999', '$50,000 - $74,999', '$75,000 - $99,999', 'Over $100,000']

SOCIAL_STATUS_CHOICES = ['Lower', 'Working', 'Middle', 'Upper']

INTERESTS_CHOICES = [
    "3D Graphics",
    "3D Printing",
    "Accessories",
    "Action",
    "Adoption",
    "Adult content",
    "Adventure",
    "Adventure Travel",
    "Africa",
    "Aikido",
    "Air sports",
    "Airplanes",
    "Alternative medicine",
    "Alternative/Indie rock",
    "American",
    "American football",
    "Americana",
    "Amusement/Theme Parks",
    "Android",
    "Animation",
    "Anime",
    "Apple",
    "Appliances",
    "Archery",
    "Art/culture",
    "Arts & crafts",
    "Asia",
    "Asian",
    "Astrology",
    "Athletics",
    "Australasia",
    "Australian",
    "Avant-garde",
    "Babies/Toddlers",
    "Badminton",
    "Barbecues/Grilling",
    "Baseball",
    "Basketball",
    "Bass Guitar",
    "Beach volleyball",
    "Beaches",
    "Bed & Breakfasts",
    "Beer",
    "Billiards/Pool",
    "Biographies/Memoirs",
    "Biography",
    "Biology",
    "Birdwatching",
    "Blogging",
    "Blues",
    "Board/Card games",
    "Boating",
    "Bodybuilding",
    "Bollywood",
    "Books",
    "Boots",
    "Botany",
    "Bowling",
    "Boxing",
    "Brazilian jiu-Jitsu",
    "Budget Travel",
    "Business",
    "Business Travel",
    "Cajun/Creole",
    "Cake/cookies",
    "Cameras/Camcorders",
    "Camping",
    "Canadian",
    "Cancer",
    "Cannabis",
    "Canoeing/Kayaking",
    "Cardiology",
    "Careers advice",
    "Caribbean",
    "Cars",
    "Cartoons",
    "Cats",
    "Celebrity",
    "Celebrity gossip",
    "Charity",
    "Cheerleading",
    "Chemistry",
    "Chess",
    "Chicken",
    "Children's",
    "Children's books",
    "Children's music",
    "Chinese",
    "Chocolate",
    "Christian & gospel",
    "Cigars/Smoking",
    "Circuits",
    "Classical",
    "Climatology",
    "Climbing",
    "Clothing",
    "Club/Dance",
    "Cocktails",
    "Coffee",
    "Collecting things",
    "College education",
    "Comedy",
    "Comics",
    "Comics/Graphic novels",
    "Computer parts & peripherals",
    "Computer reviews",
    "Computers",
    "Contemporary",
    "Contemporary/Designer",
    "Cooking",
    "Country",
    "Coupons",
    "Credit/loans",
    "Cricket",
    "Crime",
    "Crime/Mystery",
    "Cruises",
    "Cultural",
    "Curling",
    "Cycling",
    "Dance",
    "Dance music",
    "Dance-Pop",
    "Dating/romance",
    "Deals & Last Minute",
    "Dental Care",
    "Dermatology",
    "Design",
    "Desserts/Baking",
    "Diabetes",
    "Digital music",
    "Disco",
    "Distance learning",
    "Documentary",
    "Dogs",
    "Drag racing",
    "Drama",
    "Drawing & sketching",
    "Drones",
    "Drums",
    "Easy listening",
    "Eclectic",
    "Economic",
    "Education",
    "Elderly care",
    "Electric & hybrid cars",
    "Electric scooters",
    "Electronic",
    "Endurance racing",
    "Energy drinks",
    "English",
    "Entertainment",
    "Entrepreneurship",
    "Environment",
    "Equestrian",
    "Europe",
    "European",
    "Exercise",
    "Extreme sports",
    "Eye Health",
    "Eyewear",
    "Family",
    "Family & Parenting",
    "Family life",
    "Fantasy",
    "Fantasy sports",
    "Fashion",
    "Fast food",
    "Fiction",
    "Figure skating",
    "Film/TV",
    "Financial",
    "Financial planning",
    "Fine dining",
    "Fishing",
    "Fishkeeping",
    "Fitness",
    "Folk",
    "Formula 1",
    "Formula E",
    "Freelance writing",
    "French",
    "Funds",
    "Furniture",
    "Gambling",
    "Game show",
    "Gaming",
    "Gardening",
    "Gay life",
    "Genealogy",
    "Geography",
    "Geology",
    "German",
    "Gin",
    "Gluten-free",
    "Golf",
    "Graduate school",
    "Gran touring",
    "Greek",
    "Guitar",
    "Gym",
    "Gymnastics",
    "Hair Care",
    "Handbags/Wallets",
    "Handball",
    "Hard rock",
    "Hats",
    "Hawaiian",
    "Health",
    "Health/Lowfat cooking",
    "Healthcare",
    "Heavy metal",
    "Hi-Fi stereo",
    "High school",
    "Hiking",
    "Historical fiction",
    "History",
    "Hockey",
    "Home & garden",
    "Home improvement",
    "Home theater",
    "Homebrewing",
    "Honeymoons",
    "Horror",
    "Horse racing",
    "Horses",
    "House",
    "Humor",
    "Hunting",
    "Ice skating",
    "Immigration",
    "Independent movies",
    "Indian",
    "IndyCar",
    "Insurance",
    "Interior decorating",
    "International",
    "iPhones",
    "Irish",
    "Islands",
    "Italian",
    "Japanese",
    "Japanese sake",
    "Jazz",
    "Jewelry",
    "Jewelry making/Beadwork",
    "Jiu-Jitsu",
    "Job search",
    "Jogging & running",
    "Journalism",
    "J-Pop",
    "Judo",
    "Juices",
    "Karate",
    "Kickboxing",
    "Kids Clothing",
    "Kindergarten",
    "Kitesurfing",
    "Knitting",
    "Korean",
    "K-Pop",
    "Krav Maga",
    "Kung Fu",
    "Lacrosse",
    "Language learning",
    "Latin",
    "Latin American",
    "Linux",
    "Literature",
    "Live music",
    "Local",
    "Lotteries",
    "Luxury Beauty",
    "Luxury cars",
    "Magic & illusion",
    "Makeup",
    "Marriage",
    "Maternity",
    "Maths & Stats",
    "Medicine",
    "Mediterranean",
    "Men's grooming",
    "Men's health",
    "Mental illness",
    "Mexican",
    "Mexico",
    "Middle Eastern",
    "Middle school",
    "Milkshakes",
    "Mind & body",
    "MMA",
    "Model building",
    "Modeling",
    "Motocross",
    "MotoGP",
    "Motor sports",
    "Motorcycles",
    "Mountain biking",
    "Muay Thai",
    "Music",
    "Musical",
    "Mystery",
    "Nail care",
    "Nascar",
    "National",
    "National Parks",
    "Natural beauty products",
    "Needlework",
    "New age",
    "News",
    "Nightlife/partying",
    "Noir",
    "Nonfiction",
    "North America",
    "Nutrition/Weight loss",
    "Olympics",
    "Online courses",
    "Opera",
    "Organic",
    "Origami",
    "Outdoor life",
    "Paintball",
    "Painting",
    "Pediatrics",
    "Performance arts",
    "Perfume/Cologne",
    "Personal care",
    "Petite",
    "Pets",
    "Philosophy",
    "Photography",
    "Physical therapy",
    "Physics",
    "Piano",
    "Pilates",
    "Pizza",
    "Plastic surgery",
    "Plus-size",
    "Poetry",
    "Poker",
    "Political",
    "Politics",
    "Polo",
    "Pop",
    "Pregnancy",
    "Private school",
    "Programming",
    "Psychological therapy",
    "Psychology",
    "Public transport",
    "Punk",
    "R&B",
    "Radio",
    "Rafting",
    "Rally",
    "Rap & hip hop",
    "Real estate",
    "Reality TV",
    "Reggae",
    "Religion",
    "Reptiles/arachnids",
    "Resorts",
    "Retirement planning",
    "Robotics",
    "Rock",
    "Rock & roll",
    "Rodeo",
    "Roleplay games",
    "Roller derby",
    "Romance",
    "Rowing",
    "Rugby",
    "Rum",
    "Sailing",
    "Scandinavian",
    "Scholarships/Financial aid",
    "Science",
    "Science Fiction",
    "Scientific",
    "Sci-fi",
    "Scrapbooking",
    "Screenwriting",
    "Scuba diving",
    "Seafood",
    "Security",
    "Self help",
    "Senior health",
    "Shareware/Freeware",
    "Shoes",
    "Shooting",
    "Shopping",
    "Short stories",
    "Show business",
    "Skateboarding",
    "Skating",
    "Skiing",
    "Skin care",
    "Skydiving",
    "Smartphones",
    "Snowboarding",
    "Soccer",
    "Social networks",
    "Social sciences",
    "Soft drinks",
    "Softball",
    "Software",
    "Soul",
    "South America",
    "South East Asia",
    "Southeast Asian",
    "Southern",
    "Southwestern",
    "Space/Astronomy",
    "Spanish",
    "Spas/Beauty salons",
    "Special needs children",
    "Spirituality",
    "Sport",
    "Sporting goods",
    "Sports",
    "Sportsware",
    "Squash",
    "Stamps & coins",
    "Startups",
    "Stock market",
    "Superbike",
    "Surfing",
    "Suspence/Thriller",
    "Swimming",
    "Swimwear",
    "Table tennis",
    "Tablets",
    "Taekwondo",
    "Tai Chi",
    "Talk show",
    "Tattoos",
    "Tax planning",
    "Tea",
    "Tech",
    "Techno",
    "Technology",
    "Teen pop",
    "Tennis",
    "Thai",
    "The economy",
    "The paranormal",
    "Theater",
    "Thriller",
    "Toys",
    "Training",
    "Trains",
    "Trance",
    "Travel",
    "Traveling With Kids",
    "Triathlon",
    "Trucks",
    "Underwear",
    "Uniforms",
    "Variety show",
    "Vegan",
    "Vegetarian",
    "Veterinary",
    "Violin",
    "Virtual reality",
    "Vocal",
    "Vodka",
    "Volleyball",
    "War",
    "Watches",
    "Water polo",
    "Waterskiing/Wakeboarding",
    "Weather",
    "Western",
    "Whiskey",
    "Windows",
    "Wine",
    "Wining & dining",
    "Women's books",
    "Women's health",
    "Woodworking",
    "World music",
    "Wrestling",
    "Writing",
    "Yoga",
    "Young adult",
]

COUNTRY_CHOICES = (
    ("AU", "Australia"),
    ("AX", "Aland Islands"),
    ("AL", "Albania"),
    ("DZ", "Algeria"),
    ("AS", "American Samoa"),
    ("AD", "Andorra"),
    ("AI", "Anguilla"),
    ("AQ", "Antarctica"),
    ("AG", "Antigua and Barbuda"),
    ("AR", "Argentina"),
    ("AM", "Armenia"),
    ("AW", "Aruba"),
    ("AT", "Austria"),
    ("AZ", "Azerbaijan"),
    ("BS", "Bahamas"),
    ("BH", "Bahrain"),
    ("BD", "Bangladesh"),
    ("BB", "Barbados"),
    ("BE", "Belgium"),
    ("BZ", "Belize"),
    ("BJ", "Benin"),
    ("BM", "Bermuda"),
    ("BT", "Bhutan"),
    ("BO", "Bolivia"),
    ("BO", "Bonaire, Sint Eustatius and Saba"),
    ("BA", "Bosnia and Herzegovina"),
    ("BW", "Botswana"),
    ("BR", "Brazil"),
    ("IO", "British Indian Ocean Territory"),
    ("VG", "British Virgin Islands"),
    ("BN", "Brunei Darussalam"),
    ("BG", "Bulgaria"),
    ("BF", "Burkina Faso"),
    ("BI", "Burundi"),
    ("KH", "Cambodia"),
    ("CM", "Cameroon"),
    ("CA", "Canada"),
    ("CV", "Cape Verde"),
    ("KY", "Cayman Islands"),
    ("TD", "Chad"),
    ("JE", "Channel Islands and Jersey"),
    ("CL", "Chile"),
    ("CN", "China"),
    ("CO", "Colombia"),
    ("KM", "Comoros"),
    ("CG", "Congo"),
    ("CK", "Cook Islands"),
    ("CR", "Costa Rica"),
    ("HR", "Croatia"),
    ("CY", "Cyprus"),
    ("CZ", "Czech Republic"),
    ("DK", "Denmark"),
    ("DJ", "Djibouti"),
    ("DM", "Dominica"),
    ("DO", "Dominican Republic"),
    ("EC", "Ecuador"),
    ("EG", "Egypt"),
    ("SV", "El Salvador"),
    ("GQ", "Equatorial Guinea"),
    ("ER", "Eritrea"),
    ("EE", "Estonia"),
    ("ET", "Ethiopia"),
    ("FO", "Faroe Islands"),
    ("FK", "Falkland Islands (Malvinas)"),
    ("FJ", "Fiji"),
    ("FI", "Finland"),
    ("FR", "France"),
    ("GF", "French Guiana"),
    ("PF", "French Polynesia"),
    ("GA", "Gabon"),
    ("GM", "Gambia"),
    ("GE", "Georgia"),
    ("DE", "Germany"),
    ("GH", "Ghana"),
    ("GI", "Gibraltar"),
    ("GR", "Greece"),
    ("GL", "Greenland"),
    ("GD", "Grenada"),
    ("GP", "Guadeloupe"),
    ("GU", "Guam"),
    ("GT", "Guatemala"),
    ("GG", "Guernsey"),
    ("GN", "Guinea"),
    ("GW", "Guinea-Bissau"),
    ("GY", "Guyana"),
    ("HT", "Haiti"),
    ("VA", "Holy See"),
    ("HN", "Honduras"),
    ("HK", "Hong Kong"),
    ("HU", "Hungary"),
    ("IS", "Iceland"),
    ("IN", "India"),
    ("ID", "Indonesia"),
    ("IE", "Ireland"),
    ("IM", "Isle of Man"),
    ("IL", "Israel"),
    ("IT", "Italy"),
    ("JM", "Jamaica"),
    ("JP", "Japan"),
    ("JO", "Jordan"),
    ("KZ", "Kazakhstan"),
    ("KE", "Kenya"),
    ("KI", "Kiribati"),
    ("KW", "Kuwait"),
    ("KG", "Kyrgyzstan"),
    ("LA", "Lao People'S Democratic Republic"),
    ("LV", "Latvia"),
    ("LB", "Lebanon"),
    ("LS", "Lesotho"),
    ("LR", "Liberia"),
    ("LI", "Liechtenstein"),
    ("LT", "Lithuania"),
    ("LU", "Luxembourg"),
    ("MO", "Macao Special Administrative Region of China"),
    ("MG", "Madagascar"),
    ("MW", "Malawi"),
    ("MY", "Malaysia"),
    ("MV", "Maldives"),
    ("ML", "Mali"),
    ("MT", "Malta"),
    ("MH", "Marshall Islands"),
    ("MQ", "Martinique"),
    ("MR", "Mauritania"),
    ("MU", "Mauritius"),
    ("YT", "Mayotte"),
    ("MX", "Mexico"),
    ("FM", "Micronesia, Federated States of"),
    ("MC", "Monaco"),
    ("MN", "Mongolia"),
    ("ME", "Montenegro"),
    ("MS", "Montserrat"),
    ("MA", "Morocco"),
    ("MZ", "Mozambique"),
    ("NA", "Namibia"),
    ("NP", "Nepal"),
    ("NL", "Netherlands"),
    ("AN", "Netherlands Antilles"),
    ("NC", "New Caledonia"),
    ("NZ", "New Zealand"),
    ("NI", "Nicaragua"),
    ("NE", "Niger"),
    ("NU", "Niue"),
    ("NF", "Norfolk Island"),
    ("MP", "Northern Mariana Islands"),
    ("NO", "Norway"),
    ("PS", "Occupied Palestinian Territory"),
    ("OM", "Oman"),
    ("PK", "Pakistan"),
    ("PW", "Palau"),
    ("PA", "Panama"),
    ("PG", "Papua New Guinea"),
    ("PY", "Paraguay"),
    ("PE", "Peru"),
    ("PH", "Philippines"),
    ("PN", "Pitcairn"),
    ("PL", "Poland"),
    ("PT", "Portugal"),
    ("PR", "Puerto Rico"),
    ("QA", "Qatar"),
    ("KR", "Republic of Korea"),
    ("MD", "Republic of Moldova"),
    ("RE", "Reunion"),
    ("RO", "Romania"),
    ("RU", "Russian Federation"),
    ("RW", "Rwanda"),
    ("SH", "Saint Helena"),
    ("KN", "Saint Kitts and Nevis"),
    ("LC", "Saint Lucia"),
    ("MF", "Saint Martin"),
    ("PM", "Saint Pierre and Miquelon"),
    ("VC", "Saint Vincent and the Grenadines"),
    ("WS", "Samoa"),
    ("SM", "San Marino"),
    ("ST", "Sao Tome and Principe"),
    ("SA", "Saudi Arabia"),
    ("SN", "Senegal"),
    ("RS", "Serbia"),
    ("SC", "Seychelles"),
    ("SG", "Singapore"),
    ("SK", "Slovakia"),
    ("SI", "Slovenia"),
    ("SB", "Solomon Islands"),
    ("ZA", "South Africa"),
    ("ES", "Spain"),
    ("LK", "Sri Lanka"),
    ("SR", "Suriname"),
    ("SJ", "Svalbard and Jan Mayen Islands"),
    ("SZ", "Swaziland"),
    ("SE", "Sweden"),
    ("CH", "Switzerland"),
    ("TW", "Taiwan (Republic of China)"),
    ("TJ", "Tajikistan"),
    ("TH", "Thailand"),
    ("MK", "The former Yugoslav Republic of Macedonia"),
    ("TG", "Togo"),
    ("TK", "Tokelau"),
    ("TO", "Tonga"),
    ("TT", "Trinidad and Tobago"),
    ("TN", "Tunisia"),
    ("TR", "Turkey"),
    ("TM", "Turkmenistan"),
    ("TC", "Turks and Caicos Islands"),
    ("TV", "Tuvalu"),
    ("UG", "Uganda"),
    ("UA", "Ukraine"),
    ("AE", "United Arab Emirates"),
    ("GB", "United Kingdom"),
    ("TZ", "United Republic of Tanzania"),
    ("US", "United States"),
    ("VI", "United States Virgin Islands"),
    ("UY", "Uruguay"),
    ("UZ", "Uzbekistan"),
    ("VU", "Vanuatu"),
    ("VE", "Venezuela"),
    ("VN", "Viet Nam"),
    ("WF", "Wallis and Futuna Islands"),
    ("EH", "Western Sahara"),
    ("ZM", "Zambia"),
)

CURRENCY_CHOICES = (
    ('usd', 'USD'),
    ('eur', 'EUR'),
)