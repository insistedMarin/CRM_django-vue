<template>
  <div v-if="show" class="modal-overlay" @click="closeModal">
    <div class="modal" @click.stop>
      <h1>Add New Opportunity</h1>
      <form @submit.prevent="saveOpportunity">
      <div>
        <label>Expected Revenue:</label>
        <input type="number" v-model="opportunity.expected_revenue" required />
      </div>
      <div>
        <label>Current Stage:</label>
        <select v-model="opportunity.current_stage" required>
            <option value="initial_contact">Initial Contact</option>
            <option value="proposal">Proposal</option>
            <option value="negotiation">Negotiation</option>
          </select>
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
  name: "OpportunityAdd",
  props: {
    show: Boolean,
    customerData: Number
  },
  watch: {
    customerData(newVal) {
      this.opportunity.customer = newVal;
    }
  },
 data() {
    return {
      opportunity: {
        customer: '',
        expected_revenue: 0,
        current_stage: 'initial_contact',
      }
    };
  },
   methods: {
    async saveOpportunity() {
        
      const token = localStorage.getItem('access_token');
      try {
        const response = await axios.post('http://127.0.0.1:8000/salesopportunities/', this.opportunity,{
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });
        console.log(response)
        this.$emit('saved');
        this.closeModal();
      } catch (error) {
        console.error('Error saving opportunity:', error);
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
