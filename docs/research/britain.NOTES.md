# britain.json — coverage notes

442 entries, written from recall (no web search), schema exactly as specified.

Breakdown by kind: reign 198, event 156, polity 55, era 21, period 12.

## What is covered
- **English monarchs**: Alfred the Great (871) through Anne (to 1707), including the Danish kings, Edgar the Ætheling, Empress Matilda, Lady Jane Grey, Philip of Spain as jure uxoris king, and separate entries for the interrupted reigns (Æthelred restored, Henry VI readeption, Edward IV first/second), plus Oliver and Richard Cromwell as Lord Protector.
- **Scottish monarchs**: Kenneth I MacAlpin (843) through Anne (to 1707), including Macbeth, Lulach, the Balliols, Margaret Maid of Norway.
- **Great Britain / UK monarchs**: Anne 1707 through Charles III (extant, end_year null).
- **Prime ministers**: 82 ministry-level entries, Walpole 1721 → Starmer 2024 (extant), with repeat premierships as separate entries (Newcastle, Rockingham, Pitt, Portland, Derby ×3, Palmerston, Russell, Gladstone ×4, Salisbury ×3, Baldwin ×3, MacDonald, Churchill, Wilson, plus Wellington's 1834 caretaker ministry).
- **Polities**: Roman Britain, sub-Roman Britain, the seven Heptarchy kingdoms individually (plus Bernicia, Deira, York/Jórvík), Danelaw, England, Scotland, Pictland, Dál Riata, Strathclyde, the Welsh kingdoms and Principality, Lordship and Kingdom of Ireland, Gaelic Ireland, Commonwealth and Protectorate, Great Britain 1707, UK 1801, UK 1922 (extant), British Empire (with first/second empire periods), Northern Ireland, Irish Free State, Republic of Ireland, Isle of Man, Channel Islands, Lordship of the Isles.
- **Dynasties** (kind "polity"): Wessex, Denmark/Knýtlinga, Normandy, Blois, Plantagenet, Lancaster, York, Tudor, Stuart, Orange-Nassau, Hanover, Saxe-Coburg-Gotha, Windsor (extant), plus Alpin, Dunkeld, Balliol, Bruce and the Jacobite succession.
- **Wars**: all requested, plus Roman conquest, Boudica, Barons' Wars, conquest of Wales, both Scottish independence wars, Glyndŵr, Anglo-Spanish, Nine Years War in Ireland, Bishops' Wars, all three Civil Wars and the Wars of the Three Kingdoms, Cromwellian and Williamite Ireland, Spanish and Austrian Succession, American Independence, 1798, Revolutionary/Napoleonic/Peninsular/1812, Crimea, 1857, both Boer wars, both World Wars with Dunkirk/Battle of Britain, Korea, Suez, Malaya, Mau Mau, Troubles and Bloody Sunday, Falklands, Gulf, Iraq, Afghanistan.
- **Constitutional/political events**: all requested, plus Domesday, Provisions of Westminster, de Montfort's parliament, Declaration of Arbroath, Peasants' Revolt, Act of Supremacy, Pilgrimage of Grace, Prayer Book, Elizabethan and Scottish Reformations, Plantation of Ulster, Gunpowder Plot, Petition of Right, Personal Rule, Long Parliament, regicide, Navigation Acts, Restoration, plague and fire, Habeas Corpus, Exclusion Crisis, Claim of Right, Bank of England, Act of Settlement, Septennial Act, South Sea Bubble, Highland Clearances, Somerset case, Gordon Riots, Peterloo, all Reform Acts and the 1918/1928 franchise acts, slavery abolition, New Poor Law, Chartism, Corn Laws, Great Exhibition, 1870 Education Act, Ballot Act, Home Rule Bills, People's Budget, Parliament Act, suffrage movement, Government of Ireland Act, Anglo-Irish Treaty, Statute of Westminster, abdication, Beveridge, 1944 Education Act, NHS, nationalisation, Windrush, decolonisation, Indian partition, modern Commonwealth, EEC accession and 1975 referendum, Winter of Discontent, miners' strike, privatisation, poll tax, Black Wednesday, Good Friday Agreement, devolution, Lords Act, HRA, 2014 indyref, Brexit referendum and withdrawal, Covid-19.
- **Eras/periods**: Industrial and Agricultural Revolutions, Georgian, Regency, Victorian (with early/mid/late sub-periods), Edwardian, interwar, Great Depression, Great Famine, Blitz, postwar austerity and consensus, Swinging Sixties, Thatcherism, New Labour, 2010s austerity, Brexit era, cost of living crisis, plus Tudor/Elizabethan/Jacobean/Caroline/Interregnum/Restoration/Augustan, Scottish Enlightenment, Black Death, high and late medieval England.

## Dating conventions applied
- `start_dating_method: "calendar"` for every entry starting 1066 or later; no uncertainty bounds anywhere.
- `"received"` for Anglo-Saxon, Pictish, Gaelic and early Scottish material, with the uncertainty stated in the summary text (chronicle/king-list tradition).
- `"first-attestation"` used for Mercia and East Anglia, whose foundation dates rest on first record rather than an event.
- `extant: true` with `end_year: null` for: the United Kingdom, Northern Ireland, Republic of Ireland, Isle of Man, Channel Islands, House of Windsor, Charles III, Keir Starmer.

## Build files
`build_britain_1.py` (monarchs), `build_britain_2.py` (everything else), `build_britain_main.py` (assembles, validates key order, slug uniqueness, summary length/newlines, dating rules, extant consistency, then writes `britain.json`).
