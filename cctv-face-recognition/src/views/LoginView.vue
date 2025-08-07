<template>
  <div class="login-wrapper">
    <div class="login-box">
      <h2>Login</h2>
      <p class="subtitle">Sign in to your account</p>

      <form @submit.prevent="handleLogin">
        <div class="input-group">
          <i class="icon">👤</i>
          <input type="text" placeholder="Username" v-model="username" required />
        </div>

        <div class="input-group">
          <i class="icon">🔒</i>
          <input type="password" placeholder="Password" v-model="password" required />
        </div>

        <div class="input-group">
          <i class="icon">🌐</i>
          <select v-model="language">
            <option>English</option>
            <option>Hindi</option>
            <option>Malayalam</option>
          </select>
        </div>

        <button type="submit" class="login-btn">Login</button>
        <p class="forgot"><a href="#">Forget password</a></p>
      </form>

      <div class="powered">
        Powered by
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      language: 'English'
    };
  },
  methods: {
    handleLogin() {
      alert(`Logging in as ${this.username}`);
      // Replace with actual logic
    }
  }
};
</script>

<style scoped>
body {
  margin: 0;
  padding: 0;
  font-family: 'Segoe UI', sans-serif;
}

.login-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: radial-gradient(circle at center, #222 0%, #111 100%);
}

.login-box {
  background-color: #1c1c1c;
  color: white;
  padding: 2rem;
  border-radius: 8px;
  width: 300px;
  box-shadow: 0 0 10px #000;
  text-align: center;
}

.login-box h2 {
  margin-bottom: 0.5rem;
}

.subtitle {
  font-size: 0.9rem;
  color: #aaa;
  margin-bottom: 1.5rem;
}

.input-group {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
  background-color: #2a2a2a;
  border-radius: 4px;
  padding: 0.5rem;
}

.input-group i.icon {
  margin-right: 0.5rem;
}

.input-group input,
.input-group select {
  background: transparent;
  border: none;
  outline: none;
  color: white;
  width: 100%;
}

.login-btn {
  width: 100%;
  padding: 0.5rem;
  margin-top: 1rem;
  background: #007bff;
  border: none;
  color: white;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

.login-btn:hover {
  background: #0056b3;
}

.forgot {
  margin-top: 1rem;
  font-size: 0.8rem;
  color: #aaa;
}

.forgot a {
  color: #4faaff;
  text-decoration: none;
}

.powered {
  margin-top: 1.5rem;
  font-size: 0.75rem;
  color: #666;
}
</style>
