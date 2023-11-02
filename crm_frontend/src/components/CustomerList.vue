<template>
  <div>
    <NavBar />

    <div class="dashboard">
      <SidebarMenu />

      <!-- 主内容区 -->
      <div class="main-content">
        <h1>Customers</h1>

        <input type="text" v-model="search" placeholder="Search for a customer..."/>

        <button @click="openAddCustomerModel">Add New Customer</button>
        <CustomerAdd :show="showAddModal" @close="showAddModal = false" @saved="fetchCustomers"></CustomerAdd>
        <CustomerEdit :show="showEditModal" :customerData="selectedCustomer" @close="showEditModal = false" @updated="fetchCustomers"></CustomerEdit>
        <OpportunityAdd :show="showAddOpportunityModel" :customerData="selectedCustomer" @close="showAddOpportunityModel = false"></OpportunityAdd>
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Company</th>
              <th>Email</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="customer in filteredCustomers" :key="customer.id">
              <td>{{ customer.name }}</td>
              <td>{{ customer.company }}</td>
              <td>{{ customer.email }}</td>
              <td>
                <button @click="editCustomer(customer)">Edit</button>
                <button @click="deleteCustomer(customer.id)">Delete</button>
                <button @click="openAddOpportunityModel(customer.id)">Add Opportunity</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import NavBar from './NavBar.vue';
import CustomerAdd from "@/components/CustomerAdd.vue";
import CustomerEdit from "@/components/CustomerEdit.vue";
import OpportunityAdd from "@/components/OpportunityAdd.vue";
import SidebarMenu from "@/components/SidebarMenu.vue";

export default {
  name: "CustomersList",
  components: {
    NavBar,
    SidebarMenu,
    CustomerAdd,
    CustomerEdit,
    OpportunityAdd
  },
  data() {
    return {
      customers: [],
      showAddModal: false,
      showAddOpportunityModel:false,
      search: '',
      showEditModal: false,
    selectedCustomer: null,
    };
  },
  computed: {
    filteredCustomers() {
      if (this.search) {
        return this.customers.filter(customer => customer.name.includes(this.search));
      }
      return this.customers;
    }
  },
  methods: {
    fetchCustomers() {
      const token = localStorage.getItem('access_token');
      axios.get('http://127.0.0.1:8000/customers',{
          headers: {
            'Authorization': `Bearer ${token}`
          }
        })
        .then(response => {
          console.log("获得数据")
          console.log(response)
          this.customers = response.data;
        })
        .catch(error => {
          console.error('Error fetching customers:', error);
        });
    },
    openAddCustomerModel() {
      this.showAddModal = true;
    },
    openAddOpportunityModel(customerid){
      this.selectedCustomer=customerid
      this.showAddOpportunityModel=true;
    },
    editCustomer(customer) {
      this.selectedCustomer = customer;
      this.showEditModal = true;
    },
    deleteCustomer(customerId) {
       const token = localStorage.getItem('access_token');
      axios.delete(`http://127.0.0.1:8000/customers/${customerId}`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then(() => {
        this.customers = this.customers.filter(customer => customer.id !== customerId);
      })
      .catch(error => {
        console.error('Error deleting customer:', error);
        alert('Failed to delete customer. Please try again later.');
      });
    }
  },
  created() {
    this.fetchCustomers();
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
