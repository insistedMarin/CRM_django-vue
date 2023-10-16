<template>
  <div>
    <NavBar />
    <div class="user-info-container">
      <div class="user-card">
        <img src="@/assets/logo.png" alt="User Avatar" class="user-avatar"/> <!-- 默认头像，您可以更改路径 -->
        <h2>{{ userInfo.username }}</h2>
        <p>Email: {{ userInfo.email }}</p>
        <div class="user-actions">
          <button @click="editInfo">Edit information</button>
          <button @click="changePassword">Change password</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import NavBar from "@/components/NavBar.vue";

export default {
   components: {
    NavBar
  },
  data() {
    return {
      userInfo: {}
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
           this.userInfo.username = response.data.username;
        })
        .catch(error => {
          console.error('Error fetching user info', error);
        });
      }
    },
    editInfo(){},
    changePassword(){}

}}
</script>

<style scoped>
.user-info-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 60px); /* 假设NavBar的高度为60px */
}

.user-card {
  max-width: 400px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.user-avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin-bottom: 20px;
}

.user-actions {
  margin-top: 20px;
}

button {
  margin: 0 10px;
  padding: 10px 20px;
  border: none;
  border-radius: 3px;
  background-color: #007bff;
  color: #fff;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>