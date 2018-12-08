const feature = require('./feature')

describe('there is a feature to double a number', () => {
  test('double 1 equals 2', () => {
    expect(feature.double(1)).toEqual(2)
  })
})

describe('there is a feature to calculate sum of two number', () => {
  test('sum of 1 and 2 equals 3', () => {
    expect(feature.sum(1, 2)).toEqual(3)
  })
})
