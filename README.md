# Jump math

The engine names the amps, the box names the pulse, and the morning names the margin.

Jump starters are sold on peak amps - a pulse measured into a dead short, not the current that cranks an engine. The honest number is cranking amps, and a cold morning moves it twice: the stiff engine wants more while the cold pack has less.

## The three tools

- **Crank plan** - engine size and fuel become honest cranking amps by a labeled norm (110 A per liter gas, 240 diesel), rounded to the nearest 10.
- **Box decoder** - the advertised peak becomes a working estimate at a labeled `peak / 3.5`, banded on the unrounded figure from a phone charger with ambition to shop-grade.
- **Cold plan** - temperature bands (labeled norms) raise the engine's ask and shrink the pack's offer: need x1.25/x1.6/x2 and pack x0.85/x0.7/x0.55 below 50/32/0 F.

## Honesty notes

Illustrative planning arithmetic only. Every figure is a labeled norm; your manual and the battery plate name the real numbers. Connect positive first, then negative to a ground point away from the battery; never lean over a battery while cranking; a battery that is frozen, swollen or leaking is done - do not jump it.

## Files

- `index.html` - the pitch
- `app.html` - the calculators
- `engine.js` - the arithmetic (browser and node)
- `oracle.py` - the same arithmetic, float-for-float, writing `expected.json`
- `test.js` - runs every case in `expected.json` through `engine.js` and compares results and renders exactly

Run the check:

```
python3 oracle.py && node test.js
```
