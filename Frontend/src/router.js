import WelcomePage from './components/WelcomePage.vue'
import SignUp from './components/accountPages/SignUp.vue'
import LoginPage from './components/accountPages/LoginPage.vue'
import MyProfile from './components/profile/MyProfile.vue'
import MySettings from './components/profile/MySettings.vue'
import LiveMarket from './components/mainPages/LiveMarket.vue'
import ConverterPage from './components/mainPages/ConverterPage.vue'
import ExchangesPage from './components/mainPages/ExchangesPage.vue'
import InvestmentData from './components/mainPages/InvestmentData.vue'
import CoinData from './components/mainPages/CoinData.vue'
import HomePage from './components/mainPages/HomePage.vue'
import NotFound from './components/NotFound.vue'
//import Router from 'vue-router'
//import Vue from 'vue'

//Vue.use(Router)



import { createRouter , createWebHistory} from 'vue-router'


const  routes = [

    {
        path : '/',
        name : 'welcome',
        component : WelcomePage
    },
    {
        path : '/signup',
        name : 'signup',
        component : SignUp
    },
    {
        path : '/login',
        name : 'login',
        component : LoginPage
    },
    {
        path : '/home',
        name : 'home',
        component : HomePage
    },
    {
        path : '/profile',
        name : 'profile',
        component : MyProfile
    },
    {
        path : '/settings',
        name : 'settings',
        component : MySettings
    },
    {
        path : '/market',
        name : 'market',
        component : LiveMarket
    },
    {
        path : '/investmentData',
        name : 'investmentData',
        component : InvestmentData
    },
    {
        path : '/converter',
        name : 'converter',
        component : ConverterPage
    },
    {
        path : '/exchanges',
        name : 'exchanges',
        component : ExchangesPage
    },
    {
        path : '/cointData/:id',
        name : 'coinData',
        component :CoinData,
        props:true
    },
    {
        path : '/:pathMacth(.*)*',
        name : 'notFound',
        component : NotFound
    }
    

]





const router = createRouter({
    history: createWebHistory(),
    routes,


})


export default router;