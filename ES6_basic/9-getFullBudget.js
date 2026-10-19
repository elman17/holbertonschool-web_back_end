import getBudgetForCurrentYear from "./8-getBudgetCurrentYear";

export default function getFullBudgetObject(income, gdp, cspiys) {
  const budget = getBudgetForCurrentYear(income, gdp, capita);

  const fullBudget = {
    ...budget,
    getIncomeInDollars(income) {
      return `$${income}`;
    },
    getIncomeInEuros(income) {
      return `${income} euros`;
    },
  };

  return fullBudget;
}
