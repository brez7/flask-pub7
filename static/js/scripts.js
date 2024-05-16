<script>
    document.addEventListener("DOMContentLoaded", function () {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 100) {
                document.getElementById('mainNav').classList.add('navbar-shrink');
            } else {
                document.getElementById('mainNav').classList.remove('navbar-shrink');
            }
        });
    });
</script>