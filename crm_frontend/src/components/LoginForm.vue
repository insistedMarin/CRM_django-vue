<template>
<div class="login-container">
  <h1>Login</h1>
  <form @submit.prevent="login" class="login-form">
    <input v-model="username" placeholder="Username" class="input-field" name="username" />
    <input v-model="password" type="password" placeholder="Password" class="input-field" name="password" />
    <button type="submit" class="login-button">Login</button>
  </form>
</div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    login() {
      // 准备要发送的数据
      const data = {
        username: this.username,
        password: this.password,
      };

      // 发送登录请求
    axios.post('http://127.0.0.1:8000/login/', data)
        .then(response => {
          console.log('Login successful', response.data);
          localStorage.setItem('access_token', response.data.access_token);

          // 跳转到主页
          this.$router.push({ name: 'Home' });
      })
        .catch(error => {
          if (error.response && error.response.data) {
            console.error('Login failed', error.response.data);
              } else {
            console.error('Login failed', error.message);
            }
        });
    },
  },
};
</script>

<style scoped>
.login-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #2c3e50;
  color: white;
}

h1 {
  margin-bottom: 20px;
}

.login-form {
  width: 300px;
  padding: 30px;
  border-radius: 5px;
  background-color: rgba(44, 62, 80, 0.8);
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
}


.input-field {
  width: 100%;
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #3498db;
  border-radius: 3px;
  background-color: rgba(255, 255, 255, 0.1);
  color: white;
  outline: none;
  box-sizing: border-box;  /* 确保input宽度包括内边距和边框 */
}

.input-field::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.login-button {
  width: 100%;  /* 让按钮的宽度也占满容器 */
  margin-top: 10px;
  background-color: #3498db;
  border: none;
  padding: 10px 20px;
  border-radius: 3px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.login-button:hover {
  background-color: #2980b9;
}
</style>

