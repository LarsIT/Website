document.addEventListener('DOMContentLoaded', function() {
    // Get all project elements
    const projects = document.querySelectorAll('.project');
    
    // Add click event listener to each project
    projects.forEach(project => {
        project.addEventListener('click', function() {
            const modalId = this.getAttribute('data-modal-target');
            const modal = document.querySelector(modalId);
            if (modal) {
                modal.style.display = 'block';
            }
        });
    });
    
    // Get all close buttons
    const closeButtons = document.querySelectorAll('[data-modal-close]');
    
    // Add click event listener to each close button
    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const modalId = this.getAttribute('data-modal-close');
            const modal = document.querySelector(modalId);
            if (modal) {
                modal.style.display = 'none';
            }
        });
    });
    
    // Close modal if user clicks outside of the modal content
    window.addEventListener('click', function(event) {
        if (event.target.classList.contains('modal')) {
            event.target.style.display = 'none';
        }
    });
});
