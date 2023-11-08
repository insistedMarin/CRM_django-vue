<template>
  <div>
    <NavBar />

    <div class="dashboard">
      <!-- 左侧导航栏 -->
      <SidebarMenu />

      <!-- 主内容区 -->
      <div class="main-content">
        <h1>Reports</h1>

        <!-- Report List -->
        <button @click="openAddReportModel">Add New Report</button>
        <ReportAdd :show="showAddModal" @close="showAddModal = false" @saved="fetchReports"></ReportAdd>
        <ReportEdit :show="showEditModal" :ReportData="selectedReport" @close="showEditModal = false" @updated="fetchReports"></ReportEdit>
        <ReportView :show="showViewModal" :ReportData="selectedReport" @close="showViewModal = false"></ReportView>
        <div class="report-list">
          <table>
            <thead>
              <tr>
                <th>Report Type</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="report in reports" :key="report.id">
                <td>{{ report.report_type }}</td>
                <td>
                  <button @click="viewReport(report)">View</button>
                  <button @click="editReport(report)">Edit</button>
                  <button @click="deleteReport(report.id)">Delete</button>
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
import ReportEdit from "@/components/ReportEdit.vue";
import ReportAdd from "@/components/ReportAdd.vue";
import ReportView from "@/components/ReportView.vue"
import axios from 'axios';

export default {
  name: "ReportList",
  components: {
    NavBar,
    SidebarMenu,
    ReportEdit,
    ReportAdd,
    ReportView
  },
  data() {
    return {
        showAddModal: false,
        showEditModal: false,
        showViewModal: false,
        selectedReport: null,
        reports: [],
    };
  },
  methods: {
    // Fetch reports from the API
    fetchReports() {
      const token = localStorage.getItem('access_token');
      axios.get('http://127.0.0.1:8000/reports', {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then(response => {
        this.reports = response.data;
      })
      .catch(error => {
        console.error('Error fetching reports:', error);
      });
    },
    openAddReportModel() {
      this.showAddModal = true;
    },
    editReport(report) {
      this.selectedReport = report;
      console.log(report);
      this.showEditModal = true;
    },
    viewReport(report) {
      this.selectedReport = report;
      console.log(report);
      this.showViewModal = true;
    },
    deleteReport(reportId) {
      const token = localStorage.getItem('access_token');
      axios.delete(`http://127.0.0.1:8000/reports/${reportId}`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then(() => {
        this.reports = this.reports.filter(report => report.id !== reportId);
      })
      .catch(error => {
        console.error('Error deleting report:', error);
        alert('Failed to delete report. Please try again later.');
      });
    }
  },
  created() {
    this.fetchReports();
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

.report-list {
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
