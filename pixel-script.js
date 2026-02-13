/* ============================================
   🎮 PIXEL VALENTINE'S GAME - JavaScript
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {
    // === Page Navigation ===
    const pages = document.querySelectorAll('.page');
    let currentPage = 1;

    function showPage(pageNum) {
        pages.forEach(page => page.classList.remove('active'));
        const targetPage = document.getElementById(`page-${pageNum}`);
        if (targetPage) {
            targetPage.classList.add('active');
            currentPage = pageNum;
        }
    }

    // === Page 1: Yes/No Buttons ===
    const btnYes = document.getElementById('btn-yes');
    const btnNo = document.getElementById('btn-no');
    const runningOverlay = document.getElementById('running-overlay');
    const notAllowedMsg = document.querySelector('.not-allowed-message');

    let noClickCount = 0;
    let noRunAwayActive = true;

    if (btnYes) {
        btnYes.addEventListener('click', () => {
            // Show running overlay animation
            if (runningOverlay) {
                runningOverlay.classList.remove('hidden');
                // After animation, go to page 2
                setTimeout(() => {
                    runningOverlay.classList.add('hidden');
                    showPage(2);
                }, 3000);
            } else {
                showPage(2);
            }
        });
    }

    if (btnNo) {
        // No button runs away!
        btnNo.addEventListener('mouseenter', () => {
            if (!noRunAwayActive) return;

            noClickCount++;

            if (noClickCount < 6) {
                // Run away to random position
                const maxX = window.innerWidth - btnNo.offsetWidth - 100;
                const maxY = window.innerHeight - btnNo.offsetHeight - 200;
                const randomX = Math.random() * maxX;
                const randomY = Math.max(100, Math.random() * maxY);

                btnNo.style.position = 'fixed';
                btnNo.style.left = randomX + 'px';
                btnNo.style.top = randomY + 'px';
                btnNo.style.zIndex = '100';
            } else {
                // After 6 attempts, show "Not Allowed" and reset
                noRunAwayActive = false;
                if (notAllowedMsg) {
                    notAllowedMsg.classList.remove('hidden');
                    setTimeout(() => {
                        notAllowedMsg.classList.add('hidden');
                        noRunAwayActive = true;
                        noClickCount = 0;
                        btnNo.style.position = '';
                        btnNo.style.left = '';
                        btnNo.style.top = '';
                    }, 3000);
                }
            }
        });

        btnNo.addEventListener('click', () => {
            // If they somehow click it, show message
            if (notAllowedMsg) {
                notAllowedMsg.classList.remove('hidden');
                setTimeout(() => {
                    notAllowedMsg.classList.add('hidden');
                }, 3000);
            }
        });
    }

    // === Page Navigation Arrows ===
    const nextPage2 = document.getElementById('next-page-2');
    const nextPage3 = document.getElementById('next-page-3');
    const showEnding = document.getElementById('show-ending');
    const endingOverlay = document.getElementById('ending-overlay');

    // Helper function to transition with running animation
    function transitionWithAnimation(targetPage) {
        if (runningOverlay) {
            runningOverlay.classList.remove('hidden');
            setTimeout(() => {
                runningOverlay.classList.add('hidden');
                showPage(targetPage);
            }, 3000);
        } else {
            showPage(targetPage);
        }
    }

    if (nextPage2) nextPage2.addEventListener('click', () => transitionWithAnimation(3));
    if (nextPage3) nextPage3.addEventListener('click', () => transitionWithAnimation(4));

    if (showEnding && endingOverlay) {
        showEnding.addEventListener('click', () => {
            endingOverlay.classList.remove('hidden');
        });
    }

    // === Timeline Memories ===
    const timelineItems = document.querySelectorAll('.timeline-item');
    const memoryPopup = document.querySelector('.memory-popup');
    const memoryText = document.querySelector('.memory-text');

    timelineItems.forEach(item => {
        item.addEventListener('click', (e) => {
            const memory = item.getAttribute('data-memory');
            if (memoryText && memoryPopup) {
                memoryText.textContent = memory;

                // Position popup next to the clicked item using fixed positioning
                const rect = item.getBoundingClientRect();

                // Use fixed positioning relative to viewport
                memoryPopup.style.position = 'fixed';
                memoryPopup.style.left = (rect.right + 20) + 'px';
                memoryPopup.style.top = rect.top + 'px';

                // Ensure popup stays within viewport
                const popupWidth = 300; // max-width from CSS
                if (rect.right + 20 + popupWidth > window.innerWidth) {
                    // Position to the left of the item if it would overflow
                    memoryPopup.style.left = (rect.left - popupWidth - 20) + 'px';
                }

                memoryPopup.classList.remove('hidden');

                // Auto-hide after 3 seconds
                setTimeout(() => {
                    memoryPopup.classList.add('hidden');
                }, 3000);
            }
        });
    });

    // Click anywhere to close memory popup
    if (memoryPopup) {
        memoryPopup.addEventListener('click', () => {
            memoryPopup.classList.add('hidden');
        });
    }

    // === Scene Playback (Autoplay) ===

    // Function to handle video playback when page is active
    function checkAutoplay() {
        const kissVideo = document.getElementById('kiss-video');
        const tickleImg = document.getElementById('tickle-img');

        // If we are on Page 3 (or generally, try to play if element exists)
        if (kissVideo) {
            kissVideo.play().catch(e => {
                console.log("Autoplay prevented:", e);
                // Retry on interaction if needed, but 'muted' usually allows it
            });
        }

        // Ensure tickle image has animation
        if (tickleImg) {
            tickleImg.style.animation = 'shake 2s ease-in-out infinite';
        }
    }

    // Hook into page navigation to trigger autoplay
    const originalShowPage = showPage;
    // We can't easily override local function 'showPage' unless we modify it directly.
    // Instead, we'll listen for the class change or just check periodically/on click of nav buttons.

    // Better approach: Modify the nav button event listeners or the transition function.
    // Since 'showPage' is local, let's just add a side-effect to the nav buttons that lead to Page 3.

    if (nextPage2) {
        nextPage2.addEventListener('click', () => {
            // We are going to Page 3
            setTimeout(() => {
                checkAutoplay();
            }, 1000); // Wait for transition
        });
    }

    // Also run on load just in case we start on Page 3 (dev mode)
    checkAutoplay();

    // === Eyes Following Cursor ===
    const kittiesWithEyes = document.querySelectorAll('.pixel-hello-kitty.with-eyes');

    document.addEventListener('mousemove', (e) => {
        kittiesWithEyes.forEach(kitty => {
            const pupils = kitty.querySelectorAll('.hk-pupil');

            pupils.forEach(pupil => {
                const eye = pupil.parentElement;
                const eyeRect = eye.getBoundingClientRect();
                const eyeCenterX = eyeRect.left + eyeRect.width / 2;
                const eyeCenterY = eyeRect.top + eyeRect.height / 2;

                const angle = Math.atan2(e.clientY - eyeCenterY, e.clientX - eyeCenterX);
                const distance = Math.min(2, Math.hypot(e.clientX - eyeCenterX, e.clientY - eyeCenterY) / 50);

                const moveX = Math.cos(angle) * distance;
                const moveY = Math.sin(angle) * distance;

                pupil.style.transform = `translate(calc(-50% + ${moveX}px), ${moveY}px)`;
            });
        });
    });

    // === Background Music (optional) ===
    const bgMusic = document.getElementById('bg-music');

    // Try to play music on first interaction
    // Try to play music on first interaction
    document.addEventListener('click', () => {
        if (bgMusic && bgMusic.paused) {
            bgMusic.volume = 0.3;
            // Set start time to 37s
            if (bgMusic.currentTime < 37) {
                bgMusic.currentTime = 37;
            }
            bgMusic.play().catch(() => {
                // Autoplay blocked, that's okay
            });
        }
    }, { once: true });

    // Handle Looping manually to start from 37s
    if (bgMusic) {
        // Ensure regular loop attribute is false so we can handle 'ended'
        bgMusic.loop = false;

        bgMusic.addEventListener('ended', () => {
            bgMusic.currentTime = 37;
            bgMusic.play();
        });

        // Failsafe: if loop attribute was set in HTML, it might jump to 0. 
        // We watch for timeupdate to catch the loop transition if browser handles it.
        // However, 'ended' event is cleaner if we disable the HTML loop attribute via JS above.
    }

    // === Floating Hearts Extra Animation ===
    function createFloatingHeart() {
        const heart = document.createElement('div');
        heart.className = 'floating-heart-extra';
        heart.textContent = ['❤️', '💕', '💖', '💗', '💓'][Math.floor(Math.random() * 5)];
        heart.style.cssText = `
            position: fixed;
            left: ${Math.random() * 100}%;
            bottom: -50px;
            font-size: ${16 + Math.random() * 16}px;
            opacity: 0.7;
            pointer-events: none;
            z-index: 1000;
            animation: floatUp 4s ease-out forwards;
        `;
        document.body.appendChild(heart);

        setTimeout(() => heart.remove(), 4000);
    }

    // Add floating hearts animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes floatUp {
            0% { transform: translateY(0) rotate(0deg); opacity: 0.7; }
            100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
        }
    `;
    document.head.appendChild(style);

    // Occasional floating hearts
    setInterval(() => {
        if (currentPage === 4 && (endingOverlay && endingOverlay.classList.contains('hidden'))) {
            createFloatingHeart();
        }
    }, 500);

    console.log('💖 Pixel Valentine\'s Game Loaded! 💖');
});
