/**
 * Smart Tangibles Companion Site
 * Main JavaScript
 */

document.addEventListener('DOMContentLoaded', function() {
    // Mobile Navigation Toggle
    initMobileNav();

    // Digest Form Handling
    initDigestForm();

    // Smooth Scroll for anchor links
    initSmoothScroll();

    // Navbar scroll effect
    initNavbarScroll();

    // Animate elements on scroll
    initScrollAnimations();
});

/**
 * Mobile Navigation
 */
function initMobileNav() {
    const toggle = document.querySelector('.nav-toggle');
    const menu = document.querySelector('.nav-menu');

    if (toggle && menu) {
        toggle.addEventListener('click', function() {
            menu.classList.toggle('active');
            toggle.classList.toggle('active');
        });

        // Close menu when clicking a link
        menu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                menu.classList.remove('active');
                toggle.classList.remove('active');
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!menu.contains(e.target) && !toggle.contains(e.target)) {
                menu.classList.remove('active');
                toggle.classList.remove('active');
            }
        });
    }
}

/**
 * Digest Signup - Opens mailto with prefilled subject and body
 */
function initDigestForm() {
    const subscribeBtn = document.getElementById('subscribeBtn');

    if (subscribeBtn) {
        subscribeBtn.addEventListener('click', function() {
            const roleSelect = document.getElementById('role');
            const industrySelect = document.getElementById('industry');

            const role = roleSelect.value || 'Not specified';
            const industry = industrySelect.value || 'Not specified';

            const recipient = 'hello@theroadtlv.com';
            const subject = 'Please subscribe me to Smart Tangibles News digest';
            const body = `Hello,

Please subscribe me to the Smart Tangibles Weekly Digest.

Role: ${role}
Industry: ${industry}

Thank you!`;

            // Encode for mailto URL
            const mailtoUrl = `mailto:${recipient}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;

            // Open default email client
            window.location.href = mailtoUrl;

            // Show success feedback
            showSuccessMessage(subscribeBtn);
        });
    }
}

/**
 * Show success message after mailto trigger
 */
function showSuccessMessage(button) {
    const container = button.parentElement;

    // Change button appearance temporarily
    const originalText = button.textContent;
    button.textContent = 'Email client opened!';
    button.style.backgroundColor = '#10b981';
    button.style.borderColor = '#10b981';

    // Add success message below button
    const existingMsg = container.querySelector('.success-message');
    if (existingMsg) existingMsg.remove();

    const successMsg = document.createElement('p');
    successMsg.className = 'success-message';
    successMsg.textContent = 'Please send the email to complete your subscription.';
    successMsg.style.cssText = `
        color: #10b981;
        font-size: 14px;
        text-align: center;
        margin-top: 12px;
        font-weight: 500;
    `;

    // Insert after the button
    button.insertAdjacentElement('afterend', successMsg);

    // Reset after 4 seconds
    setTimeout(() => {
        button.textContent = originalText;
        button.style.backgroundColor = '';
        button.style.borderColor = '';
        successMsg.remove();
    }, 4000);
}

/**
 * Smooth scrolling for anchor links
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#') return;

            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/**
 * Navbar scroll effect
 */
function initNavbarScroll() {
    const navbar = document.querySelector('.navbar');
    if (!navbar) return;

    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        // Add shadow when scrolled
        if (currentScroll > 10) {
            navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
        } else {
            navbar.style.boxShadow = 'none';
        }

        lastScroll = currentScroll;
    }, { passive: true });
}

/**
 * Scroll animations
 */
function initScrollAnimations() {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe elements that should animate
    const animateElements = document.querySelectorAll('.value-card, .tool-card, .chapter-card, .service-card');
    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        observer.observe(el);
    });

    // Add animation class styles
    const style = document.createElement('style');
    style.textContent = `
        .animate-in {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
    `;
    document.head.appendChild(style);
}

/**
 * Tool card hover effects (for interactive previews)
 */
document.querySelectorAll('.tool-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        // Animate risk meter
        const riskFill = this.querySelector('.risk-fill');
        if (riskFill) {
            riskFill.style.width = (Math.random() * 40 + 40) + '%';
        }

        // Animate bars
        const bars = this.querySelectorAll('.bar');
        bars.forEach(bar => {
            bar.style.height = (Math.random() * 60 + 20) + '%';
        });
    });
});
