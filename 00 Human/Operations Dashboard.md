---
type: dashboard
tags:
  - dashboard
cssclasses:
  - ops-dashboard-note
---
	
```dataviewjs
/* =====================================================================
   OPERATIONS DASHBOARD  v1  (DataviewJS)
   Reads today's daily note + Metrics.md and renders an interactive
   dashboard. Styling lives in .obsidian/snippets/dashboard.css
   ===================================================================== */

const DAILY_DIR    = "00 Human/10 Daily Notes";
const METRICS_PATH = "00 Human/70 Context/Metrics.md";
const INBOX_PATH   = "00 Human/00 Inbox/Inbox.md";
const DL = dv.luxon.DateTime;

const today     = DL.now().toFormat("yyyy-MM-dd");
const dailyPath = `${DAILY_DIR}/${today}.md`;
const page      = dv.page(dailyPath);

let raw = "";
try { raw = (await dv.io.load(dailyPath)) || ""; } catch (e) { raw = ""; }

// unprocessed inbox count for the header (bullets under "## Unprocessed")
let inboxN = 0;
try {
  const inboxRaw = (await dv.io.load(INBOX_PATH)) || "";
  const body = inboxRaw.split(/##\s*Unprocessed/)[1] || "";
  inboxN = (body.match(/^\s*[-*]\s+\S/gm) || []).length;
} catch (e) { inboxN = 0; }

const esc = (s) => (s ?? "").toString()
  .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

/* escape first (XSS-safe), THEN convert a small subset of inline markdown so
   things like **bold**, `code`, and [[wikilinks]] render instead of showing
   their raw markers. */
const mdInline = (s) => esc(s)
  .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
  .replace(/`([^`]+?)`/g, "<code>$1</code>")
  .replace(/\[\[[^\]|]+\|([^\]]+)\]\]/g, "$1")
  .replace(/\[\[([^\]]+)\]\]/g, "$1");

/* --- section splitter -------------------------------------------------- */
const chunks = raw.split(/\n##\s+/);
const section = (label) => chunks.find((c) => c.startsWith(label)) || "";

/* --- current focus ----------------------------------------------------- */
const focus = section("🎯 Today's Focus");
const grab  = (re) => (focus.match(re) || [])[1]?.trim() || "";
const one   = grab(/\*\*ONE Thing:\*\*\s*(.+)/) || "Set your ONE Thing in today's note.";
const p2    = grab(/\*\*Priority 2:\*\*\s*(.+)/);
const p3    = grab(/\*\*Priority 3:\*\*\s*(.+)/);

/* --- task counts ------------------------------------------------------- */
const tasks = page ? page.file.tasks : [];
const doneN = tasks.filter((t) => t.completed).length;
const openN = tasks.filter((t) => !t.completed).length;

/* --- priorities (Frogs, fall back to Today's Tasks) -------------------- */
const inSection = (t, name) => (t.section?.subpath || "").includes(name);
let priorities = tasks.filter((t) => inSection(t, "Frogs"));
if (priorities.length === 0) priorities = tasks.filter((t) => inSection(t, "Today's Tasks"));
priorities = priorities.slice(0, 5);

/* --- daily drivers ----------------------------------------------------- */
const drivers   = tasks.filter((t) => inSection(t, "Daily Drivers"));
const driverDone = drivers.filter((t) => t.completed).length;
const driverPct  = drivers.length ? Math.round((driverDone / drivers.length) * 100) : 0;

/* --- schedule (parse the Calendar table) ------------------------------- */
// parse "9:00" / "1:30 PM" -> minutes since midnight; `fallback` supplies the
// AM/PM when the token itself omits it (e.g. the start of "9:00–10:30 AM").
function toMin(str, fallback) {
  const m = str.match(/(\d{1,2}):(\d{2})\s*(AM|PM)?/i);
  if (!m) return null;
  let h = +m[1]; const min = +m[2];
  const ap = (m[3] || fallback || "").toUpperCase();
  if (ap === "PM" && h !== 12) h += 12;
  if (ap === "AM" && h === 12) h = 0;
  return h * 60 + min;
}
// format minutes-since-midnight back into a consistent 12h label, so every
// schedule row reads "9:00 AM" regardless of how the source table wrote it.
function fmtMin(m) {
  if (m == null) return "";
  const ap = m >= 720 ? "PM" : "AM";
  let h = Math.floor(m / 60) % 12; if (h === 0) h = 12;
  return `${h}:${String(m % 60).padStart(2, "0")} ${ap}`;
}
// parse a "start–end" range cell into {start, end}. end is null for single times.
function parseRange(cell) {
  const clean = cell.replace(/[*`]/g, "").trim();
  const ampm  = clean.match(/(AM|PM)/gi) || [];
  const lastAp = ampm[ampm.length - 1] || "";
  const parts = clean.split(/[–—-]/).map((s) => s.trim());
  return { start: toMin(parts[0], ampm[0] || lastAp), end: parts[1] ? toMin(parts[1], lastAp) : null };
}
const cal = section("📅 Calendar");
let events = cal.split("\n")
  .filter((l) => l.trim().startsWith("|") && !/^\s*\|[\s\-|:]+\|?\s*$/.test(l))
  .map((l) => l.split("|").map((c) => c.trim()).filter((c) => c.length))
  .filter((cells) => cells.length >= 2 && cells[0].toLowerCase() !== "time")
  .map((cells) => { const r = parseRange(cells[0]); return { time: cells[0], title: cells[1], start: r.start, end: r.end }; })
  .filter((e) => e.start !== null)
  .sort((a, b) => a.start - b.start);

const nowMin = DL.now().hour * 60 + DL.now().minute;
// "Now" = a block currently in progress (start <= now < end). For a block with
// no explicit end, fall back to the next block's start, else start + 60 min.
let nowIdx = -1;
for (let i = 0; i < events.length; i++) {
  const end = events[i].end ?? events[i + 1]?.start ?? (events[i].start + 60);
  if (events[i].start <= nowMin && nowMin < end) { nowIdx = i; break; }
}
// "Next" = the first block that hasn't started yet.
const nextIdx = events.findIndex((e) => e.start > nowMin);
const nowTitle = nowIdx >= 0 ? events[nowIdx].title : (nextIdx >= 0 ? `next up ${events[nextIdx].title}` : "—");

/* --- metrics (parse Metrics.md table) ---------------------------------- */
let metricRows = [];
try {
  const mraw = (await dv.io.load(METRICS_PATH)) || "";
  metricRows = mraw.split("\n")
    .filter((l) => l.trim().startsWith("|") && !/^\s*\|[\s\-|:]+\|?\s*$/.test(l))
    .map((l) => l.split("|").map((c) => c.trim()).filter((c) => c.length))
    .filter((cells) => cells[0]?.toLowerCase() !== "date" && /\d{4}-\d{2}-\d{2}/.test(cells[0]));
} catch (e) { metricRows = []; }

const METRIC_DEFS = [
  { key: 1, label: "YouTube",   unit: "Subscribers" },
  { key: 2, label: "Instagram", unit: "Followers" },
  { key: 3, label: "Threads",   unit: "Followers" },
  { key: 4, label: "X",         unit: "Followers" },
  { key: 5, label: "TikTok",    unit: "Followers" },
];

function metricCard(def) {
  if (metricRows.length === 0) {
    return `<div class="ops-metric"><div class="ops-metric-label">${def.label}</div>
      <div class="ops-metric-value">—</div><div class="ops-metric-unit">no data</div></div>`;
  }
  const last = metricRows[metricRows.length - 1];
  const prev = metricRows[metricRows.length - 2];
  const cur  = Number(last[def.key]) || 0;
  const dY   = prev ? cur - (Number(prev[def.key]) || 0) : 0;
  // week: row ~7 days back (or the oldest row if fewer than 7 rows)
  const lastDate = DL.fromISO(last[0]);
  let weekRow = metricRows.find((r) => DL.fromISO(r[0]).plus({ days: 7 }) >= lastDate) || metricRows[0];
  const dW = cur - (Number(weekRow[def.key]) || 0);
  const cls  = (n) => (n > 0 ? "" : n < 0 ? " down" : " flat");
  const sign = (n) => (n > 0 ? "+" : "");
  return `<div class="ops-metric">
    <div class="ops-metric-label">${def.label}</div>
    <div class="ops-metric-value">${cur.toLocaleString()}</div>
    <div class="ops-delta${cls(dY)}">${sign(dY)}${dY} vs yesterday</div>
    <div class="ops-delta${cls(dW)}">${sign(dW)}${dW} this week</div>
    <div class="ops-metric-unit">${def.unit}</div>
  </div>`;
}

/* --- helpers: render task rows ----------------------------------------- */
function taskRow(t) {
  const checked = t.completed ? "checked" : "";
  return `<label class="ops-sched-row" style="cursor:pointer">
    <input type="checkbox" class="ops-task" data-line="${t.line}" ${checked}>
    <span class="ops-sched-body ops-sched-title" style="font-weight:${t.completed ? 400 : 600};
      opacity:${t.completed ? .55 : 1};text-decoration:${t.completed ? "line-through" : "none"}">
      ${mdInline(t.text)}</span>
  </label>`;
}

/* ======================================================================
   RENDER
   ====================================================================== */
const root = dv.el("div", "", { cls: "ops-dashboard" });

root.innerHTML = `
  <h1 class="ops-title">Operations Dashboard</h1>
  <div class="ops-subtitle">${DL.now().toFormat("h:mm a")} · Now: ${mdInline(nowTitle)} · ${doneN} done · ${openN} open · ${inboxN} inbox</div>

  <div class="ops-grid">
    <div class="ops-col">

      <!-- CURRENT FOCUS -->
      <div class="ops-card ops-focus">
        <div class="ops-card-head">📌 Current Focus</div>
        <h2>${mdInline(one)}</h2>
        ${p2 ? `<div class="ops-sub">${mdInline(p2)}</div>` : ""}
        <div class="ops-chips">
          <span class="ops-chip">${openN} open tasks</span>
          <span class="ops-chip">${events.length} scheduled</span>
          <span class="ops-chip">${driverDone}/${drivers.length} drivers</span>
        </div>
        <div class="ops-btns">
          <button class="ops-btn ops-primary" id="ops-open-today">→ Open Today</button>
          <button class="ops-btn" id="ops-open-metrics">📊 Metrics</button>
        </div>
      </div>

      <!-- TODAY'S PRIORITIES -->
      <div class="ops-card">
        <div class="ops-card-head">☰ Today's Priorities</div>
        ${priorities.length ? priorities.map(taskRow).join("") : `<div class="ops-empty">No frogs/tasks in today's note.</div>`}
      </div>

      <!-- METRICS -->
      <div class="ops-card">
        <div class="ops-card-head">📈 Metrics <span class="ops-spacer"></span></div>
        <div class="ops-tabs">
          <span class="ops-tab active">Audience</span>
          <span class="ops-tab" data-soon>Business</span>
          <span class="ops-tab" data-soon>Personal</span>
          <span class="ops-tab" data-soon>Ops</span>
        </div>
        <div class="ops-metrics">${METRIC_DEFS.map(metricCard).join("")}</div>
        <div class="ops-feedback" id="ops-metric-fb" style="margin-top:10px"></div>
      </div>

    </div>
    <div class="ops-col">

      <!-- SCHEDULE -->
      <div class="ops-card">
        <div class="ops-card-head">🗓 Today's Schedule</div>
        ${events.length ? events.map((e, i) => `
          <div class="ops-sched-row">
            <span class="ops-sched-time">${fmtMin(e.start)}</span>
            <div class="ops-sched-body"><div class="ops-sched-title">${mdInline(e.title)}</div></div>
            ${i === nowIdx ? `<span class="ops-badge now">Now</span>` : ""}
            ${i === nextIdx ? `<span class="ops-badge next">Next</span>` : ""}
          </div>`).join("") : `<div class="ops-empty">No time blocks in the Calendar table.</div>`}
      </div>

      <!-- DAILY DRIVERS -->
      <div class="ops-card">
        <div class="ops-card-head">🔁 Daily Drivers</div>
        <div class="ops-progress-wrap">
          <div class="ops-progress-label">${driverDone} / ${drivers.length} complete · ${driverPct}%</div>
          <div class="ops-progress"><span style="width:${driverPct}%"></span></div>
        </div>
        ${drivers.length ? drivers.map(taskRow).join("") : `<div class="ops-empty">Add a "## 🔁 Daily Drivers" section to today's note.</div>`}
      </div>

      <!-- QUICK CAPTURE -->
      <div class="ops-card">
        <div class="ops-card-head">⚡ Quick Capture</div>
        <div style="color:var(--ops-muted);font-size:13px">Capture a thought, task, or idea into your inbox to triage later with <code>/new</code>.</div>
        <textarea class="ops-qc" id="ops-qc-text" placeholder="Capture a thought, task, or idea…"></textarea>
        <div class="ops-qc-row">
          <button class="ops-btn ops-primary" id="ops-qc-send">Capture</button>
          <span class="ops-feedback" id="ops-qc-fb"></span>
        </div>
      </div>

      <!-- AGENT ACTIONS -->
      <div class="ops-card">
        <div class="ops-card-head">🤖 Agent Actions</div>
        <div class="ops-btns">
          <button class="ops-btn" data-cmd="/today">☀ Today</button>
          <button class="ops-btn" data-cmd="/closeday">🌙 Close Day</button>
          <button class="ops-btn" data-cmd="/content">✎ Content</button>
          <button class="ops-btn" data-cmd="/job-apply">🔎 Job Apply</button>
        </div>
        <div class="ops-feedback" id="ops-agent-fb" style="margin-top:10px"></div>
      </div>

    </div>
  </div>
`;

/* ======================================================================
   WIRE INTERACTIVITY
   ====================================================================== */
const $ = (sel) => root.querySelector(sel);

// task checkbox toggles -> rewrite the exact line in the daily note
root.querySelectorAll(".ops-task").forEach((cb) => {
  cb.addEventListener("change", async (ev) => {
    ev.preventDefault();
    const line = Number(cb.dataset.line);
    const f = app.vault.getAbstractFileByPath(dailyPath);
    if (!f) return;
    await app.vault.process(f, (data) => {
      const lines = data.split("\n");
      const l = lines[line] ?? "";
      if (/- \[ \]/.test(l)) lines[line] = l.replace("- [ ]", "- [x]");
      else lines[line] = l.replace(/- \[[xX]\]/, "- [ ]");
      return lines.join("\n");
    });
  });
});

// open today's note
$("#ops-open-today").addEventListener("click", async () => {
  const f = app.vault.getAbstractFileByPath(dailyPath);
  if (!f) { $("#ops-metric-fb").textContent = "Run /today to create today's note first."; return; }
  await app.workspace.getLeaf(false).openFile(f);
});

// open metrics file
$("#ops-open-metrics").addEventListener("click", async () => {
  const f = app.vault.getAbstractFileByPath(METRICS_PATH);
  if (f) await app.workspace.getLeaf(false).openFile(f);
});

// metrics tabs (only Audience wired in v1)
root.querySelectorAll(".ops-tab[data-soon]").forEach((tab) => {
  tab.addEventListener("click", () => {
    $("#ops-metric-fb").textContent = `${tab.textContent} metrics are not tracked yet (v1 covers Audience).`;
  });
});

// quick capture -> append to Activity Log
$("#ops-qc-send").addEventListener("click", async () => {
  const ta = $("#ops-qc-text");
  const val = ta.value.trim();
  const fb = $("#ops-qc-fb");
  if (!val) { fb.textContent = "Nothing to capture."; return; }
  const f = app.vault.getAbstractFileByPath(INBOX_PATH);
  if (!f) { fb.textContent = "Inbox note is missing (00 Inbox/Inbox.md)."; return; }
  const stamp = DL.now().toFormat("HH:mm");
  await app.vault.process(f, (data) => {
    const marker = "## Unprocessed";
    const idx = data.indexOf(marker);
    const bullet = `- [${stamp}] ${val}`;
    if (idx === -1) return `${data.replace(/\s+$/, "")}\n\n${marker}\n${bullet}\n`;
    const after = data.indexOf("\n", idx);
    const nextH = data.slice(after).search(/\n##\s/);
    const insertAt = nextH === -1 ? data.length : after + nextH;
    // trim trailing whitespace off the section, drop leading newlines from any
    // following heading, then rejoin with a guaranteed blank line on each side.
    const head = data.slice(0, insertAt).replace(/\s+$/, "");
    const tail = data.slice(insertAt).replace(/^\n+/, "");
    return tail ? `${head}\n${bullet}\n\n${tail}` : `${head}\n${bullet}\n`;
  });
  ta.value = "";
  fb.textContent = `Captured to inbox at ${stamp} ✓`;
});

// agent actions -> copy slash command to clipboard (paste into Claude/terminal)
root.querySelectorAll("[data-cmd]").forEach((btn) => {
  btn.addEventListener("click", async () => {
    const cmd = btn.dataset.cmd;
    try { await navigator.clipboard.writeText(cmd); } catch (e) {}
    $("#ops-agent-fb").textContent = `Copied "${cmd}" — paste it into Claude Code to run.`;
  });
});
```
