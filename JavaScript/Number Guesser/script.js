let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// This is the area where the challenge takes place, all code written is my own, no AI used (shocker in today's age.)

const generateTarget = () => {
  return Math.floor(Math.random() * 9);
};

const compareGuesses = (human, computer, secret) => {
  if (Math.abs(human - secret) <= (Math.abs(computer - secret))) {
    return true;
  } else {
    return false;
  };
};

const updateScore = (winner) => {
  if (winner === 'human') {
    humanScore += 1;
  } else if (winner === 'computer') {
    computerScore += 1;
  } else {
    return 'Error';
  };
};

const advanceRound = () => {
  currentRoundNumber += 1;
};