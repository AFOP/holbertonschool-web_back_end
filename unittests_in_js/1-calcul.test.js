const calculateNumber = require("./1-calcul.js");
const assert = require("assert");

describe('SUM', () => {
  it('returns rounded positive sum', () => {
    assert.strictEqual(calculateNumber('SUM', 4, 8), 12);
    assert.strictEqual(calculateNumber('SUM', 1.9, 0), 2);
    assert.strictEqual(calculateNumber('SUM', 6.1, 6.1), 12);
    assert.strictEqual(calculateNumber('SUM', 0.1, 0.2), 0);
    assert.strictEqual(calculateNumber('SUM', 0.1, 0.6), 1);
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
  });

  it('returns rounded negative sum', () => {
    assert.strictEqual(calculateNumber('SUM', -1, -3), -4);
    assert.strictEqual(calculateNumber('SUM', -1.4, -3.6), -5);
  });

  it('returns TypeError', () => {
    assert.throws(() => calculateNumber('SUM', NaN, 5.6), { name: 'TypeError' });
    assert.throws(() => calculateNumber('SUM', 5.6, NaN), { name: 'TypeError' });
    assert.throws(() => calculateNumber('SUM', NaN, NaN), { name: 'TypeError' });
  });
});
