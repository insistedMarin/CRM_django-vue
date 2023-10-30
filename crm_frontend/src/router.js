import { createRouter, createWebHistory } from 'vue-router';
import LoginForm from "@/components/LoginForm.vue";
import RegisterForm from "@/components/RegisterForm.vue";
import HomePage from "@/components/HomePage.vue";
import UserInfo from "@/components/UserInfo.vue";
import CustomerList from "@/components/CustomerList.vue";
import axios from "axios";

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomePage,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/userinfo',
        name: 'UserInfo',
        component: UserInfo,
        meta: {
            requiresAuth: true
        }
    },
  {
    path: '/login',
    name: 'Login',
    component: LoginForm
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterForm
  },
    {
    path: '/customer-list',
    name: 'CustomerList',
    component: CustomerList,
        meta: {
        requiresAuth: true
    }
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        const token = localStorage.getItem('access_token');
        if (!token) {
            next({ name: 'Login' });
            return;
        }else{
            axios.get('http://127.0.0.1:8000/user_info/', {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        })
        .then(() => {
          next()
        })
        .catch(()=> {
             next({ name: 'Login' });
            return;
        });
        }
    } else {
        next();
    }
});

export default router;
