// Select DOM elements
const open_btn = document.querySelector('.open-btn');
const close_btn = document.querySelector('.close-btn');
const nav = document.querySelectorAll('.my-nav');
const mainContent = document.getElementById('main-content');
const menuItems = document.querySelectorAll('.list li a');

// Function to change the content
function changeContent(e) {
    e.preventDefault();
    const contentId = idMap[this.textContent];
    const contentElement = document.getElementById(contentId);
    if (contentElement) {
        // Hide all sections
        sections.forEach(section => {
            section.style.display = 'none';
        });
        // Show the corresponding section
        contentElement.style.display = 'block';
    }
}

// Function to handle project click
function handleProjectClick() {
    if (projectList.style.display === "none") {
        projectList.style.display = "block";
    } else {
        projectList.style.display = "none";
    }

    if (projectList.style.maxHeight){
        projectList.style.maxHeight = null;
    } else {
        projectList.style.maxHeight = projectList.scrollHeight + "px";
    } 
}

// Function to handle certifications click
function handleCertificationsClick() {
    if (certificationsList.style.display === "none") {
        certificationsList.style.display = "block";
    } else {
        certificationsList.style.display = "none";
    }

    if (certificationsList.style.maxHeight){
        certificationsList.style.maxHeight = null;
    } else {
        certificationsList.style.maxHeight = certificationsList.scrollHeight + "px";
    } 
}



// Add click event to each menu item
menuItems.forEach(item => {
    item.addEventListener('click', changeContent);
});

// Add click event to project
document.getElementById("projects").addEventListener("click", handleProjectClick);

document.getElementById("certifications").addEventListener("click", handleCertificationsClick);


// Function to handle menu opening
open_btn.addEventListener('click', () => {
    nav.forEach(nav_el => nav_el.classList.add('visible'));
    document.body.classList.add('menu-open'); // Add class to body
});

// Function to handle menu closing
close_btn.addEventListener('click', () => {
    nav.forEach(nav_el => nav_el.classList.remove('visible'));
    document.body.classList.remove('menu-open'); // Remove class from body
    mainContent.classList.add('menu-closing'); // Add class when menu starts to close
});

// Function to handle end of transition
mainContent.addEventListener('transitionend', function() {
  mainContent.classList.remove('menu-closing'); // Remove class when transition ends
});

// Titles for typing function
let titles = ['Hello, I\'m Renato Souza', 'Welcome to my portfolio!'];
let i = 0;
let titleIndex = 0;

let isFirstRun = true;
// Typing function
function typeWriter() {
    if (i < titles[titleIndex].length) {
        document.getElementById('text').innerHTML += titles[titleIndex].charAt(i);
        i++;
        setTimeout(typeWriter, 100);
    } else {
        document.getElementById('text').style.animation = 'none';
        let delayBeforeNextTitle = titles[titleIndex] === 'Hello, I\'m Renato Souza' ? 0 : 2000;
        setTimeout(() => {
            document.getElementById('text').innerHTML = '';
            document.getElementById('text').style.animation = '';
            i = 0;
            titleIndex = (titleIndex + 1) % titles.length;
            let newTitle = document.getElementById('text').cloneNode(true);
            document.getElementById('text').parentNode.replaceChild(newTitle, document.getElementById('text'));
            setTimeout(typeWriter, delayBeforeNextTitle);
        }, 3000);
    }
}
if (isFirstRun) {
    typeWriter();
    isFirstRun = false;
} else {
    setTimeout(typeWriter, 4000);
}
