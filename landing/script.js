document.addEventListener('DOMContentLoaded', function() {
  
  // 1. ANIME KPI CONTADORES (Efecto Cuenta Atrás / Cuenta Arriba)
  function animateCounter(id, targetValue, duration, isPercentage = false, decimals = 0) {
    const el = document.getElementById(id);
    if (!el) return;
    
    let startTimestamp = null;
    const step = (timestamp) => {
      if (!startTimestamp) startTimestamp = timestamp;
      const progress = Math.min((timestamp - startTimestamp) / duration, 1);
      const currentValue = progress * targetValue;
      
      el.textContent = currentValue.toFixed(decimals) + (isPercentage ? '%' : '');
      
      if (progress < 1) {
        window.requestAnimationFrame(step);
      }
    };
    window.requestAnimationFrame(step);
  }

  // Trigger counters with a slight delay for better visual effect on page entry
  setTimeout(() => {
    animateCounter('kpi-accuracy', 96.67, 1500, true, 2);
    animateCounter('kpi-aciertos', 29, 1200, false, 0);
    animateCounter('kpi-f1', 97.00, 1500, true, 0);
  }, 300);

  // 2. SCROLL SPY (Destacar menú activo al hacer scroll)
  const sections = document.querySelectorAll('section');
  const navLinks = document.querySelectorAll('.nav-link');

  const observerOptions = {
    root: null,
    rootMargin: '-20% 0px -60% 0px', // Activa el enlace cuando la sección ocupa la parte central
    threshold: 0
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const activeId = entry.target.getAttribute('id');
        
        navLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${activeId}`) {
            link.classList.add('active');
          }
        });
      }
    });
  }, observerOptions);

  sections.forEach(section => {
    observer.observe(section);
  });

  // 3. DESPLAZAMIENTO SUAVE (Smooth Scroll para navegadores antiguos)
  navLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const targetId = this.getAttribute('href');
      const targetSection = document.querySelector(targetId);
      
      if (targetSection) {
        targetSection.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
        
        // En móviles, cerramos o actualizamos el foco
        navLinks.forEach(l => l.classList.remove('active'));
        this.classList.add('active');
      }
    });
  });

});
