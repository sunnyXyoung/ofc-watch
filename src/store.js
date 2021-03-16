import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

// 定義一個新的 Vue Store
const store = new Vuex.Store({
    state: {
        round: '4',
    },
    mutations: {
        // 將state設定為參數
        ChangeRound(state, round) {
            // state的isLoading true/false 互轉
            state.round = round
        }
    }

})
export default store;