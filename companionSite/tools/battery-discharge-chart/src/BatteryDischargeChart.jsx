import { useState, useMemo } from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, ReferenceLine, Label } from "recharts";

function generateCurve(points) {
  var data = [];
  for (var i = 0; i < points.length - 1; i++) {
    var mAh1 = points[i][0], v1 = points[i][1];
    var mAh2 = points[i + 1][0], v2 = points[i + 1][1];
    var steps = Math.max(1, Math.round((mAh2 - mAh1) / 10));
    for (var s = 0; s <= steps; s++) {
      var t = s / steps;
      var mAh = mAh1 + (mAh2 - mAh1) * t;
      var smooth = t * t * (3 - 2 * t);
      var v = v1 + (v2 - v1) * smooth;
      data.push({ mAh: Math.round(mAh), v: Math.round(v * 1000) / 1000 });
    }
  }
  return data;
}

var zincCarbonPts = [
  [0, 1.55], [20, 1.48], [50, 1.38], [100, 1.28], [150, 1.20],
  [200, 1.14], [250, 1.08], [300, 1.02], [350, 0.95], [400, 0.88],
  [450, 0.80], [500, 0.72], [530, 0.65]
];
var zincChloridePts = [
  [0, 1.58], [30, 1.50], [80, 1.42], [150, 1.34], [250, 1.26],
  [350, 1.18], [450, 1.10], [550, 1.02], [620, 0.95], [680, 0.88],
  [720, 0.80], [750, 0.72]
];
var alkalinePts = [
  [0, 1.58], [50, 1.50], [150, 1.42], [300, 1.34], [450, 1.26],
  [600, 1.20], [750, 1.14], [900, 1.08], [1000, 1.02], [1100, 0.96],
  [1200, 0.90], [1300, 0.82], [1350, 0.75]
];
var nicdPts = [
  [0, 1.38], [10, 1.30], [25, 1.24], [50, 1.22], [100, 1.21],
  [200, 1.20], [300, 1.19], [350, 1.18], [400, 1.17], [430, 1.15],
  [450, 1.12], [470, 1.05], [490, 0.95], [510, 0.80]
];

var CHEMISTRIES = [
  { key: "ZnC", name: "Zinc-Carbon (Leclanch\u00e9)", color: "#d97706", desc: "~400\u2013600 mAh" },
  { key: "ZnCl", name: "Zinc-Chloride (Heavy Duty)", color: "#059669", desc: "~600\u2013800 mAh" },
  { key: "Alk", name: "Alkaline (Zn-MnO\u2082)", color: "#2563eb", desc: "~1,200\u20131,500 mAh" },
  { key: "NiCd", name: "Nickel-Cadmium (rechargeable)", color: "#dc2626", desc: "~500 mAh" },
];

var NAME_MAP = {};
CHEMISTRIES.forEach(function(c) { NAME_MAP[c.key] = c.name; });

function mergeData() {
  var map = new Map();
  var addSeries = function(series, key) {
    series.forEach(function(item) {
      var bucket = Math.round(item.mAh / 5) * 5;
      if (!map.has(bucket)) map.set(bucket, { mAh: bucket });
      map.get(bucket)[key] = item.v;
    });
  };
  addSeries(generateCurve(zincCarbonPts), "ZnC");
  addSeries(generateCurve(zincChloridePts), "ZnCl");
  addSeries(generateCurve(alkalinePts), "Alk");
  addSeries(generateCurve(nicdPts), "NiCd");
  return Array.from(map.values()).sort(function(a, b) { return a.mAh - b.mAh; });
}

function CustomTooltip(props) {
  if (!props.active || !props.payload || props.payload.length === 0) return null;
  return (
    <div style={{ background: "white", border: "1px solid #e2e8f0", borderRadius: 8, padding: "8px 12px", fontSize: 12 }}>
      <div style={{ fontWeight: 600, marginBottom: 4, color: "#475569" }}>{props.label} mAh</div>
      {props.payload.map(function(p) {
        return (
          <div key={p.dataKey} style={{ color: p.stroke, marginBottom: 2 }}>
            {NAME_MAP[p.dataKey] || p.dataKey}: {p.value.toFixed(3)} V
          </div>
        );
      })}
    </div>
  );
}

export default function BatteryDischargeChart() {
  var chartData = useMemo(function() { return mergeData(); }, []);
  var stateHook = useState({ ZnC: true, ZnCl: true, Alk: true, NiCd: true });
  var active = stateHook[0];
  var setActive = stateHook[1];

  function toggle(key) {
    setActive(function(prev) {
      var next = {};
      Object.keys(prev).forEach(function(k) { next[k] = prev[k]; });
      next[key] = !next[key];
      return next;
    });
  }

  return (
    <div style={{ fontFamily: '"Times New Roman", "Liberation Serif", Georgia, serif', maxWidth: 720, margin: "0 auto", padding: "32px 24px" }}>

      <p style={{ fontSize: 14, fontWeight: 700, marginBottom: 4, color: "#000" }}>
        Figure 1
      </p>
      <p style={{ fontSize: 14, fontStyle: "italic", marginTop: 0, marginBottom: 20, color: "#000", lineHeight: 1.5 }}>
        Discharge Voltage as a Function of Delivered Capacity for AA-Size Cells of Four Electrochemical Systems Available in the Mid-1970s
      </p>

      <div style={{ width: "100%", height: 400 }}>
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={chartData} margin={{ top: 10, right: 15, bottom: 40, left: 20 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="#ccc" />
            <XAxis
              dataKey="mAh"
              type="number"
              domain={[0, 1400]}
              tickCount={8}
              tick={{ fontSize: 11, fill: "#333", fontFamily: '"Times New Roman", Georgia, serif' }}
            >
              <Label value="Capacity (mAh)" position="bottom" offset={15} style={{ fontSize: 12, fill: "#000", fontFamily: '"Times New Roman", Georgia, serif' }} />
            </XAxis>
            <YAxis
              domain={[0.6, 1.7]}
              tickCount={12}
              tick={{ fontSize: 11, fill: "#333", fontFamily: '"Times New Roman", Georgia, serif' }}
            >
              <Label value="Terminal Voltage (V)" angle={-90} position="insideLeft" offset={-5} style={{ fontSize: 12, fill: "#000", fontFamily: '"Times New Roman", Georgia, serif' }} />
            </YAxis>
            <ReferenceLine y={0.9} stroke="#999" strokeDasharray="6 3" />
            <Tooltip content={CustomTooltip} />
            {active.Alk ? <Line dataKey="Alk" stroke="#2563eb" strokeWidth={2} dot={false} connectNulls={true} /> : null}
            {active.ZnCl ? <Line dataKey="ZnCl" stroke="#059669" strokeWidth={2} dot={false} connectNulls={true} /> : null}
            {active.ZnC ? <Line dataKey="ZnC" stroke="#d97706" strokeWidth={2} dot={false} connectNulls={true} /> : null}
            {active.NiCd ? <Line dataKey="NiCd" stroke="#dc2626" strokeWidth={2} dot={false} connectNulls={true} /> : null}
          </LineChart>
        </ResponsiveContainer>
      </div>

      <div style={{ display: "flex", flexWrap: "wrap", gap: 12, marginTop: 8, justifyContent: "center" }}>
        {CHEMISTRIES.map(function(c) {
          var isOn = active[c.key];
          return (
            <button
              key={c.key}
              onClick={function() { toggle(c.key); }}
              style={{
                display: "flex", alignItems: "center", gap: 6,
                padding: "4px 10px", borderRadius: 4, fontSize: 12,
                border: "1px solid " + (isOn ? c.color : "#ccc"),
                background: "white", cursor: "pointer",
                opacity: isOn ? 1 : 0.4,
                fontFamily: '"Times New Roman", Georgia, serif'
              }}
            >
              <span style={{ width: 18, height: 3, backgroundColor: c.color, display: "inline-block" }} />
              <span>{c.name} ({c.desc})</span>
            </button>
          );
        })}
      </div>

      <p style={{ fontSize: 12, marginTop: 20, color: "#000", lineHeight: 1.8, textAlign: "left" }}>
        <span style={{ fontStyle: "italic" }}>Note.</span> Curves were generated by Claude (Anthropic) using interpolated voltage–capacity profiles derived from published manufacturer datasheets and battery handbooks of the 1970s. Constant 250 mA resistive load at 20 °C; dashed line indicates 0.9 V cutoff. Values are approximate and intended for illustrative comparison only.
      </p>
    </div>
  );
}
