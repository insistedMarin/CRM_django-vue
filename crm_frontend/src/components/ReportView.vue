<template>
  <div class="report-viewer" v-if="show">
    <div class="modal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <h2>Report Viewer</h2>
        <h3>{{report.report_type}}</h3>
        <div class="report-data">
          <pre>{{ report.data }}</pre>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    show: Boolean,
    ReportData: Object,
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
        console.log("view report");
        console.log(newVal)
      this.report = { ...newVal };
    }
  },
  methods: {
    closeModal() {
      this.$emit('close');
    },
  },
};
</script>

<style scoped>
/* 模态窗口的样式 */
.modal {
  display: block;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  position: relative;
  padding: 20px;
  width: 80%;
  background-color: #f9f9f9;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
}

.close {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 24px;
  cursor: pointer;
}

.report-data {
  text-align: left;
  padding: 10px;
}

pre {
  white-space: pre-wrap; /* 处理文本换行 */
}
</style>
