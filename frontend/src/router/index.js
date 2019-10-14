import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/main/index'
import MainPage from '@/components/page/MainPage'
import ErrorPage from '@/components/error/ErrorPage'
import Login from '@/components/login/login'
import ProjectDetail from '@/components/page/ProjectDetail'

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
            }, {
                name: 'projectDetail',
                path: '/projectDetail',
                component: ProjectDetail
            }]
        }, {
            path: '*',
            name: 'error',
            component: ErrorPage,
        }
    ]
})
