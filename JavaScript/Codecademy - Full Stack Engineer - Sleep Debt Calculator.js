function getSleepHours(day) {
  day = day.toLowerCase()
  if (day === 'monday') {
    return 8;
  } else if (day === 'tuesday') {
    return 7;
  } else if (day === 'wednesday') {
    return 6;
  } else if (day === 'thursday') {
    return 9;
  } else if (day === 'friday') {
    return 5;
  } else if (day === 'saturday') {
    return 8;
  } else if (day === 'sunday') {
    return 9;
  } else {
    return 'Not a valid day';
  };
};

function getActualSleepHours() {
  let total = 0;
  total += getSleepHours('monday');
  total += getSleepHours('tuesday');
  total += getSleepHours('wednesday');
  total += getSleepHours('thursday');
  total += getSleepHours('friday');
  total += getSleepHours('saturday');
  total += getSleepHours('sunday');
  return total;
};

function getIdealSleepHours() {
  let idealHours = 8;
  return (idealHours * 7);
};

function calculateSleepDebt() {
  let actualSleepHours = getActualSleepHours();
  let idealSleepHours = getIdealSleepHours();
  if (actualSleepHours === idealSleepHours) {
    console.log('You got a perfect amount of sleep this week!');
  } else if (actualSleepHours > idealSleepHours) {
    console.log('You got more hours of sleep than you needed this week! You must be well rested.');
  } else {
    let sleepDebt = idealSleepHours - actualSleepHours;
    console.log('You should get some more rest, you need it!');
    console.log('You need approximately ' + sleepDebt + ' more hours of sleep.');
  };
};

calculateSleepDebt();