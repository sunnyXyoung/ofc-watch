import Vue from 'vue';
import Vuex from 'vuex';

const localStoragePlugin = store => {
    store.subscribe((mutation, {round}) => {
        if (mutation.type === "ChangeRound") {
            window.localStorage.setItem("round", round);
        }
    });
};
Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        round: '4',
    },
    mutations: {
        ChangeRound(state, round) {
            state.round = round
        }
    },
    plugins: [localStoragePlugin]
})
export default store;