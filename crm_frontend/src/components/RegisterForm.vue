<template>
  <div class="register-container">
    <h1>Register</h1>
    <form @submit.prevent="register" class="register-form">
      <input v-model="username" placeholder="Username" class="input-field" name="username" /> <!-- 添加 name 属性 -->
      <input v-model="password" type="password" placeholder="Password" class="input-field" name="password1" /> <!-- 添加 name 属性 -->
      <input v-model="password_confirm" type="password" placeholder="Confirm Password" class="input-field" name="password2" /> <!-- 添加 name 属性 -->
      <input v-model="email" placeholder="Email" class="input-field" name="email" /> <!-- 添加 name 属性 -->
      <button type="submit" class="register-button">Register</button>
    </form>
  </div>
</template>



<script>
import axios from "axios";
export default {
  data() {
    return {
      username: '',
      password: '',
      password_confirm: '',
      email: '',
    };
  },
  methods: {
    register() {
      // 检查密码是否一致
      if (this.password !== this.password_confirm) {
        alert('Passwords do not match');
        return;
      }

      // 准备要发送的数据
      const data = {
        username: this.username,
        password: this.password,
        email: this.email,
        first_name: 'Test456', // 这里可以设置默认的 first_name 和 last_name
        last_name: 'User456',
      };

      // 发送注册请求
      axios.post(' http://127.0.0.1:8000/register/', data)
        .then(response => {
          // 处理注册成功的情况
          console.log('Registration successful', response.data);
          // 可以跳转到登录页或其他操作
        })
        .catch(error => {
          // 处理注册失败的情况
          console.error('Registration failed', error.response.data);
          // 可以显示错误信息给用户
        });
    },
  },
};
</script>

<style scoped>
.register-container {
  text-align: center;
  margin-top: 60px;
}

.register-form {
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

.register-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 3px;
  cursor: pointer;
  font-weight: bold;
}

.register-button:hover {
  background-color: #0056b3;
}
</style>
