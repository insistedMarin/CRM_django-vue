<template>
<div class="login-container">
  <h1>Login</h1>
  <form @submit.prevent="login" class="login-form">
    <input v-model="username" placeholder="Username" class="input-field" name="username" /> <!-- 添加 name 属性 -->
    <input v-model="password" type="password" placeholder="Password" class="input-field" name="password" /> <!-- 添加 name 属性 -->
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
      axios.post(' http://127.0.0.1:8000/login/', data)
        .then(response => {
          // 处理登录成功的情况
          console.log('Login successful', response.data);
          // 可以跳转到用户的个人页面或其他操作
        })
        .catch(error => {
          // 处理登录失败的情况
          console.error('Login failed', error.response.data);
          // 可以显示错误信息给用户
        });
    },
  },
};
</script>

<style scoped>
.login-container {
  text-align: center;
  margin: 0 auto;
}

.login-form {
  display: inline-block;
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.input-field {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 3px;
  outline: none;
}

.login-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 3px;
  cursor: pointer;
  font-weight: bold;
}

.login-button:hover {
  background-color: #0056b3;
}
</style>

