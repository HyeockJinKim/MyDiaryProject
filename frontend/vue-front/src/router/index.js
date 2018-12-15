import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
    {path: '/', component: 'Home'},
    {
        path: '/diary',
        component: 'Diary',
        children: [
            { path: 'new', component: () => import(`@/components/Edit.vue`), name: 'new' },
            { path: 'edit/', component: () => import(`@/components/Edit.vue`), name: 'edit_new' },
            { path: 'edit/:id', component: () => import(`@/components/Edit.vue`), name: 'edit' },
            { path: 'post/', component: () => import(`@/components/Page.vue`), name: 'latest_post' },
            { path: 'post/:id', component: () => import(`@/components/Page.vue`), name: 'post' }
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