import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

// 创建Vuex实例
const store = new Vuex.Store({
    state: {
        count: 5,
    },
    getters: {
        getCount: function (state) {
            return state.count+10;
        },
    },
    mutations: {
        reductionFun(state) {
            state.count--;
        },
        addFun(state, n) {
            state.count+=n;
        },
    },
    actions: {
        reductionCount(context) {
            context.commit("reductionFun");
        },
        addCount(context, n) {
            context.commit("addFun", n);
        },
    },
})

export default store
