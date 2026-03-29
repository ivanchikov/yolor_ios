# Low-Fi Wireframes

## 1. Input

```
+--------------------------------------------------+
| Yolor                                    Profile |
+--------------------------------------------------+
| Plan your trip                                  |
| [ Destination or social URL                 ]    |
|                                                  |
| Trip length                                      |
| [ 1 day ] [ 3 days ] [ 5 days ]                 |
|                                                  |
| Pace                                             |
| [ Relaxed ] [ Balanced ] [ Packed ]             |
|                                                  |
| [ Generate Trip ]                                |
+--------------------------------------------------+
```

Notes:
- One primary field handles destination text and social URL paste.
- Follow-up controls stay compact and progressive, not form-heavy.

## 2. Generation

```
+--------------------------------------------------+
| Building your trip                               |
+--------------------------------------------------+
| Step 1  Resolve places                     Done  |
| Step 2  Cluster days                   In progress|
| Step 3  Optimize route                    Pending |
|                                                  |
| If import data is incomplete, we continue with   |
| the verified places and show what was skipped.   |
|                                                  |
| [ Cancel ]                        [ Retry ]      |
+--------------------------------------------------+
```

Notes:
- Progress should use plain language tied to backend stages.
- Fallback reasons are visible, not buried in logs.

## 3. Trip Review

```
+--------------------------------------------------+
| Day 1   Day 2   Day 3                    Profile |
+--------------------------------------------------+
| [ Map for selected day ]                         |
|                                                  |
| 09:00  Coffee Shop                               |
| 09 min drive                                     |
| 10:00  Museum                                    |
| 14 min walk                                      |
| 12:30  Lunch                                     |
|                                                  |
| [ Add Stop ] [ Regenerate ]                      |
+--------------------------------------------------+
```

Notes:
- Only one day is active at a time.
- Map and stop list represent the same canonical day model.

## 4. Saved Trips

```
+--------------------------------------------------+
| Saved Trips                                      |
+--------------------------------------------------+
| Tokyo Spring                                     |
| 3 days available offline                         |
|                                                  |
| Shanghai Food Crawl                              |
| 2 days available offline                         |
+--------------------------------------------------+
```

Notes:
- Saved trips emphasize offline readability and confidence in what is stored locally.
