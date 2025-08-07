<template>
  <div class="investigation-content-container">
    <div class="investigation-header">
      <div class="sub-tabs">
        <a href="#" :class="{ active: activeSubTab === 'all' }" @click.prevent="activeSubTab = 'all'">All</a>
        <a href="#" :class="{ active: activeSubTab === 'completed' }" @click.prevent="activeSubTab = 'completed'">Completed</a>
        <a href="#" :class="{ active: activeSubTab === 'processing' }" @click.prevent="activeSubTab = 'processing'">Processing</a>
      </div>
    </div>
    
    <div class="task-list">
      <!-- Processing Task -->
      <div v-if="activeSubTab === 'all' || activeSubTab === 'processing'" class="task-card processing">
        <div class="task-image">
          <img src="https://placehold.co/100x100/363636/E0E0E0?text=Face" alt="Face" class="face-image">
        </div>
        <div class="task-details">
          <div class="task-status">
            <span>Processing</span>
            <span class="status-indicator"></span>
          </div>
          <div class="task-info">
            <span class="task-title">task-04082025-1620</span>
            <p>Execution time: 4 Aug 2025 16:20:38</p>
            <p>Duration: &lt; 10 sec.</p>
            <p>Time range: 4 Aug 2025 15:29 - 4 Aug 2025 16:29</p>
            <p>Live Channel: rtsp://11.0.0.101</p>
            <p>Nx Video Archive: rtsp://192.168.1.101</p>
          </div>
          <div class="task-ips">
            <div class="ip-group">
              <span class="ip">rtsp://11.0.0.102</span>
              <span class="ip">rtsp://11.0.0.101</span>
              <span class="ip">rtsp://192.168.2.101</span>
            </div>
            <div class="ip-group">
              <span class="ip">CS-C6N-B0-1GZWF-IND-CXD</span>
              <span class="ip">rtsp://192.168.2.0.0</span>
              <span class="ip">CS-C6N-B0-1GZWF-IND-CXD</span>
            </div>
            <div class="ip-group">
              <span class="ip">rtsp://192.168.2.135</span>
              <span class="ip">rtsp://192.168.68.111</span>
              <span class="ip">rtsp://192.168.0.199</span>
            </div>
            <div class="ip-group">
              <span class="ip">rtsp://192.168.2.135</span>
              <span class="ip">CS-H6c-R105-1L2WF</span>
            </div>
          </div>
        </div>
        <div class="task-actions">
          <div class="progress-bar-container">
            <div class="progress-fill" style="width: 50%;"></div>
            <span class="progress-text">50%</span>
          </div>
          <button class="action-btn stop-btn">Stop</button>
        </div>
      </div>

      <!-- Completed Tasks -->
      <div v-if="activeSubTab === 'all' || activeSubTab === 'completed'" class="task-card completed">
        <div class="task-image">
          <img src="https://placehold.co/100x100/363636/E0E0E0?text=Face" alt="Face" class="face-image">
        </div>
        <div class="task-details">
          <div class="task-status">
            <span>Completed</span>
            <span class="status-indicator"></span>
          </div>
          <div class="task-info">
            <span class="task-title">task-15072025-1412</span>
            <p>Execution time: 15 Jul 2025 14:13:00</p>
            <p>Duration: &lt; 29 sec.</p>
            <p>Time range: 15 Jul 2025 13:23 - 15 Jul 2025 14:23</p>
            <p>Live Channel: rtsp://11.0.0.101</p>
            <p>Nx Video Archive: rtsp://192.168.1.101</p>
          </div>
          <div class="task-ips">
            <div class="ip-group">
              <span class="ip">rtsp://11.0.0.102</span>
              <span class="ip">rtsp://192.168.2.0.0</span>
              <span class="ip">rtsp://11.0.0.101</span>
            </div>
            <div class="ip-group">
              <span class="ip">CS-C6N-B0-1GZWF-IND-CXD</span>
              <span class="ip">rtsp://192.168.68.111</span>
              <span class="ip">rtsp://192.168.0.199</span>
            </div>
            <div class="ip-group">
              <span class="ip">rtsp://192.168.2.135</span>
              <span class="ip">CS-H6c-R105-1L2WF</span>
            </div>
          </div>
        </div>
        <div class="task-actions">
          <div class="progress-bar-container">
            <div class="progress-fill completed" style="width: 100%;"></div>
            <span class="progress-text">100%</span>
          </div>
          <div class="completed-actions">
            <button class="action-btn">Delete</button>
            <button class="action-btn">View</button>
          </div>
        </div>
      </div>

      <!-- More Completed Tasks -->
      <div v-if="activeSubTab === 'all' || activeSubTab === 'completed'" class="task-card completed">
        <div class="task-image">
          <img src="https://placehold.co/100x100/363636/E0E0E0?text=Face" alt="Face" class="face-image">
        </div>
        <div class="task-details">
          <div class="task-status">
            <span>Completed</span>
            <span class="status-indicator"></span>
          </div>
          <div class="task-info">
            <span class="task-title">task-15072025-1409</span>
            <p>Execution time: 15 Jul 2025 14:09:53</p>
            <p>Duration: &lt; 29 sec.</p>
            <p>Time range: 15 Jul 2025 10:51 - 15 Jul 2025 11:51</p>
            <p>Live Channel: rtsp://11.0.0.101</p>
            <p>Nx Video Archive: rtsp://192.168.1.101</p>
          </div>
          <div class="task-ips">
            <div class="ip-group">
              <span class="ip">rtsp://11.0.0.102</span>
              <span class="ip">rtsp://192.168.2.0.0</span>
              <span class="ip">rtsp://11.0.0.101</span>
            </div>
            <div class="ip-group">
              <span class="ip">CS-C6N-B0-1GZWF-IND-CXD</span>
              <span class="ip">rtsp://192.168.68.111</span>
              <span class="ip">rtsp://192.168.0.199</span>
            </div>
            <div class="ip-group">
              <span class="ip">rtsp://192.168.2.135</span>
              <span class="ip">CS-H6c-R105-1L2WF</span>
            </div>
          </div>
        </div>
        <div class="task-actions">
          <div class="progress-bar-container">
            <div class="progress-fill completed" style="width: 100%;"></div>
            <span class="progress-text">100%</span>
          </div>
          <div class="completed-actions">
            <button class="action-btn">Delete</button>
            <button class="action-btn">View</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const activeSubTab = ref('all');
</script>

<style scoped>
.investigation-content-container {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.investigation-header {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 1rem;
}

.sub-tabs {
  display: flex;
  background-color: #383838;
  border-radius: 8px;
  overflow: hidden;
}

.sub-tabs a {
  padding: 0.5rem 1rem;
  text-decoration: none;
  color: #ccc;
  font-weight: bold;
  transition: all 0.3s ease;
}

.sub-tabs a:hover {
  background-color: #4a4a4a;
}

.sub-tabs a.active {
  background-color: #007bff;
  color: white;
}

.task-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  overflow-y: auto;
  flex-grow: 1;
}

.task-card {
  display: grid;
  grid-template-columns: 100px 1fr 150px;
  gap: 1rem;
  background-color: #2c2c2c;
  border-radius: 8px;
  padding: 1rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
}

.task-image {
  width: 100px;
  height: 100px;
  overflow: hidden;
  border-radius: 8px;
}

.face-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.task-details {
  display: flex;
  flex-direction: column;
}

.task-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: bold;
  color: #007bff;
}

.task-status span {
  font-size: 0.9rem;
}

.task-info {
  margin-top: 0.5rem;
}

.task-title {
  font-weight: bold;
  color: white;
}

.task-info p {
  font-size: 0.8rem;
  color: #ccc;
  margin: 0;
  line-height: 1.5;
}

.task-ips {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-top: 0.5rem;
}

.ip-group {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.ip {
  font-size: 0.7rem;
  color: #aaa;
}

.task-actions {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  gap: 0.5rem;
}

.progress-bar-container {
  width: 100%;
  background-color: #4a4a4a;
  height: 10px;
  border-radius: 5px;
  position: relative;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background-color: #007bff;
  border-radius: 5px;
  transition: width 0.3s ease;
}

.progress-fill.completed {
  background-color: #4CAF50;
}

.progress-text {
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  color: white;
  font-size: 0.7rem;
}

.action-btn {
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  transition: background 0.3s ease;
}

.stop-btn {
  background-color: #F44336;
}

.stop-btn:hover {
  background-color: #d32f2f;
}

.action-btn:hover {
  background-color: #0056b3;
}

.completed-actions {
  display: flex;
  gap: 0.5rem;
}
</style>
