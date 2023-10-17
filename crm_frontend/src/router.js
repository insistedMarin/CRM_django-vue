import { createRouter, createWebHistory } from 'vue-router';
import LoginForm from "@/components/LoginForm.vue";
import RegisterForm from "@/components/RegisterForm.vue";
import HomePage from "@/components/HomePage.vue";
import UserInfo from "@/components/UserInfo.vue";

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
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
    // 检查要访问的路由是否需要身份验证
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (!localStorage.getItem('access_token')) {
            // 如果用户未登录，重定向到登录页面
            next({ name: 'Login' });
        } else {
            next();
        }
    } else {
        next();
    }
});

export default router;
