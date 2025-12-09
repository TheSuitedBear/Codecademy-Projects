// This variable holds the age of the person
let myAge = prompt('Enter your age:');
// The first 2 years of a dogs life is longer
let earlyYears = 2;

earlyYears = earlyYears * 10.5;

// The later years are different, so we subtract 2 to avoid the complications of the first 2 years
let laterYears = myAge - 2;

// Each subsequent year after 2 is worth 4 in dog years
laterYears *= 4

console.log(earlyYears)
console.log(laterYears)

// This adds both previous values to give the total value in dog years
let myAgeInDogYears = earlyYears + laterYears

// Returns my name in all lower case
let myName = "Callum".toLowerCase();

// This puts it all together in one sentence
console.log(`my name is ${myName}. I am ${myAge} years old in human years which is ${myAgeInDogYears} years old in dog years.`)

console.log(myAge)