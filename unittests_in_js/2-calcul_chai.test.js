const calculateNumber = require("./2-calcul_chai.js");
const { expect } = require("chai");

describe('SUM', () => {
  it('returns rounded positive sum', () => {
    expect(calculateNumber('SUM', 4, 8)).to.equal(12);
    expect(calculateNumber('SUM', 1.9, 0)).to.equal(2);
    expect(calculateNumber('SUM', 6.1, 6.1)).to.equal(12);
    expect(calculateNumber('SUM', 0.1, 0.2)).to.equal(0);
    expect(calculateNumber('SUM', 0.1, 0.6)).to.equal(1);
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  });

  it('returns rounded negative sum', () => {
    expect(calculateNumber('SUM', -1, -3)).to.equal(-4);
    expect(calculateNumber('SUM', -1.4, -3.6)).to.equal(-5);
  });

  it('returns TypeError', () => {
    expect(() => calculateNumber('SUM', NaN, 5.6)).to.throw(TypeError);
    expect(() => calculateNumber('SUM', 5.6, NaN)).to.throw(TypeError);
    expect(() => calculateNumber('SUM', NaN, NaN)).to.throw(TypeError);
  });
});
