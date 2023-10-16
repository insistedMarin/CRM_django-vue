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
      // 密码格式验证
    const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    if (!passwordPattern.test(this.password)) {
      alert('Password should be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character.');
      return;
    }

    // 邮件格式验证
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;

    if (!emailPattern.test(this.email)) {
      alert('Invalid email format.');
      return;
    }


      // 准备要发送的数据
      const data = {
        username: this.username,
        password: this.password,
        password_confirm: this.password_confirm,
        email: this.email,
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
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #2c3e50;
  color: white;
}

.register-form {
  border: 1px solid #ccc;
  padding: 25px 40px; /* 增加左右的内边距 */
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.input-field {
  display: block; /* 使输入框占满整行 */
  width: 100%;
  padding: 10px;
  margin: 10px 0; /* 上下间距保持为10px，左右间距为0 */
  border: 1px solid #ccc;
  border-radius: 3px;
  outline: none;
  box-sizing: border-box; /* 保证宽度包括内边距和边框 */
}

.register-button {
  display: block; /* 使按钮占满整行 */
  width: 100%;
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 3px;
  cursor: pointer;
  font-weight: bold;
  margin-top: 10px; /* 与最后一个输入框的间距 */
}

.register-button:hover {
  background-color: #0056b3;
}
</style>

