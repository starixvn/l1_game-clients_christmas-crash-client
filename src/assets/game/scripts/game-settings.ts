

export const GAME_NAME = "ChristmasCrash";

export const settings = {
    id: 106,
    name: GAME_NAME,
    observerNamespace: GAME_NAME,
    namespaces: [GAME_NAME, "Spaceflight"],
    durations: {
        wholeRound: 14,
        lockingBet: 3,
        placingBet: 10,
        generatingResult: 0,
        startRound: 1,
    },
    numberOfRoundHistory: 11,
    validateBalanceWhenBet: true,
};

