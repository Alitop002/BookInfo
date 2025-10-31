// Navigation active link
function setActiveNav(page) {
  document.querySelectorAll(".nav-links a").forEach((link) => {
    link.classList.remove("active")
  })
  document.querySelector(`a[href="${page}"]`)?.classList.add("active")
}

// Modal functions
function openModal(modalId) {
  document.getElementById(modalId).classList.add("active")
}

function closeModal(modalId) {
  document.getElementById(modalId).classList.remove("active")
}

// Close modal on outside click
document.addEventListener("click", (event) => {
  if (event.target.classList.contains("modal")) {
    event.target.classList.remove("active")
  }
})

// Form validation
function validateForm(formId) {
  const form = document.getElementById(formId)
  const inputs = form.querySelectorAll("input[required], textarea[required]")

  let isValid = true
  inputs.forEach((input) => {
    if (!input.value.trim()) {
      input.style.borderColor = "var(--danger)"
      isValid = false
    } else {
      input.style.borderColor = "var(--border)"
    }
  })

  return isValid
}

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault()
    const target = document.querySelector(this.getAttribute("href"))
    if (target) {
      target.scrollIntoView({
        behavior: "smooth",
        block: "start",
      })
    }
  })
})

// Intersection Observer для анимации при скролле
const observerOptions = {
  threshold: 0.1,
  rootMargin: "0px 0px -50px 0px",
}

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = "1"
    }
  })
}, observerOptions)

document.querySelectorAll(".book-card, .review-item").forEach((item) => {
  observer.observe(item)
})

// Logout function
function logout() {
  localStorage.removeItem("user")
  localStorage.removeItem("favorites")
  window.location.href = "index.html"
}

// Check if user is logged in
function checkAuth() {
  const user = JSON.parse(localStorage.getItem("user"))
  const authButtons = document.querySelector(".auth-buttons")

  if (user && authButtons) {
    authButtons.innerHTML = `
            <a href="profile.html" class="btn btn-secondary">Profile</a>
            <button onclick="logout()" class="btn btn-danger">Logout</button>
        `
  }
}

// Initialize on page load
document.addEventListener("DOMContentLoaded", checkAuth)

