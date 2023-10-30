<template>
  <div v-if="show" class="modal-overlay" @click="closeModal">
    <div class="modal" @click.stop>
      <h1>Add New Customer</h1>
      <form @submit.prevent="saveCustomer">
      <div>
        <label>Name:</label>
        <input type="text" v-model="customer.name" required />
      </div>
      <div>
        <label>Company:</label>
        <input type="text" v-model="customer.company" required />
      </div>
      <div>
        <label>Job Title:</label>
        <input type="text" v-model="customer.job_title" />
      </div>
      <div>
        <label>Phone:</label>
        <input type="text" v-model="customer.phone" />
      </div>
      <div>
        <label>Email:</label>
        <input type="email" v-model="customer.email" required />
      </div>
      <div>
        <label>Address:</label>
        <textarea v-model="customer.address"></textarea>
      </div>
      <div>
        <label>Interactions:</label>
        <textarea v-model="customer.interactions"></textarea>
      </div>

      <button type="submit">Save</button>
        <button @click="closeModal">Cancel</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CustomerAdd",
  props: {
    show: Boolean
  },
 data() {
    return {
      customer: {
        name: '',
        company: '',
        job_title: '',
        phone: '',
        email: '',
        address: '',
        interactions: ''
      }
    };
  },
   methods: {
    async saveCustomer() {
      const token = localStorage.getItem('access_token');
      try {
        const response = await axios.post('http://127.0.0.1:8000/customers/', this.customer,{
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });
        console.log(response)
        this.$emit('saved');
        this.closeModal();
      } catch (error) {
        console.error('Error saving customer:', error);
      }
    },
    closeModal() {
      this.$emit('close');
    }
  }
};
</script>

<style scoped>
/* 全局样式 */
h1 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

form {
  background-color: #f6f6f6;
  padding: 2rem;
  border-radius: 8px;
  max-width: 600px;
  margin: 0 auto;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

input[type="text"],
input[type="email"],
textarea {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #e5e5e5;
  border-radius: 4px;
  margin-bottom: 1rem;
}

button {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s;
}

button[type="submit"] {
  background-color: #007BFF;
  color: #ffffff;
  margin-right: 1rem;
}

button[type="submit"]:hover {
  background-color: #0056b3;
}

button[@click="cancel"] {
  background-color: #e5e5e5;
  color: #333333;
}

button[@click="cancel"]:hover {
  background-color: #c3c3c3;
}
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  background-color: #ffffff;
  padding: 2rem;
  width: 60%;
  max-width: 600px;
  border-radius: 8px;
}
</style>
