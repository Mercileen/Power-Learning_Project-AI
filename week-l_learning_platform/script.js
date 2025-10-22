// Course Data
const courses = [
  {
    id: 1,
    title: "HTML Basics",
    description: "Learn the building blocks of web development.",
    lessons: ["Introduction to HTML", "Tags and Elements", "Forms and Inputs", "Links and Images"]
  },
  {
    id: 2,
    title: "CSS Fundamentals",
    description: "Style your web pages with CSS.",
    lessons: ["Selectors and Properties", "Colors and Fonts", "Box Model", "Flexbox Basics"]
  },
  {
    id: 3,
    title: "JavaScript Essentials",
    description: "Add interactivity to your websites.",
    lessons: ["Variables and Data Types", "Functions", "DOM Manipulation", "Events"]
  }
];

// Display Courses on Home Page
if (document.getElementById("course-list")) {
  const courseList = document.getElementById("course-list");
  courses.forEach(course => {
    const card = document.createElement("div");
    card.className = "course-card";
    card.innerHTML = `
      <h3>${course.title}</h3>
      <p>${course.description}</p>
      <button onclick="viewCourse(${course.id})">View Course</button>
    `;
    courseList.appendChild(card);
  });
}

// Go to Course Detail Page
function viewCourse(id) {
  localStorage.setItem("selectedCourseId", id);
  window.location.href = "course.html";
}

// Display Course Details
if (document.getElementById("lesson-list")) {
  const courseId = localStorage.getItem("selectedCourseId");
  const course = courses.find(c => c.id == courseId);
  const lessonList = document.getElementById("lesson-list");
  const courseTitle = document.getElementById("course-title");
  const progressText = document.getElementById("progress-text");
  const completeBtn = document.getElementById("complete-btn");

  if (course) {
    courseTitle.textContent = course.title;
    course.lessons.forEach(lesson => {
      const item = document.createElement("div");
      item.className = "lesson-item";
      item.textContent = lesson;
      lessonList.appendChild(item);
    });

    const completed = localStorage.getItem(`completed_${course.id}`) === "true";
    updateProgressText(completed);

    completeBtn.addEventListener("click", () => {
      localStorage.setItem(`completed_${course.id}`, "true");
      updateProgressText(true);
      alert("Course marked as completed!");
    });
  }
}

// Update Progress Display
function updateProgressText(isCompleted) {
  const text = isCompleted ? "✅ Course Completed" : "📘 In Progress";
  document.getElementById("progress-text").textContent = text;
}

// Navigate Back
function goHome() {
  window.location.href = "index.html";
}
