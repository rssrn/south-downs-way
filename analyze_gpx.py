"""
Analyze South Downs Way GPX track to extract per-stage distances and elevation data.
@author Claude Opus 4.6 Anthropic
"""

import xml.etree.ElementTree as ET
import math

GPX_FILE = "sdw-linear.gpx"
NS = {"gpx": "http://www.topografix.com/GPX/1/1"}


def haversine(lat1, lon1, lat2, lon2):
    """Distance in miles between two lat/lon points."""
    R = 3958.8  # Earth radius in miles
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)
    return R * 2 * math.asin(math.sqrt(a))


def parse_gpx(filename):
    """Parse GPX, deduplicate consecutive identical points, return list of (lat, lon, ele)."""
    tree = ET.parse(filename)
    root = tree.getroot()
    raw_points = []
    for trkpt in root.findall(".//gpx:trkpt", NS):
        lat = float(trkpt.get("lat"))
        lon = float(trkpt.get("lon"))
        ele = float(trkpt.find("gpx:ele", NS).text)
        raw_points.append((lat, lon, ele))

    # Deduplicate consecutive identical points
    points = [raw_points[0]]
    for p in raw_points[1:]:
        if p != points[-1]:
            points.append(p)
    return points


def cumulative_distances(points):
    """Return cumulative distance in miles for each point."""
    dists = [0.0]
    for i in range(1, len(points)):
        d = haversine(points[i-1][0], points[i-1][1], points[i][0], points[i][1])
        dists.append(dists[-1] + d)
    return dists


def find_nearest_point(points, cum_dists, lat, lon):
    """Find the index of the point nearest to given lat/lon."""
    best_idx = 0
    best_dist = float("inf")
    for i, (plat, plon, _) in enumerate(points):
        d = haversine(plat, plon, lat, lon)
        if d < best_dist:
            best_dist = d
            best_idx = i
    return best_idx, best_dist


def stage_stats(points, cum_dists, start_idx, end_idx):
    """Compute distance, ascent, descent, max/min elevation for a segment."""
    dist = cum_dists[end_idx] - cum_dists[start_idx]
    ascent = 0.0
    descent = 0.0
    max_ele = points[start_idx][2]
    min_ele = points[start_idx][2]
    for i in range(start_idx + 1, end_idx + 1):
        diff = points[i][2] - points[i-1][2]
        if diff > 0:
            ascent += diff
        else:
            descent += abs(diff)
        max_ele = max(max_ele, points[i][2])
        min_ele = min(min_ele, points[i][2])
    return dist, ascent, descent, max_ele, min_ele


# Key waypoint coordinates - use trail crossing points, not village centres,
# for places that are off-trail. Mileage chart distances used to validate.
# Mileage chart: Win=0, Exton=12.5, Buriton=25.5(trail), Cocking=36.5(trail),
#   Amberley=48.5, Washington=55, Steyning=58.5(trail), Adur=62, Pyecombe=68
WAYPOINTS = {
    "Winchester":       (51.0609, -1.3080),   # start, on trail
    "Exton":            (50.9795, -1.0830),   # trail passes through village
    "Buriton":          (50.9870, -0.9590),   # 0.5mi off trail
    "Cocking":          (50.9520, -0.7410),   # 1mi off trail (use Cocking Hill on trail)
    "Amberley":         (50.8935, -0.5420),   # station is on trail
    "Steyning":         (50.8870, -0.3290),   # 1mi off trail
    "Upper Beeding":    (50.8775, -0.3050),   # near trail
    "Pyecombe":         (50.8930, -0.1660),   # on trail
    "Brighton":         (50.8225, -0.1372),
}

# Also locate these on-trail reference points for cross-checking
REFERENCE_POINTS = {
    "Milburys Inn":     (50.9936, -1.1299),   # on trail, mile 9
    "QE Country Park":  (50.9720, -0.9770),   # on trail, mile 23.5
    "Harting Down":     (50.9580, -0.8560),   # on trail, mile 29.5
    "Cocking Hill":     (50.9590, -0.7540),   # on trail, mile 36.5
    "Bignor Hill":      (50.9130, -0.6370),   # on trail, mile 44
    "Washington":       (50.8980, -0.4070),   # on trail, mile 55
    "River Adur":       (50.8720, -0.2940),   # on trail, mile 62
    "Truleigh Hill":    (50.8820, -0.2600),   # on trail, mile 64
    "Devils Dyke":      (50.8810, -0.2110),   # on trail, mile 66.5
}

# CSV plan stages
STAGES = [
    ("TRAVEL/Day 0", "Winchester", "Winchester", "Arrive Winchester"),
    ("Day 1", "Winchester", "Exton", "12mi / 300m↑ 260m↓"),
    ("Day 2", "Exton", "Buriton", "11-12.5mi / 380m↑ 350m↓"),
    ("Day 3", "Buriton", "Cocking", "11-12mi / 340m↑ 360m↓"),
    ("Day 4", "Cocking", "Amberley", "12mi / 350m↑ 380m↓"),
    ("Day 5", "Amberley", "Steyning", "12mi / 420m↑ 400m↓"),
    ("Day 6", "Steyning", "Pyecombe", "12mi / 380m↑ 350m↓"),
]


def main():
    print("Parsing GPX...")
    points = parse_gpx(GPX_FILE)
    print(f"  {len(points)} unique trackpoints (from ~{len(points)*3} raw)")
    print(f"  Start: ({points[0][0]:.4f}, {points[0][1]:.4f}) ele={points[0][2]:.0f}m")
    print(f"  End:   ({points[-1][0]:.4f}, {points[-1][1]:.4f}) ele={points[-1][2]:.0f}m")

    cum_dists = cumulative_distances(points)
    total_dist = cum_dists[-1]
    print(f"  Total track distance: {total_dist:.1f} miles")
    print()

    # First validate with on-trail reference points (known mile markers)
    print("Reference point validation (on-trail points with known distances):")
    print(f"  {'Name':<20} {'Expected mi':>12} {'GPX mi':>8} {'Diff':>6} {'Off-trk':>8}")
    expected_miles = {
        "Milburys Inn": 9, "QE Country Park": 23.5, "Harting Down": 29.5,
        "Cocking Hill": 36.5, "Bignor Hill": 44, "Washington": 55,
        "River Adur": 62, "Truleigh Hill": 64, "Devils Dyke": 66.5,
    }
    for name, (lat, lon) in REFERENCE_POINTS.items():
        idx, off_track = find_nearest_point(points, cum_dists, lat, lon)
        gpx_mi = cum_dists[idx]
        exp = expected_miles[name]
        diff = gpx_mi - exp
        flag = " ⚠" if abs(diff) > 2 else ""
        print(f"  {name:<20} {exp:>10.1f}   {gpx_mi:>7.1f} {diff:>+5.1f}  {off_track:>6.2f} mi{flag}")
    print()

    # Find waypoint indices - for off-trail villages, use expected cumulative
    # distance from mileage chart to find the nearest trail point at that distance
    wp_indices = {}
    # Expected trail-distances from mileage chart (where trail passes nearest)
    expected_trail_miles = {
        "Winchester": 0, "Exton": 12.5, "Buriton": 25.5,
        "Cocking": 36.5, "Amberley": 48.5, "Steyning": 58.5,
        "Upper Beeding": 62, "Pyecombe": 68, "Brighton": None,
    }
    print("Locating stage waypoints on track:")
    for name, (lat, lon) in WAYPOINTS.items():
        # For off-trail locations, find by expected distance instead of lat/lon
        exp_mi = expected_trail_miles.get(name)
        idx, off_track = find_nearest_point(points, cum_dists, lat, lon)

        # If the nearest point is >0.5mi off trail AND we have an expected distance,
        # use distance-based matching instead
        if off_track > 0.5 and exp_mi is not None:
            # Find point closest to expected cumulative distance
            best_idx = min(range(len(cum_dists)),
                          key=lambda i: abs(cum_dists[i] - exp_mi))
            idx = best_idx
            method = "by-dist"
        else:
            method = "by-loc"

        wp_indices[name] = idx
        print(f"  {name:20s} → pt {idx:5d}, "
              f"cum = {cum_dists[idx]:6.1f} mi, "
              f"off-trk = {off_track:.2f} mi, "
              f"ele = {points[idx][2]:.0f}m  ({method})")
    print()

    # Stage analysis
    print("=" * 90)
    print(f"{'Stage':<12} {'Route':<28} {'GPX mi':>7} {'CSV mi':>10} "
          f"{'GPX ↑m':>7} {'CSV ↑m':>7} {'GPX ↓m':>7} {'CSV ↓m':>7} "
          f"{'Max m':>6} {'Min m':>6}")
    print("=" * 90)

    csv_data = [
        None,  # travel day
        (12, 300, 260),
        (12, 380, 350),
        (11.5, 340, 360),
        (12, 350, 380),
        (12, 420, 400),
        (12, 380, 350),
    ]

    for i, (day, start, end, csv_note) in enumerate(STAGES):
        if start == end:
            continue
        s_idx = wp_indices[start]
        e_idx = wp_indices[end]
        dist, asc, desc, max_e, min_e = stage_stats(points, cum_dists, s_idx, e_idx)
        csv_d, csv_a, csv_desc = csv_data[i]
        print(f"{day:<12} {start + ' → ' + end:<28} {dist:>6.1f}  {csv_d:>9}  "
              f"{asc:>6.0f}  {csv_a:>6}  {desc:>6.0f}  {csv_desc:>6}  "
              f"{max_e:>5.0f}  {min_e:>5.0f}")

    # Totals
    s_idx = wp_indices["Winchester"]
    e_idx = wp_indices["Pyecombe"]
    dist, asc, desc, max_e, min_e = stage_stats(points, cum_dists, s_idx, e_idx)
    print("-" * 90)
    print(f"{'TOTAL':<12} {'Winchester → Pyecombe':<28} {dist:>6.1f}  "
          f"{'~71.5':>9}  {asc:>6.0f}  {'2170':>6}  {desc:>6.0f}  {'2100':>6}  "
          f"{max_e:>5.0f}  {min_e:>5.0f}")
    print()

    # Also show what the mileage chart says for comparison
    print("Mileage chart reference distances (from route-reference.md):")
    ref = {
        "Winchester → Exton": 12.5,
        "Exton → Buriton": 13.5,
        "Buriton → Cocking": 11.0,
        "Cocking → Amberley": 12.0,
        "Amberley → Steyning": 11.5,
        "Steyning → Pyecombe": 8.0,
        "Winchester → Pyecombe": 68.0,
    }
    for route, d in ref.items():
        print(f"  {route:<28} {d:.1f} mi")


if __name__ == "__main__":
    main()
