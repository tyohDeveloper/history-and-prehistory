import json, re

E = []

def add(slug, name, kind, sy, ey, parent, summary, aliases=None, extant=None, conf="high", dm="calendar"):
    if extant is None:
        extant = ey is None
    E.append({
        "suggested_id_slug": slug,
        "name": name,
        "kind": kind,
        "start_year": sy,
        "end_year": ey,
        "extant": bool(extant),
        "parent_hint": parent,
        "start_dating_method": dm,
        "summary": " ".join(summary.split()),
        "aliases": aliases or [],
        "confidence": conf,
    })

US = "United States"
COL = "Colonial North America"
NA = "North America"

# ---------------- TOP-LEVEL POLITIES ----------------
add("united-states", "United States of America", "polity", 1776, None, NA,
    "Federal republic founded by thirteen British colonies that declared independence in 1776; expanded across North America and became a global superpower in the 20th century.",
    ["USA", "US", "America", "United States"], True)
add("colonial-north-america", "Colonial North America", "period", 1585, 1783, NA,
    "Era of European colonisation of eastern North America by England, France, the Netherlands, Sweden and Spain, ending with US independence.",
    ["British North America", "American colonial period"], False)
add("british-north-america", "British North America", "polity", 1607, 1783, COL,
    "English and later British colonial holdings in North America, from Jamestown to the Treaty of Paris that recognised American independence.",
    ["English America", "Thirteen Colonies and beyond"], False)
add("new-netherland", "New Netherland", "polity", 1614, 1667, COL,
    "Dutch colony on the Hudson and Delaware rivers centred on New Amsterdam, conquered by England in 1664 and ceded in 1667.",
    ["Nieuw-Nederland", "New Amsterdam colony"], False)
add("new-sweden", "New Sweden", "polity", 1638, 1655, COL,
    "Small Swedish colony on the lower Delaware River, absorbed by New Netherland in 1655.",
    ["Nya Sverige"], False)
add("new-france", "New France", "polity", 1534, 1763, NA,
    "French colonial empire in North America including Canada, Acadia and Louisiana, ceded to Britain and Spain in 1763.",
    ["Nouvelle-France"], False)
add("spanish-florida", "Spanish Florida", "polity", 1513, 1821, NA,
    "Spanish colonial province in the southeast, centred on St. Augustine, transferred to the United States under the Adams-Onis Treaty.",
    ["La Florida"], False)
add("spanish-new-mexico", "Spanish New Mexico", "polity", 1598, 1821, NA,
    "Spanish colonial province in the upper Rio Grande valley, later a Mexican territory and then a US territory.",
    ["Santa Fe de Nuevo Mexico"], False)
add("russian-america", "Russian America", "polity", 1799, 1867, NA,
    "Russian colonial possession in Alaska administered by the Russian-American Company, sold to the United States in 1867.",
    ["Russian Alaska"], False)
add("confederate-states-of-america", "Confederate States of America", "polity", 1861, 1865, NA,
    "Breakaway slaveholding republic of eleven southern states, defeated by the Union in the Civil War and dissolved in 1865.",
    ["Confederacy", "CSA", "the South"], False)
add("republic-of-texas", "Republic of Texas", "polity", 1836, 1845, NA,
    "Independent republic that broke from Mexico in 1836 and was annexed by the United States in 1845.",
    ["Texian Republic"], False)
add("kingdom-of-hawaii", "Kingdom of Hawaii", "polity", 1795, 1893, NA,
    "Unified Hawaiian monarchy founded by Kamehameha I, overthrown in 1893 and annexed by the United States in 1898.",
    ["Hawaiian Kingdom"], False)
add("republic-of-hawaii", "Republic of Hawaii", "polity", 1894, 1898, NA,
    "Short-lived settler-led republic in Hawaii between the overthrow of the monarchy and US annexation.",
    ["Hawaiian Republic"], False)
add("california-republic", "California Republic", "polity", 1846, 1846, NA,
    "Brief settler rebellion republic proclaimed at Sonoma during the Bear Flag Revolt, absorbed into US forces within weeks.",
    ["Bear Flag Republic"], False)
add("vermont-republic", "Vermont Republic", "polity", 1777, 1791, NA,
    "Self-declared independent republic between New York and New Hampshire that joined the Union as the fourteenth state in 1791.",
    ["Republic of New Connecticut"], False)
add("state-of-franklin", "State of Franklin", "polity", 1784, 1788, NA,
    "Unrecognised breakaway state in what is now eastern Tennessee, reabsorbed by North Carolina.",
    ["Frankland"], False)

# ---------------- GOVERNMENT PERIODS ----------------
add("continental-congress", "Continental Congress", "polity", 1774, 1789, US,
    "Governing assembly of the rebelling colonies and then of the United States, spanning the First and Second Congresses and the Confederation Congress.",
    ["Second Continental Congress", "Confederation Congress"], False)
add("articles-of-confederation", "Articles of Confederation", "period", 1781, 1789, US,
    "First US constitution, ratified in 1781, creating a weak central Confederation government without power to tax; replaced by the Constitution in 1789.",
    ["Confederation period", "Articles government"], False)
add("early-republic", "Early Republic", "era", 1789, 1815, US,
    "Formative decades of the constitutional United States, from Washington's inauguration through the War of 1812.",
    ["Federalist era and Jeffersonian era"], False)
add("federalist-era", "Federalist Era", "era", 1789, 1801, US,
    "Period of Federalist Party dominance under Washington and John Adams, marked by Hamilton's financial system and partisan conflict.",
    ["Washington-Adams era"], False)
add("jeffersonian-era", "Jeffersonian Era", "era", 1801, 1825, US,
    "Period of Democratic-Republican ascendancy featuring the Louisiana Purchase, the War of 1812 and the Era of Good Feelings.",
    ["Virginia Dynasty"], False)
add("era-of-good-feelings", "Era of Good Feelings", "era", 1815, 1825, US,
    "Period of one-party nationalism after the War of 1812, associated with James Monroe's presidency and the Monroe Doctrine.",
    [], False)
add("jacksonian-era", "Jacksonian Era", "era", 1828, 1854, US,
    "Age of mass democracy, spoils politics, Indian removal and the Second Party System, named for Andrew Jackson.",
    ["Age of Jackson", "Jacksonian democracy"], False)
add("antebellum-period", "Antebellum Period", "era", 1815, 1861, US,
    "Decades before the Civil War marked by market revolution, westward expansion, slavery's growth and intensifying sectional crisis.",
    ["Antebellum America"], False)
add("sectional-crisis", "Sectional Crisis", "era", 1846, 1861, US,
    "Escalating North-South conflict over slavery's extension, from the Wilmot Proviso to secession.",
    ["Crisis of the Union", "road to disunion"], False)
add("civil-war-reconstruction", "Civil War & Reconstruction", "era", 1861, 1877, US,
    "Period of the American Civil War and the postwar reconstruction of the southern states, including emancipation and the Reconstruction Amendments.",
    ["Civil War era"], False)
add("reconstruction", "Reconstruction", "era", 1865, 1877, US,
    "Postwar rebuilding of the South, with federal military occupation, Black political participation and the Fourteenth and Fifteenth Amendments; ended by the Compromise of 1877.",
    ["Radical Reconstruction"], False)
add("presidential-reconstruction", "Presidential Reconstruction", "period", 1865, 1867, US,
    "Andrew Johnson's lenient restoration policy for the ex-Confederate states, which produced Black Codes and provoked congressional backlash.",
    ["Johnson's Reconstruction"], False)
add("congressional-reconstruction", "Congressional Reconstruction", "period", 1867, 1877, US,
    "Radical Republican programme imposing military districts and Black male suffrage on the South under the Reconstruction Acts.",
    ["Radical Reconstruction", "Military Reconstruction"], False)
add("redemption-south", "Redemption", "period", 1870, 1877, US,
    "Campaign by white Democratic 'Redeemers' to overthrow Reconstruction governments in the South, often by paramilitary violence.",
    ["Redeemer era"], False)
add("jim-crow-era", "Jim Crow Era", "era", 1877, 1965, US,
    "Long period of legally enforced racial segregation and Black disenfranchisement in the South, ended by civil rights legislation.",
    ["segregation era", "Jim Crow"], False)
add("gilded-age", "Gilded Age", "era", 1877, 1896, US,
    "Era of rapid industrialisation, railroads, immigration, urban growth, machine politics and extreme inequality named after a Twain novel.",
    ["Gilded Age America"], False)
add("progressive-era", "Progressive Era", "era", 1896, 1917, US,
    "Reform period targeting trusts, corruption, unsafe food and labour conditions, producing antitrust action, direct election of senators and suffrage momentum.",
    ["Progressive movement"], False)
add("jazz-age", "Jazz Age", "era", 1920, 1929, US,
    "Prosperous, culturally exuberant 1920s of jazz, flappers, radio, automobiles and Prohibition-era nightlife.",
    ["Roaring Twenties"], False)
add("great-depression", "Great Depression", "era", 1929, 1941, US,
    "Worst economic collapse in US history, beginning with the 1929 crash and producing mass unemployment, bank failures and the New Deal.",
    ["the Depression"], False)
add("new-deal", "New Deal", "era", 1933, 1939, US,
    "Franklin Roosevelt's programme of relief, recovery and reform, creating Social Security, the SEC, the TVA and federal work relief agencies.",
    ["First New Deal", "Second New Deal"], False)
add("home-front-wwii", "World War II Home Front", "period", 1941, 1945, US,
    "Wartime mobilisation of the US economy and society, with rationing, war bonds, women in industry and Japanese American incarceration.",
    ["American home front"], False)
add("postwar-boom", "Postwar Boom", "era", 1945, 1964, US,
    "Era of sustained prosperity, suburbanisation, the baby boom, the GI Bill and mass consumer culture.",
    ["Golden Age of Capitalism", "Fifties America"], False)
add("cold-war-us", "Cold War (United States)", "era", 1947, 1991, US,
    "Global geopolitical struggle between the United States and the Soviet Union, shaping US foreign, military and domestic policy for four decades.",
    ["Cold War"], False)
add("red-scare-first", "First Red Scare", "period", 1917, 1920, US,
    "Postwar panic over anarchism and Bolshevism, marked by the Palmer Raids, mass deportations and suppression of radical labour.",
    ["Palmer Raids era"], False)
add("red-scare-second", "Second Red Scare", "period", 1947, 1957, US,
    "Cold War anticommunist campaign of loyalty oaths, blacklists and congressional investigations into alleged subversion.",
    ["Red Scare", "the great fear"], False)
add("mccarthyism", "McCarthyism", "period", 1950, 1954, US,
    "Senator Joseph McCarthy's aggressive and largely unsubstantiated hunt for communists in government, discredited after the 1954 Army-McCarthy hearings.",
    ["McCarthy era"], False)
add("prohibition", "Prohibition", "period", 1920, 1933, US,
    "Nationwide ban on alcoholic beverages under the Eighteenth Amendment and Volstead Act, repealed by the Twenty-first Amendment.",
    ["the dry years", "Noble Experiment"], False)
add("manifest-destiny", "Manifest Destiny", "era", 1845, 1860, US,
    "Ideology holding that the United States was destined to expand across North America, used to justify Texas annexation, Oregon and the Mexican-American War.",
    ["continental expansion"], False)
add("westward-expansion", "Westward Expansion", "era", 1803, 1890, US,
    "Century of US territorial and settler expansion from the Louisiana Purchase to the closing of the frontier.",
    ["frontier era", "American West"], False)
add("great-society", "Great Society", "era", 1964, 1968, US,
    "Lyndon Johnson's sweeping domestic programme creating Medicare, Medicaid, federal education aid, immigration reform and civil rights enforcement.",
    ["Johnson's Great Society"], False)
add("war-on-poverty", "War on Poverty", "period", 1964, 1968, US,
    "Johnson administration antipoverty campaign launched by the Economic Opportunity Act, creating Head Start, Job Corps, VISTA and community action agencies.",
    ["Economic Opportunity programmes"], False)
add("civil-rights-movement", "Civil Rights Movement", "era", 1954, 1968, US,
    "Mass campaign against segregation and disenfranchisement, from Brown v. Board and the Montgomery bus boycott to the Civil Rights and Voting Rights Acts.",
    ["Black freedom struggle", "Second Reconstruction"], False)
add("black-power-movement", "Black Power Movement", "period", 1966, 1975, US,
    "Militant turn in Black politics stressing self-determination, community control and racial pride, associated with SNCC's later phase and the Black Panther Party.",
    ["Black Power"], False)
add("second-wave-feminism", "Second-Wave Feminism", "period", 1963, 1982, US,
    "Women's movement for legal and economic equality, producing NOW, Title IX, Roe v. Wade and the failed Equal Rights Amendment campaign.",
    ["women's liberation movement"], False)
add("counterculture-1960s", "1960s Counterculture", "period", 1964, 1974, US,
    "Youth rebellion against mainstream norms featuring antiwar protest, rock music, communal living and drug experimentation.",
    ["hippie movement"], False)
add("new-left", "New Left", "period", 1960, 1973, US,
    "Radical student and intellectual movement centred on SDS, participatory democracy and opposition to the Vietnam War.",
    [], False)
add("environmental-movement-us", "American Environmental Movement", "period", 1962, 1980, US,
    "Wave of ecological activism sparked by Silent Spring, producing Earth Day, the EPA, the Clean Air Act and the Endangered Species Act.",
    ["ecology movement"], False)
add("watergate-scandal", "Watergate Scandal", "event", 1972, 1974, US,
    "Break-in at Democratic headquarters and the Nixon administration cover-up that led to the president's resignation in August 1974.",
    ["Watergate"], False)
add("stagflation-1970s", "Stagflation Era", "period", 1973, 1982, US,
    "Decade of simultaneous high inflation and unemployment triggered by oil shocks and ended by Volcker's tight money policy.",
    ["1970s economic crisis"], False)
add("reagan-revolution", "Reagan Revolution", "era", 1981, 1989, US,
    "Conservative realignment of tax cuts, deregulation, military buildup and confrontation with the Soviet Union.",
    ["Reaganomics", "conservative ascendancy"], False)
add("culture-wars", "American Culture Wars", "era", 1980, None, US,
    "Ongoing political conflict over abortion, religion, sexuality, race, guns, education and national identity.",
    ["culture war"], True, "medium")
add("dot-com-boom", "Dot-Com Boom and Bust", "period", 1995, 2001, US,
    "Internet-driven stock bubble and subsequent crash that reshaped the American technology economy.",
    ["dot-com bubble"], False)
add("war-on-terror", "War on Terror", "era", 2001, 2021, US,
    "Global US counterterrorism campaign launched after the September 11 attacks, encompassing the Afghanistan and Iraq wars and expanded surveillance.",
    ["Global War on Terrorism", "GWOT"], False)
add("great-recession", "Great Recession", "period", 2007, 2009, US,
    "Severe downturn triggered by the subprime mortgage collapse and financial crisis, prompting TARP and the 2009 stimulus.",
    ["financial crisis of 2008"], False)
add("covid-19-pandemic-us", "COVID-19 Pandemic in the United States", "event", 2020, 2023, US,
    "Coronavirus pandemic that killed over a million Americans, closed schools and businesses and prompted unprecedented fiscal relief.",
    ["coronavirus pandemic"], False)

# ---------------- PRESIDENCIES ----------------
pres = [
 ("presidency-george-washington","Presidency of George Washington",1789,1797,"First president; set precedents for the office, established the cabinet and federal finance, suppressed the Whiskey Rebellion and urged neutrality in his Farewell Address.",["George Washington","Washington administration"]),
 ("presidency-john-adams","Presidency of John Adams",1797,1801,"Federalist second president; navigated the Quasi-War with France, signed the Alien and Sedition Acts and lost re-election in 1800.",["John Adams","Adams administration"]),
 ("presidency-thomas-jefferson","Presidency of Thomas Jefferson",1801,1809,"Third president; completed the Louisiana Purchase, sent Lewis and Clark west, fought the Barbary pirates and imposed the Embargo Act.",["Thomas Jefferson"]),
 ("presidency-james-madison","Presidency of James Madison",1809,1817,"Fourth president; led the nation through the War of 1812 and the burning of Washington, then presided over postwar nationalism.",["James Madison"]),
 ("presidency-james-monroe","Presidency of James Monroe",1817,1825,"Fifth president; oversaw the Era of Good Feelings, the acquisition of Florida, the Missouri Compromise and the Monroe Doctrine.",["James Monroe"]),
 ("presidency-john-quincy-adams","Presidency of John Quincy Adams",1825,1829,"Sixth president, elected by the House in the disputed 1824 contest; promoted internal improvements but was blocked by Jacksonian opposition.",["John Quincy Adams"]),
 ("presidency-andrew-jackson","Presidency of Andrew Jackson",1829,1837,"Seventh president; destroyed the Second Bank, faced down South Carolina's nullification and forced Indian removal along the Trail of Tears.",["Andrew Jackson","Old Hickory"]),
 ("presidency-martin-van-buren","Presidency of Martin Van Buren",1837,1841,"Eighth president; his term was consumed by the Panic of 1837 depression and the continuing Second Seminole War.",["Martin Van Buren"]),
 ("presidency-william-henry-harrison","Presidency of William Henry Harrison",1841,1841,"Ninth president; died of illness thirty-one days after inauguration, the shortest presidency in US history.",["William Henry Harrison","Tippecanoe"]),
 ("presidency-john-tyler","Presidency of John Tyler",1841,1845,"Tenth president and first to succeed on a death; expelled from the Whig Party, he secured the annexation of Texas.",["John Tyler","His Accidency"]),
 ("presidency-james-k-polk","Presidency of James K. Polk",1845,1849,"Eleventh president; expansionist who settled the Oregon boundary and won the Mexican-American War, adding the Southwest and California.",["James K. Polk","James Knox Polk"]),
 ("presidency-zachary-taylor","Presidency of Zachary Taylor",1849,1850,"Twelfth president; Mexican War hero who died of illness sixteen months into his term amid the crisis over slavery in the new territories.",["Zachary Taylor","Old Rough and Ready"]),
 ("presidency-millard-fillmore","Presidency of Millard Fillmore",1850,1853,"Thirteenth president; signed the Compromise of 1850 including the Fugitive Slave Act, and opened Japan via the Perry expedition.",["Millard Fillmore"]),
 ("presidency-franklin-pierce","Presidency of Franklin Pierce",1853,1857,"Fourteenth president; his support for the Kansas-Nebraska Act ignited Bleeding Kansas and shattered the Democratic coalition.",["Franklin Pierce"]),
 ("presidency-james-buchanan","Presidency of James Buchanan",1857,1861,"Fifteenth president; failed to halt sectional collapse or secession, widely ranked among the least successful presidents.",["James Buchanan"]),
 ("presidency-abraham-lincoln","Presidency of Abraham Lincoln",1861,1865,"Sixteenth president; led the Union through the Civil War, issued the Emancipation Proclamation and was assassinated days after Confederate surrender.",["Abraham Lincoln","Honest Abe"]),
 ("presidency-andrew-johnson","Presidency of Andrew Johnson",1865,1869,"Seventeenth president; clashed bitterly with Radical Republicans over Reconstruction and was impeached and acquitted by one vote.",["Andrew Johnson"]),
 ("presidency-ulysses-s-grant","Presidency of Ulysses S. Grant",1869,1877,"Eighteenth president; enforced Reconstruction and prosecuted the Klan while his administration was marred by financial scandals and the Panic of 1873.",["Ulysses S. Grant","U.S. Grant"]),
 ("presidency-rutherford-b-hayes","Presidency of Rutherford B. Hayes",1877,1881,"Nineteenth president; took office via the Compromise of 1877, withdrew federal troops from the South and pursued civil service reform.",["Rutherford B. Hayes"]),
 ("presidency-james-a-garfield","Presidency of James A. Garfield",1881,1881,"Twentieth president; shot by Charles Guiteau four months into his term and died in September 1881.",["James A. Garfield","James Abram Garfield"]),
 ("presidency-chester-a-arthur","Presidency of Chester A. Arthur",1881,1885,"Twenty-first president; a former spoilsman who surprised critics by signing the Pendleton Civil Service Act.",["Chester A. Arthur","Chester Alan Arthur"]),
 ("presidency-grover-cleveland-first","First Presidency of Grover Cleveland",1885,1889,"Twenty-second president; fiscally conservative Democrat who vetoed pension bills and fought tariffs before losing the 1888 electoral vote.",["Grover Cleveland first term"]),
 ("presidency-benjamin-harrison","Presidency of Benjamin Harrison",1889,1893,"Twenty-third president; signed the Sherman Antitrust Act and the high McKinley Tariff and admitted six western states.",["Benjamin Harrison"]),
 ("presidency-grover-cleveland-second","Second Presidency of Grover Cleveland",1893,1897,"Twenty-fourth president; the only non-consecutive second term, dominated by the Panic of 1893 and the Pullman Strike.",["Grover Cleveland second term"]),
 ("presidency-william-mckinley","Presidency of William McKinley",1897,1901,"Twenty-fifth president; won the Spanish-American War, annexed Hawaii and the Philippines and was assassinated in Buffalo in 1901.",["William McKinley"]),
 ("presidency-theodore-roosevelt","Presidency of Theodore Roosevelt",1901,1909,"Twenty-sixth president; trust-busting Progressive who championed conservation, the Pure Food and Drug Act and the Panama Canal.",["Theodore Roosevelt","Teddy Roosevelt","TR"]),
 ("presidency-william-howard-taft","Presidency of William Howard Taft",1909,1913,"Twenty-seventh president; pursued more antitrust suits than Roosevelt but split the Republican Party and lost the 1912 election.",["William Howard Taft"]),
 ("presidency-woodrow-wilson","Presidency of Woodrow Wilson",1913,1921,"Twenty-eighth president; created the Federal Reserve, led the US into World War I and championed the League of Nations.",["Woodrow Wilson"]),
 ("presidency-warren-g-harding","Presidency of Warren G. Harding",1921,1923,"Twenty-ninth president; promised a 'return to normalcy' and died in office in 1923 as the Teapot Dome scandal emerged.",["Warren G. Harding","Warren Gamaliel Harding"]),
 ("presidency-calvin-coolidge","Presidency of Calvin Coolidge",1923,1929,"Thirtieth president; presided over 1920s prosperity with tax cuts and minimal government activism.",["Calvin Coolidge","Silent Cal"]),
 ("presidency-herbert-hoover","Presidency of Herbert Hoover",1929,1933,"Thirty-first president; the 1929 crash and Great Depression overwhelmed his limited relief efforts, and he lost in a 1932 landslide.",["Herbert Hoover"]),
 ("presidency-franklin-d-roosevelt","Presidency of Franklin D. Roosevelt",1933,1945,"Thirty-second president and only four-term president; enacted the New Deal and led the Allied war effort until his death in April 1945.",["Franklin D. Roosevelt","FDR","Franklin Delano Roosevelt"]),
 ("presidency-harry-s-truman","Presidency of Harry S. Truman",1945,1953,"Thirty-third president; authorised the atomic bombings, launched the Marshall Plan, NATO and containment, and committed forces to Korea.",["Harry S. Truman","Harry Truman"]),
 ("presidency-dwight-d-eisenhower","Presidency of Dwight D. Eisenhower",1953,1961,"Thirty-fourth president; ended the Korean War, built the Interstate Highway System and sent troops to enforce desegregation at Little Rock.",["Dwight D. Eisenhower","Ike"]),
 ("presidency-john-f-kennedy","Presidency of John F. Kennedy",1961,1963,"Thirty-fifth president; faced the Bay of Pigs and Cuban Missile Crisis, launched the Moon programme and was assassinated in Dallas.",["John F. Kennedy","JFK"]),
 ("presidency-lyndon-b-johnson","Presidency of Lyndon B. Johnson",1963,1969,"Thirty-sixth president; passed the Civil Rights and Voting Rights Acts and the Great Society, but was undone by the Vietnam War.",["Lyndon B. Johnson","LBJ"]),
 ("presidency-richard-nixon","Presidency of Richard Nixon",1969,1974,"Thirty-seventh president; opened relations with China, pursued detente and withdrew from Vietnam before resigning over Watergate.",["Richard Nixon","Richard Milhous Nixon"]),
 ("presidency-gerald-ford","Presidency of Gerald Ford",1974,1977,"Thirty-eighth president and the only one never elected to either national office; pardoned Nixon and battled inflation and recession.",["Gerald Ford","Gerald R. Ford"]),
 ("presidency-jimmy-carter","Presidency of Jimmy Carter",1977,1981,"Thirty-ninth president; brokered the Camp David Accords but was hampered by stagflation, the energy crisis and the Iran hostage crisis.",["Jimmy Carter","James Earl Carter"]),
 ("presidency-ronald-reagan","Presidency of Ronald Reagan",1981,1989,"Fortieth president; cut taxes, expanded the military, weathered the Iran-Contra affair and negotiated arms reductions with Gorbachev.",["Ronald Reagan"]),
 ("presidency-george-h-w-bush","Presidency of George H. W. Bush",1989,1993,"Forty-first president; managed the end of the Cold War and German reunification and led the coalition that won the Gulf War.",["George H. W. Bush","George Bush Sr."]),
 ("presidency-bill-clinton","Presidency of Bill Clinton",1993,2001,"Forty-second president; presided over budget surpluses, NAFTA and welfare reform, and was impeached and acquitted in 1998-99.",["Bill Clinton","William Jefferson Clinton"]),
 ("presidency-george-w-bush","Presidency of George W. Bush",2001,2009,"Forty-third president; responded to the September 11 attacks with the wars in Afghanistan and Iraq, and left office amid the financial crisis.",["George W. Bush","George Bush Jr."]),
 ("presidency-barack-obama","Presidency of Barack Obama",2009,2017,"Forty-fourth president and first African American president; enacted the Affordable Care Act and stimulus recovery and normalised relations with Cuba.",["Barack Obama"]),
 ("presidency-donald-trump-first","First Presidency of Donald Trump",2017,2021,"Forty-fifth president; cut taxes, reshaped the judiciary, was impeached twice and managed the initial COVID-19 response.",["Donald Trump first term"]),
 ("presidency-joe-biden","Presidency of Joe Biden",2021,2025,"Forty-sixth president; passed infrastructure and climate legislation, withdrew from Afghanistan and backed Ukraine against Russia.",["Joe Biden","Joseph R. Biden"]),
 ("presidency-donald-trump-second","Second Presidency of Donald Trump",2025,None,"Forty-seventh president; returned to office in 2025 after a non-consecutive gap, pursuing tariffs, immigration enforcement and federal restructuring.",["Donald Trump second term"]),
]
for slug, name, sy, ey, summ, al in pres:
    add(slug, name, "reign", sy, ey, US, summ, al, extant=(ey is None))

# ---------------- WARS AND CONFLICTS ----------------
wars = [
 ("american-revolutionary-war","American Revolutionary War","event",1775,1783,US,"War of independence in which the thirteen colonies, aided by France, defeated Britain; ended by the Treaty of Paris recognising US sovereignty.",["American Revolution","War of Independence","Revolutionary War"]),
 ("american-revolution","American Revolution","era",1765,1789,US,"Political revolution from the Stamp Act crisis through independence and the framing of the Constitution.",["Revolutionary era"]),
 ("northwest-indian-war","Northwest Indian War","event",1785,1795,US,"Conflict between the United States and a confederacy of Ohio Country nations, ended by Fallen Timbers and the Treaty of Greenville.",["Little Turtle's War","Ohio War"]),
 ("whiskey-rebellion","Whiskey Rebellion","event",1791,1794,US,"Armed tax revolt by western Pennsylvania distillers, suppressed by a federalised militia led personally by President Washington.",[]),
 ("quasi-war","Quasi-War","event",1798,1800,US,"Undeclared naval war with revolutionary France in the Caribbean, ended by the Convention of 1800.",["Franco-American War"]),
 ("first-barbary-war","First Barbary War","event",1801,1805,US,"US naval campaign against Tripoli and other Barbary states over tribute demands and captured sailors.",["Tripolitan War"]),
 ("second-barbary-war","Second Barbary War","event",1815,1815,US,"Short US naval expedition under Decatur that ended Algerine attacks on American shipping.",["Algerine War"]),
 ("war-of-1812","War of 1812","event",1812,1815,US,"War with Britain over impressment, trade restrictions and western expansion; included the burning of Washington and Jackson's victory at New Orleans.",["Second War of Independence"]),
 ("creek-war","Creek War","event",1813,1814,US,"War against the Red Stick Creeks in Alabama, won by Andrew Jackson at Horseshoe Bend and ending in massive land cessions.",["Red Stick War"]),
 ("first-seminole-war","First Seminole War","event",1817,1818,US,"Jackson's invasion of Spanish Florida against Seminoles and maroons, which precipitated the US acquisition of Florida.",[]),
 ("black-hawk-war","Black Hawk War","event",1832,1832,US,"Brief war in Illinois and Wisconsin against Sauk and Meskwaki led by Black Hawk, ending at Bad Axe.",[]),
 ("second-seminole-war","Second Seminole War","event",1835,1842,US,"Longest and costliest of the Indian removal wars, fought in Florida swamps against Seminoles under Osceola.",["Florida War"]),
 ("texas-revolution","Texas Revolution","event",1835,1836,NA,"Anglo-Texan and Tejano revolt against Mexico, marked by the Alamo and Goliad and won at San Jacinto.",["Texian War of Independence"]),
 ("mexican-american-war","Mexican-American War","event",1846,1848,US,"War with Mexico that ended in the Treaty of Guadalupe Hidalgo, transferring California and the Southwest to the United States.",["Mexican War","US-Mexican War"]),
 ("bleeding-kansas","Bleeding Kansas","event",1854,1859,US,"Guerrilla warfare between proslavery and free-state settlers over Kansas's status, a prelude to civil war.",["Border War","Kansas conflict"]),
 ("utah-war","Utah War","event",1857,1858,US,"Largely bloodless confrontation between the federal government and Mormon settlers in Utah Territory.",["Mormon War"]),
 ("third-seminole-war","Third Seminole War","event",1855,1858,US,"Final campaign to expel remaining Seminoles from Florida.",[]),
 ("american-civil-war","American Civil War","event",1861,1865,US,"War between the Union and eleven seceding slave states, the deadliest in US history, ending slavery and preserving the Union.",["Civil War","War Between the States","War of the Rebellion"]),
 ("dakota-war-1862","Dakota War of 1862","event",1862,1862,US,"Uprising of Dakota Sioux in Minnesota, followed by the largest mass execution in US history at Mankato.",["Sioux Uprising","Little Crow's War"]),
 ("red-cloud-war","Red Cloud's War","event",1866,1868,US,"Lakota, Cheyenne and Arapaho campaign against forts on the Bozeman Trail, won at the Treaty of Fort Laramie.",["Bozeman War","Powder River War"]),
 ("red-river-war","Red River War","event",1874,1875,US,"Army campaign that broke Comanche, Kiowa and Southern Cheyenne resistance on the southern Plains.",[]),
 ("great-sioux-war","Great Sioux War of 1876","event",1876,1877,US,"War over the Black Hills including the Lakota-Cheyenne victory at Little Bighorn and subsequent US reconquest.",["Black Hills War","Little Bighorn campaign"]),
 ("nez-perce-war","Nez Perce War","event",1877,1877,US,"Fighting retreat of Chief Joseph's band across 1,170 miles toward Canada before surrender in the Bear Paw Mountains.",["Chief Joseph's War"]),
 ("apache-wars","Apache Wars","event",1849,1886,US,"Decades of conflict in the Southwest with Chiricahua and other Apache bands, ending with Geronimo's surrender.",["Geronimo campaign"]),
 ("american-indian-wars","American Indian Wars","era",1622,1924,US,"Four centuries of warfare between Euro-American colonists and later the United States and Indigenous nations across the continent.",["Indian Wars","Native American wars"]),
 ("wounded-knee-massacre","Wounded Knee Massacre","event",1890,1890,US,"US cavalry killed roughly 250-300 Lakota, mostly noncombatants, at Wounded Knee Creek, conventionally closing the Indian Wars.",["Wounded Knee"]),
 ("spanish-american-war","Spanish-American War","event",1898,1898,US,"Brief war that expelled Spain from Cuba and gave the United States Puerto Rico, Guam and the Philippines.",["War of 1898"]),
 ("philippine-american-war","Philippine-American War","event",1899,1902,US,"Brutal counterinsurgency against the Philippine Republic following US annexation of the islands.",["Philippine Insurrection"]),
 ("boxer-rebellion-us","Boxer Rebellion Intervention","event",1900,1901,US,"US participation in the eight-nation expedition that relieved the Beijing legations during the Boxer uprising.",["China Relief Expedition"]),
 ("banana-wars","Banana Wars","era",1898,1934,US,"Series of US military interventions and occupations in Central America and the Caribbean protecting commercial and strategic interests.",["Caribbean interventions"]),
 ("occupation-of-haiti","US Occupation of Haiti","event",1915,1934,US,"Nineteen-year Marine occupation of Haiti that reorganised its finances and provoked the Caco rebellion.",[]),
 ("pancho-villa-expedition","Pancho Villa Expedition","event",1916,1917,US,"Punitive expedition led by John J. Pershing into Mexico after Villa's raid on Columbus, New Mexico.",["Mexican Punitive Expedition"]),
 ("world-war-i-us","World War I (United States)","event",1917,1918,US,"US entry into the Great War, sending two million troops of the AEF to France and turning the Western Front against Germany.",["Great War","First World War"]),
 ("world-war-ii-us","World War II (United States)","event",1941,1945,US,"US involvement from Pearl Harbor to the surrender of Japan, fighting in Europe, North Africa and the Pacific and developing the atomic bomb.",["Second World War","WWII"]),
 ("korean-war","Korean War","event",1950,1953,US,"US-led UN intervention to repel North Korea's invasion of the South, ending in an armistice near the 38th parallel.",["Forgotten War"]),
 ("vietnam-war-us","Vietnam War (United States)","event",1955,1975,US,"Long US intervention against communist forces in Vietnam, escalating after 1964 and ending with withdrawal in 1973 and Saigon's fall in 1975.",["Second Indochina War","Vietnam conflict"]),
 ("bay-of-pigs","Bay of Pigs Invasion","event",1961,1961,US,"Failed CIA-sponsored landing of Cuban exiles intended to topple Fidel Castro.",["Playa Giron"]),
 ("cuban-missile-crisis","Cuban Missile Crisis","event",1962,1962,US,"Thirteen-day nuclear standoff over Soviet missiles in Cuba, resolved by a blockade and secret missile withdrawals.",["October Crisis"]),
 ("dominican-intervention-1965","Dominican Republic Intervention","event",1965,1966,US,"US military intervention in the Dominican civil war, sending over 20,000 troops to prevent a feared communist takeover.",["Operation Power Pack"]),
 ("invasion-of-grenada","Invasion of Grenada","event",1983,1983,US,"US-led invasion that removed the revolutionary government of Grenada after a coup.",["Operation Urgent Fury"]),
 ("invasion-of-panama","Invasion of Panama","event",1989,1990,US,"US invasion that ousted and captured Manuel Noriega.",["Operation Just Cause"]),
 ("gulf-war","Gulf War","event",1990,1991,US,"US-led coalition war that expelled Iraqi forces from Kuwait through Operations Desert Shield and Desert Storm.",["Persian Gulf War","Operation Desert Storm","First Iraq War"]),
 ("somalia-intervention","Somalia Intervention","event",1992,1994,US,"US humanitarian and military mission in Somalia that ended after the Battle of Mogadishu.",["Operation Restore Hope","Black Hawk Down"]),
 ("kosovo-war-us","Kosovo Intervention","event",1999,1999,US,"NATO air campaign led by the United States against Yugoslavia over the expulsion of Kosovar Albanians.",["Operation Allied Force"]),
 ("september-11-attacks","September 11 Attacks","event",2001,2001,US,"Al-Qaeda hijackers destroyed the World Trade Center and struck the Pentagon, killing nearly 3,000 people and reshaping US policy.",["9/11","World Trade Center attacks"]),
 ("war-in-afghanistan","War in Afghanistan","event",2001,2021,US,"America's longest war, begun to destroy al-Qaeda and topple the Taliban and ended by the 2021 withdrawal and Taliban return.",["Afghan War","Operation Enduring Freedom"]),
 ("iraq-war","Iraq War","event",2003,2011,US,"US-led invasion that toppled Saddam Hussein, followed by insurgency, sectarian civil war and the 2007 surge.",["Second Gulf War","Operation Iraqi Freedom"]),
 ("war-against-isis","Intervention against ISIS","event",2014,2019,US,"US-led coalition campaign of airstrikes and advisers that destroyed the Islamic State's territorial caliphate in Iraq and Syria.",["Operation Inherent Resolve"]),
]
for slug, name, kind, sy, ey, parent, summ, al in wars:
    add(slug, name, kind, sy, ey, parent, summ, al)

# ---------------- CIVIL WAR CAMPAIGNS AND MAJOR BATTLES ----------------
battles = [
 ("battles-of-lexington-and-concord","Battles of Lexington and Concord",1775,1775,"american-revolutionary-war","First shots of the Revolutionary War, as Massachusetts militia turned back British regulars sent to seize colonial arms.",["shot heard round the world"]),
 ("battle-of-bunker-hill","Battle of Bunker Hill",1775,1775,"american-revolutionary-war","Costly British victory on the Charlestown heights outside Boston that showed colonial militia could stand against regulars.",[]),
 ("battles-of-saratoga","Battles of Saratoga",1777,1777,"american-revolutionary-war","Decisive American victory that destroyed Burgoyne's army and brought France into the war as an ally.",["Saratoga campaign"]),
 ("valley-forge","Valley Forge Encampment",1777,1778,"american-revolutionary-war","Winter camp where Washington's army endured privation and was retrained under von Steuben.",[]),
 ("siege-of-yorktown","Siege of Yorktown",1781,1781,"american-revolutionary-war","Franco-American siege that forced Cornwallis's surrender and effectively ended the Revolutionary War.",["Battle of Yorktown"]),
 ("battle-of-tippecanoe","Battle of Tippecanoe",1811,1811,"war-of-1812","Harrison's attack on Prophetstown that broke Tenskwatawa's confederacy and helped precipitate the War of 1812.",[]),
 ("burning-of-washington","Burning of Washington",1814,1814,"war-of-1812","British forces captured the capital and burned the Capitol and White House in retaliation for raids in Canada.",[]),
 ("battle-of-new-orleans","Battle of New Orleans",1815,1815,"war-of-1812","Jackson's lopsided victory over British regulars, fought after the peace treaty was signed, made him a national hero.",[]),
 ("battle-of-the-alamo","Battle of the Alamo",1836,1836,"texas-revolution","Thirteen-day siege in San Antonio in which Santa Anna's army killed the entire Texian garrison, creating a rallying cry.",["Siege of the Alamo"]),
 ("first-battle-of-bull-run","First Battle of Bull Run",1861,1861,"american-civil-war","First major land battle of the Civil War, a Confederate victory that shattered hopes of a quick Union win.",["First Manassas"]),
 ("battle-of-shiloh","Battle of Shiloh",1862,1862,"american-civil-war","Bloody two-day Union victory in Tennessee that revealed the war's likely cost.",["Battle of Pittsburg Landing"]),
 ("battle-of-antietam","Battle of Antietam",1862,1862,"american-civil-war","Bloodiest single day in American history; the strategic Union result let Lincoln issue the Emancipation Proclamation.",["Battle of Sharpsburg"]),
 ("battle-of-gettysburg","Battle of Gettysburg",1863,1863,"american-civil-war","Three-day Union victory in Pennsylvania that turned back Lee's second invasion of the North.",[]),
 ("siege-of-vicksburg","Siege of Vicksburg",1863,1863,"american-civil-war","Grant's siege that captured the last Confederate stronghold on the Mississippi, splitting the Confederacy.",["Vicksburg campaign"]),
 ("shermans-march-to-the-sea","Sherman's March to the Sea",1864,1864,"american-civil-war","Union campaign of destruction from Atlanta to Savannah intended to break southern will to fight.",["Savannah campaign"]),
 ("appomattox-surrender","Surrender at Appomattox",1865,1865,"american-civil-war","Lee's surrender to Grant at Appomattox Court House, effectively ending the Civil War.",["Appomattox Court House"]),
 ("battle-of-little-bighorn","Battle of the Little Bighorn",1876,1876,"great-sioux-war","Lakota, Cheyenne and Arapaho warriors annihilated Custer's detachment of the 7th Cavalry in Montana.",["Custer's Last Stand","Battle of the Greasy Grass"]),
 ("attack-on-pearl-harbor","Attack on Pearl Harbor",1941,1941,"world-war-ii-us","Japanese surprise attack on the Pacific Fleet in Hawaii that brought the United States into World War II.",["Pearl Harbor"]),
 ("battle-of-midway","Battle of Midway",1942,1942,"world-war-ii-us","Decisive US naval victory that destroyed four Japanese carriers and turned the Pacific war.",[]),
 ("normandy-landings","Normandy Landings",1944,1944,"world-war-ii-us","Allied amphibious invasion of German-occupied France, opening the Western Front in Europe.",["D-Day","Operation Overlord"]),
 ("battle-of-iwo-jima","Battle of Iwo Jima",1945,1945,"world-war-ii-us","Costly Marine assault on a fortified Japanese island, immortalised by the flag-raising on Mount Suribachi.",[]),
 ("atomic-bombings","Atomic Bombings of Hiroshima and Nagasaki",1945,1945,"world-war-ii-us","US atomic attacks that killed well over 100,000 people and preceded Japan's surrender.",["Hiroshima and Nagasaki"]),
 ("manhattan-project","Manhattan Project",1942,1946,"world-war-ii-us","Secret Allied programme led by the United States that built the first nuclear weapons at Los Alamos, Oak Ridge and Hanford.",[]),
 ("inchon-landing","Inchon Landing",1950,1950,"korean-war","MacArthur's amphibious envelopment that recaptured Seoul and reversed the North Korean advance.",["Operation Chromite"]),
 ("tet-offensive","Tet Offensive",1968,1968,"vietnam-war-us","Coordinated communist attacks across South Vietnam that were militarily repulsed but shattered US public confidence.",[]),
 ("fall-of-saigon","Fall of Saigon",1975,1975,"vietnam-war-us","North Vietnamese capture of Saigon and the chaotic US evacuation, ending the Vietnam War.",["Liberation of Saigon","Operation Frequent Wind"]),
]
for slug, name, sy, ey, parent, summ, al in battles:
    add(slug, name, "event", sy, ey, parent, summ, al)

# ---------------- FOUNDING AND CONSTITUTIONAL ----------------
found = [
 ("stamp-act-crisis","Stamp Act Crisis","event",1765,1766,US,"Colonial resistance to Parliament's direct tax on printed materials, producing the Stamp Act Congress and repeal.",["Stamp Act"]),
 ("boston-massacre","Boston Massacre","event",1770,1770,US,"British soldiers fired into a Boston crowd, killing five and giving Patriots a propaganda cause.",[]),
 ("boston-tea-party","Boston Tea Party","event",1773,1773,US,"Sons of Liberty dumped East India Company tea into Boston Harbor, provoking the Coercive Acts.",[]),
 ("intolerable-acts","Intolerable Acts","event",1774,1774,US,"Punitive British laws closing Boston's port and altering Massachusetts government, which united the colonies in resistance.",["Coercive Acts"]),
 ("first-continental-congress","First Continental Congress","event",1774,1774,US,"Twelve colonies met in Philadelphia to coordinate resistance to the Intolerable Acts through boycott and petition.",[]),
 ("declaration-of-independence","Declaration of Independence","event",1776,1776,US,"Continental Congress declared the thirteen colonies free of British rule in a document drafted chiefly by Thomas Jefferson.",["Declaration of July 4, 1776"]),
 ("treaty-of-paris-1783","Treaty of Paris (1783)","event",1783,1783,US,"Anglo-American peace treaty recognising US independence and setting borders to the Mississippi River.",[]),
 ("northwest-ordinance","Northwest Ordinance","event",1787,1787,US,"Confederation Congress law organising the Northwest Territory, banning slavery there and setting the process for admitting new states.",["Ordinance of 1787"]),
 ("shays-rebellion","Shays' Rebellion","event",1786,1787,US,"Debtor farmers' armed revolt in western Massachusetts that exposed the weakness of the Articles of Confederation.",[]),
 ("constitutional-convention","Constitutional Convention","event",1787,1787,US,"Philadelphia convention that drafted the US Constitution, resolving representation through the Great Compromise.",["Philadelphia Convention","Federal Convention"]),
 ("us-constitution","United States Constitution","event",1788,1788,US,"Supreme law of the United States, ratified in 1788 and effective in 1789, creating a federal government of three branches.",["the Constitution"]),
 ("federalist-papers","The Federalist Papers","event",1787,1788,US,"Eighty-five essays by Hamilton, Madison and Jay arguing for ratification of the Constitution.",["Federalist"]),
 ("bill-of-rights","Bill of Rights","event",1791,1791,US,"First ten amendments to the Constitution, guaranteeing speech, religion, arms, due process and other individual and state protections.",["first ten amendments"]),
 ("judiciary-act-1789","Judiciary Act of 1789","event",1789,1789,US,"Statute establishing the federal court system and the office of Attorney General.",[]),
 ("alien-and-sedition-acts","Alien and Sedition Acts","event",1798,1798,US,"Federalist laws restricting immigration and criminalising criticism of the government, provoking the Virginia and Kentucky Resolutions.",[]),
 ("louisiana-purchase","Louisiana Purchase","event",1803,1803,US,"Acquisition of 828,000 square miles from France for about $15 million, doubling the size of the United States.",["Louisiana Territory purchase"]),
 ("lewis-and-clark-expedition","Lewis and Clark Expedition","event",1804,1806,US,"Corps of Discovery's overland journey to the Pacific and back, mapping the Louisiana Purchase and beyond.",["Corps of Discovery"]),
 ("embargo-act","Embargo Act of 1807","event",1807,1809,US,"Jefferson's ban on American exports intended to coerce Britain and France, which devastated US commerce instead.",[]),
 ("adams-onis-treaty","Adams-Onis Treaty","event",1819,1819,US,"Treaty by which Spain ceded Florida to the United States and fixed the boundary of the Louisiana Purchase.",["Transcontinental Treaty","Florida Purchase"]),
 ("missouri-compromise","Missouri Compromise","event",1820,1820,US,"Congressional bargain admitting Missouri as a slave state and Maine as free, and barring slavery north of 36 degrees 30 minutes in the Louisiana Territory.",["Compromise of 1820"]),
 ("monroe-doctrine","Monroe Doctrine","event",1823,1823,US,"Declaration that the Americas were closed to further European colonisation, becoming a pillar of US foreign policy.",[]),
 ("indian-removal-act","Indian Removal Act","event",1830,1830,US,"Law authorising treaties to relocate eastern Indigenous nations west of the Mississippi, leading to forced removals.",[]),
 ("nullification-crisis","Nullification Crisis","event",1832,1833,US,"South Carolina's attempt to void federal tariffs, defused by Jackson's Force Bill and a compromise tariff.",[]),
 ("trail-of-tears","Trail of Tears","event",1830,1850,US,"Forced removals of Cherokee, Choctaw, Chickasaw, Creek and Seminole nations to Indian Territory, killing thousands en route.",["Cherokee removal"]),
 ("oregon-treaty","Oregon Treaty","event",1846,1846,US,"Anglo-American agreement dividing the Oregon Country at the 49th parallel.",["Oregon boundary settlement"]),
 ("treaty-of-guadalupe-hidalgo","Treaty of Guadalupe Hidalgo","event",1848,1848,US,"Treaty ending the Mexican-American War, ceding California, Nevada, Utah and more to the United States for $15 million.",["Mexican Cession"]),
 ("gadsden-purchase","Gadsden Purchase","event",1853,1854,US,"Purchase of southern Arizona and New Mexico land from Mexico for a southern railroad route.",["Treaty of La Mesilla"]),
 ("compromise-of-1850","Compromise of 1850","event",1850,1850,US,"Package of laws admitting California free, organising Utah and New Mexico by popular sovereignty and toughening the Fugitive Slave Act.",[]),
 ("kansas-nebraska-act","Kansas-Nebraska Act","event",1854,1854,US,"Law repealing the Missouri Compromise line in favour of popular sovereignty, igniting Bleeding Kansas and creating the Republican Party.",[]),
 ("john-browns-raid","John Brown's Raid on Harpers Ferry","event",1859,1859,US,"Abolitionist John Brown's failed attempt to spark a slave insurrection by seizing a federal armoury; his execution deepened sectional fear.",["Harpers Ferry raid"]),
 ("secession-winter","Secession Winter","event",1860,1861,US,"Departure of eleven southern states from the Union following Lincoln's election, culminating in the firing on Fort Sumter.",["Southern secession"]),
 ("emancipation-proclamation","Emancipation Proclamation","event",1863,1863,US,"Lincoln's executive order declaring enslaved people in rebel territory free and authorising Black enlistment in the Union army.",[]),
 ("homestead-act","Homestead Act","event",1862,1862,US,"Law granting 160 acres of public land to settlers who improved it for five years, accelerating western settlement.",[]),
 ("pacific-railway-acts","Pacific Railway Acts","event",1862,1864,US,"Laws chartering and subsidising the first transcontinental railroad, completed at Promontory Summit in 1869.",["transcontinental railroad legislation"]),
 ("thirteenth-amendment","Thirteenth Amendment","event",1865,1865,US,"Constitutional amendment abolishing slavery and involuntary servitude except as criminal punishment.",["abolition amendment"]),
 ("fourteenth-amendment","Fourteenth Amendment","event",1868,1868,US,"Amendment granting birthright citizenship and guaranteeing due process and equal protection against state action.",["equal protection amendment"]),
 ("fifteenth-amendment","Fifteenth Amendment","event",1870,1870,US,"Amendment barring denial of the vote on grounds of race, colour or previous condition of servitude.",[]),
 ("alaska-purchase","Alaska Purchase","event",1867,1867,US,"US purchase of Alaska from Russia for $7.2 million, derided at the time as 'Seward's Folly'.",["Seward's Folly"]),
 ("compromise-of-1877","Compromise of 1877","event",1877,1877,US,"Bargain resolving the disputed 1876 election by seating Hayes in exchange for ending federal Reconstruction.",["Bargain of 1877"]),
 ("chinese-exclusion-act","Chinese Exclusion Act","event",1882,1882,US,"First US law barring immigration by an entire nationality, prohibiting Chinese labourers for ten years and later extended.",[]),
 ("sherman-antitrust-act","Sherman Antitrust Act","event",1890,1890,US,"Landmark law outlawing monopolistic combinations and restraints of trade.",[]),
 ("interstate-commerce-act","Interstate Commerce Act","event",1887,1887,US,"First major federal regulation of private industry, creating the Interstate Commerce Commission to oversee railroads.",[]),
 ("sixteenth-amendment","Sixteenth Amendment","event",1913,1913,US,"Amendment authorising a federal income tax without apportionment among the states.",["income tax amendment"]),
 ("seventeenth-amendment","Seventeenth Amendment","event",1913,1913,US,"Amendment providing for direct popular election of United States senators.",[]),
 ("federal-reserve-act","Federal Reserve Act","event",1913,1913,US,"Law creating the Federal Reserve System as the nation's central bank.",[]),
 ("eighteenth-amendment","Eighteenth Amendment","event",1919,1919,US,"Amendment prohibiting the manufacture, sale and transport of intoxicating liquors, implemented by the Volstead Act.",["Prohibition amendment"]),
 ("nineteenth-amendment","Nineteenth Amendment","event",1920,1920,US,"Amendment guaranteeing women the right to vote after a seventy-year suffrage campaign.",["women's suffrage amendment"]),
 ("womens-suffrage-movement","Women's Suffrage Movement","period",1848,1920,US,"Campaign from Seneca Falls to the Nineteenth Amendment for women's voting rights, led by Stanton, Anthony, Catt and Paul.",["suffragist movement"]),
 ("indian-citizenship-act","Indian Citizenship Act","event",1924,1924,US,"Law conferring US citizenship on all Native Americans born within the country's territory.",["Snyder Act"]),
 ("immigration-act-1924","Immigration Act of 1924","event",1924,1924,US,"Law imposing national-origin quotas that sharply cut southern and eastern European immigration and barred most Asians.",["Johnson-Reed Act"]),
 ("twenty-first-amendment","Twenty-first Amendment","event",1933,1933,US,"Amendment repealing Prohibition, the only amendment to nullify a previous one.",["repeal amendment"]),
 ("social-security-act","Social Security Act","event",1935,1935,US,"New Deal law creating old-age pensions, unemployment insurance and aid to dependent children.",[]),
 ("wagner-act","National Labor Relations Act","event",1935,1935,US,"Law guaranteeing private-sector collective bargaining and creating the National Labor Relations Board.",["Wagner Act"]),
 ("gi-bill","GI Bill","event",1944,1944,US,"Law providing veterans with college tuition, job training, unemployment pay and subsidised home loans, expanding the middle class.",["Servicemen's Readjustment Act"]),
 ("marshall-plan","Marshall Plan","event",1948,1952,US,"US programme of roughly $13 billion in aid to rebuild western European economies and contain communism.",["European Recovery Program"]),
 ("truman-doctrine","Truman Doctrine","event",1947,1947,US,"Pledge to support free peoples resisting subjugation, beginning the containment policy with aid to Greece and Turkey.",[]),
 ("nato-founding","Founding of NATO","event",1949,1949,US,"US-led creation of the North Atlantic Treaty Organization as a collective defence alliance against the Soviet Union.",["North Atlantic Treaty"]),
 ("twenty-second-amendment","Twenty-second Amendment","event",1951,1951,US,"Amendment limiting presidents to two elected terms, a response to Franklin Roosevelt's four victories.",["term limits amendment"]),
 ("interstate-highway-act","Federal-Aid Highway Act of 1956","event",1956,1956,US,"Law funding the 41,000-mile Interstate Highway System, transforming American mobility and suburban growth.",["Interstate Highway Act"]),
 ("civil-rights-act-1964","Civil Rights Act of 1964","event",1964,1964,US,"Landmark law banning discrimination in public accommodations, employment and federally funded programmes.",[]),
 ("voting-rights-act","Voting Rights Act of 1965","event",1965,1965,US,"Law banning literacy tests and imposing federal oversight of elections in jurisdictions with histories of discrimination.",[]),
 ("twenty-fourth-amendment","Twenty-fourth Amendment","event",1964,1964,US,"Amendment abolishing poll taxes in federal elections.",[]),
 ("immigration-act-1965","Immigration and Nationality Act of 1965","event",1965,1965,US,"Law abolishing national-origin quotas and reshaping the sources of American immigration.",["Hart-Celler Act"]),
 ("medicare-medicaid","Creation of Medicare and Medicaid","event",1965,1965,US,"Great Society amendments to Social Security establishing federal health insurance for the elderly and poor.",["Social Security Amendments of 1965"]),
 ("fair-housing-act","Fair Housing Act","event",1968,1968,US,"Law prohibiting discrimination in the sale, rental and financing of housing, passed days after Martin Luther King Jr.'s assassination.",["Civil Rights Act of 1968"]),
 ("twenty-sixth-amendment","Twenty-sixth Amendment","event",1971,1971,US,"Amendment lowering the voting age to eighteen amid the Vietnam War draft.",[]),
 ("equal-rights-amendment","Equal Rights Amendment Campaign","period",1972,1982,US,"Congressional passage and ultimately failed state ratification drive for a constitutional guarantee of sex equality.",["ERA"]),
 ("nixon-china-visit","Nixon's Visit to China","event",1972,1972,US,"Nixon's week in Beijing that reopened US-Chinese relations after twenty-two years of estrangement.",["opening to China"]),
 ("camp-david-accords","Camp David Accords","event",1978,1978,US,"Carter-brokered framework leading to the Egypt-Israel peace treaty.",[]),
 ("iran-hostage-crisis","Iran Hostage Crisis","event",1979,1981,US,"Seizure of the US embassy in Tehran and 444-day detention of 52 Americans, which crippled Carter's presidency.",[]),
 ("iran-contra-affair","Iran-Contra Affair","event",1985,1987,US,"Scandal over secret US arms sales to Iran with proceeds diverted to Nicaraguan Contras in defiance of a congressional ban.",["Irangate"]),
 ("americans-with-disabilities-act","Americans with Disabilities Act","event",1990,1990,US,"Law barring discrimination against disabled people and mandating accessibility in employment and public life.",["ADA"]),
 ("nafta","North American Free Trade Agreement","event",1994,1994,US,"Trade pact eliminating most tariffs among the United States, Canada and Mexico; replaced by the USMCA in 2020.",["NAFTA"]),
 ("usa-patriot-act","USA PATRIOT Act","event",2001,2001,US,"Post-9/11 law greatly expanding federal surveillance, detention and financial-tracking powers.",["Patriot Act"]),
 ("affordable-care-act","Affordable Care Act","event",2010,2010,US,"Health reform law expanding insurance coverage through exchanges, subsidies, Medicaid expansion and pre-existing condition protections.",["Obamacare","ACA"]),
]
for slug, name, kind, sy, ey, parent, summ, al in found:
    add(slug, name, kind, sy, ey, parent, summ, al)

# ---------------- SUPREME COURT ----------------
cases = [
 ("marbury-v-madison","Marbury v. Madison",1803,"Chief Justice Marshall's ruling establishing judicial review, the Court's power to strike down unconstitutional laws.",[]),
 ("mcculloch-v-maryland","McCulloch v. Maryland",1819,"Upheld the constitutionality of the national bank and broad implied federal powers while barring state taxation of federal institutions.",[]),
 ("gibbons-v-ogden","Gibbons v. Ogden",1824,"Established broad federal authority over interstate commerce, striking down a New York steamboat monopoly.",[]),
 ("cherokee-nation-v-georgia","Cherokee Nation v. Georgia",1831,"Held the Cherokee were a 'domestic dependent nation' lacking standing to sue Georgia in the Supreme Court.",["Cherokee Nation v. State of Georgia"]),
 ("worcester-v-georgia","Worcester v. Georgia",1832,"Ruled Georgia law had no force in Cherokee territory, a decision the Jackson administration declined to enforce.",[]),
 ("dred-scott-v-sandford","Dred Scott v. Sandford",1857,"Held Black Americans could not be citizens and that Congress could not bar slavery in the territories, inflaming the sectional crisis.",["Dred Scott decision"]),
 ("ex-parte-milligan","Ex parte Milligan",1866,"Held that military tribunals cannot try civilians where civil courts are open, limiting wartime executive power.",[]),
 ("civil-rights-cases","Civil Rights Cases",1883,"Struck down the Civil Rights Act of 1875, holding the Fourteenth Amendment did not reach private discrimination.",[]),
 ("plessy-v-ferguson","Plessy v. Ferguson",1896,"Upheld 'separate but equal' racial segregation, constitutional cover for Jim Crow for fifty-eight years.",[]),
 ("lochner-v-new-york","Lochner v. New York",1905,"Struck down maximum-hours legislation on freedom-of-contract grounds, defining an era of judicial resistance to regulation.",[]),
 ("schenck-v-united-states","Schenck v. United States",1919,"Upheld Espionage Act convictions and introduced the 'clear and present danger' test for speech.",[]),
 ("korematsu-v-united-states","Korematsu v. United States",1944,"Upheld the wartime exclusion of Japanese Americans from the West Coast; repudiated by the Court in 2018.",[]),
 ("brown-v-board-of-education","Brown v. Board of Education",1954,"Unanimously held racially segregated public schools unconstitutional, overturning Plessy and catalysing the civil rights movement.",["Brown v. Board"]),
 ("mapp-v-ohio","Mapp v. Ohio",1961,"Applied the exclusionary rule for illegally seized evidence to state criminal prosecutions.",[]),
 ("gideon-v-wainwright","Gideon v. Wainwright",1963,"Guaranteed appointed counsel to indigent defendants in state felony cases.",[]),
 ("miranda-v-arizona","Miranda v. Arizona",1966,"Required police to warn suspects of their rights to silence and counsel before custodial interrogation.",["Miranda warning case"]),
 ("loving-v-virginia","Loving v. Virginia",1967,"Struck down state bans on interracial marriage as violations of equal protection and due process.",[]),
 ("roe-v-wade","Roe v. Wade",1973,"Recognised a constitutional right to abortion; overruled in 2022 by Dobbs v. Jackson Women's Health Organization.",[]),
 ("united-states-v-nixon","United States v. Nixon",1974,"Held that executive privilege does not shield evidence in a criminal case, forcing release of the Watergate tapes.",[]),
 ("regents-v-bakke","Regents of the University of California v. Bakke",1978,"Barred racial quotas in university admissions while permitting race as one factor in pursuing diversity.",["Bakke"]),
 ("bush-v-gore","Bush v. Gore",2000,"Halted the Florida recount, effectively deciding the 2000 presidential election for George W. Bush.",[]),
 ("citizens-united","Citizens United v. FEC",2010,"Held that corporate and union independent political spending is protected speech, reshaping campaign finance.",["Citizens United"]),
 ("obergefell-v-hodges","Obergefell v. Hodges",2015,"Held that same-sex couples have a constitutional right to marry nationwide.",[]),
 ("dobbs-v-jackson","Dobbs v. Jackson Women's Health Organization",2022,"Overruled Roe v. Wade, returning abortion regulation to the states.",["Dobbs"]),
]
for slug, name, yr, summ, al in cases:
    add(slug, name, "event", yr, yr, "United States Supreme Court", summ, al)

# ---------------- COLONIAL PERIOD ----------------
colonial = [
 ("roanoke-colony","Roanoke Colony","polity",1585,1590,COL,"Failed English settlement off North Carolina whose second group of colonists vanished, remembered as the Lost Colony.",["Lost Colony"]),
 ("jamestown","Jamestown","event",1607,1699,COL,"First permanent English settlement in North America, on the James River in Virginia; survived starvation to become the tobacco colony's capital.",["Jamestowne","James Fort"]),
 ("plymouth-colony","Plymouth Colony","polity",1620,1691,COL,"Separatist Pilgrim colony founded after the Mayflower voyage and governed by the Mayflower Compact; merged into Massachusetts in 1691.",["Plymouth","New Plymouth","Pilgrim colony"]),
 ("mayflower-compact","Mayflower Compact","event",1620,1620,COL,"Self-government agreement signed by Mayflower passengers before landing, an early instance of consent-based colonial rule.",[]),
 ("massachusetts-bay-colony","Massachusetts Bay Colony","polity",1630,1691,COL,"Puritan colony centred on Boston founded during the Great Migration, notable for congregational churches and Harvard College.",["Massachusetts Bay"]),
 ("province-of-massachusetts-bay","Province of Massachusetts Bay","polity",1691,1776,COL,"Royal province combining Massachusetts Bay, Plymouth and Maine; the epicentre of revolutionary resistance.",["Massachusetts colony"]),
 ("colony-of-virginia","Colony of Virginia","polity",1607,1776,COL,"Oldest of the thirteen colonies, built on tobacco, enslaved labour and the House of Burgesses.",["Virginia colony","Dominion of Virginia"]),
 ("province-of-new-hampshire","Province of New Hampshire","polity",1623,1776,COL,"Northern New England colony of fishing, timber and shipbuilding, long entangled with Massachusetts.",["New Hampshire colony"]),
 ("colony-of-rhode-island","Colony of Rhode Island and Providence Plantations","polity",1636,1776,COL,"Colony founded by Roger Williams on religious liberty and separation of church and state.",["Rhode Island colony"]),
 ("connecticut-colony","Connecticut Colony","polity",1636,1776,COL,"Puritan colony governed under the Fundamental Orders, one of the earliest written constitutions in the colonies.",["Connecticut"]),
 ("new-haven-colony","New Haven Colony","polity",1638,1665,COL,"Strict Puritan colony on Long Island Sound, absorbed into Connecticut in 1665.",[]),
 ("province-of-maryland","Province of Maryland","polity",1632,1776,COL,"Proprietary colony granted to the Calverts as a Catholic refuge, home of the 1649 Act of Toleration.",["Maryland colony"]),
 ("province-of-new-york","Province of New York","polity",1664,1776,COL,"Former New Netherland granted to the Duke of York, a diverse commercial colony centred on New York City.",["New York colony"]),
 ("province-of-new-jersey","Province of New Jersey","polity",1664,1776,COL,"Colony divided into East and West Jersey before reuniting as a royal province in 1702.",["New Jersey colony"]),
 ("province-of-pennsylvania","Province of Pennsylvania","polity",1681,1776,COL,"Quaker colony founded by William Penn on religious tolerance and fair dealing with the Lenape; Philadelphia became the largest colonial city.",["Pennsylvania colony","Penn's Woods"]),
 ("delaware-colony","Delaware Colony","polity",1664,1776,COL,"Lower counties on the Delaware, held under Penn's proprietorship with a separate assembly from 1704.",["Lower Counties on the Delaware"]),
 ("province-of-north-carolina","Province of North Carolina","polity",1712,1776,COL,"Southern colony of small farms, naval stores and backcountry settlement, split from Carolina in 1712.",["North Carolina colony"]),
 ("province-of-south-carolina","Province of South Carolina","polity",1712,1776,COL,"Rice and indigo colony with a Black majority population, centred on Charles Town.",["South Carolina colony"]),
 ("province-of-carolina","Province of Carolina","polity",1663,1712,COL,"Original proprietary grant covering the later Carolinas, governed under the Fundamental Constitutions.",["Carolina colony"]),
 ("province-of-georgia","Province of Georgia","polity",1732,1776,COL,"Last of the thirteen colonies, founded by Oglethorpe as a debtors' refuge and military buffer against Spanish Florida.",["Georgia colony"]),
 ("thirteen-colonies","Thirteen Colonies","polity",1607,1776,COL,"The British colonies on the Atlantic seaboard from New Hampshire to Georgia that united to form the United States.",["Original Thirteen","Thirteen British colonies"]),
 ("dominion-of-new-england","Dominion of New England","polity",1686,1689,COL,"Short-lived consolidation of the northern colonies under Governor Andros, overthrown after England's Glorious Revolution.",[]),
 ("house-of-burgesses","House of Burgesses","polity",1619,1776,COL,"First elected legislative assembly in English America, meeting in Virginia.",["Virginia General Assembly"]),
 ("first-africans-virginia-1619","Arrival of the First Africans in Virginia","event",1619,1619,COL,"About twenty captive Africans were sold at Point Comfort, beginning African bondage in English North America.",["1619"]),
 ("bacons-rebellion","Bacon's Rebellion","event",1676,1676,COL,"Backcountry uprising in Virginia against Governor Berkeley and Indigenous neighbours, which hastened the shift to racialised slavery.",[]),
 ("pequot-war","Pequot War","event",1636,1638,COL,"War in Connecticut in which English colonists and allies destroyed the Pequot, including the Mystic massacre.",[]),
 ("king-philips-war","King Philip's War","event",1675,1678,COL,"Devastating war between New England colonists and Wampanoag, Narragansett and Nipmuc forces under Metacom.",["Metacom's War","Metacom's Rebellion"]),
 ("king-williams-war","King William's War","event",1688,1697,COL,"First of the intercolonial wars between English and French colonists and their Indigenous allies.",[]),
 ("queen-annes-war","Queen Anne's War","event",1702,1713,COL,"North American theatre of the War of the Spanish Succession, ending with British gains at Utrecht.",[]),
 ("king-georges-war","King George's War","event",1744,1748,COL,"North American theatre of the War of the Austrian Succession, including the capture and return of Louisbourg.",[]),
 ("french-and-indian-war","French and Indian War","event",1754,1763,COL,"North American theatre of the Seven Years' War in which Britain and its colonists conquered New France, ended by the Treaty of Paris.",["Seven Years' War in America"]),
 ("pontiacs-war","Pontiac's War","event",1763,1766,COL,"Pan-Indigenous uprising in the Great Lakes against British rule after the French defeat, prompting the Proclamation of 1763.",["Pontiac's Rebellion"]),
 ("proclamation-of-1763","Royal Proclamation of 1763","event",1763,1763,COL,"British order barring colonial settlement west of the Appalachians, a grievance for land-hungry colonists.",[]),
 ("salem-witch-trials","Salem Witch Trials","event",1692,1693,COL,"Mass witchcraft panic in Essex County, Massachusetts, that executed twenty people and imprisoned scores more.",["Salem witchcraft trials"]),
 ("first-great-awakening","First Great Awakening","period",1730,1755,COL,"Wave of evangelical revival led by Whitefield, Edwards and Tennent that reshaped colonial religion and undermined established churches.",["Great Awakening"]),
 ("second-great-awakening","Second Great Awakening","period",1790,1840,US,"Protestant revival movement of camp meetings and reform societies that fuelled abolition, temperance and women's activism.",[]),
 ("stono-rebellion","Stono Rebellion","event",1739,1739,COL,"Largest slave revolt in the British mainland colonies, in South Carolina, followed by a harsh Negro Act.",[]),
 ("colonial-slavery","Slavery in Colonial and Antebellum America","period",1619,1865,US,"Institution of chattel slavery in what became the United States, from the first Africans in Virginia to the Thirteenth Amendment.",["American slavery","chattel slavery"]),
 ("transatlantic-slave-trade-us","Transatlantic Slave Trade to North America","period",1619,1808,US,"Forced transport of enslaved Africans to the mainland colonies and the United States, banned by federal law in 1808.",["Middle Passage"]),
 ("abolitionist-movement","Abolitionist Movement","period",1830,1865,US,"Campaign to end American slavery led by figures such as Garrison, Douglass, Tubman and the Grimke sisters.",["abolitionism"]),
 ("underground-railroad","Underground Railroad","period",1810,1865,US,"Clandestine network of routes and safe houses helping enslaved people escape to free states and Canada.",[],),
 ("nat-turners-rebellion","Nat Turner's Rebellion","event",1831,1831,US,"Slave uprising in Southampton County, Virginia, that killed about sixty whites and triggered severe repression.",["Southampton Insurrection"]),
]
for row in colonial:
    slug, name, kind, sy, ey, parent, summ = row[0], row[1], row[2], row[3], row[4], row[5], row[6]
    al = row[7] if len(row) > 7 else []
    add(slug, name, kind, sy, ey, parent, summ, al)

# ---------------- INDIGENOUS ----------------
IND = "Indigenous North America"
indig = [
 ("paleo-indian-period","Paleo-Indian Period","culture",-15000,-8000,IND,"Earliest human occupation of the Americas, associated with big-game hunting and fluted-point traditions.",["Lithic stage"],"radiocarbon","medium"),
 ("clovis-culture","Clovis Culture","culture",-11050,-10800,IND,"Widespread early Paleo-Indian tradition identified by distinctive fluted spear points found across North America.",["Llano culture"],"radiocarbon","medium"),
 ("folsom-culture","Folsom Culture","culture",-10800,-10200,IND,"Paleo-Indian bison-hunting tradition of the Great Plains known for thin fluted points.",[],"radiocarbon","medium"),
 ("archaic-period-north-america","Archaic Period","culture",-8000,-1000,IND,"Long era of diversified foraging, regional adaptation and early plant domestication before widespread pottery and farming.",["Meso-Indian period"],"radiocarbon","medium"),
 ("poverty-point","Poverty Point Culture","culture",-1700,-1100,IND,"Late Archaic culture in Louisiana that built massive earthen ridges and mounds and traded exotic stone widely.",[],"radiocarbon","medium"),
 ("adena-culture","Adena Culture","culture",-800,100,IND,"Ohio Valley mound-building culture known for conical burial mounds and elaborate grave goods.",[],"radiocarbon","medium"),
 ("hopewell-culture","Hopewell Tradition","culture",-100,500,IND,"Woodland culture of the Ohio and Mississippi valleys famed for geometric earthworks and a continental exchange network.",["Hopewell exchange system"],"radiocarbon","medium"),
 ("mississippian-culture","Mississippian Culture","culture",800,1600,IND,"Maize-farming mound-building civilisation of the Mississippi valley and Southeast, organised in chiefdoms with plazas and platform mounds.",["Mississippian tradition","Mound Builders"],"radiocarbon","high"),
 ("cahokia","Cahokia","polity",1050,1350,"mississippian-culture","Largest pre-Columbian city north of Mexico, near modern St. Louis, with Monks Mound and perhaps 15,000-20,000 residents at its height.",["Cahokia Mounds"],"radiocarbon","high"),
 ("moundville","Moundville","polity",1120,1500,"mississippian-culture","Major Mississippian centre on the Black Warrior River in Alabama with twenty-nine mounds around a plaza.",[],"radiocarbon","medium"),
 ("etowah","Etowah","polity",1000,1550,"mississippian-culture","Mississippian mound centre in northwest Georgia known for elite copper plates and marble statuary.",["Etowah Indian Mounds"],"radiocarbon","medium"),
 ("spiro-mounds","Spiro Mounds","polity",800,1450,"mississippian-culture","Caddoan Mississippian ceremonial centre in eastern Oklahoma, source of extraordinary craft and shell artefacts.",["Spiro"],"radiocarbon","medium"),
 ("natchez-people","Natchez","people",700,1731,IND,"Last major Mississippian-descended chiefdom, ruled by the Great Sun on the lower Mississippi, dispersed by the French after 1729.",["Natchez Nation"],"calendar","high"),
 ("hohokam","Hohokam","culture",300,1450,IND,"Southwestern culture of the Sonoran Desert notable for extensive irrigation canals, ballcourts and platform mounds.",[],"radiocarbon","high"),
 ("mogollon","Mogollon Culture","culture",200,1450,IND,"Southwestern culture of southern New Mexico and Arizona, including the Mimbres tradition's painted pottery.",["Mimbres"],"radiocarbon","medium"),
 ("ancestral-puebloans","Ancestral Puebloans","culture",100,1300,IND,"Farming culture of the Four Corners known for great houses, cliff dwellings and Chaco Canyon's regional system.",["Anasazi","Ancestral Pueblo"],"radiocarbon","high"),
 ("chaco-canyon","Chaco Canyon","polity",850,1150,"ancestral-puebloans","Ancestral Puebloan ceremonial and political centre in New Mexico with monumental great houses and a road network.",["Chaco Culture","Chacoan system"],"dendrochronology","high"),
 ("mesa-verde","Mesa Verde","polity",600,1300,"ancestral-puebloans","Ancestral Puebloan settlement region in Colorado famous for large cliff dwellings such as Cliff Palace.",[],"dendrochronology","high"),
 ("pueblo-peoples","Pueblo Peoples","people",1300,None,IND,"Southwestern agricultural nations of New Mexico and Arizona, including Hopi, Zuni, Acoma, Taos and the Rio Grande pueblos, continuing today.",["Puebloans","Pueblo Nations"],"calendar","high"),
 ("hopi","Hopi","people",1150,None,"pueblo-peoples","Pueblo nation of northern Arizona with continuously inhabited villages including Oraibi, one of the oldest settlements in North America.",["Hopi Tribe","Moqui"],"calendar","high"),
 ("zuni","Zuni","people",1250,None,"pueblo-peoples","Pueblo nation of western New Mexico with a distinct language, targeted by Coronado's 1540 expedition.",["A:shiwi","Zuni Pueblo"],"calendar","high"),
 ("acoma-pueblo","Acoma Pueblo","people",1150,None,"pueblo-peoples","Mesa-top Pueblo community in New Mexico, among the oldest continuously inhabited places in the United States.",["Sky City"],"calendar","high"),
 ("pueblo-revolt","Pueblo Revolt","event",1680,1692,"pueblo-peoples","Coordinated uprising led by Pope that expelled the Spanish from New Mexico for twelve years.",["Pope's Rebellion"],"calendar","high"),
 ("iroquois-confederacy","Iroquois Confederacy","polity",1450,None,IND,"Confederation of Mohawk, Oneida, Onondaga, Cayuga and Seneca (joined by Tuscarora in 1722) governed by the Great Law of Peace; still active today.",["Haudenosaunee","Six Nations","Five Nations","League of the Iroquois"],"calendar","high"),
 ("mohawk-nation","Mohawk Nation","people",1450,None,"iroquois-confederacy","Easternmost Haudenosaunee nation, 'keepers of the eastern door', in the Mohawk Valley and later Quebec and Ontario.",["Kanien'keha:ka"],"calendar","high"),
 ("oneida-nation","Oneida Nation","people",1450,None,"iroquois-confederacy","Haudenosaunee nation of central New York that largely sided with the Americans in the Revolution.",["Onyota'a:ka"],"calendar","high"),
 ("onondaga-nation","Onondaga Nation","people",1450,None,"iroquois-confederacy","Haudenosaunee nation that hosts the Grand Council fire as the confederacy's capital.",["Onondowaga"],"calendar","high"),
 ("cayuga-nation","Cayuga Nation","people",1450,None,"iroquois-confederacy","Haudenosaunee nation of the Finger Lakes region of New York.",["Gayogohono"],"calendar","high"),
 ("seneca-nation","Seneca Nation","people",1450,None,"iroquois-confederacy","Largest Haudenosaunee nation, 'keepers of the western door', in western New York.",["Onondowahgah"],"calendar","high"),
 ("tuscarora-nation","Tuscarora Nation","people",1600,None,"iroquois-confederacy","Iroquoian nation originally of North Carolina that migrated north and became the sixth nation of the confederacy in 1722.",["Skarureh"],"calendar","high"),
 ("beaver-wars","Beaver Wars","event",1609,1701,"iroquois-confederacy","Prolonged Iroquois campaigns for control of the fur trade that shattered Huron, Erie and other nations in the Great Lakes.",["French and Iroquois Wars"],"calendar","high"),
 ("huron-wendat","Wendat Confederacy","polity",1440,1650,IND,"Iroquoian confederacy of the Great Lakes, dispersed by Iroquois attacks and epidemics in 1649-50.",["Huron","Wyandot"],"calendar","high"),
 ("powhatan-confederacy","Powhatan Confederacy","polity",1570,1677,IND,"Paramount chiefdom of about thirty Algonquian-speaking groups in Tidewater Virginia under Wahunsenacawh, which fought and then fell to the Jamestown colony.",["Powhatan","Tsenacommacah","Powhatan Paramount Chiefdom"],"calendar","high"),
 ("anglo-powhatan-wars","Anglo-Powhatan Wars","event",1610,1646,"powhatan-confederacy","Three wars between Virginia colonists and the Powhatan that ended Powhatan independence and confined survivors to reservations.",["Powhatan Wars"],"calendar","high"),
 ("wampanoag","Wampanoag","people",1400,None,IND,"Algonquian nation of southeastern Massachusetts and Rhode Island who met the Pilgrims and later fought King Philip's War; federally recognised today.",["Pokanoket","Mashpee Wampanoag"],"calendar","high"),
 ("narragansett","Narragansett","people",1400,None,IND,"Algonquian nation of Rhode Island, devastated in King Philip's War and federally recognised in 1983.",["Narragansett Indian Tribe"],"calendar","high"),
 ("pequot","Pequot","people",1500,None,IND,"Algonquian nation of southeastern Connecticut nearly destroyed in the Pequot War; the Mashantucket Pequot survive today.",["Mashantucket Pequot"],"calendar","high"),
 ("lenape","Lenape","people",1400,None,IND,"Algonquian nation of the Delaware valley whose lands became New Jersey, Pennsylvania and New York, later removed to Oklahoma and Ontario.",["Delaware Nation","Lenni Lenape"],"calendar","high"),
 ("abenaki","Abenaki","people",1400,None,IND,"Algonquian nation of northern New England and Quebec, part of the Wabanaki Confederacy.",["Abnaki","Wabanaki"],"calendar","high"),
 ("mohegan","Mohegan","people",1600,None,IND,"Connecticut Algonquian nation that split from the Pequot under Uncas and is federally recognised today.",["Mohegan Tribe"],"calendar","high"),
 ("cherokee-nation","Cherokee Nation","polity",1500,None,IND,"Iroquoian-speaking southeastern nation that adopted a written constitution and Sequoyah's syllabary, was forcibly removed on the Trail of Tears, and today is the largest US tribal nation.",["Tsalagi","Aniyunwiya","Cherokee"],"calendar","high"),
 ("eastern-band-cherokee","Eastern Band of Cherokee Indians","people",1868,None,"cherokee-nation","Federally recognised Cherokee community in western North Carolina descended from those who avoided removal.",["Eastern Cherokee"],"calendar","high"),
 ("muscogee-creek","Muscogee (Creek) Nation","polity",1500,None,IND,"Southeastern confederacy of towns in Georgia and Alabama, removed to Indian Territory and now a large sovereign nation in Oklahoma.",["Creek Confederacy","Muscogee","Creek Nation"],"calendar","high"),
 ("choctaw-nation","Choctaw Nation","polity",1500,None,IND,"Muskogean nation of Mississippi, first removed under the 1830 Treaty of Dancing Rabbit Creek; sovereign today in southeastern Oklahoma.",["Chahta","Choctaw"],"calendar","high"),
 ("chickasaw-nation","Chickasaw Nation","polity",1500,None,IND,"Muskogean nation of northern Mississippi and western Tennessee, removed to Indian Territory and sovereign today.",["Chikasha","Chickasaw"],"calendar","high"),
 ("seminole-nation","Seminole Nation","polity",1750,None,IND,"Nation formed in Florida from Creek migrants, free and fugitive Black allies and remnant groups; fought three wars and survives in Oklahoma and Florida.",["Seminole Tribe of Florida","Seminole"],"calendar","high"),
 ("five-civilized-tribes","Five Tribes of Indian Territory","polity",1830,None,IND,"Cherokee, Choctaw, Chickasaw, Muscogee and Seminole nations relocated to Indian Territory, later reorganised as sovereign governments in Oklahoma.",["Five Civilized Tribes"],"calendar","high"),
 ("indian-territory","Indian Territory","polity",1834,1907,US,"Federal territory in present-day Oklahoma set aside for removed Indigenous nations, dissolved at Oklahoma statehood.",["Oklahoma Territory era"],"calendar","high"),
 ("lakota","Lakota","people",1700,None,IND,"Westernmost Sioux division of seven bands, dominant horse-and-bison power of the northern Plains and victors at Little Bighorn.",["Teton Sioux","Titunwan","Lakota Sioux"],"calendar","high"),
 ("great-sioux-nation","Great Sioux Nation","polity",1700,None,IND,"Oceti Sakowin, the Seven Council Fires uniting Lakota, Dakota and Nakota peoples across the northern Plains.",["Oceti Sakowin","Sioux Nation","Seven Council Fires"],"calendar","high"),
 ("dakota-people","Dakota","people",1600,None,"great-sioux-nation","Eastern Sioux peoples of Minnesota and the Dakotas, forced from Minnesota after the 1862 war.",["Santee Sioux","Eastern Dakota"],"calendar","high"),
 ("comanche-empire","Comanche Nation","polity",1700,None,IND,"Equestrian power that dominated the southern Plains from the 18th century, checking Spanish, Mexican and Texan expansion until the 1870s.",["Comancheria","Numunuu","Comanche"],"calendar","high"),
 ("kiowa","Kiowa","people",1700,None,IND,"Southern Plains nation allied with the Comanche, confined to a reservation after the Red River War.",["Kiowa Tribe"],"calendar","high"),
 ("cheyenne","Cheyenne","people",1700,None,IND,"Algonquian Plains nation of the Northern and Southern divisions, central to the Plains wars and the Sand Creek and Washita attacks.",["Tsitsistas","Northern Cheyenne","Southern Cheyenne"],"calendar","high"),
 ("arapaho","Arapaho","people",1700,None,IND,"Algonquian Plains nation allied with the Cheyenne and Lakota, now the Northern Arapaho of Wyoming and Southern Arapaho of Oklahoma.",["Hinono'eino"],"calendar","high"),
 ("blackfeet","Blackfoot Confederacy","polity",1700,None,IND,"Alliance of Piikani, Kainai and Siksika nations on the northern Plains, with the Blackfeet Nation in Montana today.",["Niitsitapi","Blackfeet Nation"],"calendar","high"),
 ("crow-nation","Crow Nation","people",1600,None,IND,"Plains nation of Montana, frequent US allies against the Lakota, sovereign on the Crow Reservation today.",["Apsaalooke","Absaroka"],"calendar","high"),
 ("pawnee","Pawnee Nation","people",1500,None,IND,"Caddoan farming and hunting nation of the Platte valley in Nebraska, later removed to Oklahoma.",["Pawnee","Chaticks si Chaticks"],"calendar","high"),
 ("osage-nation","Osage Nation","people",1600,None,IND,"Dhegihan Siouan nation that dominated the Ozarks and later grew wealthy and was preyed upon during the Oklahoma oil boom.",["Wazhazhe","Osage"],"calendar","high"),
 ("navajo-nation","Navajo Nation","polity",1400,None,IND,"Largest Native American reservation and one of the largest tribal nations, spanning Arizona, New Mexico and Utah; endured the 1864 Long Walk.",["Dine","Dineh","Navajo"],"calendar","high"),
 ("long-walk-navajo","Long Walk of the Navajo","event",1864,1866,"navajo-nation","Forced march of thousands of Navajo to Bosque Redondo internment, where many died before the 1868 treaty allowed return.",["Bosque Redondo"],"calendar","high"),
 ("apache-nations","Apache Nations","people",1400,None,IND,"Southern Athabaskan peoples including Chiricahua, Mescalero, Jicarilla and Western Apache of the Southwest.",["Apache","Nde"],"calendar","high"),
 ("chiricahua-apache","Chiricahua Apache","people",1600,None,"apache-nations","Apache band led at various times by Cochise, Victorio and Geronimo, whose resistance ended with imprisonment in Florida and Oklahoma.",["Chiricahua"],"calendar","high"),
 ("ute-people","Ute","people",1400,None,IND,"Numic nation of Colorado and Utah, among the first Plains-adjacent peoples to acquire horses from the Spanish.",["Nuche","Ute Tribe"],"calendar","high"),
 ("shoshone","Shoshone","people",1400,None,IND,"Numic peoples of the Great Basin and Snake River, including Sacagawea's Lemhi band and Chief Washakie's Eastern Shoshone.",["Shoshoni","Newe"],"calendar","high"),
 ("paiute","Paiute","people",1400,None,IND,"Numic peoples of the Great Basin, divided into Northern, Southern and Owens Valley groups, origin of the Ghost Dance prophet Wovoka.",["Numu","Nuwuvi"],"calendar","high"),
 ("nez-perce","Nez Perce","people",1500,None,IND,"Plateau nation of Idaho, Oregon and Washington, renowned horse breeders led in 1877 by Chief Joseph.",["Nimiipuu"],"calendar","high"),
 ("chinook-people","Chinook","people",1400,None,IND,"Lower Columbia River peoples who dominated Northwest trade and gave their name to the Chinook Jargon trade language.",["Chinookan peoples"],"calendar","high"),
 ("tlingit","Tlingit","people",1000,None,IND,"Northwest Coast nation of southeastern Alaska known for clan houses, totemic art and resistance to Russian colonisation.",["Lingit"],"calendar","medium"),
 ("haida","Haida","people",1000,None,IND,"Northwest Coast nation of Haida Gwaii and southern Alaska, celebrated for monumental cedar carving and canoes.",["Haida Nation"],"calendar","medium"),
 ("chumash","Chumash","people",-1000,None,IND,"Maritime people of the southern California coast and Channel Islands, known for tomol plank canoes and shell-bead money.",["Chumash people"],"radiocarbon","medium"),
 ("ohlone","Ohlone","people",1000,None,IND,"Peoples of the San Francisco and Monterey bay areas, devastated by the Spanish mission system.",["Costanoan"],"calendar","medium"),
 ("inuit-alaska","Inupiat and Yupik Peoples","people",1000,None,IND,"Arctic and subarctic peoples of Alaska descended from the Thule tradition, sustained by marine hunting.",["Inupiat","Yupik","Alaska Native peoples"],"radiocarbon","medium"),
 ("aleut","Unangax (Aleut)","people",1000,None,IND,"Peoples of the Aleutian Islands, enslaved and decimated under Russian fur-trade rule and interned by the US during World War II.",["Aleut","Unangan"],"calendar","medium"),
 ("shawnee","Shawnee","people",1600,None,IND,"Algonquian nation of the Ohio Valley, home of Tecumseh and Tenskwatawa, later removed to Kansas and Oklahoma.",["Shawnee Tribe"],"calendar","high"),
 ("miami-tribe","Miami Tribe","people",1600,None,IND,"Algonquian nation of the Wabash valley led by Little Turtle in the Northwest Indian War.",["Myaamia"],"calendar","high"),
 ("potawatomi","Potawatomi","people",1600,None,IND,"Algonquian nation of the Great Lakes, part of the Council of Three Fires, removed in the 1838 Trail of Death.",["Bodewadmi"],"calendar","high"),
 ("ojibwe","Ojibwe","people",1400,None,IND,"Large Algonquian nation of the western Great Lakes with many US and Canadian communities, known for wild rice harvesting and birchbark scrolls.",["Chippewa","Anishinaabe"],"calendar","high"),
 ("ho-chunk","Ho-Chunk","people",1500,None,IND,"Siouan-speaking nation of Wisconsin, repeatedly removed but returned to their homeland.",["Winnebago"],"calendar","high"),
 ("tecumsehs-confederacy","Tecumseh's Confederacy","polity",1805,1813,IND,"Pan-Indigenous alliance built by Tecumseh and Tenskwatawa to resist US expansion, allied with Britain and broken at the Thames.",["Northwest Confederacy","Prophetstown alliance"],"calendar","high"),
 ("ghost-dance-movement","Ghost Dance Movement","period",1889,1891,IND,"Revitalisation religion spread by the Paiute prophet Wovoka, whose growth among the Lakota preceded the Wounded Knee massacre.",["Ghost Dance"],"calendar","high"),
 ("dawes-act","Dawes Act","event",1887,1934,US,"Allotment policy dividing tribal lands into individual parcels, costing Indigenous nations about ninety million acres.",["General Allotment Act"],"calendar","high"),
 ("indian-reorganization-act","Indian Reorganization Act","event",1934,1934,US,"New Deal law ending allotment and restoring tribal self-government and land bases.",["Wheeler-Howard Act","Indian New Deal"],"calendar","high"),
 ("indian-termination-policy","Indian Termination Policy","period",1953,1968,US,"Federal effort to dissolve tribal status and relocate Native people to cities, later reversed by self-determination policy.",["termination era"],"calendar","high"),
 ("red-power-movement","Red Power Movement","period",1968,1978,US,"Native activist movement including the Alcatraz occupation, AIM and Wounded Knee 1973, which won self-determination reforms.",["American Indian Movement","AIM"],"calendar","high"),
 ("indian-self-determination-act","Indian Self-Determination and Education Assistance Act","event",1975,1975,US,"Law allowing tribes to contract and administer federal programmes themselves, ending the termination era.",[],"calendar","high"),
 ("mcgirt-v-oklahoma","McGirt v. Oklahoma","event",2020,2020,US,"Supreme Court ruling that much of eastern Oklahoma remains Indian country for criminal jurisdiction purposes.",["McGirt"],"calendar","high"),
]
for row in indig:
    if len(row) == 9:
        slug, name, kind, sy, ey, parent, summ, al, dm = row
        conf = "medium"
        # last element is dating method; confidence default
        add(slug, name, kind, sy, ey, parent, summ, al, extant=(ey is None), conf=conf, dm=dm)
    else:
        slug, name, kind, sy, ey, parent, summ, al, dm, conf = row
        add(slug, name, kind, sy, ey, parent, summ, al, extant=(ey is None), conf=conf, dm=dm)

# fix poverty point (had wrong arity) -> handled below by check

# ---------------- EXPLORATION, SOCIAL, ECONOMIC, CULTURAL ----------------
misc = [
 ("norse-vinland","Norse Settlement of Vinland","event",1000,1020,NA,"Short-lived Norse presence in northeastern North America, archaeologically confirmed at L'Anse aux Meadows.",["Vinland"],"radiocarbon","medium"),
 ("columbus-voyages","Voyages of Columbus","event",1492,1504,NA,"Four Spanish-sponsored crossings that initiated sustained European contact with the Americas.",["Columbian voyages"],"calendar","high"),
 ("columbian-exchange","Columbian Exchange","period",1492,1800,NA,"Transfer of crops, animals, people and diseases between the Americas and the Old World, including epidemics that devastated Indigenous populations.",[],"calendar","high"),
 ("coronado-expedition","Coronado Expedition","event",1540,1542,NA,"Spanish expedition across the Southwest and Plains in search of Cibola, the first European contact for many Indigenous nations.",[],"calendar","high"),
 ("de-soto-expedition","De Soto Expedition","event",1539,1543,NA,"Spanish march through the Southeast that described late Mississippian societies and spread devastating disease.",[],"calendar","high"),
 ("st-augustine-founding","Founding of St. Augustine","event",1565,1565,NA,"Spanish settlement in Florida, the oldest continuously occupied European city in the continental United States.",["San Agustin"],"calendar","high"),
 ("santa-fe-founding","Founding of Santa Fe","event",1610,1610,NA,"Spanish colonial capital of New Mexico, the oldest state capital in the United States.",[],"calendar","high"),
 ("california-missions","California Mission System","period",1769,1834,NA,"Chain of twenty-one Franciscan missions that coerced Indigenous labour and conversion in Alta California until Mexican secularisation.",["Alta California missions"],"calendar","high"),
 ("fur-trade-north-america","North American Fur Trade","period",1600,1870,NA,"Continental commerce in beaver and other pelts that structured Indigenous-European relations and drove exploration.",["beaver trade"],"calendar","high"),
 ("market-revolution","Market Revolution","period",1815,1860,US,"Transformation of the American economy by canals, railroads, textile mills and wage labour.",[],"calendar","high"),
 ("erie-canal","Erie Canal","event",1817,1825,US,"363-mile canal linking the Hudson to Lake Erie, slashing freight costs and making New York the nation's leading port.",[],"calendar","high"),
 ("industrial-revolution-us","American Industrial Revolution","period",1790,1900,US,"Shift from agrarian craft production to mechanised factory industry, from Slater's mill to steel and electricity.",["industrialisation"],"calendar","high"),
 ("california-gold-rush","California Gold Rush","event",1848,1855,US,"Discovery at Sutter's Mill drew some 300,000 migrants to California, accelerating statehood and devastating Native communities.",["Forty-niners"],"calendar","high"),
 ("panic-of-1837","Panic of 1837","event",1837,1843,US,"Financial crisis and prolonged depression following speculation, the Specie Circular and British credit contraction.",[],"calendar","high"),
 ("panic-of-1873","Panic of 1873","event",1873,1879,US,"Railroad and banking collapse that began the Long Depression and undermined Reconstruction.",[],"calendar","high"),
 ("panic-of-1893","Panic of 1893","event",1893,1897,US,"Severe depression with mass unemployment, railroad bankruptcies and violent labour conflict.",[],"calendar","high"),
 ("wall-street-crash-1929","Wall Street Crash of 1929","event",1929,1929,US,"October stock market collapse that wiped out fortunes and signalled the onset of the Great Depression.",["Black Tuesday","Great Crash"],"calendar","high"),
 ("dust-bowl","Dust Bowl","event",1930,1940,US,"Severe drought and soil erosion on the southern Plains that displaced hundreds of thousands of farm families.",["Dirty Thirties"],"calendar","high"),
 ("great-migration","Great Migration","period",1916,1970,US,"Movement of about six million African Americans from the rural South to northern, midwestern and western cities.",["Black Migration"],"calendar","high"),
 ("harlem-renaissance","Harlem Renaissance","period",1918,1937,US,"Flowering of African American literature, music and art centred in Harlem, with figures such as Hughes, Hurston and Ellington.",["New Negro Movement"],"calendar","high"),
 ("labor-movement-us","American Labor Movement","period",1866,None,US,"Long struggle for union recognition, shorter hours and workplace safety, from the National Labor Union through the AFL-CIO.",["organised labor"],"calendar","high"),
 ("haymarket-affair","Haymarket Affair","event",1886,1886,US,"Chicago rally bombing and mass trial that set back the eight-hour movement and became a global labour symbol.",["Haymarket riot"],"calendar","high"),
 ("pullman-strike","Pullman Strike","event",1894,1894,US,"National railway boycott broken by federal troops and injunction, making Eugene Debs a socialist leader.",[],"calendar","high"),
 ("triangle-shirtwaist-fire","Triangle Shirtwaist Factory Fire","event",1911,1911,US,"Fire that killed 146 garment workers in New York and spurred landmark workplace safety laws.",[],"calendar","high"),
 ("populist-movement","Populist Movement","period",1877,1896,US,"Agrarian revolt against railroads, banks and the gold standard that produced the People's Party and Bryan's 1896 campaign.",["People's Party","Populism"],"calendar","high"),
 ("temperance-movement","Temperance Movement","period",1826,1920,US,"Long campaign against alcohol led by the WCTU and Anti-Saloon League, culminating in national Prohibition.",[],"calendar","high"),
 ("lost-generation","Lost Generation","period",1918,1930,US,"Cohort of American writers and expatriates disillusioned by World War I, including Hemingway and Fitzgerald.",[],"calendar","medium"),
 ("space-race","Space Race","period",1957,1975,US,"US-Soviet competition in spaceflight, from Sputnik through the Apollo Moon landings and Apollo-Soyuz.",[],"calendar","high"),
 ("apollo-11","Apollo 11 Moon Landing","event",1969,1969,US,"First human landing on the Moon, with Neil Armstrong and Buzz Aldrin walking on the lunar surface.",["Moon landing"],"calendar","high"),
 ("montgomery-bus-boycott","Montgomery Bus Boycott","event",1955,1956,"civil-rights-movement","Year-long boycott sparked by Rosa Parks's arrest that desegregated Montgomery buses and elevated Martin Luther King Jr.",[],"calendar","high"),
 ("little-rock-crisis","Little Rock Integration Crisis","event",1957,1957,"civil-rights-movement","Eisenhower sent federal troops to escort nine Black students into Central High School after the governor blocked desegregation.",["Little Rock Nine"],"calendar","high"),
 ("march-on-washington","March on Washington for Jobs and Freedom","event",1963,1963,"civil-rights-movement","Mass rally of about 250,000 people where Martin Luther King Jr. delivered the 'I Have a Dream' speech.",["March on Washington"],"calendar","high"),
 ("freedom-summer","Freedom Summer","event",1964,1964,"civil-rights-movement","Mississippi voter registration campaign marked by the murders of three activists and the challenge of the MFDP.",["Mississippi Freedom Summer"],"calendar","high"),
 ("selma-marches","Selma to Montgomery Marches","event",1965,1965,"civil-rights-movement","Voting rights marches including 'Bloody Sunday' at the Edmund Pettus Bridge, which spurred the Voting Rights Act.",["Bloody Sunday"],"calendar","high"),
 ("assassination-of-mlk","Assassination of Martin Luther King Jr.","event",1968,1968,"civil-rights-movement","King's murder in Memphis triggered unrest in over a hundred cities and hastened the Fair Housing Act.",[],"calendar","high"),
 ("stonewall-riots","Stonewall Riots","event",1969,1969,US,"Uprising against a police raid on a Greenwich Village gay bar, conventionally the start of the modern LGBT rights movement.",["Stonewall"],"calendar","high"),
 ("aids-crisis-us","AIDS Crisis in the United States","period",1981,1996,US,"Epidemic that killed hundreds of thousands of Americans and produced militant activism by groups such as ACT UP.",["HIV/AIDS epidemic"],"calendar","high"),
 ("japanese-american-incarceration","Japanese American Incarceration","event",1942,1946,US,"Forced removal and confinement of about 120,000 people of Japanese descent under Executive Order 9066.",["Japanese American internment","Executive Order 9066"],"calendar","high"),
 ("brown-decision-aftermath","Massive Resistance","period",1954,1964,US,"Southern campaign of school closures, private academies and interposition laws to defy Brown v. Board of Education.",[],"calendar","high"),
 ("oklahoma-land-rush","Oklahoma Land Rush","event",1889,1895,US,"Series of land runs opening former Indian Territory to non-Native settlement.",["land run"],"calendar","high"),
 ("closing-of-the-frontier","Closing of the American Frontier","event",1890,1890,US,"Census finding that no continuous frontier line remained, framed by Frederick Jackson Turner as the end of an era.",["Turner thesis"],"calendar","high"),
 ("transcontinental-railroad-completion","Completion of the Transcontinental Railroad","event",1869,1869,US,"Union Pacific and Central Pacific rails met at Promontory Summit, joining the coasts by rail.",["golden spike"],"calendar","high"),
 ("statehood-expansion","Admission of the States","period",1787,1959,US,"Process by which fifty states joined the Union, from Delaware's ratification to Alaska and Hawaii in 1959.",["statehood"],"calendar","high"),
 ("american-imperialism","American Imperialism","era",1898,1934,US,"Period of overseas expansion producing colonies and protectorates in the Caribbean and Pacific, including Puerto Rico and the Philippines.",["overseas expansion"],"calendar","high"),
 ("progressive-amendments","Progressive Era Amendments","period",1913,1920,US,"Cluster of four amendments creating the income tax, direct senatorial election, Prohibition and women's suffrage.",[],"calendar","medium"),
 ("election-of-1800","Election of 1800","event",1800,1801,US,"Contested election resolved by the House that produced the first peaceful transfer of power between parties.",["Revolution of 1800"],"calendar","high"),
 ("election-of-1860","Election of 1860","event",1860,1860,US,"Four-way contest won by Lincoln with under 40 percent of the vote, prompting southern secession.",[],"calendar","high"),
 ("election-of-1876","Election of 1876","event",1876,1877,US,"Disputed election between Hayes and Tilden resolved by an electoral commission and the Compromise of 1877.",[],"calendar","high"),
 ("election-of-1932","Election of 1932","event",1932,1932,US,"Roosevelt's landslide over Hoover that created the New Deal coalition and realigned American politics.",[],"calendar","high"),
 ("election-of-2000","Election of 2000","event",2000,2000,US,"Election decided by 537 Florida votes after a recount halted by the Supreme Court.",[],"calendar","high"),
 ("impeachment-andrew-johnson","Impeachment of Andrew Johnson","event",1868,1868,US,"First presidential impeachment, over violation of the Tenure of Office Act; Johnson survived by one Senate vote.",[],"calendar","high"),
 ("impeachment-bill-clinton","Impeachment of Bill Clinton","event",1998,1999,US,"House impeachment for perjury and obstruction arising from the Lewinsky investigation; the Senate acquitted him.",[],"calendar","high"),
 ("impeachments-donald-trump","Impeachments of Donald Trump","event",2019,2021,US,"Two House impeachments, over Ukraine aid in 2019 and incitement of the January 6 attack in 2021; the Senate acquitted both times.",[],"calendar","high"),
 ("january-6-attack","January 6 Capitol Attack","event",2021,2021,US,"Mob storming of the Capitol seeking to block certification of the 2020 election results.",["Capitol riot","January 6"],"calendar","high"),
 ("nixon-resignation","Resignation of Richard Nixon","event",1974,1974,US,"First resignation of a US president, following the Supreme Court tapes ruling and imminent impeachment.",[],"calendar","high"),
 ("assassination-of-lincoln","Assassination of Abraham Lincoln","event",1865,1865,US,"John Wilkes Booth shot Lincoln at Ford's Theatre days after Appomattox, elevating Andrew Johnson.",[],"calendar","high"),
 ("assassination-of-jfk","Assassination of John F. Kennedy","event",1963,1963,US,"Kennedy was shot in Dallas; Lee Harvey Oswald was charged and the Warren Commission investigated.",[],"calendar","high"),
 ("berlin-airlift","Berlin Airlift","event",1948,1949,US,"US and British air supply of West Berlin during the Soviet blockade, a defining early Cold War operation.",["Operation Vittles"],"calendar","high"),
 ("arms-race-nuclear","Nuclear Arms Race","period",1945,1991,US,"US-Soviet buildup of nuclear arsenals and delivery systems, shaped by deterrence doctrine and arms control treaties.",["nuclear standoff"],"calendar","high"),
 ("civil-rights-act-1875","Civil Rights Act of 1875","event",1875,1875,US,"Reconstruction law barring discrimination in public accommodations, struck down by the Supreme Court in 1883.",[],"calendar","high"),
 ("freedmens-bureau","Freedmen's Bureau","polity",1865,1872,"reconstruction","Federal agency providing relief, labour contracts, courts and schools to freedpeople and refugees in the postwar South.",["Bureau of Refugees, Freedmen, and Abandoned Lands"],"calendar","high"),
 ("black-codes","Black Codes","event",1865,1866,"reconstruction","Southern state laws restricting freedpeople's labour, movement and rights, which provoked congressional Reconstruction.",[],"calendar","high"),
 ("ku-klux-klan-first","First Ku Klux Klan","polity",1865,1872,US,"Postwar white terrorist organisation that attacked Black voters and Republicans until suppressed by the Enforcement Acts.",["KKK"],"calendar","high"),
 ("ku-klux-klan-second","Second Ku Klux Klan","polity",1915,1944,US,"Revived mass Klan of the 1920s, nativist and anti-Catholic as well as racist, with millions of members before collapsing in scandal.",["1920s Klan"],"calendar","high"),
 ("lend-lease","Lend-Lease","event",1941,1945,US,"Programme supplying about $50 billion in war material to Britain, the Soviet Union and other Allies before and during US belligerency.",[],"calendar","high"),
 ("neutrality-and-isolationism","American Isolationism","period",1920,1941,US,"Interwar retreat from European commitments, expressed in Senate rejection of the League and the Neutrality Acts.",["isolationist era"],"calendar","high"),
 ("bonus-army","Bonus Army March","event",1932,1932,US,"Veterans' encampment in Washington demanding early bonus payment, dispersed by the Army under MacArthur.",[],"calendar","high"),
 ("tva","Tennessee Valley Authority","polity",1933,None,"new-deal","New Deal public corporation that built dams, generated power and modernised the Tennessee Valley.",["TVA"],"calendar","high"),
 ("ccc","Civilian Conservation Corps","polity",1933,1942,"new-deal","New Deal work relief agency that employed three million young men on forestry, parks and erosion projects.",["CCC"],"calendar","high"),
 ("wpa","Works Progress Administration","polity",1935,1943,"new-deal","Largest New Deal agency, employing 8.5 million people on public works, arts and writing projects.",["WPA","Work Projects Administration"],"calendar","high"),
 ("nra-recovery","National Recovery Administration","polity",1933,1935,"new-deal","New Deal agency setting industrial codes on prices and wages, struck down by the Supreme Court in 1935.",["NRA"],"calendar","high"),
 ("aaa-agriculture","Agricultural Adjustment Administration","polity",1933,1942,"new-deal","New Deal agency that paid farmers to cut production in order to raise crop prices.",["AAA"],"calendar","high"),
 ("court-packing-plan","Court-Packing Plan","event",1937,1937,US,"Roosevelt's failed proposal to add Supreme Court justices after the Court struck down New Deal laws.",["Judicial Procedures Reform Bill"],"calendar","high"),
 ("puerto-rico-us","Puerto Rico under US Rule","polity",1898,None,US,"Caribbean island ceded by Spain in 1898, an unincorporated US territory whose residents are citizens without presidential votes.",["Commonwealth of Puerto Rico"],"calendar","high"),
 ("philippines-us-rule","US Rule in the Philippines","polity",1898,1946,US,"American colonial administration of the Philippines from the Spanish cession to independence in 1946.",["Insular Government"],"calendar","high"),
 ("alaska-territory","Alaska Territory","polity",1912,1959,US,"Organised US territory in the far northwest, admitted as the 49th state in 1959.",["District of Alaska"],"calendar","high"),
 ("hawaii-territory","Territory of Hawaii","polity",1898,1959,US,"US territory from annexation until statehood as the 50th state in 1959.",["Hawaiian Territory"],"calendar","high"),
 ("panama-canal-construction","Construction of the Panama Canal","event",1904,1914,US,"US engineering project that cut a shipping route across the isthmus after acquiring rights from newly independent Panama.",["Panama Canal"],"calendar","high"),
 ("interstate-migration-sunbelt","Sunbelt Migration","period",1945,2000,US,"Long shift of population, industry and political power from the Northeast and Midwest to the South and Southwest.",["Sunbelt shift","Rust Belt decline"],"calendar","medium"),
 ("gilded-age-immigration","Age of Mass Immigration","period",1880,1924,US,"Arrival of over twenty million immigrants, mostly from southern and eastern Europe, processed largely at Ellis Island.",["new immigration"],"calendar","high"),
 ("ellis-island","Ellis Island Immigration Station","polity",1892,1954,US,"Principal US immigrant inspection station in New York Harbor, through which about twelve million people passed.",[],"calendar","high"),
 ("angel-island","Angel Island Immigration Station","polity",1910,1940,US,"West Coast immigration station in San Francisco Bay where Asian arrivals, especially Chinese, faced prolonged detention.",[],"calendar","high"),
 ("gettysburg-address","Gettysburg Address","event",1863,1863,US,"Lincoln's brief speech dedicating the Soldiers' National Cemetery, redefining the war as a struggle for democratic equality.",[],"calendar","high"),
 ("seneca-falls-convention","Seneca Falls Convention","event",1848,1848,US,"First US women's rights convention, which issued the Declaration of Sentiments demanding equality including the vote.",[],"calendar","high"),
 ("uncle-toms-cabin","Publication of Uncle Tom's Cabin","event",1852,1852,US,"Harriet Beecher Stowe's antislavery novel sold hundreds of thousands of copies and hardened sectional opinion.",[],"calendar","high"),
 ("lincoln-douglas-debates","Lincoln-Douglas Debates","event",1858,1858,US,"Seven Illinois Senate debates over slavery in the territories that made Lincoln a national figure.",[],"calendar","high"),
 ("federal-writers-project","Federal Writers' Project Slave Narratives","event",1936,1938,US,"WPA programme that recorded more than 2,300 interviews with formerly enslaved people.",["WPA slave narratives"],"calendar","medium"),
 ("hurricane-katrina","Hurricane Katrina","event",2005,2005,US,"Storm that flooded New Orleans, killed over 1,800 people and exposed failures in federal and local emergency response.",[],"calendar","high"),
 ("black-lives-matter","Black Lives Matter Movement","period",2013,None,US,"Movement against police violence and racial injustice that produced the largest protests in US history in 2020.",["BLM"],"calendar","high"),
 ("me-too-movement","MeToo Movement","period",2017,None,US,"Mass reckoning with sexual harassment and assault that toppled prominent figures across industries.",["#MeToo"],"calendar","medium"),
]
for row in misc:
    slug, name, kind, sy, ey, parent, summ, al, dm, conf = row
    add(slug, name, kind, sy, ey, parent, summ, al, extant=(ey is None), conf=conf, dm=dm)

# ---- validation ----
seen = set()
for e in E:
    assert e["suggested_id_slug"] not in seen, e["suggested_id_slug"]
    seen.add(e["suggested_id_slug"])
    assert "\n" not in e["summary"]
    assert len(e["summary"]) < 300, (e["suggested_id_slug"], len(e["summary"]))
    assert e["kind"] in {"reign","polity","era","period","event","culture","people"}, e
    assert isinstance(e["start_year"], int)
    if e["start_year"] >= 1500 and e["start_dating_method"] != "calendar":
        raise AssertionError((e["suggested_id_slug"], e["start_dating_method"]))
    assert e["end_year"] is None or isinstance(e["end_year"], int)
    if e["start_year"] > 1500:
        pass
    if e["end_year"] is None:
        assert e["extant"] is True, e["suggested_id_slug"]
    for k in ["suggested_id_slug","name","kind","start_year","end_year","extant","parent_hint","start_dating_method","summary","aliases","confidence"]:
        assert k in e
    assert list(e.keys()) == ["suggested_id_slug","name","kind","start_year","end_year","extant","parent_hint","start_dating_method","summary","aliases","confidence"]

with open("/home/user/workspace/hp/docs/research/usa.json","w") as f:
    json.dump(E, f, indent=2, ensure_ascii=False)
print(len(E))
print(sum(1 for e in E if e["kind"]=="reign"), "reigns")
