import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/main/index'
import MainPage from '@/components/page/MainPage'
import ErrorPage from '@/components/error/ErrorPage'
import Login from '@/components/login/login'

Vue.use(Router)

export default new Router({
    // mode: 'history',
    routes: [
        {
            path: '/',
            name: 'index',
            component: Main,
            children: [{
                path: '/mainPage',
                name: 'MainPage',
                component: MainPage,
            },{
                path: '/login',
                name: 'login',
                component: Login
            }]
        }, {
            path: '*',
            name: 'error',
            component: ErrorPage,
        }
    ]
})
