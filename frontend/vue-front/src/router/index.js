import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
    {path: '/', component: 'Home'},
    {
        path: '/diary',
        component: 'Diary',
        children: [
            { path: 'new', component: () => import(`@/components/Edit.vue`) },
            { path: 'edit/', component: () => import(`@/components/Edit.vue`) },
            { path: 'edit/:id', component: () => import(`@/components/Edit.vue`) },
            { path: 'post/', component: () => import(`@/components/Page.vue`) },
            { path: 'post/:id', component: () => import(`@/components/Page.vue`) }
        ]
    },
    {path: '*', component: 'NotFound'}
];

const routes = routerOptions.map(route => {
    return {
        ...route,
        component: () => import(`@/components/${route.component}.vue`),
    }
});

Vue.use(Router);

export default new Router({
    routes,
    mode: 'history'
})