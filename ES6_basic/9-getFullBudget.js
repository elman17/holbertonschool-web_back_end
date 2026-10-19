import getBudgetForCurrentYear from "./8-getBudgetCurrentYear.js";

export default function getFullBudgetObject(income, gdp, capita) {
  const budget = getBudgetForCurrentYear(income, gdp, capita);

  const fullBudget = {
    ...budget,
    income,
    gdp,
    capita,
    getIncomeInDollars(income) {
      return `$${income}`;
    },
    getIncomeInEuros(income) {
      return `${income} euros`;
    },
  };

  return fullBudget;
}
