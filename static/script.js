function validateNewRoundForm() {
    const scoreInputs = document.querySelectorAll('input[name="scores[]"]');
    const playerCount = scoreInputs.length;

    if (playerCount === 0) {
        alert('Please add players before submitting a new round.');
        return false;
    }

    if (playerCount === 1) {
        alert('There is only one player. Swipe requires at least two players. Please add an additional player!');
        return false;
    }

    return validateScores(scoreInputs);
}

function validateScores(scoreInputs) {
    let zeroCount = 0;
    let nonZeroCount = 0;

    for (const input of scoreInputs) {
        const score = parseInt(input.value);

        if (isNaN(score) || score < 0) {
            alert('Score must be a positive integer');
            return false;
        }

        if (score === 0) {
            zeroCount++;
        } else {
            nonZeroCount++;
        }
    }

    if (zeroCount > 1) {
        alert('There cannot be two scores with a value of 0.');
        return false;
    } else if (zeroCount === scoreInputs.length) {
        alert('At least one player should have a non-zero score.');
        return false;
    } else if (nonZeroCount === 0) {
        alert('At least one player should have a non-zero score.');
        return false;
    }

    return true;
}
