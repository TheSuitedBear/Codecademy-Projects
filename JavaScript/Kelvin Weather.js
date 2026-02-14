// This is the temperature of Kelvin
const kelvin = 295

// This is a celsius variable, it converts the temperature of Kelvin to Celsius
let celsius = kelvin - 273

// This converts celcius into Fahrenheit
let fahrenheit = celsius * (9/5) + 32

// Converts it to a whole number
fahrenheit = Math.floor(fahrenheit)

console.log("The temperature is " + fahrenheit + " degrees Fahrenheit")

let newton = celsius * (33/100)

newton = Math.floor(newton)

console.log("The temperature is " + newton + " degrees newton")