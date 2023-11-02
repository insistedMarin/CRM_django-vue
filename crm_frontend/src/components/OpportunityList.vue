<template>
  <div>
    <NavBar />

    <div class="dashboard">
      <!-- 左侧导航栏 -->
      <SidebarMenu />

      <!-- 主内容区 -->
      <div class="main-content">
        <h1>Sales Opportunities</h1>
         <OpportunityEdit :show="showEditModal" :opportunityData="selectedOpportunity" @close="showEditModal = false" @updated="fetchOpportunities"></OpportunityEdit>
        <!-- Opportunity List -->
        <div class="opportunity-list">
          <table>
            <thead>
              <tr>
                <th>Customer ID</th>
                <th>Customer Name</th>
                <th>Expected Revenue</th>
                <th>Current Stage</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="opportunity in opportunities" :key="opportunity.id">
                <td>{{ opportunity.customer}}</td>
                <td>{{ opportunity.customerName}}</td>
                <td>{{ opportunity.expected_revenue }}</td>
                <td>{{ opportunity.current_stage }}</td>
                <td>
                  <button @click="editOpportunity(opportunity)">Edit</button>
                  <button @click="deleteOpportunity(opportunity.id)">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from './NavBar.vue';
import SidebarMenu from "@/components/SidebarMenu.vue";
import OpportunityEdit from "@/components/OpportunityEdit.vue";
import axios from 'axios';

export default {
  name: "OpportunityList",
  components: {
    NavBar,
    SidebarMenu,
    OpportunityEdit
  },
  data() {
    return {
      opportunities: [],
      showEditModal: false,
    };
  },
  methods: {
    // Fetch opportunities from the API
    
   fetchOpportunities() {
  const token = localStorage.getItem('access_token');
  axios.get('http://127.0.0.1:8000/salesopportunities', {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  })
  .then(response => {
    // 获取销售机会数据
    const opportunities = response.data;

    // 遍历销售机会并获取客户信息
    const updatedOpportunities = opportunities.map(async opportunity => {
      const customerID = opportunity.customer;

      // 获取客户信息
      const customerResponse = await axios.get(`http://127.0.0.1:8000/customers/${customerID}`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      const customer = customerResponse.data;

      // 更新销售机会对象，将客户名称添加到销售机会数据中
      opportunity.customerName = customer.name;

      return opportunity;
    });

    // 将更新后的销售机会数据存储在组件中
    Promise.all(updatedOpportunities)
      .then(updatedOpportunities => {
        this.opportunities = updatedOpportunities;
      });
  })
  .catch(error => {
    console.error('Error fetching opportunities:', error);
  });
},
    editOpportunity(opportunity) {
      this.selectedOpportunity = opportunity;
      this.showEditModal = true;
      console.log(opportunity)
    },
    deleteOpportunity(opportunityId) {
       const token = localStorage.getItem('access_token');
      axios.delete(`http://127.0.0.1:8000/salesopportunities/${opportunityId}`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then(() => {
        this.opportunities = this.opportunities.filter(opportunity => opportunity.id !== opportunityId);
      })
      .catch(error => {
        console.error('Error deleting opportunity:', error);
        alert('Failed to delete opportunity. Please try again later.');
      });
    }
  },
  created() {
    this.fetchOpportunities();
  }
}
</script>

<style scoped>
.dashboard {
  display: flex;
}

.main-content {
  flex: 1;
  padding: 2rem;
}

.opportunity-list {
  margin-top: 2rem;
}

table {
  width: 100%;
  border-collapse: collapse;
}

table, th, td {
  border: 1px solid #e5e5e5;
}

th, td {
  padding: 0.5rem;
  text-align: left;
}

button {
  margin-right: 10px;
}
</style>
