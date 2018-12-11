import Vue from 'vue'
import Vuex from 'vuex'
import diary from './modules/diary'

Vue.use(Vuex)

// meet up.vue component

export const store = new Vuex.Store({
    modules: {
        diary
    }
})