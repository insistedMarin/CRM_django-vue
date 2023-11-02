<template>
  <div>
    <NavBar />

    <div class="dashboard">
      <SidebarMenu />
      <!-- 主内容区 -->
      <div class="main-content">
        <h1>Tasks</h1>
        <TaskEdit :show="showEditModal" :taskData="selectedTask" @close="showEditModal = false" @updated="fetchTasks"></TaskEdit>
        <!-- Task List -->
        <div class="task-list">
          <table>
            <thead>
              <tr>
                <th>Title</th>
                <th>Description</th>
                <th>Due Date</th>
                <th>Reminder</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="task in tasks" :key="task.id">
                <td>{{ task.title }}</td>
                <td>{{ task.description }}</td>
                <td>{{ task.due_date }}</td>
                <td>{{ task.reminder }}</td>
                <td>
                  <button @click="editTask(task)">Edit</button>
                  <button @click="deleteTask(task.id)">Delete</button>
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
import TaskEdit from "@/components/TaskEdit.vue";
import axios from 'axios';

export default {
  name: "TaskList",
  components: {
    NavBar,
    SidebarMenu,
    TaskEdit
  },
  data() {
    return {
      tasks: [],
      showEditModal: false,
    };
  },
  methods: {
    fetchTasks() {
      const token = localStorage.getItem('access_token');
      axios.get('http://127.0.0.1:8000/tasks', {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then(response => {
        this.tasks = response.data;
      })
      .catch(error => {
        console.error('Error fetching tasks:', error);
      });
    },
    editTask(task) {
      this.selectedTask = task;
      this.showEditModal = true;
    },
    deleteTask(taskId) {
      const token = localStorage.getItem('access_token');
      axios.delete(`http://127.0.0.1:8000/tasks/${taskId}`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then(() => {
        this.tasks = this.tasks.filter(task => task.id !== taskId);
      })
      .catch(error => {
        console.error('Error deleting task:', error);
        alert('Failed to delete task. Please try again later.');
      });
    }
  },
  created() {
    this.fetchTasks();
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
