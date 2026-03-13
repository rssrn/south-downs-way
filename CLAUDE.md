# South Downs Way Trip Planning

## Overview

Planning a multi-day walk on the South Downs Way. **Dates: Saturday 25 April 2026 to Monday 4 May 2026 inclusive (10 days).** We need a travel day at start and end, point of origin for travel is Bradford-On-Avon.

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

### Next Steps
- Verify accommodation options with real data (previous LLM session hallucinated names/prices)
- Consider whether shorter days or different stage boundaries would better match on-trail accommodation
- Prioritise on-trail/ridge accommodation to avoid extra valley climbs
