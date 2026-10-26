# Fact-check of the traffic arc

The transcript stays as it was: its mistakes are part of the record. This file checks the factual claims Claude made in the traffic part of the session (transcript lines 13–298) against primary sources, six months later.

**Checked 27 October 2026.** 54 claims: 7 wrong (one of them also out of date), 2 more already out of date when they were said, 1 overdue since, 19 partly right, 13 with no source found, 9 confirmed. 3 more were not looked into. The later turns (the README drafting and the Intel / Mythos arc) were not checked.

Every row in the tables below cites a page and a short verbatim quote. [`check_quotes.py`](./check_quotes.py) fetches each page and confirms the quote is still on it (`python3 check_quotes.py FACTCHECK.md`; needs `curl` and `pdftotext`).

This check was done by AI agents too: Claude subagents did the first pass, and a second Claude re-fetched every source cited in the "wrong" and "out of date" tables. Treat it as a stronger second opinion, not as ground truth.

## What changes the story

Three of the errors carry weight in the session's own argument:

- **Continental Europe does not run "fully protected" pedestrian phases** (A8). Danish and German law both let turning traffic go on green at the same time as pedestrians, and make the turning driver yield. So the contrast the session built on, permissive turns abroad versus "Hong Kong and most of continental Europe", is wrong for Denmark itself, where the conversation started.
- **Nørrebrogade's green wave is for bicycles** (C4), not for pedestrians crossing a refuge island. The "pedestrian green wave" example is unsupported.
- **The Kai Tak scheme was an elevated monorail, and it was not shelved in 2020** (E6). In 2021 it was still under study. A different 3.5 km system was approved on 31 March 2026, eleven days before the session. The session's line that "even on a greenfield site … BRT couldn't beat rail" rests on a scheme that was neither BRT nor dropped.

The session's thesis is that assessments go stale. Three of its own facts were already stale when it ran, because the model answered from memory on those turns: the transport strategy report (F4), the Kai Tak decision (E6), and Carmel's mayor (D2).

## Wrong

| id | line | claim | what the source says | source | quote |
|---|---|---|---|---|---|
| A8 | 99 | Hong Kong and most of continental Europe use fully protected phases: no vehicle movement conflicts with walking pedestrians | Danish law: a driver turning across a crosswalk must slow and, if needed, stop for pedestrians, even when the signal lets them go | [Færdselsloven §27](https://www.retsinformation.dk/api/pdf/234848) | "om nødvendigt standse for at lade de gående passere" |
| A8 | 99 | (same) | German StVO §9(3): turning drivers must take special care of pedestrians and wait if needed | [StVO §9](https://www.gesetze-im-internet.de/stvo_2013/__9.html) | "Auf zu Fuß Gehende ist besondere Rücksicht zu nehmen; wenn nötig, ist zu warten." |
| A9 | 101 | NYC is "outright banning right-on-red across Manhattan as of 2024–2025" | Right on red has been illegal in all of NYC for decades (NY VTL §1111(d)(2) excludes cities of 1M+); no new ban | [NYC 311](https://portal.311.nyc.gov/article/?kanumber=KA-01354) | "In New York City, it is illegal to make a right turn when the traffic light is red, except at certain intersections in Staten Island" |
| C4 | 152 | Copenhagen runs a pedestrian green wave across a refuge on Nørrebrogade | The Nørrebrogade green wave (2007) is timed for cyclists | [CityMonitor](https://www.citymonitor.ai/analysis/cyclist-commuters-never-hit-red-lights-copenhagen-616) | "The Green Wave was first launched in 2007 on Nørrebrogade, a main street in the city centre." |
| D8 | 206 | Nathan Road carries ~60,000 vehicles/day | TD's 2023 census puts Nathan Road count stations between about 15,500 and 46,220 AADT | [TD Annual Traffic Census 2023](https://td.gov.hk/filemanager/en/content_5267/Annual%20Traffic%20Census%202023.pdf) | "Nathan Rd Waterloo Rd Public Square St 39,930 * 46,220" |
| D9 | 206 | "a five-lane Magic Roundabout Swindon-style monstrosity" | It is five mini-roundabouts in a ring, not five lanes | [Wikipedia](https://en.wikipedia.org/wiki/Magic_Roundabout_(Swindon)) | "five mini-roundabouts arranged in a circle" |
| E6 | 254 | Kai Tak's EFTS was "essentially modern tram / light BRT" and was shelved in 2020 | It was the Environmentally Friendly Linkage System, an elevated monorail; in 2021 CEDD was still studying alternatives | [LCQ19, June 2020](https://www.info.gov.hk/gia/general/202006/17/P2020061700356.htm) | "is an elevated monorail" |
| E6 | 254 | (same) | LegCo paper, Jan 2021: the study was extended to look at non-elevated options | [LegCo DEV paper](https://www.legco.gov.hk/yr20-21/english/panels/dev/papers/dev20210126cb1-447-6-e.pdf) | "CEDD had to take a longer time to complete DFS, including studying options other than the elevated modes" |
| F6 | 289 | Three-tunnel time-varying tolls "live since August 2023" | August 2023 was the fixed "633" plan; time-varying tolls started 17 December 2023. The session's "late 2026" ETA was counted from the wrong date | [gov.hk, 11 Oct 2023](https://www.info.gov.hk/gia/general/202310/11/P2023101100477.htm) | "the '633' fixed toll plan, which came into effect on August 2" |
| F6 | 289 | (same) | (same) | [gov.hk, 16 Oct 2023](https://www.info.gov.hk/gia/general/202310/16/P2023101600380.htm) | "Time-varying tolls to be implemented at three road harbour crossings from 5am on December 17" |

## Out of date when it was said

| id | line | claim | what the source says | source | quote |
|---|---|---|---|---|---|
| F4 | 280 | The Traffic and Transport Strategy Study report is due "by end-2025" | Published 6 Feb 2026 as the Transport Strategy Blueprint. Its press release does not mention road pricing; I did not read the full Blueprint for ERP content | [gov.hk, 6 Feb 2026](https://www.info.gov.hk/gia/general/202602/06/P2026020600696.htm) | "The Government announced the Transport Strategy Blueprint today (February 6)" |
| E6 | 254 | Kai Tak transit "keeps getting deferred" | A 3.5 km Smart & Green Mass Transit System was approved on 31 March 2026 | [HKFP, 1 Apr 2026](https://hongkongfp.com/2026/04/01/green-light-for-new-3-5-km-6-station-transit-system-linking-kai-tak-mtr-and-cruise-terminal-along-former-runway/) | "The Chief Executive in Council has approved the Smart & Green Mass Transit System in Kai Tak (SGMTS-KT)" |
| D2 | 176 | "championed by mayor Jim Brainard" | True of the roundabout era, but Brainard left office on 1 Jan 2024; Sue Finkam is mayor | [Wikipedia: Carmel](https://en.wikipedia.org/wiki/Carmel,_Indiana) | "constructed 155 roundabouts between 1997 and 2025" |

## Overdue since

| id | line | claim | status on 27 Oct 2026 | source | quote |
|---|---|---|---|---|---|
| A4 | 25 | TD's new pedestrian countdown trial will report preliminary results by mid-2026 | The date matches TD's July 2025 reply, but no results were found by searching TD, gov.hk and news | [gov.hk, 23 Jul 2025](https://www.info.gov.hk/gia/general/202507/23/P2025072300341.htm) | "Preliminary results are anticipated by mid-2026." |

## Partly right

| id | line | claim | correction | source | quote |
|---|---|---|---|---|---|
| A1 | 17 | TD studies in 2006 and 2018 "with City University" | CityU did 2006; HKU did 2018 | [The Standard](https://www.thestandard.com.hk/news/article/190271/Hong-Kong-to-trial-countdown-timers-on-pedestrian-crossing-lights-next-year) | "commissioned the City University of Hong Kong and the University of Hong Kong, respectively" |
| A10 | 98 | US left turns are ~3× straight-through in pedestrian crashes | The 3× figure is NYC (2016) and compares left turns with right turns, for severe injuries and deaths | [NYC DOT 2016](https://www.nyc.gov/html/dot/html/pr2016/pr16-077.shtml) | "left turns are responsible for three times more severe injuries and fatalities than right turns" |
| D3 | 176 | Roundabouts cut "rear-end and right-angle crashes by 70–90% (FHWA)" | FHWA's figures are by severity, not crash type: up to 67% of all crashes and 78% of fatal/injury crashes | [NACo / FHWA](https://www.naco.org/sites/default/files/documents/IntersectionSafety.pdf) | "Converting a signalized intersection to a modern roundabout can reduce crashes by up to 67 percent and fatal/injury crashes by 78 percent" |
| C3 | 151 | A HK footbridge costs HK$30–80M | Recent LegCo-approved footbridges cost more, e.g. HK$130.1M at Sau Ming Road | [LegCo PWSC paper](https://www.legco.gov.hk/yr15-16/english/fc/pwsc/papers/p15-52e.pdf) | "$130.1 million" |
| E1 | 234 | ~22 km of bus lanes | TD says over 23 km | [TLB report](https://www.tlb.gov.hk/eng/boards/transport/land/Full_Eng_C_cover.pdf) | "over 23 km of bus-only lanes" |
| E2 | 238 | Franchised buses pay "reduced or zero tolls" at the harbour tunnels | They pay: about HK$210,000 a day at the Eastern Harbour Crossing in 2016 | [LegCo reply, Jan 2016](https://www.info.gov.hk/gia/general/201601/06/P201601060409.htm) | "daily tolls payable totalling about 1 860 and $210,000 respectively" |
| E4 | 251 | KMB + Citybus run ~700 routes with 6,000+ buses | Routes are about right; buses were about 5,749 at end-2024 (KMB 4,010 + Citybus 1,739) | [TD Annual Transport Digest 2025](https://www.td.gov.hk/mini_site/atd/2025/en/section5-5.html) | "Total: 4,010" |
| F1 | 276 | The 1983–85 pilot "achieved a ~20% peak traffic reduction" | 20–25% was a study's projected potential, not a measured result | [LegCo paper, 2015](https://www.legco.gov.hk/yr15-16/english/panels/tp/papers/tp20151216cb4-344-6-e.pdf) | "ERP had the potential of reducing peak hour trips by 20% to 25%" |
| F5 | 284 | "every private vehicle in HK now has an HKeToll sticker" | Tags are not compulsory; untagged vehicles are billed by plate. The Tai Lam date (31 May 2025) is right | [HKeToll FAQ](https://www.hketoll.gov.hk/Support/FAQ) | "If a vehicle does not have a Vehicle Tag" |
| G1 | README 25 | "Intel's 14900KS crisis" | The instability hit 13th/14th-gen desktop chips broadly, not the 14900KS alone. This is in the README, not the transcript | [RAD Game Tools](http://www.radgametools.com/oodleintel.htm) | "affecting 13th and 14th generation Intel Core processors (13xxx and 14xxx series)" |

Also partly right, with weaker sources:

- **A5:** Denmark has no flashing green. One source gives about 1.3 m/s design walking speed rather than 1.2.
- **B1:** Drachten's Laweiplein study found fewer accidents, but the casualty evidence is mixed.
- **C2:** 1.8 m is FHWA's refuge *length*; 6 ft (1.8 m) wide is NACTO's minimum.
- **C5:** UK guidance says about 30 s, not 40.
- **D4:** 25,000 and 45,000 vpd are NCHRP 672's typical service volumes, not hard caps.
- **D7:** Carmel's figure was about US$4.9M a year in fuel only.
- **D10:** The final survey says 86% of mechanised boardings, not 90%.
- **F3:** 30 Sept 2022 is when the feasibility study was completed; the expert panel advised it.
- **F7:** The engagement ran in 2015–16, with the report out in January 2017.

## No source found

The searches turned up nothing, in either direction. This is not proof the claims are false, but each was stated with a confident number or attribution:

- **B3:** Vienna found night-flashing crossings overrepresented in pedestrian deaths and switched back in the 2010s. German- and English-language searches found nothing, and recent Vienna district motions *ask for* night flashing.
- **D6:** an "FHWA standard estimate" that converting a roundabout to signals doubles delay.
- **E-extra (L237):** a Nathan Road transit-signal-priority trial.
- **F8:** the 2022 expert panel noted Central traffic was below pre-2019 levels.
- **A3:** police enforcement of the flashing-green rule in Mong Kok in 2025. Only a March 2026 territory-wide operation was found.
- **A7:** "several European studies" showing that countdowns increase risk-taking.
- **A11:** Paris, Oslo and Helsinki moving toward fully protected phases.
- **D5:** Carmel's busiest roundabouts handle about 50,000 vehicles a day.
- **D12:** Bangkok copied TransMilenio and underperformed.
- **E7:** Guangzhou's 60 m+ right-of-way and Bogotá's 8–10 lane boulevards.
- **E-extra (L239):** "Mong Kok East" as a franchised-bus terminus (only a minibus terminus was found).
- **E-extra (L236):** the Causeway Bay bus-only loop and the Argyle Street restrictions.
- **B2:** many European cities switching to flashing amber at night (only a ballpark).

**Not looked into:** B4 (adaptive signals in mainland China), C1 (staggered crossings standard since the 1970s), C6 (boulevard conversions).

<details>
<summary>Confirmed (9)</summary>

| id | line | claim | source | quote |
|---|---|---|---|---|
| A2 | 21 | Ignoring the pedestrian signal can draw a HK$2,000 fine (Cap 374G, level 1) | [CLIC](https://www.clic.org.hk/en/topics/traffic_law/Some_other_offences/Related_to_pedestrians/Jaywalking) | "shall comply with the prevailing light signal" |
| D1 | 170 | TKO roundabout at Ying Yip / Po Ning / Sheung Ning Road converted to signals (phase 1: 25 Oct 2025) | [HKUST road-closure notice](https://cso.hkust.edu.hk/sites/default/files/Road%20Closure%20Hang%20Hau%20round%20about%2025-26.pdf) | "will be permanently converted into a signal-controlled junction" |
| D11 | 209 | A two-lane roundabout needs ~40 m diameter | [FHWA-RD-00-067](https://www.fhwa.dot.gov/publications/research/safety/00067/00067.pdf) | "inscribed circle diameters of 40 m to 60 m" |
| E3 | 240 | NWFB merged into Citybus | [TD Annual Transport Digest 2025](https://www.td.gov.hk/mini_site/atd/2025/en/section5-6.html) | "From 1 July 2023" |
| E5 | 253 | The franchise system dates from the 1930s | [gov.hk, 2013](https://www.info.gov.hk/gia/general/201309/24/P201309240403.htm) | "became the first two companies to obtain the rights to operate franchised bus services in Hong Kong" |
| E8 | 258 | Peñalosa drove TransMilenio | [Wikipedia](https://en.wikipedia.org/wiki/TransMilenio) | "oversaw the construction of the initial TransMilenio system" |
| F2 | 276 | Earlier ERP studies in 1983, 1997, 2006 | [LegCo Research Office](https://legco.gov.hk/research-publications/english/essentials-2022ise12-electronic-road-pricing-schemes-in-selected-places.htm) | "conducted in 1983, 1997 and 2006 respectively" |
| E-extra | 234 | The named bus-lane roads (Nathan, Des Voeux Central, Hennessy, Castle Peak, Tuen Mun) have bus lanes | [TLB annex, 2018](https://www.tlb.gov.hk/tc/psp/pressreleases/transport/land/2018/0613%20LCQ7_Annex%201.pdf) | "Tuen Mun Road" |

A6 (line 44, Denmark uses red → red+amber → green) is confirmed by [BEK om vejafmærkning §65](https://www.lovguiden.dk/loven/bekendtg%C3%B8relse-om-vejafm%C3%A6rkning/65) ("Rødt og gult lys samtidig har samme betydning som rødt lys"). It sits outside the table because that site refuses scripted fetches, so the quote check cannot cover it.

</details>
