/* enlist-disable */
export default function hasValuesFromArray(set, array) {
  const has = array.every((value) => set.has(value));
  return has;
}
