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
            <p>500</p>
          </div>

          <div class="widget">
            <h3>Open Opportunities</h3>
            <p>120</p>
          </div>

          <div class="widget">
            <h3>Tasks Due Today</h3>
            <p>10</p>
          </div>
        </div>

        <!-- 近期活动 -->
        <div class="recent-activities">
          <h2>Recent Activities</h2>
          <!-- ... 显示近期活动列表 -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from './NavBar.vue';
import SidebarMenu from "@/components/SidebarMenu.vue";

export default {
  name: "HomePage",
  components: {
    NavBar,
    SidebarMenu
  },

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
