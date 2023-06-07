function pickingNumbers(a) {
  const cd = {};

  // build frequency object of number in array
  for (let c of a) {
    if (c in cd) {
      cd[c] += 1;
    } else {
      cd[c] = 1;
    }
  }

  const vals = Object.keys(cd).sort();
  let cv = +vals[0];
  let mx = cd[vals[0]];

  for (let i = 1; i < vals.length; i++) {
    // update maximum
    mx = mx > cd[vals[i]] ? mx : cd[vals[i]];
    if (+vals[i] - cv == 1) {
      mx = mx > cd[vals[i]] + cd[cv] ? mx : cd[vals[i]] + cd[cv];
    }
    cv = +vals[i];
  }
  return mx;
}
