// Select DOM elements
const open_btn = document.querySelector('.open-btn');
const close_btn = document.querySelector('.close-btn');
const nav = document.querySelectorAll('.my-nav');
const mainContent = document.getElementById('main-content');
const menuItems = document.querySelectorAll('.list li a');
const sections = document.querySelectorAll('section');
const projectList = document.getElementById("projectList");

window.addEventListener('DOMContentLoaded', () => {
    const aboutMeLink = document.querySelector('a[href="#about"]');
    if (aboutMeLink) {
        changeContent.call(aboutMeLink, { preventDefault: () => { } }); // Chama a função para "About Me"
    }
});

sections.forEach(section => {
    if (section.id !== 'header') {
        section.style.display = 'none';
    }
});

document.getElementById('about').style.display = 'block';

// Mapping between the text of the menu item and the section ID
const idMap = {
    'About Me': 'about',
    'Skills': 'skills',
    'Graduations': 'graduations',
    'Courses': 'courses',
    'HTML/CSS': 'html-css',
    'Python': 'python',
    'Contact Me': 'contact'
};

// Function to change the content
function changeContent(e) {
    e.preventDefault();
    const contentId = idMap[this.textContent];
    const contentElement = document.getElementById(contentId);
    if (contentElement) {
        sections.forEach(section => {
            if (section.id !== 'header') {
                section.style.display = 'none';
            }
        });

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

    if (projectList.style.maxHeight) {
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

    if (certificationsList.style.maxHeight) {
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
mainContent.addEventListener('transitionend', function () {
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
        document.getElementById('title').innerHTML += titles[titleIndex].charAt(i);
        i++;
        setTimeout(typeWriter, 100);
    } else {
        document.getElementById('title').style.animation = 'none';
        let delayBeforeNextTitle = titles[titleIndex] === 'Hello, I\'m Renato Souza' ? 0 : 2000;
        setTimeout(() => {
            document.getElementById('title').innerHTML = '';
            document.getElementById('title').style.animation = '';
            i = 0;
            titleIndex = (titleIndex + 1) % titles.length;
            let newTitle = document.getElementById('title').cloneNode(true);
            document.getElementById('title').parentNode.replaceChild(newTitle, document.getElementById('title'));
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
