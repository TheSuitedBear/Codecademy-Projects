const getUserChoice = userInput => {
  userInput = userInput.toLowerCase();
  if (userInput === 'rock' || userInput === 'paper' || userInput === 'scissors' || userInput === 'bomb') {
    return userInput;
  } else {
    console.log("Error, input not accepted.");
  };
};

function getComputerChoice() {
  let number = Math.random() * 3;
  number = Math.floor(number);
  if (number === 0) {
    return 'rock'; 
  } else if (number === 1) {
    return 'paper';
  } else if (number === 2) {
    return 'scissors';
  } else {
    return 'Error';
  };
};

function determineWinner(userChoice, computerChoice) {
  if (userChoice === 'bomb') {
    return 'The Player won, and destroyed the arena with them.'
  }
  if (userChoice === computerChoice) {
    return 'The game is a tie!';
  };
  if (userChoice === 'rock') {
    if (computerChoice === 'paper') {
      return 'The Computer wins!';
    } else {
      return 'The Player wins!';
    };
  } else if (userChoice === 'paper') {
      if (computerChoice === 'scissors') {
        return 'The Computer wins!';
      } else {
        return 'The Player wins!';
      };
  } else if (userChoice === 'scissors') {
      if (computerChoice === 'rock') {
        return 'The Computer wins!';
      } else {
        return 'The Player wins!';
      };
  };
};

function playGame() {
  let userChoice = getUserChoice('paper');
  let computerChoice = getComputerChoice();
  console.log('Player picks ' + userChoice);
  console.log('Computer picks ' + computerChoice);
  console.log(determineWinner(userChoice, computerChoice));
};

playGame();