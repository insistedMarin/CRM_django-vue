<template>
  <div class="navbar">
    <div class="navbar-brand" @click="navigateToHome">MyCRM</div>
    <div class="nav-links">
      <!-- 你可以添加其他导航链接在这里 -->
      <div v-if="username"  class="username" @click="navigateToUserInfo">{{ username }}</div>
      <div v-if="username" class="logout" @click="logout">Logout</div>
      <div v-else class="login" @click="navigateToLogin">Login</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: ''
    };
  },
  created() {
    this.fetchUserInfo();
  },
  methods: {
    fetchUserInfo() {
      const token = localStorage.getItem('access_token');
      if (token) {
        axios.get('http://127.0.0.1:8000/user_info/', {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        })
        .then(response => {
          this.username = response.data.username;
        })
        .catch(error => {
          console.error('Error fetching user info', error);
        });
      }
    },
    logout() {
    // 删除存储的token
    localStorage.removeItem('access_token');

    // 删除当前用户名
    this.username = '';

    // 重定向到登录页面
    this.$router.push({ name: 'Login' });
  },
    navigateToHome(){
       this.$router.push({ name: 'Home' });
    },
    navigateToLogin() {
      this.$router.push({ name: 'Login' });
    },
    navigateToUserInfo() {
      this.$router.push({ name: 'UserInfo' });
    }
  }
};
</script>
<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 40px;
  background-color: #2c3e50;
  color: white;
  height: 60px;
  width: 100%;
}

.navbar-brand {
  font-size: 1.5rem;
  font-weight: bold;
  cursor: pointer;
}

.nav-links {
  display: flex;
  gap: 20px;
}

.nav-links a, .nav-links div {
  color: white;
  text-decoration: none;
  padding: 10px 15px;
  transition: background-color 0.3s;
  border-radius: 4px;

  /* 为链接添加悬停效果 */
  &:hover {
    background-color: rgba(255, 255, 255, 0.1);
  }
}

.username {
  cursor: pointer;
}

.logout, .login {
  cursor: pointer;
  background-color: #3498db;
  color: white;
  padding: 5px 10px;
  border-radius: 4px;
  transition: background-color 0.3s;

  &:hover {
    background-color: #2980b9;
  }
}
.logout:hover, .login:hover {
  background-color: #2980b9;
}
</style>