# South Downs Way Trip Planning

## Overview

Planning a multi-day walk on the South Downs Way. **Dates: Friday 24 April to Monday 4 May 2026 inclusive (11 days).** Travel from Bradford-on-Avon on Friday evening after work. Originally planned Saturday 25 April start but shifted to Friday to avoid Saturday-night accommodation premiums in Winchester.

It's for a couple - experienced walkers but not fast, aged 50-ish. We can probably go 8-12 miles per day. We won't be carrying a tent. We are price-sensitive, will need accommodation every night, high preference for accommodation on-trail or close walk to trail.

We want to walk west to east, starting in Winchester. We won't make it all the way to Eastbourne, just want to complete a comfortable amount of the trail within our constraints.

## Key Resources

- https://www.nationaltrail.co.uk/en_GB/trails/south-downs-way/
- https://www.nationaltrail.co.uk/en_GB/trails/south-downs-way/accommodation/
- Official mileage chart PDF: https://fulking.net/wp-content/uploads/2012/07/South_Downs_Way_mileage_chart.pdf

Keep in mind suggested "sections" may be too long for our capabilities.

### Google Sheets Spreadsheet
- **Title:** "South Downs Way (Claude)"
- **Spreadsheet ID:** `1mHPA6HjeplBMZp_YTz1PTAJUNkSDeDZDMP93Q_KI-TQ`
- **URL:** https://docs.google.com/spreadsheets/d/1mHPA6HjeplBMZp_YTz1PTAJUNkSDeDZDMP93Q_KI-TQ
- **Access:** Read/write via Google Sheets API v4 using `gcloud auth print-access-token` (authenticated as rossarn@gmail.com). The CSV export endpoint doesn't work; use the REST API at `sheets.googleapis.com/v4/spreadsheets/{id}` instead.

## Files

- **CLAUDE.md** - This file. Project context and constraints.
- **route-reference.md** - Comprehensive waypoint table with cumulative distances (from official SDW mileage chart), elevation profile, 12 official Cicerone stages, river crossings, rail bail-out points, and A-road crossings.
- **south-downs-way-main-plan.csv** - Draft 6-day itinerary (Winchester to Pyecombe). Generated from a previous LLM session. **Distances are roughly correct but accommodation names/prices are unverified and likely inaccurate.**
- **accommodation-options.md** - Researched accommodation for miles 0–37 (Winchester to Cocking). Prices web-sourced March 2026; some unconfirmed and marked for phone verification. Includes emerging plan, staging analysis, and phone call priority list.
- **accommodation-research-buriton-area.md** - Detailed Buriton-area research notes (raw findings, supplementary to main file).
- **accommodation-research-pyecombe-area.md** - Pyecombe area research (too pricey/unavailable) + Brighton options for Day 6 night.
- **South_Downs_Way_Elev.gpx** - GPX track with elevation data (~10k trackpoints). **Contains alternative routes** so total distance is ~249mi rather than ~100mi. Not suitable for direct distance/elevation calculations without filtering.
- **sdw-linear.gpx** - Clean single-track GPX from Saturday Walkers Club (784 trackpoints with elevation). Suitable for analysis. Non-commercial use only.
- **analyze_gpx.py** - Python script to parse GPX and compute per-stage distances, ascent, and descent. Uses scaled mileage-chart distances to locate stage boundaries on the GPX track.
- **food-research-cocking-area.md** - Food options in Cocking village and on trail miles 25–37. Key finding: Blue Bell pub CLOSED Mondays (Day 3 arrival). Cadence cafe on ridge open daily 9–15:30. Manor Farm provides continental breakfast. Action items for phone calls.

## Key Findings So Far

### Distances (from official mileage chart, cross-checked against web sources March 2026)
The current plan covers Winchester (mile 0) to Pyecombe (mile 68) in 6 walking days. Distances are accommodation-to-accommodation including off-trail detours:
- Day 1: Winchester → Meonstoke = ~12.4mi (11.9 trail + 0.57 off-trail to Bucks Head). Web: 12–12.5mi Winchester to Exton.
- Day 2: Meonstoke → Hampshire Hog, Clanfield = ~12mi (10.7 trail + 0.57 + 0.49 off-trail, over Butser Hill). Web: 12.5mi Exton to Buriton (our leg slightly shorter).
- Day 3: Hampshire Hog → Manor Farm (on trail above Cocking) = ~12mi (11.5 trail + 0.5 off from Hog). Web: 11.1mi Buriton to Cocking (we start ~1mi before Buriton). Manor Farm is ON trail so no descent to Cocking village.
- Day 4: Manor Farm → Amberley = ~12mi (on trail, mile 36.5 to 48.5). Web: 11.8–12mi Cocking to Amberley.
- Day 5: Amberley → Steyning = ~11mi (10 trail + 1 off to Steyning). Web: 10–11mi confirmed.
- Day 6: Steyning → Pyecombe = ~10.5mi (1 back to trail + 9.5 trail). Web: consistent with Cicerone stages 7+8 combined.

### Elevation (from GPX analysis)
The CSV systematically underestimates climbing. GPX-derived figures for on-trail ascent/descent:

| Stage | Ascent | Descent | Notes |
|-------|--------|---------|-------|
| Day 1 | 326m | 314m | |
| Day 2 | 503m | 430m | Toughest day - Butser Hill (270m, highest point) |
| Day 3 | 439m | 437m | Harting Down |
| Day 4 | 422m | 435m | |
| Day 5 | 407m | 356m | Chanctonbury Ring |
| Day 6 | 339m | 457m | Devil's Dyke |

### Important: Off-trail accommodation adds climbing
The SDW is a ridge walk. Many overnight stops (Exton, Buriton, Cocking, Steyning) are in valleys below the ridge. This means descending off the ridge each evening and re-ascending the next morning - potentially adding 100-200m extra climb per day that is NOT captured in the GPX figures. Prioritising on-trail or ridge-top accommodation avoids this penalty.

### Accommodation Research Progress (March 2026)
Miles 0–37 (Winchester to Cocking) are researched in detail in accommodation-options.md. Key confirmed prices:
- Winchester Travelodge: £70 (Fri 24 Apr) — Saturday pricing £99+ is terrible
- King Alfred Winchester: £103 inc breakfast — **sold out Sat 25 Apr**
- Black Hole Winchester: £172 Sat / ~£89–119 other nights
- Complyns, Chilcomb: £70 inc breakfast (mile 2.5, ON trail)
- Crossways B&B, Exton: **BOOKED OUT** Sat 25 Apr. Recommended Bucks Head Meonstoke.
- Bucks Head Inn, Meonstoke: **£140 BOOKED & PAID** (Sat 25 Apr) inc breakfast (mile ~12.8, 0.57mi off trail, 57m elevation — trail is at ~60m here so no climbing penalty). 5 rooms, riverside.
- SD Eco Lodge hostel twin: £70 (mile ~17, ON trail) — **has availability late April**
- SD Eco Lodge B&B: from ~£70 (mile ~17, ON trail)
- Hampshire Hog, Clanfield: **£107 advance / £119 flexible** (Sun 26 Apr) inc breakfast (mile ~25, **0.5mi off trail**, lat 50.95248 lon -0.98334, 145m altitude — +39m climb from trail, similar to trail low point post-Butser Hill — no significant extra climbing penalty)
- Nest Hotel, Buriton: £130+ and **closed Sun/Mon/Tue** — not an option
- Manor Farm, Cocking: Shepherd's Hut **£109 BOOKED** (Mon 27 Apr, self-catering, mile ~36.5, ON trail above Cocking village). B&B £75 inc breakfast also available (only 1 room). Log Cabin £126 also available.
- Five Bells, Buriton: self-catering cottages, **price unknown — must phone**
- Black Horse, Amberley: **£110** (Tue 28 Apr) — ⚠️ only 1 room left, ⚠️ Google Maps says "temporarily closed" (may be wrong)
- The Sportsman, Amberley: **£120** (Tue 28 Apr) — ⚠️ possibly only 1 room left

### Emerging Itinerary (first 4 walking days)
| Night | Where | Day's walk | Miles | Cost | Status |
|-------|-------|-----------|-------|------|--------|
| Fri 24 | Travelodge Winchester | Travel (eve) | — | £70 | ⏳ Book |
| Sat 25 | Bucks Head, Meonstoke | Winchester → Meonstoke | 12.4 (11.9 trail + 0.57 off) | £140 | ✅ Booked & paid |
| Sun 26 | Hampshire Hog, Clanfield | Meonstoke → Clanfield (Butser Hill) | 11.8 (10.7 trail + 0.57 + 0.49 off) | £107 | ⏳ Book |
| Mon 27 | Manor Farm Shepherd's Hut, Cocking | Clanfield → Manor Farm (Harting Down) | ~12 (11.5 trail + 0.5 off) | £109 | ✅ Booked |
| Tue 28 | Black Horse or Sportsman, Amberley | Manor Farm → Amberley | ~12 (on trail) | £110–120 | ⏳ Phone/book |
| Wed 29 | Steyning area (see steyning research) | Amberley → Steyning | ~11 | £91–100 | ⏳ Phone/book |
| Thu 30 | **Brighton** (bus/train from Pyecombe) | Steyning → Pyecombe | ~10.5 | ~£55–72 | ⏳ Book |
| Fri 1+ | Brighton (rest day / continue) | — | — | | |

### Pyecombe Area: Too Pricey
Pyecombe-area accommodation is £130–159/night. South Downs Way B&B Poynings (best option at ~£85) is **unavailable** Thu 30 Apr. Duck Lodge confirmed **£159**. **Plan: get train from Hassocks (1.5mi from Pyecombe, 12 min) to Brighton.** See accommodation-research-pyecombe-area.md.

### Brighton Options (Thu 30 Apr)
Top picks for budget + character:
- **Paskins Town House:** ~£65 inc outstanding breakfast, art deco, Kemptown
- **Sea Spray Brighton:** ~£72 inc breakfast, themed rooms, seafront, couples favourite
- **Strawberry Fields:** ~£55–65, no breakfast (£5pp baps), stylish, central
- **ibis Brighton Station:** ~£55–65 (functional, right at station)
See full research in accommodation-research-pyecombe-area.md.

### Next Steps
- **Phone calls:** Black Horse Amberley (verify open + availability!), Five Bells Buriton (cottage price), Manor Farm Cocking (confirm £75 B&B availability), SD Eco Lodge (prices). See priority list in accommodation-options.md.
- **Book urgently:** Hampshire Hog Clanfield (Sun 26), Black Horse or Sportsman Amberley (1 room each!), Manor Farm Cocking
- **Book Day 5 (Wed 29):** Steyning area — Castle Inn Bramber (£91) or Chequer Inn Steyning (£100). See accommodation-research-steyning-area.md.
- **Book Day 6 (Thu 30):** Brighton — check Paskins, Sea Spray, or Strawberry Fields for Thu 30 Apr
- **Alternative staging:** "Chilcomb trick" remains a fallback if Friday travel doesn't work — see accommodation-options.md
