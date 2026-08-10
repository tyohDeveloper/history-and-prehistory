# -*- coding: utf-8 -*-
"""Part 1: monarchs of England (Wessex line onward), Scotland, Great Britain / UK."""

ENTRIES = []

def E(slug, name, kind, start, end, parent, summary, aliases=None, conf="high", dm=None, extant=False):
    if dm is None:
        dm = "calendar" if (start is not None and start >= 1066) else "received"
    ENTRIES.append({
        "suggested_id_slug": slug,
        "name": name,
        "kind": kind,
        "start_year": start,
        "end_year": end,
        "extant": extant,
        "parent_hint": parent,
        "start_dating_method": dm,
        "summary": " ".join(summary.split()),
        "aliases": aliases or [],
        "confidence": conf,
    })

AS_NOTE = "Regnal dates are those received from the Anglo-Saxon Chronicle and later chronicles and may be uncertain by a year or more."

# ---------------- Kings of Wessex / the English, 871-1066 ----------------
W = "Kingdom of Wessex"
EN = "Kingdom of England"

E("alfred-the-great", "Alfred the Great", "reign", 871, 899, W,
  "King of the West Saxons who resisted the Viking Great Heathen Army, secured the Danelaw frontier and promoted learning and law. " + AS_NOTE,
  ["Alfred", "AElfred", "Alfred of Wessex"])
E("edward-the-elder", "Edward the Elder", "reign", 899, 924, W,
  "Son of Alfred who conquered much of the southern Danelaw and extended West Saxon overlordship over Mercia. " + AS_NOTE,
  ["Edward I of Wessex"])
E("aelfweard", "AElfweard of Wessex", "reign", 924, 924, W,
  "Son of Edward the Elder who may have reigned in Wessex for a few weeks in 924; his kingship is disputed. Dates are received from chronicle tradition.",
  ["Aelfweard", "Elfward"], conf="medium")
E("aethelstan", "AEthelstan", "reign", 924, 939, EN,
  "First king to rule all England, victor at Brunanburh in 937 and a major legislator. " + AS_NOTE,
  ["Athelstan", "Aethelstan the Glorious"])
E("edmund-i", "Edmund I", "reign", 939, 946, EN,
  "Half-brother of AEthelstan who recovered the Five Boroughs from Norse rule; murdered at Pucklechurch. " + AS_NOTE,
  ["Edmund the Magnificent", "Edmund the Elder"])
E("eadred", "Eadred", "reign", 946, 955, EN,
  "King who finally ended the Norse kingdom of York with the death of Eric Bloodaxe in 954. " + AS_NOTE,
  ["Edred", "Eadred of England"])
E("eadwig", "Eadwig", "reign", 955, 959, EN,
  "Teenage king whose reign saw conflict with Dunstan and the loss of Mercia and Northumbria to his brother Edgar. " + AS_NOTE,
  ["Edwy", "Eadwig All-Fair"])
E("edgar-the-peaceful", "Edgar the Peaceful", "reign", 959, 975, EN,
  "King associated with the Benedictine reform, monetary reform and a famous imperial coronation at Bath in 973. " + AS_NOTE,
  ["Edgar I", "Eadgar"])
E("edward-the-martyr", "Edward the Martyr", "reign", 975, 978, EN,
  "Young king murdered at Corfe in 978 and swiftly venerated as a saint. " + AS_NOTE,
  ["Saint Edward the Martyr"])
E("aethelred-the-unready", "AEthelred the Unready", "reign", 978, 1013, EN,
  "Long reign dominated by renewed Viking invasions, Danegeld payments and the St Brice's Day massacre; driven out by Sweyn Forkbeard in 1013. " + AS_NOTE,
  ["Ethelred II", "Aethelred II", "Ethelred the Unready"])
E("sweyn-forkbeard", "Sweyn Forkbeard", "reign", 1013, 1014, EN,
  "Danish king who conquered England in 1013 and reigned for a few weeks before dying at Gainsborough. Dates are received from chronicle tradition.",
  ["Svein Haraldsson", "Swein Forkbeard"])
E("aethelred-restored", "AEthelred the Unready (restored)", "reign", 1014, 1016, EN,
  "Second reign of AEthelred after Sweyn's death, ending with his own death in London amid Cnut's invasion. " + AS_NOTE,
  ["Ethelred II restoration"])
E("edmund-ironside", "Edmund Ironside", "reign", 1016, 1016, EN,
  "Warrior son of AEthelred who fought Cnut to a partition of England at Olney and died months later. Dates are received from chronicle tradition.",
  ["Edmund II"])
E("cnut-the-great", "Cnut the Great", "reign", 1016, 1035, EN,
  "Danish conqueror who ruled England, Denmark and Norway as a North Sea empire and governed England through native institutions. Dates are received from chronicle tradition.",
  ["Canute", "Knut", "Knud the Great"])
E("harold-harefoot", "Harold Harefoot", "reign", 1035, 1040, EN,
  "Son of Cnut who ruled England, first as regent then as king, against the claims of his half-brother Harthacnut. Dates received from chronicles.",
  ["Harold I"])
E("harthacnut", "Harthacnut", "reign", 1040, 1042, EN,
  "Son of Cnut and Emma who united the English and Danish crowns briefly and died suddenly at Lambeth. Dates received from chronicles.",
  ["Harthacanute", "Hardicanute", "Cnut III"])
E("edward-the-confessor", "Edward the Confessor", "reign", 1042, 1066, EN,
  "Restored king of the house of Wessex, builder of Westminster Abbey, whose childless death triggered the succession crisis of 1066. Dates received from chronicles.",
  ["Saint Edward the Confessor", "Edward III of England"])
E("harold-godwinson", "Harold Godwinson", "reign", 1066, 1066, EN,
  "Last crowned Anglo-Saxon king of England; won at Stamford Bridge and was killed at Hastings on 14 October 1066.",
  ["Harold II", "Harold Godwineson"])
E("edgar-aetheling", "Edgar the AEtheling", "reign", 1066, 1066, EN,
  "Last male of the house of Wessex, proclaimed king in London after Hastings but never crowned; submitted to William at Berkhamsted.",
  ["Edgar II", "Edgar Atheling"], conf="medium")

# ---------------- Norman and Angevin ----------------
E("william-the-conqueror", "William I the Conqueror", "reign", 1066, 1087, EN,
  "Duke of Normandy who conquered England in 1066, imposed Norman lordship, built castles and commissioned Domesday Book.",
  ["William the Bastard", "William I of England"])
E("william-ii-rufus", "William II Rufus", "reign", 1087, 1100, EN,
  "Second Norman king, quarrelsome with the Church and killed by an arrow in the New Forest.",
  ["William Rufus"])
E("henry-i-england", "Henry I", "reign", 1100, 1135, EN,
  "Youngest son of the Conqueror who took England and Normandy, issued the Charter of Liberties and left a disputed succession after his son's death.",
  ["Henry Beauclerc"])
E("stephen-of-england", "Stephen", "reign", 1135, 1154, EN,
  "Nephew of Henry I whose contested accession produced the civil war known as the Anarchy; agreed to be succeeded by Henry of Anjou.",
  ["Stephen of Blois"])
E("empress-matilda", "Empress Matilda", "reign", 1141, 1141, EN,
  "Daughter of Henry I who controlled England briefly in 1141 as Lady of the English but was never crowned queen.",
  ["Maud", "Matilda of England"], conf="medium")
E("henry-ii-england", "Henry II", "reign", 1154, 1189, EN,
  "First Plantagenet king, ruler of a vast Angevin domain, reformer of English common law and antagonist of Thomas Becket.",
  ["Henry Curtmantle", "Henry FitzEmpress"])
E("richard-i-lionheart", "Richard I the Lionheart", "reign", 1189, 1199, EN,
  "Crusader king who spent almost his entire reign abroad on the Third Crusade and in continental war, dying at Chalus.",
  ["Richard Coeur de Lion", "Richard the Lionheart"])
E("john-england", "John", "reign", 1199, 1216, EN,
  "Lost Normandy to Philip II, quarrelled with the papacy and was forced to seal Magna Carta in 1215.",
  ["John Lackland", "King John"])
E("henry-iii-england", "Henry III", "reign", 1216, 1272, EN,
  "Boy king whose long reign saw baronial reform, the Provisions of Oxford, the Second Barons' War and the rebuilding of Westminster Abbey.",
  ["Henry of Winchester"])
E("edward-i-england", "Edward I", "reign", 1272, 1307, EN,
  "Conqueror of Wales, campaigner in Scotland and summoner of the Model Parliament of 1295.",
  ["Longshanks", "Hammer of the Scots"])
E("edward-ii-england", "Edward II", "reign", 1307, 1327, EN,
  "Defeated at Bannockburn and dominated by favourites; deposed in 1327 and died at Berkeley Castle.",
  ["Edward of Caernarfon"])
E("edward-iii-england", "Edward III", "reign", 1327, 1377, EN,
  "Claimed the French throne and opened the Hundred Years War, won Crecy and Poitiers, and ruled through the Black Death.",
  ["Edward of Windsor"])
E("richard-ii-england", "Richard II", "reign", 1377, 1399, EN,
  "Faced the Peasants' Revolt as a boy and later ruled autocratically; deposed by Henry Bolingbroke in 1399.",
  ["Richard of Bordeaux"])
E("henry-iv-england", "Henry IV", "reign", 1399, 1413, EN,
  "First Lancastrian king, who usurped Richard II and spent his reign suppressing rebellion including Glyndwr's rising and the Percys.",
  ["Henry Bolingbroke"])
E("henry-v-england", "Henry V", "reign", 1413, 1422, EN,
  "Victor of Agincourt in 1415 whose Treaty of Troyes made him heir to France; died of dysentery in 1422.",
  ["Henry of Monmouth"])
E("henry-vi-england", "Henry VI", "reign", 1422, 1461, EN,
  "Inherited England and the French claim as an infant; his incapacity and factionalism led to the loss of France and the Wars of the Roses.",
  ["Henry of Windsor"])
E("edward-iv-first", "Edward IV (first reign)", "reign", 1461, 1470, EN,
  "Yorkist king who seized the throne after Towton and was driven out in 1470 by Warwick and the Lancastrians.",
  ["Edward of York"])
E("henry-vi-restored", "Henry VI (restoration)", "reign", 1470, 1471, EN,
  "Brief Lancastrian restoration engineered by the Earl of Warwick, ending with Barnet, Tewkesbury and Henry's death in the Tower.",
  ["Readeption of Henry VI"])
E("edward-iv-second", "Edward IV (second reign)", "reign", 1471, 1483, EN,
  "Restored Yorkist rule, stabilised royal finances and reigned in comparative peace until his sudden death in 1483.",
  ["Edward IV restoration"])
E("edward-v-england", "Edward V", "reign", 1483, 1483, EN,
  "Boy king deposed after eleven weeks by his uncle Richard of Gloucester; one of the Princes in the Tower, never crowned.",
  ["Prince in the Tower"])
E("richard-iii-england", "Richard III", "reign", 1483, 1485, EN,
  "Last Yorkist and last Plantagenet king, killed at Bosworth in 1485; his remains were found in Leicester in 2012.",
  ["Richard of Gloucester"])
E("henry-vii-england", "Henry VII", "reign", 1485, 1509, EN,
  "First Tudor king, who won at Bosworth, married Elizabeth of York and restored royal finances and authority.",
  ["Henry Tudor", "Earl of Richmond"])
E("henry-viii-england", "Henry VIII", "reign", 1509, 1547, EN,
  "Broke with Rome to become Supreme Head of the Church of England, dissolved the monasteries and married six times.",
  ["Henry Tudor VIII"])
E("edward-vi-england", "Edward VI", "reign", 1547, 1553, EN,
  "Boy king under Somerset and Northumberland whose reign pushed England towards full Protestantism and the Books of Common Prayer.",
  ["Edward Tudor"])
E("jane-grey", "Lady Jane Grey", "reign", 1553, 1553, EN,
  "Proclaimed queen for nine to thirteen days in July 1553 under Northumberland's scheme; deposed by Mary I and later executed.",
  ["Jane Grey", "the Nine Days Queen"], conf="medium")
E("mary-i-england", "Mary I", "reign", 1553, 1558, EN,
  "Restored Roman Catholicism, married Philip II of Spain and presided over the Marian persecutions.",
  ["Bloody Mary", "Mary Tudor"])
E("philip-of-spain-england", "Philip of Spain as King of England", "reign", 1554, 1558, EN,
  "Jure uxoris king alongside Mary I under the terms of their marriage treaty; his title lapsed on her death.",
  ["Philip II of Spain", "Philip and Mary"], conf="medium")
E("elizabeth-i", "Elizabeth I", "reign", 1558, 1603, EN,
  "Last Tudor monarch, whose long reign saw the Elizabethan religious settlement, the defeat of the Spanish Armada and a literary golden age.",
  ["the Virgin Queen", "Good Queen Bess", "Gloriana"])

# ---------------- Stuarts and Interregnum (England / Scotland / Ireland) ----------------
E("james-i-england", "James I of England and VI of Scotland", "reign", 1603, 1625, EN,
  "First Stuart king of England, uniting the English and Scottish crowns in his person and sponsoring the Authorised Version of the Bible.",
  ["James VI and I", "James VI of Scotland"])
E("charles-i", "Charles I", "reign", 1625, 1649, EN,
  "Rule by personal prerogative and religious policy provoked the Civil Wars; tried and executed in Whitehall in January 1649.",
  ["Charles Stuart"])
E("oliver-cromwell-protector", "Oliver Cromwell as Lord Protector", "reign", 1653, 1658, "Commonwealth of England",
  "Head of state of the Protectorate over England, Scotland and Ireland after dissolving the Rump Parliament; refused the crown in 1657.",
  ["Lord Protector Cromwell"])
E("richard-cromwell-protector", "Richard Cromwell as Lord Protector", "reign", 1658, 1659, "Commonwealth of England",
  "Succeeded his father but lacked army support and resigned in May 1659, opening the way to the Restoration.",
  ["Tumbledown Dick"])
E("charles-ii", "Charles II", "reign", 1660, 1685, EN,
  "Restored Stuart king whose reign covered the Great Plague, the Fire of London, the Popish Plot and the Exclusion Crisis.",
  ["the Merry Monarch"])
E("james-ii", "James II of England and VII of Scotland", "reign", 1685, 1688, EN,
  "Catholic king deposed by the Glorious Revolution after alienating the political nation; fled to France in December 1688.",
  ["James VII", "James Stuart"])
E("william-iii", "William III", "reign", 1689, 1702, EN,
  "Dutch stadtholder invited to rule jointly with Mary II; accepted the Bill of Rights and led the Grand Alliance against Louis XIV.",
  ["William of Orange", "William II of Scotland"])
E("mary-ii", "Mary II", "reign", 1689, 1694, EN,
  "Joint sovereign with her husband William III after the Glorious Revolution; died of smallpox in 1694.",
  ["Mary Stuart II"])
E("anne-england", "Anne, Queen of England, Scotland and Ireland", "reign", 1702, 1707, EN,
  "Last Stuart monarch, who reigned over separate English and Scottish kingdoms until the Acts of Union created Great Britain in 1707.",
  ["Queen Anne"])

# ---------------- Monarchs of Scotland ----------------
SC = "Kingdom of Scotland"
SC_NOTE = "Dates are those received from later Scottish chronicle and king-list tradition and are not securely attested."

for slug, name, s, e, summ, al in [
    ("kenneth-i-scotland", "Kenneth I MacAlpin", 843, 858, "Traditionally the first king of a united Picto-Gaelic kingdom of Alba, though the union was a longer process than the king-lists suggest.", ["Cinaed mac Ailpin", "Kenneth MacAlpin"]),
    ("donald-i-scotland", "Donald I", 858, 862, "Brother of Kenneth I, remembered for promulgating the 'laws of Aed' in Alba.", ["Domnall mac Ailpin"]),
    ("constantine-i-scotland", "Constantine I", 862, 877, "King of Alba during heavy Viking pressure; killed fighting Norse raiders.", ["Constantin mac Cinaeda"]),
    ("aed-scotland", "Aed", 877, 878, "Brief-reigning king of Alba, killed after about a year.", ["Aed mac Cinaeda"]),
    ("giric-scotland", "Giric", 878, 889, "King of Alba whose relationship to the Alpinid line is obscure; may have ruled jointly with Eochaid.", ["Giric mac Dungail"]),
    ("eochaid-scotland", "Eochaid", 878, 889, "Grandson of Kenneth I recorded as ruling Alba, perhaps jointly with Giric.", ["Eochaid mac Run"]),
    ("donald-ii-scotland", "Donald II", 889, 900, "First king styled ri Alban, king of Alba, in the annals.", ["Domnall mac Custantin"]),
    ("constantine-ii-scotland", "Constantine II", 900, 943, "Long-reigning king who fought AEthelstan and lost at Brunanburh, later retiring to St Andrews.", ["Constantin mac Aeda"]),
    ("malcolm-i-scotland", "Malcolm I", 943, 954, "King of Alba who received Strathclyde or Cumbria from the English and raided Northumbria.", ["Mael Coluim mac Domnaill"]),
    ("indulf-scotland", "Indulf", 954, 962, "King of Alba during whose reign Edinburgh was said to have been taken from the Northumbrians.", ["Ildulb mac Constantin"]),
    ("dub-scotland", "Dub", 962, 967, "King of Alba killed in the dynastic feuding between the rival Alpinid branches.", ["Dub mac Maile Coluim", "Duff"]),
    ("cuilen-scotland", "Cuilen", 967, 971, "King of Alba killed by the men of Strathclyde.", ["Cuilen mac Ilduilb", "Culen"]),
    ("kenneth-ii-scotland", "Kenneth II", 971, 995, "King of Alba who raided Northumbria and was killed in a dynastic conspiracy.", ["Cinaed mac Maile Coluim"]),
    ("amlaib-scotland", "Amlaib", 973, 977, "Brother of Cuilen recorded as briefly ruling Alba in opposition to Kenneth II.", ["Olaf of Alba"]),
    ("constantine-iii-scotland", "Constantine III", 995, 997, "Short-reigning king of Alba killed in the continuing dynastic feud.", ["Constantin mac Cuilein"]),
    ("kenneth-iii-scotland", "Kenneth III", 997, 1005, "King of Alba killed at Monzievaird by his successor Malcolm II.", ["Cinaed mac Duib"]),
    ("malcolm-ii-scotland", "Malcolm II", 1005, 1034, "King who won at Carham in 1018, securing Lothian, and extended Scottish authority southwards.", ["Mael Coluim mac Cinaeda"]),
    ("duncan-i-scotland", "Duncan I", 1034, 1040, "Grandson of Malcolm II whose failed campaigns ended with his killing by Macbeth.", ["Donnchad mac Crinain"]),
    ("macbeth-scotland", "Macbeth", 1040, 1057, "King of Alba for seventeen years, remembered as a capable ruler who went on pilgrimage to Rome; killed at Lumphanan.", ["Mac Bethad mac Findlaich", "MacBeth"]),
    ("lulach-scotland", "Lulach", 1057, 1058, "Stepson of Macbeth, briefly king and killed in 1058.", ["Lulach the Unfortunate"]),
]:
    E(slug, name, "reign", s, e, SC, summ + " " + SC_NOTE, al, conf="medium")

E("malcolm-iii-scotland", "Malcolm III Canmore", "reign", 1058, 1093, SC,
  "King who killed Macbeth's heir, married the Saxon princess Margaret and raided England repeatedly until his death at Alnwick.",
  ["Mael Coluim Cenn Mor", "Malcolm Canmore"], dm="received", conf="medium")
for slug, name, s, e, summ, al in [
    ("donald-iii-scotland", "Donald III Bane", 1093, 1097, "Brother of Malcolm III who twice seized the throne in reaction against Anglo-Norman influence; deposed and blinded.", ["Donald Bane", "Domnall Ban"]),
    ("duncan-ii-scotland", "Duncan II", 1094, 1094, "Son of Malcolm III installed with English help and killed within months.", ["Donnchad mac Maile Coluim"]),
    ("edgar-scotland", "Edgar", 1097, 1107, "Son of Malcolm III and Margaret, who ruled peacefully under English patronage.", ["Edgar of Scotland"]),
    ("alexander-i-scotland", "Alexander I", 1107, 1124, "King who ruled southern Scotland while his brother David held the south-west; patron of the reformed Church.", ["Alexander the Fierce"]),
    ("david-i-scotland", "David I", 1124, 1153, "Reforming king who introduced feudal tenure, burghs, sheriffs and a silver coinage, and invaded England during the Anarchy.", ["Saint David of Scotland"]),
    ("malcolm-iv-scotland", "Malcolm IV", 1153, 1165, "Boy king known as the Maiden who ceded the northern English counties to Henry II.", ["Malcolm the Maiden"]),
    ("william-i-scotland", "William I the Lion", 1165, 1214, "Long-reigning king captured at Alnwick in 1174, whose Treaty of Falaise made Scotland briefly a fief of England.", ["William the Lion"]),
    ("alexander-ii-scotland", "Alexander II", 1214, 1249, "Settled the border by the Treaty of York in 1237 and extended royal power into the west.", ["Alexander of Scotland II"]),
    ("alexander-iii-scotland", "Alexander III", 1249, 1286, "Won the Hebrides by the Treaty of Perth in 1266; his death without an heir precipitated the succession crisis.", ["Alexander of Scotland III"]),
    ("margaret-maid-of-norway", "Margaret, Maid of Norway", 1286, 1290, "Infant granddaughter of Alexander III recognised as heir; her death at sea in 1290 opened the Great Cause.", ["Maid of Norway"]),
    ("john-balliol", "John Balliol", 1292, 1296, "Chosen king by Edward I's arbitration in the Great Cause and deposed after refusing English demands.", ["Toom Tabard", "John of Scotland"]),
    ("robert-i-scotland", "Robert I the Bruce", 1306, 1329, "Won Scottish independence at Bannockburn in 1314 and secured recognition by the Treaty of Edinburgh-Northampton.", ["Robert the Bruce"]),
    ("david-ii-scotland", "David II", 1329, 1371, "Son of Bruce whose reign included defeat and long captivity in England after Neville's Cross.", ["David Bruce"]),
    ("edward-balliol", "Edward Balliol", 1332, 1336, "English-backed claimant crowned in 1332 who held parts of Scotland intermittently before abandoning his claim.", ["Edward de Balliol"]),
    ("robert-ii-scotland", "Robert II", 1371, 1390, "First Stewart king, nephew of David II, whose reign saw renewed border war with England.", ["Robert Stewart"]),
    ("robert-iii-scotland", "Robert III", 1390, 1406, "Physically infirm king whose government was largely run by his brother the Duke of Albany.", ["John Stewart, Robert III"]),
    ("james-i-scotland", "James I of Scotland", 1406, 1437, "Held prisoner in England until 1424, then ruled forcefully at home; assassinated at Perth in 1437.", ["James Stewart I"]),
    ("james-ii-scotland", "James II of Scotland", 1437, 1460, "Broke the power of the Black Douglases and was killed by an exploding cannon at Roxburgh.", ["James of the Fiery Face"]),
    ("james-iii-scotland", "James III of Scotland", 1460, 1488, "Unpopular king who pursued peace with England and was killed at Sauchieburn.", ["James Stewart III"]),
    ("james-iv-scotland", "James IV of Scotland", 1488, 1513, "Renaissance king who married Margaret Tudor and died with much of his nobility at Flodden.", ["James Stewart IV"]),
    ("james-v-scotland", "James V of Scotland", 1513, 1542, "King who allied with France, taxed the Church heavily and died shortly after the defeat at Solway Moss.", ["James Stewart V"]),
    ("mary-queen-of-scots", "Mary, Queen of Scots", 1542, 1567, "Queen from six days old, briefly Queen of France, forced to abdicate in 1567 and later executed in England.", ["Mary Stuart", "Mary I of Scotland"]),
    ("james-vi-scotland", "James VI of Scotland", 1567, 1625, "King of Scots from infancy who inherited England in 1603 and thereafter ruled both kingdoms from London.", ["James VI and I"]),
    ("charles-i-scotland", "Charles I of Scotland", 1625, 1649, "King of Scots whose prayer book policy provoked the Covenanting revolt and the Bishops' Wars.", ["Charles Stuart of Scotland"]),
    ("charles-ii-scotland", "Charles II of Scotland", 1649, 1685, "Proclaimed King of Scots in 1649 and crowned at Scone in 1651, though exiled until the Restoration of 1660.", ["Charles Stuart II of Scotland"]),
    ("james-vii-scotland", "James VII of Scotland", 1685, 1689, "Scottish reign of James II of England, ended when the Convention of Estates declared the throne forfeited.", ["James Stuart VII"]),
    ("william-ii-mary-ii-scotland", "William II and Mary II of Scotland", 1689, 1694, "Joint Scottish monarchs after the Revolution settlement, which also re-established Presbyterian church government.", ["William of Orange in Scotland"]),
    ("anne-scotland", "Anne, Queen of Scots", 1702, 1707, "Last monarch of an independent Kingdom of Scotland before the Union of 1707.", ["Queen Anne of Scotland"]),
]:
    E(slug, name, "reign", s, e, SC, summ, al, dm=("calendar" if s >= 1066 else "received"))

# ---------------- Monarchs of Great Britain and the United Kingdom ----------------
GB = "Kingdom of Great Britain"
UK = "United Kingdom"
E("anne-great-britain", "Anne, Queen of Great Britain", "reign", 1707, 1714, GB,
  "First sovereign of the united Kingdom of Great Britain, whose reign saw the War of the Spanish Succession and Marlborough's victories.",
  ["Queen Anne"])
E("george-i", "George I", "reign", 1714, 1727, GB,
  "Elector of Hanover who succeeded under the Act of Settlement; his reign saw the 1715 Jacobite rising and the South Sea Bubble.",
  ["Georg Ludwig"])
E("george-ii", "George II", "reign", 1727, 1760, GB,
  "Last British monarch to lead troops in battle, at Dettingen in 1743; his reign covered the 1745 rising and the Seven Years War's opening.",
  ["George Augustus"])
E("george-iii", "George III", "reign", 1760, 1820, GB,
  "Reigned through the loss of the American colonies, the union with Ireland and the wars with France, and suffered recurrent mental illness.",
  ["Farmer George"])
E("george-iv", "George IV", "reign", 1820, 1830, UK,
  "Regent from 1811 and then king, famous for extravagance, patronage of the arts and the failed attempt to divorce Queen Caroline.",
  ["Prince Regent", "George Augustus Frederick"])
E("william-iv", "William IV", "reign", 1830, 1837, UK,
  "Sailor king whose short reign saw the Great Reform Act, the abolition of slavery in the colonies and the new Poor Law.",
  ["the Sailor King"])
E("queen-victoria", "Victoria", "reign", 1837, 1901, UK,
  "Longest-reigning monarch until Elizabeth II, Empress of India from 1876, presiding over industrial and imperial expansion.",
  ["Queen Victoria", "Empress of India"])
E("edward-vii", "Edward VII", "reign", 1901, 1910, UK,
  "First Saxe-Coburg-Gotha monarch, whose reign saw the Entente Cordiale and the constitutional clash over the People's Budget.",
  ["Bertie", "Albert Edward"])
E("george-v", "George V", "reign", 1910, 1936, UK,
  "Reigned through the First World War, renamed the dynasty Windsor in 1917 and oversaw Irish partition and the first Labour government.",
  ["George Frederick Ernest Albert"])
E("edward-viii", "Edward VIII", "reign", 1936, 1936, UK,
  "Reigned for 326 days in 1936 before abdicating to marry Wallis Simpson; later Duke of Windsor.",
  ["Duke of Windsor", "David"])
E("george-vi", "George VI", "reign", 1936, 1952, UK,
  "Unexpected king who became a symbol of resistance in the Second World War and saw Indian independence and the founding of the NHS.",
  ["Albert Frederick Arthur George", "Bertie"])
E("elizabeth-ii", "Elizabeth II", "reign", 1952, 2022, UK,
  "Longest-reigning British monarch, presiding over decolonisation, the creation of the Commonwealth as a free association and seven decades of change.",
  ["Queen Elizabeth II", "Elizabeth Alexandra Mary"])
E("charles-iii", "Charles III", "reign", 2022, None, UK,
  "Acceded on the death of Elizabeth II in September 2022 and was crowned in May 2023; reigning monarch of the United Kingdom.",
  ["King Charles III", "Charles Philip Arthur George"], extant=True)
