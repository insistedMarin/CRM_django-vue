<template>
  <div>
    <NavBar />

    <div class="dashboard">
      <!-- 左侧导航栏 -->
      <SidebarMenu />

      <!-- 主内容区 -->
      <div class="main-content">
        <h1>Welcome to CRM Dashboard</h1>

        <!-- 仪表板小部件 -->
        <div class="widgets">
          <div class="widget">
            <h3>Total Contacts</h3>
            <p>{{ totalContacts }}</p>
          </div>

          <div class="widget">
            <h3>Open Opportunities</h3>
            <p>{{ openOpportunities }}</p>
          </div>

          <div class="widget">
            <h3>Tasks Due Today</h3>
            <p>{{ tasksDueToday }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from './NavBar.vue';
import SidebarMenu from "@/components/SidebarMenu.vue";
import axios from "axios";

export default {
  name: "HomePage",
  components: {
    NavBar,
    SidebarMenu
  },
  data() {
    return {
      totalContacts: 0,
      openOpportunities: 0,
      tasksDueToday: 0,
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      const token = localStorage.getItem('access_token');

      // 获取总联系人数
      axios.get('http://127.0.0.1:8000/customers', {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then(response => {
        this.totalContacts = response.data.length;
      })
      .catch(error => {
        console.error("Error fetching total contacts: ", error);
      });

      // 获取开放的销售机会数量
      axios.get('http://127.0.0.1:8000/salesopportunities', {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then(response => {
        this.openOpportunities = response.data.length;
      })
      .catch(error => {
        console.error("Error fetching open opportunities: ", error);
      });

      // 获取今天到期的任务数量
      axios.get('http://127.0.0.1:8000/tasks/due_today_count/', {
  headers: {
    'Authorization': `Bearer ${token}`
  }
})
.then(response => {
  this.tasksDueToday = response.data.count; // 修改为 data.count
})
.catch(error => {
  console.error("Error fetching tasks due today: ", error);
});

    }
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

.widgets {
  display: flex;
  gap: 2rem;
}

.widget {
  flex: 1;
  padding: 2rem;
  border: 1px solid #e5e5e5;
  border-radius: 5px;
}

.recent-activities {
  margin-top: 2rem;
}
</style>
