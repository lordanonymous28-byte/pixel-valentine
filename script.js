/* ============================================
   💖 Valentine's Day Mini-Game JavaScript
   ============================================ */

// === State Management ===
const state = {
    currentPage: 1,
    totalPages: 4,
    noClickCount: 0,
    musicPlaying: false
};

// === DOM Elements ===
const elements = {
    pages: document.querySelectorAll('.page'),
    btnYes: document.getElementById('btn-yes'),
    btnNo: document.getElementById('btn-no'),
    sadMonkeyBg: document.querySelector('.sad-monkey-bg'),
    notAllowedMessage: document.querySelector('.not-allowed-message'),
    maleKittyNormal: document.querySelector('#male-kitty-p1 .normal'),
    maleKittySad: document.querySelector('#male-kitty-p1 .sad'),
    runningOverlay: document.querySelector('.running-overlay'),
    timelineItems: document.querySelectorAll('.timeline-item'),
    memoryPopup: document.querySelector('.memory-popup'),
    memoryText: document.querySelector('.memory-text'),
    navArrow2: document.getElementById('next-page-2'),
    navArrow3: document.getElementById('next-page-3'),
    chaseOverlay: document.querySelector('.chase-overlay'),
    showEnding: document.getElementById('show-ending'),
    endingOverlay: document.querySelector('.ending-overlay'),
    playSceneBtns: document.querySelectorAll('.play-scene-btn'),
    bgMusic: document.getElementById('bg-music')
};

// === Page Navigation ===
function goToPage(pageNum) {
    const currentPageEl = document.querySelector('.page.active');
    const nextPageEl = document.getElementById(`page-${pageNum}`);

    if (currentPageEl && nextPageEl) {
        currentPageEl.classList.add('slide-out-left');

        setTimeout(() => {
            currentPageEl.classList.remove('active', 'slide-out-left');
            nextPageEl.classList.add('active', 'slide-in-right');

            setTimeout(() => {
                nextPageEl.classList.remove('slide-in-right');
            }, 600);
        }, 500);

        state.currentPage = pageNum;

        // Start music on page 2
        if (pageNum === 2 && !state.musicPlaying) {
            playMusic();
        }
    }
}

// === Music Control ===
function playMusic() {
    if (elements.bgMusic) {
        elements.bgMusic.volume = 0.3;
        elements.bgMusic.play().catch(e => {
            console.log('Music autoplay blocked:', e);
        });
        state.musicPlaying = true;
    }
}

// === Page 1: Valentine Question Logic ===
function initPage1() {
    // Make the No button run away from cursor!
    function makeButtonRunAway() {
        const btn = elements.btnNo;
        const container = document.querySelector('.button-container');
        const page = document.getElementById('page-1');

        // Get page boundaries
        const pageRect = page.getBoundingClientRect();
        const btnRect = btn.getBoundingClientRect();

        // Calculate safe boundaries (with padding)
        const padding = 20;
        const maxX = pageRect.width - btnRect.width - padding;
        const maxY = pageRect.height - btnRect.height - padding;

        // Generate random position
        let newX = Math.random() * maxX;
        let newY = Math.random() * (maxY * 0.6) + (maxY * 0.2); // Keep in middle section vertically

        // Apply the new position
        btn.style.position = 'fixed';
        btn.style.left = (pageRect.left + newX) + 'px';
        btn.style.top = (pageRect.top + newY) + 'px';
        btn.style.transition = 'left 0.3s ease-out, top 0.3s ease-out';
        btn.style.zIndex = '100';
    }

    // No button hover effect - run away!
    elements.btnNo.addEventListener('mouseenter', () => {
        elements.sadMonkeyBg.classList.add('visible');
        elements.maleKittyNormal.classList.add('hidden');
        elements.maleKittySad.classList.remove('hidden');

        // Make the button run away!
        makeButtonRunAway();
    });

    elements.btnNo.addEventListener('mouseleave', () => {
        elements.sadMonkeyBg.classList.remove('visible');
        elements.maleKittyNormal.classList.remove('hidden');
        elements.maleKittySad.classList.add('hidden');
    });

    // No button click (in case they somehow manage to click it)
    elements.btnNo.addEventListener('click', () => {
        state.noClickCount++;
        elements.notAllowedMessage.classList.remove('hidden');
        elements.maleKittyNormal.classList.add('hidden');
        elements.maleKittySad.classList.remove('hidden');

        // Make it run away again!
        makeButtonRunAway();

        // Add shake animation to the message
        elements.notAllowedMessage.style.animation = 'none';
        setTimeout(() => {
            elements.notAllowedMessage.style.animation = 'shake 0.5s ease';
        }, 10);

        // Hide after 2 seconds
        setTimeout(() => {
            elements.notAllowedMessage.classList.add('hidden');
            elements.maleKittyNormal.classList.remove('hidden');
            elements.maleKittySad.classList.add('hidden');
        }, 2000);
    });

    // Yes button click
    elements.btnYes.addEventListener('click', () => {
        // Show running animation
        elements.runningOverlay.classList.remove('hidden');

        // After animation, go to page 2
        setTimeout(() => {
            elements.runningOverlay.classList.add('hidden');
            goToPage(2);
        }, 2000);
    });
}

// === Page 2: Timeline Logic ===
function initPage2() {
    elements.timelineItems.forEach(item => {
        item.addEventListener('mouseenter', (e) => {
            const memory = item.dataset.memory;
            elements.memoryText.textContent = memory;
            elements.memoryPopup.classList.remove('hidden');
        });

        item.addEventListener('mouseleave', () => {
            elements.memoryPopup.classList.add('hidden');
        });
    });

    // Nav arrow to page 3
    elements.navArrow2.addEventListener('click', () => {
        goToPage(3);
    });

    // Eye following cursor (optional enhancement)
    document.addEventListener('mousemove', (e) => {
        if (state.currentPage === 2 || state.currentPage === 3) {
            updateEyePositions(e.clientX, e.clientY);
        }
    });
}

// === Eye Following Logic ===
function updateEyePositions(mouseX, mouseY) {
    const pupils = document.querySelectorAll('.pupil');

    pupils.forEach(pupil => {
        const eye = pupil.parentElement;
        const eyeRect = eye.getBoundingClientRect();
        const eyeCenterX = eyeRect.left + eyeRect.width / 2;
        const eyeCenterY = eyeRect.top + eyeRect.height / 2;

        const angle = Math.atan2(mouseY - eyeCenterY, mouseX - eyeCenterX);
        const distance = 3; // Max pixels the pupil can move

        const x = Math.cos(angle) * distance;
        const y = Math.sin(angle) * distance;

        pupil.style.transform = `translate(calc(-50% + ${x}px), calc(-50% + ${y}px))`;
    });
}

// === Page 3: Windows Scene Logic ===
function initPage3() {
    elements.playSceneBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const sceneType = btn.dataset.scene;
            playScene(sceneType);
        });
    });

    // Chase transition to page 4
    elements.navArrow3.addEventListener('click', () => {
        // Show chase animation
        elements.chaseOverlay.classList.remove('hidden');

        // After chase animation, go to page 4
        setTimeout(() => {
            elements.chaseOverlay.classList.add('hidden');
            goToPage(4);
        }, 2200);
    });
}

// === Scene Animation Logic ===
function playScene(sceneType) {
    if (sceneType === 'kiss') {
        playKissScene();
    } else if (sceneType === 'tickle') {
        playTickleScene();
    }
}

function playKissScene() {
    const placeholder = document.getElementById('kiss-placeholder');
    const video = document.getElementById('kiss-video');

    if (!video || !placeholder) return;

    // Show video, hide placeholder
    placeholder.classList.add('hidden');
    video.classList.remove('hidden');

    // Play video
    video.currentTime = 0;
    video.play().catch(e => console.log("Video play failed:", e));

    // When video ends, show placeholder again
    video.onended = () => {
        video.classList.add('hidden');
        placeholder.classList.remove('hidden');
    };
}

function playTickleScene() {
    const placeholder = document.getElementById('tickle-placeholder');
    const img = document.getElementById('tickle-img');

    if (!img || !placeholder) return;

    // Show image, hide placeholder
    placeholder.classList.add('hidden');
    img.classList.remove('hidden');

    // Add a little shake animation to the image
    img.style.animation = 'shake 0.5s ease-in-out infinite';

    // Reset after 3 seconds
    setTimeout(() => {
        img.style.animation = '';
        img.classList.add('hidden');
        placeholder.classList.remove('hidden');
    }, 3000);
}

// === Page 4: Acts of Love ===
function initPage4() {
    elements.showEnding.addEventListener('click', () => {
        elements.endingOverlay.classList.remove('hidden');

        // Create extra floating hearts
        createFloatingHearts();
    });
}

// === Floating Hearts Effect ===
function createFloatingHearts() {
    const hearts = ['❤️', '💕', '💖', '💗', '💓', '💝', '💘', '💞'];
    const container = document.querySelector('.floating-hearts');

    for (let i = 0; i < 20; i++) {
        setTimeout(() => {
            const heart = document.createElement('span');
            heart.className = 'heart extra-heart';
            heart.textContent = hearts[Math.floor(Math.random() * hearts.length)];
            heart.style.left = Math.random() * 100 + '%';
            heart.style.animationDuration = (3 + Math.random() * 2) + 's';
            heart.style.fontSize = (1 + Math.random() * 1.5) + 'rem';
            container.appendChild(heart);

            // Remove after animation
            setTimeout(() => {
                heart.remove();
            }, 5000);
        }, i * 300);
    }
}

// === Sparkle Effect ===
function createSparkle(x, y) {
    const sparkle = document.createElement('div');
    sparkle.className = 'sparkle';
    sparkle.style.left = x + 'px';
    sparkle.style.top = y + 'px';
    document.body.appendChild(sparkle);

    setTimeout(() => sparkle.remove(), 1000);
}

// === Add click sparkles ===
document.addEventListener('click', (e) => {
    for (let i = 0; i < 5; i++) {
        setTimeout(() => {
            createSparkle(
                e.clientX + (Math.random() - 0.5) * 50,
                e.clientY + (Math.random() - 0.5) * 50
            );
        }, i * 50);
    }
});

// === Initialize Everything ===
function init() {
    initPage1();
    initPage2();
    initPage3();
    initPage4();

    // Add sparkle cursor effect
    addSparkleStyle();
}

function addSparkleStyle() {
    const style = document.createElement('style');
    style.textContent = `
        .sparkle {
            position: fixed;
            width: 10px;
            height: 10px;
            background: radial-gradient(circle, #ff69b4, transparent);
            border-radius: 50%;
            pointer-events: none;
            animation: sparkleAnim 0.6s ease-out forwards;
            z-index: 9999;
        }
        
        @keyframes sparkleAnim {
            0% {
                transform: scale(0);
                opacity: 1;
            }
            100% {
                transform: scale(2);
                opacity: 0;
            }
        }
        
        .extra-heart {
            position: absolute;
            animation: floatUp 4s ease-in-out forwards;
        }
    `;
    document.head.appendChild(style);
}

// Start the game
document.addEventListener('DOMContentLoaded', init);

// === Easter Egg: Konami Code for extra love ===
const konamiCode = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'KeyB', 'KeyA'];
let konamiIndex = 0;

document.addEventListener('keydown', (e) => {
    if (e.code === konamiCode[konamiIndex]) {
        konamiIndex++;
        if (konamiIndex === konamiCode.length) {
            // Trigger love explosion!
            createLoveExplosion();
            konamiIndex = 0;
        }
    } else {
        konamiIndex = 0;
    }
});

function createLoveExplosion() {
    const hearts = ['❤️', '💕', '💖', '💗', '💓', '💝', '💘', '💞', '🌹', '💐'];

    for (let i = 0; i < 50; i++) {
        setTimeout(() => {
            const heart = document.createElement('div');
            heart.textContent = hearts[Math.floor(Math.random() * hearts.length)];
            heart.style.cssText = `
                position: fixed;
                left: 50%;
                top: 50%;
                font-size: ${2 + Math.random() * 2}rem;
                pointer-events: none;
                z-index: 10000;
                animation: explode 2s ease-out forwards;
            `;

            const angle = (Math.PI * 2 / 50) * i;
            const distance = 100 + Math.random() * 200;
            const endX = Math.cos(angle) * distance;
            const endY = Math.sin(angle) * distance;

            heart.style.setProperty('--endX', endX + 'px');
            heart.style.setProperty('--endY', endY + 'px');

            document.body.appendChild(heart);

            setTimeout(() => heart.remove(), 2000);
        }, i * 30);
    }

    // Add explosion keyframes
    if (!document.getElementById('explosion-style')) {
        const style = document.createElement('style');
        style.id = 'explosion-style';
        style.textContent = `
            @keyframes explode {
                0% {
                    transform: translate(-50%, -50%) scale(0);
                    opacity: 1;
                }
                100% {
                    transform: translate(calc(-50% + var(--endX)), calc(-50% + var(--endY))) scale(1);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }
}
