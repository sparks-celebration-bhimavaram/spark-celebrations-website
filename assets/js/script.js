/* Shared Logic - SPARK Celebrations */

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.spark-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            createSparkBurst(e.clientX, e.clientY);
        });
    });

    function createSparkBurst(x, y) {
        for (let i = 0; i < 15; i++) {
            const spark = document.createElement('div');
            spark.className = 'spark-particle w-1.5 h-1.5';
            spark.style.left = x + 'px';
            spark.style.top = y + 'px';
            document.body.appendChild(spark);

            gsap.to(spark, {
                duration: 0.8 + Math.random(),
                x: (Math.random() - 0.5) * 200,
                y: (Math.random() - 0.5) * 200,
                opacity: 0,
                scale: 0,
                rotation: Math.random() * 360,
                ease: 'power2.out',
                onComplete: () => spark.remove()
            });
        }
    }

    let lastSparkTime = 0;
    document.addEventListener('mousemove', (e) => {
        const now = Date.now();
        if (now - lastSparkTime > 50 && Math.random() > 0.5) { // Throttle to max 1 spark per 50ms (20 per sec max)
            lastSparkTime = now;
            const spark = document.createElement('div');
            spark.className = 'spark-particle w-1 h-1 opacity-60';
            spark.style.left = e.clientX + 'px';
            spark.style.top = e.clientY + 'px';
            document.body.appendChild(spark);

            gsap.to(spark, {
                duration: 1.5,
                x: e.clientX + (Math.random() - 0.5) * 40,
                y: e.clientY + 100 + (Math.random() * 50),
                opacity: 0,
                scale: 0,
                ease: 'sine.in',
                onComplete: () => spark.remove()
            });
        }
    });

    window.whatsappRedirect = (formData, phone) => {
        const { name, userPhone, email, eventType, date, details } = formData;
        const wp = phone || '919988659759';
        const message =
`Hi SPARK Celebrations!
Name: ${name}
Phone No: ${userPhone}
Email: ${email || 'Not provided'}
Event: ${eventType}
Date: ${date}
Special Requests: ${details || 'None'}`;
        const encoded = encodeURIComponent(message);
        
        // Show success message if form elements exist
        const form = document.querySelector('form');
        const successMsg = document.getElementById('success-message');
        if (form && successMsg) {
            form.classList.add('hidden');
            successMsg.classList.remove('hidden');
            gsap.from(successMsg, { opacity: 0, y: 20, duration: 0.6 });
        }

        window.open(`https://wa.me/${wp}?text=${encoded}`, '_blank');
    };

    const getBaseUrl = () => {
        return window.location.pathname.includes('/services/') ? '../' : '';
    };

    // Redirect to separate booking page
    window.skipIntroAndBook = (e) => {
        if (e) e.preventDefault();
        window.location.href = getBaseUrl() + "index.html#booking-section";
    };

    // specifically for Reel Shoots
    window.bookReelShoot = (e) => {
        if (e) e.preventDefault();
        window.location.href = getBaseUrl() + "index.html?event=Reel Shoot#booking-section";
    };

    // Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const closeMenuBtn = document.getElementById('close-menu');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileLinks = document.querySelectorAll('.mobile-nav-link');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.remove('-translate-y-full');
            mobileMenu.classList.add('active');
        });

        if (closeMenuBtn) {
            closeMenuBtn.addEventListener('click', () => {
                mobileMenu.classList.add('-translate-y-full');
                mobileMenu.classList.remove('active');
            });
        }

        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('-translate-y-full');
                mobileMenu.classList.remove('active');
            });
        });
    }

    // Precision looping for background video: cut last 3 seconds
    const heroBgVideo = document.getElementById('hero-bg-video');
    if (heroBgVideo) {
        heroBgVideo.addEventListener('timeupdate', function() {
            // Restart loop 3 seconds before the physical end of the video
            if (this.currentTime >= this.duration - 3) {
                this.currentTime = 0;
                this.play();
            }
        });
    }

    // Swiper for Recent Reels
    new Swiper('.reelsSwiper', {
        slidesPerView: 1,
        spaceBetween: 20,
        loop: true,
        autoplay: {
            delay: 3000,
            disableOnInteraction: false,
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        breakpoints: {
            640: {
                slidesPerView: 2,
                spaceBetween: 10,
            },
            1024: {
                slidesPerView: 3,
                spaceBetween: 15,
            },
        },
    });
});



