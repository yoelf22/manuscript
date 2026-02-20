# Link Triage Report — Annotated Action Items

**Generated:** 2026-02-20
**Based on:** `reports/link-health.md` (250 URLs checked)

## Overall Status

| Status | Count | % |
|--------|------:|----:|
| Alive (including redirects) | 200 | 80% |
| Dead / Error | 47 | 18% |
| Timeout | 3 | 1% |

---

## Category A: False Positives — Bot-Blocked (No Action Needed)

These sites block automated HTTP requests but work fine in a browser. Mark as `bot-blocked` in the registry; no content change needed.

### Unsplash 401s (19 URLs)
Unsplash now requires authentication for programmatic access. All these URLs are valid for human readers.

| ID | Chapter | URL (truncated) |
|----|---------|-----------------|
| ref-ch04-001 | 4 | unsplash.com/@onurbinay |
| ref-ch04-002 | 4 | unsplash.com/photos/...GVH... |
| ref-ch05-001 | 5 | unsplash.com/@eyespeak |
| ref-ch05-002 | 5 | unsplash.com/@marcusurbenz |
| ref-ch05-003 | 5 | unsplash.com/@spacexuan |
| ref-ch05-004 | 5 | unsplash.com/@mmpower |
| ref-ch06-003 | 6 | unsplash.com/photos/...LR_wX... |
| ref-ch06-005 | 6 | unsplash.com/photos/...D3ZdfB... |
| ref-ch11-005 | 11 | unsplash.com/photos/jGdTiWw77Hw |
| ref-ch11-006 | 11 | unsplash.com/photos/...zjCc0l... |
| ref-ch11-008–018 | 11 | 9 more Unsplash URLs (profiles + photos) |
| ref-ch17-004 | 17 | unsplash.com/photos/...Rks... |
| ref-ch17-016 | 17 | unsplash.com/@lnhngyn |
| ref-ch17-017 | 17 | unsplash.com/photos/...RtijMF... |

### Corporate/Government 403s (8 URLs)
These sites block bot user agents. Content is live for humans.

| ID | Chapter | Site | URL |
|----|---------|------|-----|
| ref-ch10-004 | 10 | Trusted Computing Group | trustedcomputinggroup.org/resource/tpm-library-specification/ |
| ref-ch10-010 | 10 | Schneider Electric | se.com/ww/en/about-us/newsroom/... |
| ref-ch10-018 | 10 | ISO | iso.org/standard/80138.html |
| ref-ch08-016 | 8 | ISO | iso.org/standard/80138.html (duplicate) |
| ref-ch12-002 | 12 | Autoblog | autoblog.com/2010/07/27/... |
| ref-ch18-003 | 18 | SpeakersConnect | speakersconnect.com/... |
| ref-ch19-015 | 19 | AHA Journals | ahajournals.org/doi/... |
| ref-ch20-006 | 20 | Espacenet | worldwide.espacenet.com/... |
| ref-ch20-015 | 20 | ISO | iso.org/isoiec-27001-... |
| ref-ch20-018 | 20 | Framework | frame.work/ |
| ref-ch22-008 | 22 | Corning | corning.com/.../news-releases/... |

### Paywall/Auth-Gated (3 URLs)
Behind login walls. Valid content, just not publicly crawlable.

| ID | Chapter | Site | Notes |
|----|---------|------|-------|
| ref-ch00-001 | 0 | WSJ | Paywall — Marc Andreessen "Software Is Eating the World" |
| ref-ch13-004 | 13 | Facebook | Facebook post (login required) |
| ref-ch24-006 | 24 | Facebook | Same post as above (duplicate) |

**Total false positives: ~30 URLs** — These inflate the "dead" count. Effective dead rate is closer to **7%** (17/250), not 18%.

---

## Category B: Truly Dead — Need Replacement or Wayback Archive

### Confirmed 404s (Action Required)

| ID | Ch. | URL | Issue | Suggested Action |
|----|-----|-----|-------|------------------|
| ref-ch17-008 | 17 | computerhistory.org/blog/the-xerox-alto/ | 404 — page removed | Find Wayback snapshot or replacement URL |
| ref-ch19-002 | 19 | krebsonsecurity.com/2025/10/ddos-botnet-aisuru... | 404 — article gone | Find Wayback snapshot |
| ref-ch19-020 | 19 | bgr.com/tech/researchers-find-smart-door-locks... | 404 — article gone | Find Wayback snapshot |
| ref-ch21-004 | 21 | theguardian.com/.../hungarian-journalists-targeted... | 404 — URL likely changed | Search Guardian for updated URL |
| ref-ch21-005 | 21 | politico.eu/.../italy-prosecutors-investigate... | 404 — URL likely changed | Search Politico for updated URL |
| ref-ch21-007 | 21 | dw.com/en/german-intelligence-agency-spied... | 404 — URL likely changed | Search DW for updated URL |
| ref-ch25-005 | 25 | finance.yahoo.com/quote/IRBT/... | 500 — server error (transient?) | Re-check; clean guce tracking params from URL |

### Truncated/Malformed URLs (Action Required)

| ID | Ch. | URL | Issue | Fix |
|----|-----|-----|-------|-----|
| ref-ch11-019 | 11 | .../File:Nest_Learning_Thermostat_(cropped | Missing `)` and `.JPG` | URL in chapter is correct; extraction regex truncated at `(` |
| ref-ch05-005 | 5 | .../File:0_Venise | Truncated Wikimedia filename | URL in chapter links to long filename — extraction issue |
| ref-ch03-006 | 3 | .../File:Cyclisme_%26_GoPro_-GoPro_Hero_4%2830%29... | Encoded special chars | Verify actual URL works in browser |

---

## Category C: Broken Redirects — Content Moved or Gone

These URLs return 3xx but land somewhere wrong:

| ID | Ch. | Original URL | Redirects To | Issue | Action |
|----|-----|-------------|-------------|-------|--------|
| ref-ch17-009 | 17 | smithsonianmag.com/innovation/how-xerox-invented... | Birds/eggs article | **Content gone** — different article entirely | Find Wayback snapshot or alternative source |
| ref-ch19-008 | 19 | portswigger.net/daily-swig/iot-protocols... | portswigger.net/ (homepage) | **Content gone** — Daily Swig section retired | Find Wayback snapshot |
| ref-ch08-011 | 8 | 3gpp.org/technologies/ambient-iot | 3gpp.org/404 | **Content gone** — redirects to 404 page | Find updated 3GPP ambient IoT page |
| ref-ch08-005 | 8 | wi-fi.org/discover-wi-fi/wi-fi-certified-7 | wi-fi.org/wi-fi-macphy | **Wrong content** — page restructured | Update to correct Wi-Fi 7 certification page |

### Benign Redirects (No Action Needed)
- youtu.be → youtube.com (5 URLs) — Standard short-link expansion
- theroadtlv.com slug rename — Content still valid
- cfr.org /report → /reports — Minor path change
- threadgroup.org www → non-www — Same content
- statista.com SSO cookie redirect — Same content
- sony.net → www.sony.net — Same content

---

## Category D: Timeouts — Manual Verification Needed

| ID | Ch. | URL | Notes |
|----|-----|-----|-------|
| ref-ch17-025 | 17 | washingtonpost.com/news/innovations/... | WaPo may throttle bots — verify manually |
| ref-ch17-026 | 17 | washingtonpost.com/technology/... | Same — verify manually |
| ref-ch20-009 | 20 | fcc.gov/CyberTrustMark | Government site — may be slow — verify manually |

---

## Priority Actions

### Immediate (fix in source chapters)
1. **ref-ch25-005**: Clean Yahoo Finance URL — remove `guccounter` and `guce_referrer` tracking params
2. **ref-ch08-005**: Update Wi-Fi Alliance URL to current Wi-Fi 7 certification page
3. **ref-ch08-011**: Find updated 3GPP ambient IoT page URL

### Short-term (find replacement URLs or Wayback snapshots)
4. **ref-ch17-008**: Computer History Museum Xerox Alto article
5. **ref-ch17-009**: Smithsonian Xerox/modern computers article
6. **ref-ch19-008**: PortSwigger Daily Swig IoT protocols article
7. **ref-ch21-004/005/007**: Guardian, Politico, DW articles on surveillance
8. **ref-ch19-002**: Krebs on Security DDoS article
9. **ref-ch19-020**: BGR smart door locks article

### Deferred (during Wayback archival step)
10. Archive all 200+ alive URLs to prevent future rot
11. Add `archive_url` and `archive_date` to `references.yaml`

---

## Extraction Script Improvements Needed

The URL extraction script (`tools/extract-refs.py`) has issues with:
1. **Parentheses in URLs** — Wikimedia `File:Name_(part)` URLs get truncated at `(`
2. **Percent-encoded URLs** — Some encoded chars cause false mismatches

These should be fixed before the next extraction run to avoid phantom 404s.

---

*Report generated from `tools/check-links.py` output with manual triage annotations.*
