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

## Files

- **CLAUDE.md** - This file. Project context and constraints.
- **route-reference.md** - Comprehensive waypoint table with cumulative distances (from official SDW mileage chart), elevation profile, 12 official Cicerone stages, river crossings, rail bail-out points, and A-road crossings.
- **south-downs-way-main-plan.csv** - Draft 6-day itinerary (Winchester to Pyecombe). Generated from a previous LLM session. **Distances are roughly correct but accommodation names/prices are unverified and likely inaccurate.**
- **accommodation-options.md** - Researched accommodation for miles 0–37 (Winchester to Cocking). Prices web-sourced March 2026; some unconfirmed and marked for phone verification. Includes emerging plan, staging analysis, and phone call priority list.
- **accommodation-research-buriton-area.md** - Detailed Buriton-area research notes (raw findings, supplementary to main file).
- **South_Downs_Way_Elev.gpx** - GPX track with elevation data (~10k trackpoints). **Contains alternative routes** so total distance is ~249mi rather than ~100mi. Not suitable for direct distance/elevation calculations without filtering.
- **sdw-linear.gpx** - Clean single-track GPX from Saturday Walkers Club (784 trackpoints with elevation). Suitable for analysis. Non-commercial use only.
- **analyze_gpx.py** - Python script to parse GPX and compute per-stage distances, ascent, and descent. Uses scaled mileage-chart distances to locate stage boundaries on the GPX track.

## Key Findings So Far

### Distances (from official mileage chart)
The current plan covers Winchester (mile 0) to Pyecombe (mile 68) in 6 walking days. Mileage chart distances per stage:
- Day 1: Winchester → Exton = 12.5mi
- Day 2: Exton → Buriton = 13mi (trail mile 25.5, Buriton 0.5mi off trail)
- Day 3: Buriton → Cocking = 11mi (Cocking 1mi off trail)
- Day 4: Cocking → Amberley = 12mi (Amberley station ON trail)
- Day 5: Amberley → Steyning = 10mi (Steyning 1mi off trail)
- Day 6: Steyning → Pyecombe = 8mi (shorter than CSV's 12mi claim)

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
- Crossways B&B, Exton: ~£85–100 unconfirmed (mile 12.5, ON trail)
- SD Eco Lodge hostel twin: £70 (mile ~17, ON trail) — **has availability late April**
- SD Eco Lodge B&B: from ~£70 (mile ~17, ON trail)
- Hampshire Hog, Clanfield: **£107 advance / £119 flexible** (Sun 26 Apr) inc breakfast (mile ~25.5 area, 1.5mi off trail, 140m altitude = same as trail low point post-Butser Hill — no extra climbing penalty)
- Nest Hotel, Buriton: £130+ and **closed Sun/Mon/Tue** — not an option
- Manor Farm, Cocking: £75 inc breakfast (mile ~36.5, 1mi off trail) — cheapest B&B found, only 1 room
- Five Bells, Buriton: self-catering cottages, **price unknown — must phone**

### Emerging Itinerary (first 3 walking days)
| Night | Where | Day's walk | Miles | Cost |
|-------|-------|-----------|-------|------|
| Fri 24 | Travelodge Winchester | Travel (eve) | — | £70 |
| Sat 25 | Crossways, Exton | Winchester → Exton | 12.5 | ~£85–100 |
| Sun 26 | Hampshire Hog, Clanfield | Exton → Clanfield (Butser Hill) | ~14.5 | £107 |
| Mon 27 | Manor Farm, Cocking | Clanfield → Cocking (Harting Down) | ~11 | £75 |
| Tue 28+ | Not yet researched | Cocking → Amberley → ... | | |

### Next Steps
- **Phone calls:** Five Bells Buriton (cottage price), Manor Farm Cocking (confirm £75 + availability), Crossways Exton (rate), SD Eco Lodge (prices). See priority list in accommodation-options.md.
- **Research accommodation miles 37–68:** Cocking → Amberley → Steyning → Pyecombe area
- **Decide on Brighton accommodation** for rest day(s)
- **Book early:** Manor Farm (1 room), Crossways (1 room) — these will go fast
- **Alternative staging:** "Chilcomb trick" remains a fallback if Friday travel doesn't work — see accommodation-options.md
