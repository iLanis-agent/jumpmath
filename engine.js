// Jump math - jump starter honesty.
// Cranking amps, not peak amps. All figures are labeled norms; verdicts judge
// the unrounded figure and rounding is for display only.
var JumpMath = (function () {
  function pos(x) { return typeof x === "number" && isFinite(x) && x > 0; }
  function num(x) { return typeof x === "number" && isFinite(x); }

  // Labeled norm: a gas engine wants about 110 honest cranking amps per liter,
  // a diesel about 240 (heat and compression both cost).
  function crankPlan(liters, fuel) {
    if (!pos(liters)) return { error: "the engine size must be above zero" };
    if (fuel !== "gas" && fuel !== "diesel") return { error: "pick gas or diesel" };
    var raw = liters * (fuel === "diesel" ? 240 : 110);
    return { amps: Math.round(raw / 10) * 10, fuel: fuel };
  }

  function renderCrank(r, liters, fuel) {
    return "Your " + liters + " L " + r.fuel + " engine wants about " + r.amps
      + " honest cranking amps - a labeled norm; the battery plate and the manual name the real number.";
  }

  // Labeled norm: the advertised peak is a pulse; honest cranking capability
  // figures about peak / 3.5.
  function decodePlan(peak) {
    if (!pos(peak)) return { error: "the peak amps must be above zero" };
    var raw = peak / 3.5;
    var working = Math.round(raw / 10) * 10;
    var verdict;
    if (raw < 150) verdict = "a phone charger with ambition";
    else if (raw < 300) verdict = "small engines only";
    else if (raw < 600) verdict = "most gas cars";
    else if (raw < 1000) verdict = "trucks and diesels in fair weather";
    else verdict = "shop-grade";
    return { working: working, verdict: verdict };
  }

  function renderDecode(r, peak) {
    return "The " + peak + " peak amps on the box figure about " + r.working
      + " honest cranking amps - " + r.verdict + ". The peak is a pulse, not a crank.";
  }

  // Labeled norms: a cold engine wants more, a cold pack delivers less.
  function needFactor(tempF) {
    if (tempF >= 50) return 1;
    if (tempF >= 32) return 1.25;
    if (tempF >= 0) return 1.6;
    return 2;
  }
  function packFactor(tempF) {
    if (tempF >= 50) return 1;
    if (tempF >= 32) return 0.85;
    if (tempF >= 0) return 0.7;
    return 0.55;
  }

  function coldPlan(amps, tempF) {
    if (!pos(amps)) return { error: "the amps must be above zero" };
    if (!num(tempF)) return { error: "the temperature must be a number" };
    var need = amps * needFactor(tempF);
    var pack = packFactor(tempF);
    return { need: Math.round(need / 5) * 5, packPct: Math.round(pack * 100) };
  }

  function renderCold(r, amps, tempF) {
    return "At " + tempF + " F the engine wants about " + r.need + " honest amps and the cold pack keeps "
      + r.packPct + "% of its room-temperature best - check the margin before the morning.";
  }

  return {
    crankPlan: crankPlan, renderCrank: renderCrank,
    decodePlan: decodePlan, renderDecode: renderDecode,
    coldPlan: coldPlan, renderCold: renderCold
  };
})();
if (typeof module !== "undefined") module.exports = JumpMath;
