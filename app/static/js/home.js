/**
 * Home page: GSAP scroll reveals, 3D-style floating shapes, typewriter line.
 * Skips heavy motion when prefers-reduced-motion is set.
 */
(function () {
  function runTypewriter(el, text, onDone) {
    var i = 0;
    el.textContent = "";
    function tick() {
      if (i <= text.length) {
        el.textContent = text.slice(0, i);
        i += 1;
        window.setTimeout(tick, 55);
      } else if (typeof onDone === "function") {
        onDone();
      }
    }
    window.setTimeout(tick, 400);
  }

  function init() {
    var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var tw = document.getElementById("hero-typewriter");
    var phrase = (tw && tw.getAttribute("data-typewriter-text")) || "";

    if (tw) {
      if (reduced) {
        tw.textContent = phrase;
        tw.classList.add("is-done");
      } else {
        runTypewriter(tw, phrase, function () {
          tw.classList.add("is-done");
        });
      }
    }

    if (typeof gsap === "undefined") {
      return;
    }

    if (reduced) {
      return;
    }

    gsap.registerPlugin(ScrollTrigger);

    document.querySelectorAll(".hero-float").forEach(function (el, i) {
      gsap.to(el, {
        y: i % 2 ? -18 : 18,
        rotationX: i % 2 ? 10 : -10,
        rotationY: i % 2 ? -14 : 14,
        duration: 2.4 + i * 0.35,
        repeat: -1,
        yoyo: true,
        ease: "sine.inOut",
      });
    });

    gsap.from(".hero-panel", {
      opacity: 0,
      x: 28,
      duration: 0.75,
      ease: "power2.out",
      delay: 0.15,
    });

    gsap.from(".stats", {
      scrollTrigger: { trigger: ".stats", start: "top 88%" },
      opacity: 0,
      y: 36,
      duration: 0.65,
      ease: "power2.out",
    });

    gsap.utils.toArray(".section").forEach(function (sec) {
      gsap.from(sec, {
        scrollTrigger: { trigger: sec, start: "top 90%" },
        opacity: 0,
        y: 40,
        duration: 0.7,
        ease: "power2.out",
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
