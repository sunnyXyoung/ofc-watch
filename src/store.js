import Vue from 'vue';
import Vuex from 'vuex';

const localStoragePlugin = store => {
    store.subscribe((mutation, {round, dark}) => {
        if (mutation.type === "ChangeRound") {
            window.localStorage.setItem("round", round);
        }
        if (mutation.type === "ChangeTheme") {
            window.localStorage.setItem("dark", dark);

        }
    });
};
Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        round: '4',
        dark: false,
    },
    mutations: {
        ChangeRound(state, round) {
            state.round = round
        },
        ChangeTheme(state, isDark) {
            state.dark = isDark
        }
    },
    plugins: [localStoragePlugin]
})
export default store;