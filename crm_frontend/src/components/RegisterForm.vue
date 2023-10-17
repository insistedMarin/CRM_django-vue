<template>
  <div class="register-container">
    <h1>Register</h1>
    <form @submit.prevent="register" class="register-form">
      <input v-model="username" placeholder="Username" class="input-field" name="username" />
      <input v-model="password" type="password" placeholder="Password" class="input-field" name="password1" />
      <input v-model="password_confirm" type="password" placeholder="Confirm Password" class="input-field" name="password2" />
      <input v-model="email" placeholder="Email" class="input-field" name="email" />
      <div class="verification-container">
        <input v-model="verification_code" placeholder="Verification Code" class="input-field code-input" name="verification_code" />
        <button v-if="!verificationSuccess" class="send-code-button" @click.prevent="sendCode">Send Code</button>
        <span v-if="verificationSuccess" class="verified-icon">&#10004;</span> <!-- 使用HTML实体表示对勾 -->
      </div>
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
      verification_code: '',
      verificationSuccess: false
    };
  },
  methods: {
     sendCode() {
      axios.post('http://127.0.0.1:8000/send_verification_code/', { email: this.email })
        .then(response => {
          this.verificationSuccess = true;
          alert(response.data.message);
        })
        .catch(error => {
          alert('Error sending code:', error.response.data.detail);
        });
    },
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
  width: 300px;
  padding: 30px;
  border-radius: 5px;
  background-color: rgba(44, 62, 80, 0.8);
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
}

.input-field {
  display: block; /* 使输入框占满整行 */
  width: 100%;
  padding: 10px;
  margin: 10px 0; /* 上下间距保持为10px，左右间距为0 */
  border: 1px solid #3498db;
  border-radius: 3px;
  background-color: rgba(255, 255, 255, 0.1);
  color: white;
  outline: none;
  box-sizing: border-box; /* 保证宽度包括内边距和边框 */
}

.input-field::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.register-button {
  display: block; /* 使按钮占满整行 */
  width: 100%;
  background-color: #3498db;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 3px;
  cursor: pointer;
  transition: background-color 0.3s;
  font-weight: bold;
  margin-top: 10px; /* 与最后一个输入框的间距 */
}

.register-button:hover {
  background-color: #2980b9;
}

.verification-container {
  display: flex;
  align-items: center;  /* 垂直居中内容 */
  margin: 0;
}

.input-field, .send-code-button {
  height: 40px; /* 这个是示例高度，你可以根据需要进行调整 */
}


.code-input {
  flex: 1;  /* 使输入框占据可用空间 */
  margin-right: 10px;  /* 为了在输入框和按钮之间增加一些间隙 */
}

.send-code-button {
  /* 与.register-button的样式相似，但可能稍微缩小了 */
  background-color: #3498db;
  color: white;
  border: none;
  padding: 5px 10px;
  border-radius: 3px;
  cursor: pointer;
  transition: background-color 0.3s;
  font-weight: bold;
}

.send-code-button:hover {
  background-color: #2980b9;
}

.verified-icon {
  color: #4CAF50;  /* 对勾的颜色，你可以选择其他颜色 */
  font-size: 24px;  /* 对勾的大小 */
  margin-left: 10px;  /* 和按钮的间距 */
}

</style>

