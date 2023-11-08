<template>
  <div v-if="show" class="modal-overlay" @click="closeModal">
    <div class="modal" @click.stop>
      <h1>Edit Report</h1>
      <form @submit.prevent="updateReport">
        <div>
          <label>Report Type:</label>
          <select v-model="report.report_type" required>
            <option value="sales_funnel">Sales Funnel</option>
            <option value="customer_interaction">Customer Interaction</option>
            <option value="monthly_sales">Monthly Sales</option>
          </select>
        </div>
        <div>
          <label>Data:</label>
          <textarea v-model="report.data" class="larger-textarea"></textarea>
        </div>
        <button type="submit">Update</button>
        <button class="cancel-button" @click="closeModal">Cancel</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    show: Boolean,
    ReportData: Object
  },
  data() {
    return {
      report: {
        report_type: "",
        data:""
      }
    };
  },
  watch: {
    ReportData(newVal) {
        console.log("edit report");
        console.log(newVal)
      this.report = { ...newVal };
    }
  },
  methods: {
    async updateReport() {
      const token = localStorage.getItem('access_token');
      try {
        await axios.put(`http://127.0.0.1:8000/reports/${this.report.id}/`, this.report, {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });
        this.$emit('updated');
        this.closeModal();
      } catch (error) {
        console.error('Error updating report:', error);
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

.cancel-button {
  background-color: #e5e5e5;
  color: #333333;
}

.cancel-button:hover {
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
.larger-textarea {
  width: 70%;
  height: 300px;
}
</style>
