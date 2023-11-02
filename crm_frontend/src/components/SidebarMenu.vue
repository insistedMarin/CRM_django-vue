<template>
  <div class="sidebar">
    <!-- 使用作用域插槽自定义 router-link 的渲染 -->
    <router-link to="/" exact class="menu-item" active-class="active">
      <template v-slot:default="{ navigate, href }">
        <div class="menu-item" @click="navigate" :href="href">Dashboard</div>
      </template>
    </router-link>

    <router-link to="/customer-list" class="menu-item" active-class="active">
      <template v-slot:default="{ navigate, href }">
        <div class="menu-item" @click="navigate" :href="href">Contacts</div>
      </template>
    </router-link>
    <router-link to="/opportunity-list" class="menu-item" active-class="active">
      <template v-slot:default="{ navigate, href }">
        <div class="menu-item" @click="navigate" :href="href">Opportunities</div>
      </template>
    </router-link>
    <router-link to="/task-list" class="menu-item" active-class="active">
      <template v-slot:default="{ navigate, href }">
        <div class="menu-item" @click="navigate" :href="href">Tasks</div>
      </template>
    </router-link>
    <div class="menu-item">Reports</div>
  </div>
</template>


<script>
export default {
  name: "SidebarMenu",
}
</script>

<style scoped>
.sidebar {
  width: 20%;
  background-color: #f6f6f6;
  padding: 2rem;
}

.menu-item {
  margin-bottom: 1rem;
  cursor: pointer;
}

.menu-item:hover {
  color: blue;
}
.menu-item.active {
  color: blue;
  font-weight: bold;
}


</style>