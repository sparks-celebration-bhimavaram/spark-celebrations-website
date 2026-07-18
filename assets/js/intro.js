/* Intro Logic - SPARK Celebrations */

document.addEventListener('DOMContentLoaded', () => {
    const introOverlay = document.querySelector('#intro-overlay');
    const introContent = document.querySelector('#intro-content');
    const introLogo = document.querySelector('#intro-logo');
    const mainContent = document.querySelector('#main-content');
    const skipBtn = document.querySelector('#skip-intro');
    const sparksContainer = document.querySelector('#sparks-container');
    
    if (!introOverlay) return;

    // --- Color Palette ---
    const colors = ['#D4AF37', '#F9E27A', '#FFFDD0', '#FFFFFF', '#B7950B'];

    // --- Optimized Ambient Particle System ---
    function initSparkCanvas(canvasId, particleCount, opacityMult = 1) {
        const canvas = document.getElementById(canvasId);
        if (!canvas) return null;

        const ctx = canvas.getContext('2d');
        let particles = [];
        
        const resize = () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        };
        window.addEventListener('resize', resize);
        resize();

        class Particle {
            constructor() { this.reset(); }
            reset() {
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.size = Math.random() * 1.5 + 0.1;
                this.speedY = Math.random() * -0.6 - 0.1;
                this.speedX = (Math.random() - 0.5) * 0.2;
                this.opacity = Math.random() * 0.5 + 0.1;
                this.color = colors[Math.floor(Math.random() * colors.length)];
                this.fadeSpeed = Math.random() * 0.001 + 0.0005;
            }
            update() {
                this.y += this.speedY;
                this.x += this.speedX;
                this.opacity -= this.fadeSpeed;
                if (this.opacity <= 0 || this.y < -10) this.reset();
            }
            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fillStyle = this.color;
                ctx.globalAlpha = Math.max(0, this.opacity * opacityMult);
                // Removed shadowBlur for performance; using globalAlpha for glow feel
                ctx.fill();
            }
        }

        for (let i = 0; i < particleCount; i++) particles.push(new Particle());

        const animate = () => {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            for (let i = 0; i < particles.length; i++) {
                particles[i].update();
                particles[i].draw();
            }
            if (canvas.offsetParent !== null) requestAnimationFrame(animate);
        };
        animate();
        return { canvas, particles };
    }

    // --- High-Performance Explosion Canvas ---
    const explosionCanvas = document.getElementById('explosion-canvas');
    const expCtx = explosionCanvas ? explosionCanvas.getContext('2d') : null;
    let explosionParticles = [];

    function resizeExpCanvas() {
        if (explosionCanvas) {
            explosionCanvas.width = window.innerWidth;
            explosionCanvas.height = window.innerHeight;
        }
    }
    window.addEventListener('resize', resizeExpCanvas);
    resizeExpCanvas();

    class ExplosionParticle {
        constructor(x, y, color) {
            this.x = x;
            this.y = y;
            this.color = color;
            const angle = Math.random() * Math.PI * 2;
            const velocity = 3 + Math.random() * 10;
            this.vx = Math.cos(angle) * velocity;
            this.vy = Math.sin(angle) * velocity;
            this.size = Math.random() * 3 + 1;
            this.opacity = 1;
            this.gravity = 0.02;
            this.friction = 0.98;
        }
        update() {
            this.vx *= this.friction;
            this.vy *= this.friction;
            this.vy += this.gravity;
            this.x += this.vx;
            this.y += this.vy;
            this.opacity -= 0.015;
            this.size *= 0.99;
        }
        draw() {
            if (!expCtx) return;
            expCtx.beginPath();
            expCtx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            expCtx.fillStyle = this.color;
            expCtx.globalAlpha = Math.max(0, this.opacity);
            expCtx.fill();
        }
    }

    function animateExplosion() {
        if (!expCtx) return;
        expCtx.clearRect(0, 0, explosionCanvas.width, explosionCanvas.height);
        for (let i = explosionParticles.length - 1; i >= 0; i--) {
            explosionParticles[i].update();
            explosionParticles[i].draw();
            if (explosionParticles[i].opacity <= 0) {
                explosionParticles.splice(i, 1);
            }
        }
        if (explosionParticles.length > 0 || (introOverlay && introOverlay.style.display !== 'none')) {
            requestAnimationFrame(animateExplosion);
        }
    }

    function createSparkExplosion(count = 80) {
        const rect = introLogo.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;

        for (let i = 0; i < count; i++) {
            const color = colors[Math.floor(Math.random() * colors.length)];
            explosionParticles.push(new ExplosionParticle(centerX, centerY, color));
        }
        if (explosionParticles.length === count) animateExplosion();
    }

    // Initialize Intro Canvas
    initSparkCanvas('intro-canvas', 180);

    // --- Smoother Timeline Definition ---
    const tl = gsap.timeline({
        onComplete: finishIntro
    });

    gsap.set(introContent, { opacity: 0, scale: 0.9, transformOrigin: "center center" });
    gsap.set(introLogo, { willChange: "transform, opacity" });

    // 0-1.5s: Logo appears with silk-smooth fade
    tl.to(introContent, {
        duration: 1.8,
        opacity: 1,
        scale: 1,
        ease: "power3.out"
    });

    // 1.2-4s: Gentle zoom and rhythmic bursts
    tl.to(introLogo, {
        duration: 3.5,
        scale: 1.12,
        ease: "sine.inOut"
    }, 1.2);

    tl.call(() => createSparkExplosion(200), null, 4.0);

    // Transition to main content
    tl.to(introOverlay, {
        duration: 1.2,
        opacity: 0,
        ease: "power2.inOut"
    }, 5.5)
    .set(introOverlay, { display: 'none' });

    function finishIntro() {
        tl.kill();
        explosionParticles = [];
        gsap.to(introOverlay, { 
            opacity: 0, 
            duration: 1, 
            ease: "power2.out",
            onComplete: () => {
                introOverlay.style.display = 'none';
                document.body.style.overflowY = 'auto';
                initSparkCanvas('global-spark-canvas', 100, 0.3);
            }
        });
        gsap.to(mainContent, { opacity: 1, duration: 1.5, ease: "power2.out" });
        document.body.style.overflowY = 'auto';
    }

    if (skipBtn) skipBtn.addEventListener('click', finishIntro);
    
    // Safety timeout
    setTimeout(() => {
        if (introOverlay.style.display !== 'none') finishIntro();
    }, 9000);
});
